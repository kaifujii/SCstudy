"""
Generate dark-themed inline SVGs for vol3/vol4/vol5 architecture diagrams.
Replaces <img src="picture/..."> tags with inline SVG in the HTML files.
"""
import json, re, textwrap

# ─── SVG Design System ──────────────────────────────────────────────────────
BG       = "#0d1b2e"        # dark navy background
BOX_BG   = "#112240"        # node background
TXT      = "#c5d8ef"        # node label text
TXT_SUB  = "#7a9cbf"        # secondary text
ARROW    = "#4a9fd4"        # arrow/edge color
CLUSTER_BORDER = "#2a4a6b"  # cluster dashed border

# Service category colors
CAT = {
    "compute":     "#0072C6",
    "network":     "#107C10",
    "storage":     "#00B0F0",
    "database":    "#6264A7",
    "security":    "#E8A000",
    "monitor":     "#D13438",
    "identity":    "#7719AA",
    "integration": "#9575CD",
    "analytics":   "#00897B",
    "onprem":      "#546E7A",
    "general":     "#37474F",
}

def _esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def defs_block():
    """SVG defs: arrowhead marker, dark gradient."""
    return textwrap.dedent(f"""
      <defs>
        <marker id="arr" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">
          <polygon points="0 0,7 2.5,0 5" fill="{ARROW}"/>
        </marker>
        <marker id="arr_w" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">
          <polygon points="0 0,7 2.5,0 5" fill="#ffffff"/>
        </marker>
      </defs>
    """).strip()

def node_svg(cx, cy, lines, cat="compute", w=88, h=62):
    """Centered node box at (cx, cy).
    lines: list of text strings (first is bold abbr, rest are label lines)
    """
    color = CAT.get(cat, CAT["general"])
    x, y = cx - w//2, cy - h//2
    abbr = lines[0] if lines else ""
    label_lines = lines[1:] if len(lines) > 1 else []
    # Icon area height
    ih = 28
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{BOX_BG}" stroke="{color}" stroke-width="1.5"/>',
        f'<rect x="{x+6}" y="{y+5}" width="{w-12}" height="{ih}" rx="4" fill="{color}" fill-opacity="0.18"/>',
        f'<text x="{cx}" y="{y+5+ih//2+5}" text-anchor="middle" font-size="12" font-weight="700" fill="{color}" font-family="Segoe UI,Arial,sans-serif">{_esc(abbr)}</text>',
    ]
    ly = y + ih + 14
    for l in label_lines:
        parts.append(f'<text x="{cx}" y="{ly}" text-anchor="middle" font-size="8.5" fill="{TXT}" font-family="Segoe UI,Arial,sans-serif">{_esc(l)}</text>')
        ly += 11
    return "\n".join(parts)

def arrow_h(x1, x2, y, label=""):
    """Horizontal arrow from x1 to x2 at height y."""
    mid = (x1+x2)//2
    parts = [f'<line x1="{x1}" y1="{y}" x2="{x2-6}" y2="{y}" stroke="{ARROW}" stroke-width="1.5" marker-end="url(#arr)"/>']
    if label:
        parts.append(f'<text x="{mid}" y="{y-5}" text-anchor="middle" font-size="8" fill="{TXT_SUB}" font-family="Segoe UI,Arial,sans-serif">{_esc(label)}</text>')
    return "\n".join(parts)

def arrow_to(x1, y1, x2, y2, label="", dashed=False):
    """Arbitrary arrow."""
    dash = ' stroke-dasharray="5,3"' if dashed else ""
    parts = [f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ARROW}" stroke-width="1.5" marker-end="url(#arr)"{dash}/>']
    if label:
        mx, my = (x1+x2)//2, (y1+y2)//2
        parts.append(f'<text x="{mx}" y="{my-5}" text-anchor="middle" font-size="8" fill="{TXT_SUB}" font-family="Segoe UI,Arial,sans-serif">{_esc(label)}</text>')
    return "\n".join(parts)

def cluster_box(x, y, w, h, label="", color=None):
    c = color or CLUSTER_BORDER
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}" fill-opacity="0.06" stroke="{c}" stroke-width="1" stroke-dasharray="5,3"/>']
    if label:
        parts.append(f'<text x="{x+8}" y="{y+14}" font-size="8.5" font-weight="600" fill="{c}" font-family="Segoe UI,Arial,sans-serif">{_esc(label)}</text>')
    return "\n".join(parts)

def svg_wrap(width, height, body):
    return (
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{width}px;display:block;margin:10px auto;border-radius:10px;">'
        f'\n<rect width="{width}" height="{height}" rx="10" fill="{BG}"/>\n'
        f'{defs_block()}\n'
        f'{body}\n'
        f'</svg>'
    )

def linear_pipeline(items, edge_labels=None, width=760, height=150, clusters=None):
    """
    items: list of (lines_list, cat)  e.g. ([["EH","Event Hubs"],], "analytics")
    edge_labels: list of labels between nodes (len = len(items)-1)
    clusters: list of (start_idx, end_idx, label, color)
    """
    n = len(items)
    nw, nh = 88, 62
    gap = 32
    total_w = n * nw + (n-1) * gap
    sx = (width - total_w) // 2
    cy = height // 2
    if edge_labels is None:
        edge_labels = [""] * (n-1)

    bodies = []
    xs = []
    for i, (lines, cat) in enumerate(items):
        cx = sx + i*(nw+gap) + nw//2
        xs.append(cx)
        bodies.append(node_svg(cx, cy, lines, cat, nw, nh))

    # Clusters (drawn behind nodes - add to front of list)
    cl_parts = []
    if clusters:
        for (si, ei, lbl, clr) in clusters:
            pad = 10
            x1 = xs[si] - nw//2 - pad
            x2 = xs[ei] + nw//2 + pad
            cl_parts.append(cluster_box(x1, cy-nh//2-pad-8, x2-x1, nh+pad*2+16, lbl, clr))

    # Arrows
    for i in range(n-1):
        lbl = edge_labels[i] if i < len(edge_labels) else ""
        bodies.append(arrow_h(xs[i]+nw//2, xs[i+1]-nw//2, cy, lbl))

    return svg_wrap(width, height, "\n".join(cl_parts + bodies))


def hub_fan(hub_item, fan_items, edge_labels=None, width=760, height=None, direction="right", hub_clusters=None):
    """Hub → many. Hub on left, fan on right (stacked vertically)."""
    n = len(fan_items)
    nw, nh = 88, 62
    row_h = nh + 18
    total_fan_h = n * row_h - 18
    H = max(total_fan_h + 40, 150) if height is None else height
    cy_hub = H // 2
    cx_hub = 100
    cx_fan = 600

    if edge_labels is None:
        edge_labels = [""] * n

    bodies = []
    # Clusters
    if hub_clusters:
        for (si, ei, lbl, clr) in hub_clusters:
            pass  # placeholder

    bodies.append(node_svg(cx_hub, cy_hub, hub_item[0], hub_item[1], nw, nh))

    fan_ys = []
    start_y = (H - total_fan_h) // 2 + nh//2
    for i, (lines, cat) in enumerate(fan_items):
        cy = start_y + i * row_h
        fan_ys.append(cy)
        bodies.append(node_svg(cx_fan, cy, lines, cat, nw, nh))

    # Arrows from hub to each fan node
    for i, fy in enumerate(fan_ys):
        lbl = edge_labels[i] if i < len(edge_labels) else ""
        bodies.append(arrow_to(cx_hub+nw//2, cy_hub, cx_fan-nw//2, fy, lbl))

    return svg_wrap(width, H, "\n".join(bodies))


# ═══════════════════════════════════════════════════════════════════════════
# VOL3 SVGs
# ═══════════════════════════════════════════════════════════════════════════

SVGS = {}  # key → svg string

# Q1/Q2: AAD → Event Hubs → Functions → CosmosDB
SVGS["vol3_q01_q02"] = linear_pipeline([
    (["AAD", "Microsoft", "Entra ID"], "identity"),
    (["EH", "Event Hubs", "(サービス1)"], "analytics"),
    (["Fn", "Functions", "(サービス2)"], "compute"),
    (["CDB", "Cosmos DB", "格納"], "database"),
], edge_labels=["イベント生成", "転送", "格納"], width=740, height=150)

# Q5/Q6: OnPrem → IR → ADF → Storage
SVGS["vol3_q05_q06"] = linear_pipeline([
    (["SRV", "OnPrem", "Server1"], "onprem"),
    (["IR", "Self-hosted", "IR"], "onprem"),
    (["ADF", "Data Factory"], "analytics"),
    (["ST", "Azure", "Storage"], "storage"),
], edge_labels=["→", "コピー", "転送"], width=740, height=150,
   clusters=[(0,1,"オンプレミス","#546E7A"), (2,3,"Azure","#0072C6")])

# Q7-Q9: BCDR
SVGS["vol3_q07_q09"] = hub_fan(
    ([["RSV","Recovery Services","Vault"], "general"]),
    [
        (["ASR","販売VM","→ ASR"], "general"),
        (["BKP","財務VM","→ Backup"], "general"),
        (["BKP","レポートVM","→ Backup"], "general"),
        (["VM","フェール","オーバー先"], "compute"),
    ],
    width=760, height=210
)

# simpler approach for Q7-Q9
SVGS["vol3_q07_q09"] = linear_pipeline([
    (["VM","オンプレ VM", "3アプリ"], "onprem"),
    (["RSV","Recovery Services","Vault"], "general"),
    (["VM","Azure / 2次DC","フェールオーバー先"], "compute"),
], edge_labels=["ASR レプリ / Backup", "フェールオーバー"], width=640, height=150,
   clusters=[(0,0,"オンプレミス DC","#546E7A"), (2,2,"Azure / 2次 DC","#0072C6")])

# Q10: AKS + VM
SVGS["vol3_q10"] = linear_pipeline([
    (["VM","コンシューマー","VM"], "compute"),
    (["ILB","Internal","Load Balancer"], "network"),
    (["AKS","AKS","マイクロサービス"], "compute"),
], edge_labels=["内部アクセス", ""], width=640, height=150,
   clusters=[(0,2,"Azure VNet","#107C10")])

# Q11-Q14: Multi-region Web App
SVGS["vol3_q11_q14"] = linear_pipeline([
    (["TM","Traffic Manager","グローバル LB"], "network"),
    (["APP","Web App","リージョン A"], "compute"),
    (["APP","Web App","リージョン B"], "compute"),
], edge_labels=["ルーティング", ""], width=640, height=150)

# Q17: Logic Apps B2B
SVGS["vol3_q17"] = linear_pipeline([
    (["AAD","Ironclad","テナント"], "identity"),
    (["LA","Logic Apps","HTTP トリガー"], "integration"),
    (["SRV","オンプレ","Web サービス"], "onprem"),
], edge_labels=["B2B アクセス", "内部呼び出し"], width=640, height=150,
   clusters=[(1,2,"ApexCore Azure","#0072C6")])

# Q28: Branch → VPN → Azure Files
SVGS["vol3_q28"] = linear_pipeline([
    (["SRV","ブランチ","ユーザー"], "onprem"),
    (["VPN","VPN Gateway"], "network"),
    (["AF","Azure Files","共有ストレージ"], "storage"),
], edge_labels=["S2S VPN", ""], width=640, height=150,
   clusters=[(2,2,"Azure","#0072C6")])

# Q31-Q34: ExpressRoute Hybrid
SVGS["vol3_q31_q34"] = linear_pipeline([
    (["VM","オンプレ","VM"], "onprem"),
    (["ER","ExpressRoute"], "network"),
    (["VM","Azure VM"], "compute"),
    (["LAW","Log Analytics","Workspace"], "monitor"),
], edge_labels=["専用線", "", "ログ収集"], width=740, height=150,
   clusters=[(0,0,"オンプレミス","#546E7A"), (2,3,"Azure","#0072C6")])

# Q36: CosmosDB → Synapse
SVGS["vol3_q36"] = linear_pipeline([
    (["CDB","Cosmos DB","オペレーショナル"], "database"),
    (["ADL","Analytical","Store"], "storage"),
    (["SYN","Synapse Analytics","分析"], "analytics"),
], edge_labels=["Synapse Link", "クエリ"], width=640, height=150)

# Q43: Traffic Manager Multi-region
SVGS["vol3_q43"] = linear_pipeline([
    (["TM","Traffic Manager"], "network"),
    (["APP","App1","リージョン A"], "compute"),
    (["APP","App1","リージョン B"], "compute"),
], edge_labels=["ルーティング", ""], width=640, height=150)

# Q46/Q47: App + Managed Identity + Key Vault
SVGS["vol3_q46_q47"] = linear_pipeline([
    (["APP","App1","App Service"], "compute"),
    (["MI","Managed","Identity"], "identity"),
    (["KV","Key Vault","シークレット"], "security"),
], edge_labels=["ID 利用", "シークレット取得"], width=640, height=150)

# Q52: App Insights
SVGS["vol3_q52"] = linear_pipeline([
    (["APP","App2","App Service"], "compute"),
    (["AI","Application","Insights"], "monitor"),
    (["LAW","Log Analytics","Workspace"], "monitor"),
], edge_labels=["テレメトリ送信", "ログ保存"], width=640, height=150)


# ═══════════════════════════════════════════════════════════════════════════
# VOL4 SVGs
# ═══════════════════════════════════════════════════════════════════════════

# Q1: ADF Blob→SQL
SVGS["vol4_q01"] = linear_pipeline([
    (["ST","Blob Storage","Webアクセスログ"], "storage"),
    (["ADF","Data Factory","変換パイプライン"], "analytics"),
    (["SQL","Azure SQL DB","月次レポート"], "database"),
], edge_labels=["トリガー/コピー", "ロード"], width=640, height=150)

# Q2: Event Hubs → ADLS
SVGS["vol4_q02"] = linear_pipeline([
    (["EH","Event Hubs","JSON 取り込み"], "analytics"),
    (["CAP","EH Capture"], "analytics"),
    (["ADL","ADLS Gen2","日付別ディレクトリ"], "storage"),
], edge_labels=["Capture", "自動転送"], width=640, height=150)

# Q11: Service Bus FIFO
SVGS["vol4_q11"] = linear_pipeline([
    (["APP","送信","コンポーネント"], "compute"),
    (["SB","Service Bus","Queue (FIFO)"], "integration"),
    (["APP","受信","コンポーネント"], "compute"),
], edge_labels=["送信", "順序通り処理"], width=640, height=150)

# Q12: Multi-VNet + Front Door
SVGS["vol4_q12"] = hub_fan(
    (["FD","Front Door","HTTPS Global LB"], "network"),
    [
        (["VM","VM1 (Central US)","フロントエンド"], "compute"),
        (["VM","VM3 (West US 2)","フロントエンド"], "compute"),
        (["VM","VM2 (East US)","バックエンド"], "compute"),
    ],
    width=700, height=220
)

# Q13: App + SQL + Redis
SVGS["vol4_q13"] = linear_pipeline([
    (["APP","App Service","App1"], "compute"),
    (["RC","Redis Cache","読み取りキャッシュ"], "database"),
    (["SQL","Azure SQL DB","SQL1"], "database"),
], edge_labels=["キャッシュ確認", "キャッシュミス時"], width=640, height=150)

# Q19: Event Hubs Capture
SVGS["vol4_q19"] = linear_pipeline([
    (["APP","アプリ","50k events/日"], "compute"),
    (["EH","Event Hubs"], "analytics"),
    (["CAP","Capture","Avro 形式"], "storage"),
    (["SYN","レポーティング","システム"], "analytics"),
], edge_labels=["送信", "Capture", "バッチ処理"], width=740, height=150)

# Q23: SQL DB HA + Encryption
SVGS["vol4_q23"] = linear_pipeline([
    (["APP","Web アプリ","従業員 PII"], "compute"),
    (["SQL","SQL DB","ゾーン冗長"], "database"),
    (["KV","Key Vault","CMK for TDE"], "security"),
], edge_labels=["接続", "Column暗号化キー"], width=640, height=150)

# Q27/Q28: Virtual WAN
SVGS["vol4_q27_q28"] = hub_fan(
    (["VWAN","Virtual WAN","Standard SKU"], "network"),
    [
        (["ER","NYC ExpressRoute"], "network"),
        (["ER","SYD ExpressRoute"], "network"),
        (["ER","PAR ExpressRoute"], "network"),
        (["ER","JNB ExpressRoute"], "network"),
    ],
    width=700, height=230
)

# Q29: Databricks + VNet
SVGS["vol4_q29"] = linear_pipeline([
    (["SRV","オンプレ","アプリ"], "onprem"),
    (["VPN","VPN /"," ExpressRoute"], "network"),
    (["PE","Private","Endpoint"], "network"),
    (["DBX","Databricks","VNet Injection"], "analytics"),
], edge_labels=["→", "プライベート接続", ""], width=740, height=150,
   clusters=[(2,3,"Azure VNet","#0072C6")])

# Q37: Functions → AKS
SVGS["vol4_q37"] = linear_pipeline([
    (["EH","Event Hubs","イベントソース"], "analytics"),
    (["AKS","AKS","KEDA スケーリング"], "compute"),
    (["Fn","Functions","コンテナー"], "compute"),
], edge_labels=["トリガー", "実行"], width=640, height=150)

# Q42/Q43: PE + DNS
SVGS["vol4_q42_q43"] = linear_pipeline([
    (["SRV","オンプレ","クライアント"], "onprem"),
    (["ER","ExpressRoute"], "network"),
    (["DNS","プライベート","DNS ゾーン"], "network"),
    (["PE","Private","Endpoint"], "network"),
    (["SQL","SQLDB1"], "database"),
], edge_labels=["DNS 転送", "", "", ""], width=760, height=150,
   clusters=[(2,4,"Azure VNET1","#0072C6")])

# Q50/Q51: Global Reach + TM
SVGS["vol4_q50_q51"] = linear_pipeline([
    (["SRV","NYC / LA","オンプレ DC"], "onprem"),
    (["ER","ExpressRoute","Global Reach"], "network"),
    (["TM","Traffic Manager","フェールオーバー"], "network"),
    (["APP","App","East / West US"], "compute"),
], edge_labels=["専用線", "自動ルーティング", ""], width=740, height=150,
   clusters=[(2,3,"Azure","#0072C6")])

# Q54/Q55: Data Pipeline
SVGS["vol4_q54_q55"] = linear_pipeline([
    (["SRV","複数 SQL Server","オンプレ"], "onprem"),
    (["ADF","Data Factory","差分取り込み"], "analytics"),
    (["ST","Blob Storage","ステージング"], "storage"),
    (["SYN","Synapse Analytics","OLAP"], "analytics"),
    (["PBI","Power BI","レポーティング"], "compute"),
], edge_labels=["変更取り込み", "", "", "提供"], width=760, height=150,
   clusters=[(1,4,"Azure","#0072C6")])


# ═══════════════════════════════════════════════════════════════════════════
# VOL5 SVGs
# ═══════════════════════════════════════════════════════════════════════════

# Q1: 2 regions 4 AZ
def vol5_q01():
    w, h = 720, 160
    c = CAT["compute"]; nc = CAT["network"]
    b = [
        cluster_box(30, 20, 300, 120, "East Japan リージョン 1  VNet 1", "#0072C6"),
        cluster_box(390, 20, 300, 120, "West Japan リージョン 2  VNet 2", "#107C10"),
        node_svg(110, 90, ["VM群","AZ-1"], "compute", 80, 56),
        node_svg(230, 90, ["VM群","AZ-2"], "compute", 80, 56),
        node_svg(470, 90, ["VM群","AZ-3"], "compute", 80, 56),
        node_svg(590, 90, ["VM群","AZ-4"], "compute", 80, 56),
        f'<line x1="330" y1="90" x2="388" y2="90" stroke="{ARROW}" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr)"/>',
        f'<text x="360" y="84" text-anchor="middle" font-size="8" fill="{TXT_SUB}" font-family="Segoe UI,Arial,sans-serif">VNet Peering</text>',
    ]
    return svg_wrap(w, h, "\n".join(b))

SVGS["vol5_q01"] = vol5_q01()

# Q3/Q4: SQL migration + HA
SVGS["vol5_q03_q04"] = linear_pipeline([
    (["SRV","SQL Server","SQL1 オンプレ"], "onprem"),
    (["DMS","Database", "Migration Svc"], "general"),
    (["SQL","SQL DB","Primary"], "database"),
    (["SQL","Read-only","Replica x2"], "database"),
], edge_labels=["移行", "", "自動同期"], width=740, height=150,
   clusters=[(2,3,"Azure SQL DB Business Critical","#6264A7")])

# Q5/Q6: Data Lake
SVGS["vol5_q05_q06"] = linear_pipeline([
    (["SRC","多様な", "データソース"], "onprem"),
    (["ADL","ADLS Gen2","ペタバイト規模"], "storage"),
    (["ADE","Data Explorer","KQL クエリ"], "analytics"),
    (["SYN","Synapse","Analytics"], "analytics"),
], edge_labels=["取り込み", "", ""], width=740, height=150,
   clusters=[(1,3,"Azure","#0072C6")])

# Q16/Q17: APIM
SVGS["vol5_q16_q17"] = linear_pipeline([
    (["PTN","外部","パートナー"], "onprem"),
    (["APIM","API Management","レート制限/認証"], "integration"),
    (["APP","App Service","バックエンド"], "compute"),
], edge_labels=["HTTPS", "プロキシ"], width=640, height=150,
   clusters=[(1,2,"Azure","#0072C6")])

# Q22: Multi-tenant SaaS
SVGS["vol5_q22"] = hub_fan(
    (["APP","SaaS アプリ","App Service"], "compute"),
    [
        (["SQL","テナント DB 1"], "database"),
        (["SQL","テナント DB 2"], "database"),
        (["SQL","テナント DB N"], "database"),
    ],
    width=660, height=210
)

# Q23/Q24: AKS + ACR
SVGS["vol5_q23_q24"] = linear_pipeline([
    (["ACR","Container","Registry"], "compute"),
    (["AKS","AKS","クラスター"], "compute"),
    (["SVC","マイクロサービス","A / B"], "compute"),
], edge_labels=["イメージ プル", "デプロイ"], width=640, height=150,
   clusters=[(1,2,"Azure Kubernetes Service","#0072C6")])

# Q26: SQL Always On + TM
SVGS["vol5_q26"] = linear_pipeline([
    (["TM","Traffic Manager","フェールオーバー"], "network"),
    (["ILB","ILB Listener","East US"], "network"),
    (["VM","SQL Always On","Primary Replica"], "compute"),
    (["VM","SQL Always On","Secondary Replica"], "compute"),
], edge_labels=["ルーティング", "", "Always On 同期"], width=740, height=150,
   clusters=[(1,2,"East US VNet","#0072C6"), (3,3,"West US VNet","#107C10")])

# Q27/Q28: Front Door + WAF
SVGS["vol5_q27_q28"] = hub_fan(
    (["FD","Front Door","Global LB / WAF"], "network"),
    [
        (["APP","Web App","リージョン A"], "compute"),
        (["APP","Web App","リージョン B"], "compute"),
    ],
    width=640, height=180
)

# Q29/Q30: App + PE + DNS
SVGS["vol5_q29_q30"] = linear_pipeline([
    (["APP","WebApp1","VNet Integration"], "compute"),
    (["PE","Private","Endpoint"], "network"),
    (["DNS","プライベート","DNS ゾーン"], "network"),
    (["SQL","DB1","Azure SQL DB"], "database"),
], edge_labels=["VNet 経由", "名前解決", ""], width=740, height=150,
   clusters=[(0,3,"Azure (East Japan)","#0072C6")])

# Q31/Q32/Q33: APIM + VNet
SVGS["vol5_q31_q33"] = linear_pipeline([
    (["CLI","外部","クライアント"], "onprem"),
    (["APIM","API Management","外部 VNet モード"], "integration"),
    (["VM","VM1 / VM2","バックエンド"], "compute"),
], edge_labels=["インターネット", "内部ルーティング"], width=640, height=150,
   clusters=[(1,2,"VNet1","#0072C6")])

# Q40: AD + Entra Connect
SVGS["vol5_q40"] = linear_pipeline([
    (["AD","AD DS","corp.ironclad.com"], "onprem"),
    (["EC","Entra Connect","ID 同期"], "identity"),
    (["AAD","Microsoft","Entra ID"], "identity"),
    (["RES","Azure","リソース (RBAC)"], "compute"),
], edge_labels=["同期", "", "アクセス制御"], width=740, height=150,
   clusters=[(0,0,"オンプレミス","#546E7A"), (2,3,"Azure","#0072C6")])

# Q42/Q43: Synapse + MPE
SVGS["vol5_q42_q43"] = linear_pipeline([
    (["SYN","Synapse","Analytics"], "analytics"),
    (["MPE","Managed","Private Endpoint"], "network"),
    (["ADL","ADLS Gen2","機密データ"], "storage"),
], edge_labels=["安全なアクセス", ""], width=640, height=150,
   clusters=[(1,2,"Managed VNet","#0072C6")])

# Q49: Hybrid Monitoring
SVGS["vol5_q49"] = linear_pipeline([
    (["VM","オンプレ VM","Arc 登録済み"], "onprem"),
    (["AMA","Azure Monitor","Agent"], "monitor"),
    (["LAW","Log Analytics","Workspace"], "monitor"),
], edge_labels=["ログ送信", ""], width=640, height=150,
   clusters=[(0,0,"オンプレミス","#546E7A"), (2,2,"Azure","#0072C6")])

# Also add Azure VM as parallel source
def vol5_q49_svg():
    w, h = 700, 180
    b = [
        cluster_box(30, 20, 180, 130, "オンプレミス", "#546E7A"),
        cluster_box(410, 20, 260, 130, "Azure", "#0072C6"),
        node_svg(120, 70, ["VM","オンプレ VM","Arc 登録済み"], "onprem"),
        node_svg(120, 140, ["VM","Azure VM"], "compute"),
        node_svg(465, 85, ["AMA","Azure Monitor","Agent (AMA)"], "monitor"),
        node_svg(600, 85, ["LAW","Log Analytics","Workspace"], "monitor"),
        arrow_to(164, 70, 421, 80, "ログ"),
        arrow_to(164, 140, 421, 90, "ログ"),
        arrow_h(509, 555, 85, ""),
    ]
    return svg_wrap(w, h, "\n".join(b))
SVGS["vol5_q49"] = vol5_q49_svg()

# Q52/Q53/Q54: Hybrid SQL DR
SVGS["vol5_q52_q54"] = linear_pipeline([
    (["SQL","SQL Server","プライマリ (OnPrem)"], "onprem"),
    (["VPN","VPN / ER"], "network"),
    (["VM","SQL Server VM","セカンダリ (DR)"], "compute"),
    (["RSV","Recovery","Services Vault"], "general"),
], edge_labels=["Always On レプリ", "", "Azure Backup"], width=740, height=150,
   clusters=[(0,0,"オンプレミス DC","#546E7A"), (2,3,"Azure (DR リージョン)","#0072C6")])


# ═══════════════════════════════════════════════════════════════════════════
# Update HTML files
# ═══════════════════════════════════════════════════════════════════════════

IMG_TITLE = {
    # vol3
    "vol3_q01_q02": "AAD監査ログ取り込みパイプライン（Q1-2）",
    "vol3_q05_q06": "オンプレ → ADF → Azure Storage（Q5-6）",
    "vol3_q07_q09": "BCDR: Site Recovery + Backup（Q7-9）",
    "vol3_q10":     "AKS マイクロサービス + VM（Q10）",
    "vol3_q11_q14": "マルチリージョン Web App（Q11-14）",
    "vol3_q17":     "Logic Apps B2B フェデレーション（Q17）",
    "vol3_q28":     "ブランチ → VPN → Azure Files（Q28）",
    "vol3_q31_q34": "ExpressRoute ハイブリッド（Q31-34）",
    "vol3_q36":     "Cosmos DB → Synapse Analytics（Q36）",
    "vol3_q43":     "ApexCore: Traffic Manager マルチリージョン（Q43）",
    "vol3_q46_q47": "App Service + Managed Identity + Key Vault（Q46-47）",
    "vol3_q52":     "App Service + Application Insights（Q52）",
    # vol4
    "vol4_q01":         "ADF ETL: Blob → SQL DB（Q1）",
    "vol4_q02":         "Event Hubs → Data Lake ストリーミング（Q2）",
    "vol4_q11":         "Service Bus FIFO メッセージング（Q11）",
    "vol4_q12":         "マルチリージョン VM + Front Door（Q12）",
    "vol4_q13":         "App Service + SQL DB + Redis Cache（Q13）",
    "vol4_q19":         "Event Hubs Capture コールドパス（Q19）",
    "vol4_q23":         "SQL DB 高可用性 + 暗号化（Q23）",
    "vol4_q27_q28":     "仮想 WAN: 4拠点 + ExpressRoute（Q27-28）",
    "vol4_q29":         "Databricks + VNet プライベート接続（Q29）",
    "vol4_q37":         "Functions → AKS 移行（Q37）",
    "vol4_q42_q43":     "Private Endpoint + DNS + ExpressRoute（Q42-43）",
    "vol4_q50_q51":     "ExpressRoute Global Reach + Traffic Manager（Q50-51）",
    "vol4_q54_q55":     "データパイプライン: SQL → ADF → Synapse（Q54-55）",
    # vol5
    "vol5_q01":         "2リージョン 4可用性ゾーン VM（Q1）",
    "vol5_q03_q04":     "SQL Server → Azure SQL DB 移行 + HA（Q3-4）",
    "vol5_q05_q06":     "ペタバイト Data Lake アーキテクチャ（Q5-6）",
    "vol5_q16_q17":     "API Management + App Service バックエンド（Q16-17）",
    "vol5_q22":         "マルチテナント SaaS + Elastic Pool（Q22）",
    "vol5_q23_q24":     "AKS マイクロサービス + Container Registry（Q23-24）",
    "vol5_q26":         "SQL Always On + Traffic Manager DR（Q26）",
    "vol5_q27_q28":     "マルチリージョン Web App + Front Door WAF（Q27-28）",
    "vol5_q29_q30":     "App Service + Private Endpoint + DNS（Q29-30）",
    "vol5_q31_q33":     "APIM 外部 VNet モード + バックエンド VM（Q31-33）",
    "vol5_q40":         "オンプレミス AD + Entra ID Connect 同期（Q40）",
    "vol5_q42_q43":     "Synapse Analytics + Managed Private Endpoint（Q42-43）",
    "vol5_q49":         "ハイブリッド監視: Log Analytics + Azure Arc（Q49）",
    "vol5_q52_q54":     "ハイブリッド SQL Always On + DR（Q52-54）",
}

VOL3_MAP = {
    1: "vol3_q01_q02", 2: "vol3_q01_q02",
    5: "vol3_q05_q06", 6: "vol3_q05_q06",
    7: "vol3_q07_q09", 8: "vol3_q07_q09", 9: "vol3_q07_q09",
    10: "vol3_q10",
    11: "vol3_q11_q14", 12: "vol3_q11_q14", 13: "vol3_q11_q14", 14: "vol3_q11_q14",
    17: "vol3_q17",
    28: "vol3_q28",
    31: "vol3_q31_q34", 32: "vol3_q31_q34", 33: "vol3_q31_q34", 34: "vol3_q31_q34",
    36: "vol3_q36",
    43: "vol3_q43",
    46: "vol3_q46_q47", 47: "vol3_q46_q47",
    52: "vol3_q52",
}

VOL4_MAP = {
    1: "vol4_q01", 2: "vol4_q02",
    11: "vol4_q11", 12: "vol4_q12", 13: "vol4_q13",
    19: "vol4_q19", 23: "vol4_q23",
    27: "vol4_q27_q28", 28: "vol4_q27_q28",
    29: "vol4_q29", 37: "vol4_q37",
    42: "vol4_q42_q43", 43: "vol4_q42_q43",
    50: "vol4_q50_q51", 51: "vol4_q50_q51",
    54: "vol4_q54_q55", 55: "vol4_q54_q55",
}

VOL5_MAP = {
    1: "vol5_q01",
    3: "vol5_q03_q04", 4: "vol5_q03_q04",
    5: "vol5_q05_q06", 6: "vol5_q05_q06",
    16: "vol5_q16_q17", 17: "vol5_q16_q17",
    22: "vol5_q22",
    23: "vol5_q23_q24", 24: "vol5_q23_q24",
    26: "vol5_q26",
    27: "vol5_q27_q28", 28: "vol5_q27_q28",
    29: "vol5_q29_q30", 30: "vol5_q29_q30",
    31: "vol5_q31_q33", 32: "vol5_q31_q33", 33: "vol5_q31_q33",
    40: "vol5_q40",
    42: "vol5_q42_q43", 43: "vol5_q42_q43",
    49: "vol5_q49",
    52: "vol5_q52_q54", 53: "vol5_q52_q54", 54: "vol5_q52_q54",
}


def make_arch_box_svg(key):
    title = IMG_TITLE[key]
    svg   = SVGS[key]
    return f'<div class="arch-box"><div class="arch-title">{title}</div>{svg}</div>'


def update_json_vol(path, mapping):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'(const QUESTIONS = )(\[.*?\]);', content, re.DOTALL)
    prefix = match.group(1)
    questions = json.loads(match.group(2))
    updated = 0
    for q in questions:
        num = q['num']
        if num not in mapping:
            continue
        key = mapping[num]
        arch_box = make_arch_box_svg(key)
        exp = q.get('exp_html', '')
        # Replace existing arch-box (img) OR arch-box (svg wrap)
        new_exp = re.sub(
            r'<div class="arch-box">.*?</div>(?=<div class="exp-sections">|<div class="exp-block")|<div class="arch-svg-wrap">.*?</svg></div>',
            arch_box,
            exp, count=1, flags=re.DOTALL
        )
        if new_exp == exp:
            # Try simpler pattern
            new_exp = re.sub(r'<div class="arch-box">.*?</div>', arch_box, exp, count=1, flags=re.DOTALL)
        if new_exp != exp:
            q['exp_html'] = new_exp
            updated += 1
        else:
            print(f"  vol Q{num}: pattern not matched")
    new_json = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))
    new_content = content[:match.start()] + prefix + new_json + ';' + content[match.end():]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  Updated {updated} questions in {path}")


def update_vol5(path, mapping):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    nums_all = [int(m) for m in re.findall(r'\{num:(\d+),', content)]
    updated = 0
    for qnum, key in mapping.items():
        arch_box = make_arch_box_svg(key)
        q_start = content.find(f'{{num:{qnum},')
        idx = nums_all.index(qnum)
        q_end = content.find(f'{{num:{nums_all[idx+1]},') if idx+1 < len(nums_all) else len(content)
        block = content[q_start:q_end]
        # Replace existing arch-box
        new_block = re.sub(r'<div class="arch-box">.*?</div>', arch_box, block, count=1, flags=re.DOTALL)
        if new_block != block:
            content = content[:q_start] + new_block + content[q_end:]
            updated += 1
        else:
            print(f"  vol5 Q{qnum}: arch-box not found, adding...")
            # Insert after exp-title
            insert_after = '<div class="exp-title">解説</div>\n'
            if insert_after in block:
                new_block = block.replace(insert_after, insert_after + arch_box + '\n', 1)
                content = content[:q_start] + new_block + content[q_end:]
                updated += 1
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Updated {updated} questions in {path}")


print("=== Updating vol3.html ===")
update_json_vol('vol3.html', VOL3_MAP)

print("=== Updating vol4.html ===")
update_json_vol('vol4.html', VOL4_MAP)

print("=== Updating vol5.html ===")
update_vol5('vol5.html', VOL5_MAP)

print("\n✅ All inline SVGs embedded!")
