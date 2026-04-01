"""Replace vol2 <img src="picture/..."> with inline SVGs."""
import re, json

# ─── SVG helper ───────────────────────────────────────────────────────────────
BG = "#0d1b2e"
CARD_BG = "#112240"
TEXT_LIGHT = "#c5d8ef"
TEXT_LABEL = "#7a9cbf"
ARROW = "#4a9fd4"
FONT = "Segoe UI,Arial,sans-serif"

def svg_wrap(w, h, inner):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;display:block;margin:10px auto;border-radius:10px;">\n'
        f'<rect width="{w}" height="{h}" rx="10" fill="{BG}"/>\n'
        '<defs>\n'
        '  <marker id="arr" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">'
        '<polygon points="0 0,7 2.5,0 5" fill="#4a9fd4"/></marker>\n'
        '  <marker id="arr2" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">'
        '<polygon points="0 0,7 2.5,0 5" fill="#4a9fd4"/></marker>\n'
        '</defs>\n'
        + inner +
        '\n</svg>'
    )

def card(x, y, w, h, color, abbr, line1, line2=""):
    inner = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{CARD_BG}" stroke="{color}" stroke-width="1.5"/>\n'
        f'<rect x="{x+6}" y="{y+5}" width="{w-12}" height="24" rx="4" fill="{color}" fill-opacity="0.18"/>\n'
        f'<text x="{x+w//2}" y="{y+21}" text-anchor="middle" font-size="11" font-weight="700" fill="{color}" font-family="{FONT}">{abbr}</text>\n'
        f'<text x="{x+w//2}" y="{y+41}" text-anchor="middle" font-size="8.5" fill="{TEXT_LIGHT}" font-family="{FONT}">{line1}</text>\n'
    )
    if line2:
        inner += f'<text x="{x+w//2}" y="{y+52}" text-anchor="middle" font-size="8.5" fill="{TEXT_LIGHT}" font-family="{FONT}">{line2}</text>\n'
    return inner

def arrow(x1, y1, x2, y2, label="", aid="arr"):
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ARROW}" stroke-width="1.5" marker-end="url(#{aid})"/>\n'
    if label:
        mx, my = (x1+x2)//2, min(y1,y2)-4
        s += f'<text x="{mx}" y="{my}" text-anchor="middle" font-size="8" fill="{TEXT_LABEL}" font-family="{FONT}">{label}</text>\n'
    return s

def label(x, y, text, color=TEXT_LIGHT, size=9):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{color}" font-family="{FONT}">{text}</text>\n'

# ─── 10 diagrams ──────────────────────────────────────────────────────────────

def svg_sql_audit():
    """Q1-3: SQL Server + Storage Account (region constraints)"""
    inner = ""
    # East US group
    inner += '<rect x="20" y="20" width="320" height="120" rx="8" fill="none" stroke="#1e4080" stroke-width="1" stroke-dasharray="4,3"/>\n'
    inner += label(180, 38, "East US", "#4a9fd4", 9)
    inner += card(35, 45, 90, 82, "#0072C6", "SQL", "SQLsvr1", "East US")
    inner += arrow(130, 86, 160, 86, "監査")
    inner += card(165, 45, 90, 82, "#F97C00", "SA", "storage1", "East US ✓")
    inner += arrow(260, 86, 290, 86, "保存")
    inner += card(295, 45, 40, 82, "#107C41", "Log", "監査", "ログ")

    # West/Central group
    inner += '<rect x="360" y="20" width="370" height="120" rx="8" fill="none" stroke="#80401e" stroke-width="1" stroke-dasharray="4,3"/>\n'
    inner += label(545, 38, "West US / Central US", "#e87c3e", 9)
    inner += card(375, 45, 90, 82, "#0072C6", "SQL", "SQLsvr2", "West US")
    inner += arrow(470, 86, 500, 86, "監査?")
    inner += card(505, 45, 90, 82, "#F97C00", "SA", "storage2", "Central US ✗")
    inner += '<line x1="553" y1="45" x2="553" y2="127" stroke="#e05252" stroke-width="2"/>\n'
    inner += '<line x1="505" y1="45" x2="601" y2="127" stroke="#e05252" stroke-width="2"/>\n'
    inner += label(630, 75, "異なるリージョン", "#e05252", 8)
    inner += label(630, 87, "→ 設定不可", "#e05252", 8)

    return svg_wrap(740, 155, inner)


def svg_mgmt_group():
    """Q9-10: 管理グループ階層"""
    inner = ""
    # Root
    inner += card(310, 10, 120, 55, "#6264A7", "Root MG", "Tenant Root", "Management Group")
    # Two child MGs
    inner += arrow(370, 65, 185, 100, "")
    inner += arrow(370, 65, 555, 100, "")
    inner += card(110, 100, 120, 55, "#0072C6", "MG-A", "MG-A", "(Dept A)")
    inner += card(495, 100, 120, 55, "#0072C6", "MG-B", "MG-B", "(Dept B)")
    # Subscriptions
    inner += arrow(170, 155, 80, 195, "")
    inner += arrow(170, 155, 260, 195, "")
    inner += card(30, 195, 100, 55, "#107C41", "Sub1", "Sub-A1", "")
    inner += card(215, 195, 100, 55, "#107C41", "Sub2", "Sub-A2", "")
    inner += arrow(555, 155, 555, 195, "")
    inner += card(505, 195, 100, 55, "#107C41", "Sub3", "Sub-B1", "")
    # Policy inheritance label
    inner += label(370, 280, "ポリシー・RBAC は上位から継承", "#4a9fd4", 10)

    return svg_wrap(740, 295, inner)


def svg_frontdoor_aks():
    """Q12: Front Door + multi-region AKS"""
    inner = ""
    inner += card(20, 60, 100, 60, "#E040FB", "FD", "Azure", "Front Door")
    inner += arrow(120, 90, 155, 90, "ルーティング")
    # Region 1
    inner += '<rect x="160" y="30" width="160" height="120" rx="8" fill="none" stroke="#1e4080" stroke-width="1" stroke-dasharray="4,3"/>\n'
    inner += label(240, 48, "East US", "#4a9fd4", 9)
    inner += card(175, 55, 130, 80, "#0078D4", "AKS1", "AKS Cluster", "East US")
    inner += arrow(320, 90, 355, 90, "フォールバック")
    # Region 2
    inner += '<rect x="360" y="30" width="160" height="120" rx="8" fill="none" stroke="#1e4080" stroke-width="1" stroke-dasharray="4,3"/>\n'
    inner += label(440, 48, "West US", "#4a9fd4", 9)
    inner += card(375, 55, 130, 80, "#0078D4", "AKS2", "AKS Cluster", "West US")
    # ACR shared
    inner += arrow(240, 135, 240, 170, "")
    inner += arrow(440, 135, 530, 170, "")
    inner += card(460, 175, 120, 60, "#6264A7", "ACR", "Container", "Registry (共有)")
    inner += label(370, 255, "Front Door → 最近接リージョンへルーティング", "#4a9fd4", 9)

    return svg_wrap(740, 265, inner)


def svg_servicebus_pubsub():
    """Q17: Service Bus Topic (Pub/Sub)"""
    inner = ""
    # Publisher
    inner += card(20, 70, 100, 60, "#107C41", "App", "Publisher", "App Service")
    inner += arrow(120, 100, 155, 100, "publish")
    # Topic
    inner += card(160, 55, 120, 90, "#F97C00", "SB", "Service Bus", "Topic")
    # Subscriptions
    inner += arrow(280, 100, 315, 70, "")
    inner += arrow(280, 100, 315, 100, "")
    inner += arrow(280, 100, 315, 130, "")
    inner += card(320, 45, 110, 50, "#0072C6", "Sub1", "Subscription1", "")
    inner += card(320, 80, 110, 50, "#0072C6", "Sub2", "Subscription2", "")
    inner += card(320, 115, 110, 50, "#0072C6", "Sub3", "Subscription3", "")
    # Consumers
    inner += arrow(430, 70, 465, 70, "")
    inner += arrow(430, 105, 465, 105, "")
    inner += arrow(430, 140, 465, 140, "")
    inner += card(470, 45, 110, 50, "#6264A7", "C1", "Consumer1", "Function")
    inner += card(470, 80, 110, 50, "#6264A7", "C2", "Consumer2", "Logic App")
    inner += card(470, 115, 110, 50, "#6264A7", "C3", "Consumer3", "App Service")
    inner += label(370, 180, "1メッセージ → 複数サブスクリプションへコピー配信", "#4a9fd4", 9)

    return svg_wrap(600, 195, inner)


def svg_appgw_waf():
    """Q23-24: Application Gateway + WAF"""
    inner = ""
    # Internet
    inner += card(15, 65, 80, 60, "#7a9cbf", "Internet", "Internet", "クライアント")
    inner += arrow(95, 95, 130, 95, "HTTPS")
    # WAF
    inner += card(135, 50, 100, 90, "#E74C3C", "WAF", "App Gateway", "WAF v2")
    inner += label(185, 155, "L7 LB + WAF", "#E74C3C", 8)
    inner += arrow(235, 95, 270, 75, "")
    inner += arrow(235, 95, 270, 115, "")
    # Backend pool
    inner += '<rect x="275" y="30" width="140" height="130" rx="8" fill="none" stroke="#1e4080" stroke-width="1" stroke-dasharray="4,3"/>\n'
    inner += label(345, 48, "Backend Pool", "#4a9fd4", 9)
    inner += card(285, 55, 110, 45, "#0078D4", "VM1", "VM / App", "Service 1")
    inner += card(285, 105, 110, 45, "#0078D4", "VM2", "VM / App", "Service 2")
    # Key Vault (SSL cert)
    inner += '<line x1="185" y1="50" x2="185" y2="15" stroke="#F97C00" stroke-width="1.5" stroke-dasharray="3,2"/>\n'
    inner += card(430, 15, 110, 55, "#F97C00", "KV", "Key Vault", "SSL証明書")
    inner += '<line x1="185" y1="15" x2="485" y2="15" stroke="#F97C00" stroke-width="1.5" stroke-dasharray="3,2"/>\n'
    inner += '<line x1="485" y1="15" x2="485" y2="15" stroke="#F97C00" stroke-width="1.5" stroke-dasharray="3,2"/>\n'
    inner += label(185, 200, "WAF はOWASP ルールセットで SQLi / XSS等をブロック", "#4a9fd4", 9)

    return svg_wrap(560, 210, inner)


def svg_adf_pipeline():
    """Q28: Azure Data Factory pipeline"""
    inner = ""
    # Source
    inner += card(20, 60, 100, 60, "#E05252", "SQL", "On-prem", "SQL Server")
    inner += arrow(120, 90, 155, 90, "IR経由")
    # ADF
    inner += card(160, 45, 130, 90, "#E040FB", "ADF", "Azure Data", "Factory")
    inner += label(225, 145, "Self-hosted IR", "#c5d8ef", 8)
    inner += arrow(290, 90, 325, 90, "Copy")
    # Staging
    inner += card(330, 60, 100, 60, "#F97C00", "Blob", "Azure Blob", "Storage (Staging)")
    inner += arrow(430, 90, 465, 90, "Load")
    # Sink
    inner += card(470, 60, 110, 60, "#0072C6", "DW", "Synapse / SQL", "Data Warehouse")
    inner += label(370, 145, "Linked Service → Dataset → Pipeline → Trigger", "#7a9cbf", 9)

    return svg_wrap(600, 160, inner)


def svg_bastion():
    """Q42-43: Azure Bastion"""
    inner = ""
    # Admin
    inner += card(15, 70, 90, 60, "#7a9cbf", "Admin", "管理者", "ブラウザ")
    inner += arrow(105, 100, 140, 100, "HTTPS 443")
    # VNet
    inner += '<rect x="145" y="25" width="450" height="170" rx="8" fill="none" stroke="#1e4080" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    inner += label(370, 43, "Azure VNet", "#4a9fd4", 10)
    # Bastion Subnet
    inner += '<rect x="160" y="50" width="140" height="130" rx="6" fill="#0d1b2e" stroke="#0072C6" stroke-width="1"/>\n'
    inner += label(230, 68, "AzureBastionSubnet", "#7a9cbf", 8)
    inner += card(170, 75, 120, 90, "#0072C6", "Bastion", "Azure", "Bastion")
    # Arrow to VM
    inner += arrow(300, 100, 340, 100, "RDP/SSH (内部)")
    # VMs subnet
    inner += '<rect x="345" y="50" width="235" height="130" rx="6" fill="#0d1b2e" stroke="#107C41" stroke-width="1"/>\n'
    inner += label(462, 68, "VM Subnet", "#7a9cbf", 8)
    inner += card(355, 75, 100, 90, "#107C41", "VM1", "Windows VM", "")
    inner += card(470, 75, 100, 90, "#107C41", "VM2", "Linux VM", "")
    inner += label(370, 215, "パブリックIPなし・NSG不要・RDPポート開放不要", "#4a9fd4", 9)

    return svg_wrap(620, 230, inner)


def svg_frontdoor_global():
    """Q44: Front Door グローバル負荷分散"""
    inner = ""
    # Users
    inner += card(15, 70, 90, 60, "#7a9cbf", "Users", "グローバル", "ユーザー")
    inner += arrow(105, 100, 140, 100, "anycast")
    # Front Door
    inner += card(145, 55, 130, 90, "#E040FB", "FD", "Azure Front", "Door (Global)")
    inner += label(210, 155, "Anycast + Edge POP", "#E040FB", 8)
    # Origins
    inner += arrow(275, 85, 315, 65, "")
    inner += arrow(275, 100, 315, 100, "")
    inner += arrow(275, 115, 315, 135, "")
    inner += card(320, 40, 130, 55, "#0078D4", "App1", "App Service", "East US")
    inner += card(320, 75, 130, 55, "#0078D4", "App2", "App Service", "West EU")
    inner += card(320, 110, 130, 55, "#0078D4", "App3", "App Service", "SE Asia")
    inner += label(370, 180, "最低レイテンシ Origin へルーティング / フェイルオーバー自動", "#4a9fd4", 9)

    return svg_wrap(480, 195, inner)


def svg_apim():
    """Q46-47: API Management + Entra ID"""
    inner = ""
    # Client
    inner += card(15, 75, 90, 60, "#7a9cbf", "Client", "クライアント", "アプリ / SPA")
    inner += arrow(105, 105, 140, 105, "JWT Bearer")
    # Entra ID (auth)
    inner += '<line x1="80" y1="75" x2="80" y2="30" stroke="#7719AA" stroke-width="1.5" stroke-dasharray="3,2"/>\n'
    inner += '<line x1="80" y1="30" x2="220" y2="30" stroke="#7719AA" stroke-width="1.5" stroke-dasharray="3,2"/>\n'
    inner += card(145, 5, 150, 50, "#7719AA", "AAD", "Entra ID", "OAuth2 / OIDC")
    inner += arrow(220, 30, 250, 80, "トークン検証")
    # APIM
    inner += card(255, 60, 130, 90, "#0072C6", "APIM", "API Mgmt", "ポリシー適用")
    inner += label(320, 160, "レート制限/変換/認証", "#7a9cbf", 8)
    inner += arrow(385, 105, 420, 85, "")
    inner += arrow(385, 105, 420, 125, "")
    # Backends
    inner += card(425, 55, 120, 55, "#107C41", "BE1", "Backend API1", "App Service")
    inner += card(425, 110, 120, 55, "#107C41", "BE2", "Backend API2", "Functions")
    inner += label(370, 185, "Entra ID でトークン検証 → APIM でポリシー適用 → Backend へ転送", "#4a9fd4", 8)

    return svg_wrap(570, 200, inner)


def svg_ampls():
    """Q55: Azure Monitor Private Link Scope (AMPLS)"""
    inner = ""
    # VNet
    inner += '<rect x="15" y="20" width="300" height="200" rx="8" fill="none" stroke="#1e4080" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    inner += label(165, 38, "Azure VNet (プライベート)", "#4a9fd4", 9)
    # VMs
    inner += card(30, 50, 110, 55, "#107C41", "VM", "Azure VM", "監視対象")
    inner += card(30, 120, 110, 55, "#107C41", "AKS", "AKS", "監視対象")
    # Private Endpoint
    inner += card(175, 85, 120, 60, "#0072C6", "PE", "Private", "Endpoint")
    inner += arrow(140, 75, 170, 100, "")
    inner += arrow(140, 147, 170, 115, "")
    inner += arrow(295, 115, 335, 115, "プライベート通信")
    # AMPLS
    inner += '<rect x="340" y="20" width="380" height="200" rx="8" fill="none" stroke="#6264A7" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    inner += label(530, 38, "AMPLS (Azure Monitor Private Link Scope)", "#6264A7", 8)
    inner += card(355, 50, 130, 55, "#6264A7", "LAW", "Log Analytics", "Workspace")
    inner += card(355, 120, 130, 55, "#6264A7", "AI", "Application", "Insights")
    inner += card(510, 80, 100, 60, "#E040FB", "AM", "Azure Monitor", "管理")
    inner += arrow(485, 77, 505, 100, "")
    inner += arrow(485, 147, 505, 120, "")
    inner += label(530, 235, "パブリックインターネット経由なし・監視データ完全プライベート", "#4a9fd4", 8)

    return svg_wrap(740, 250, inner)


# ─── Main: patch vol2.html ────────────────────────────────────────────────────

SVG_MAP = {
    "vol2_q01_q03_sql_audit":       ("SQL監査ログの構成（Q1-3）",                svg_sql_audit()),
    "vol2_q09_q10_mgmt_group":      ("管理グループ階層（Q9-10）",                svg_mgmt_group()),
    "vol2_q12_frontdoor_aks":       ("Azure Front Door + マルチリージョン AKS（Q12）", svg_frontdoor_aks()),
    "vol2_q17_servicebus_pubsub":   ("Service Bus トピック（Pub/Sub）（Q17）",   svg_servicebus_pubsub()),
    "vol2_q23_q24_appgw_waf":       ("Application Gateway + WAF アーキテクチャ（Q23-24）", svg_appgw_waf()),
    "vol2_q28_adf_pipeline":        ("Azure Data Factory パイプライン（Q28）",   svg_adf_pipeline()),
    "vol2_q42_q43_bastion":         ("Azure Bastion 構成（Q42-43）",             svg_bastion()),
    "vol2_q44_frontdoor_global":    ("Azure Front Door グローバル負荷分散（Q44）", svg_frontdoor_global()),
    "vol2_q46_q47_apim":            ("API Management + Entra ID（Q46-47）",      svg_apim()),
    "vol2_q55_ampls":               ("Azure Monitor Private Link Scope / AMPLS（Q55）", svg_ampls()),
}

path = '/Users/fujiikai/SCstudy/az305/vol2.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const QUESTIONS = )(\[.*?\]);', content, re.DOTALL)
prefix = match.group(1)
raw = match.group(2)
questions = json.loads(raw)

updated = 0
for q in questions:
    exp = q.get('exp_html', '')
    # Find img tag: <img src="picture/FNAME.png" ...>
    img_match = re.search(r'<img src="picture/([^"]+)\.png"[^>]*>', exp)
    if not img_match:
        continue
    fname = img_match.group(1)
    if fname not in SVG_MAP:
        print(f"  Q{q['num']}: unknown fname {fname}")
        continue
    title, svg_html = SVG_MAP[fname]
    # Replace <img src="picture/FNAME.png"...> with inline SVG inside arch-box
    new_exp = re.sub(
        r'<img src="picture/' + re.escape(fname) + r'\.png"[^>]*>',
        svg_html,
        exp,
        count=1
    )
    if new_exp != exp:
        q['exp_html'] = new_exp
        updated += 1
        print(f"  Q{q['num']}: embedded SVG for {fname}")
    else:
        print(f"  Q{q['num']}: regex did not match arch-box")

new_json = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))
new_content = content[:match.start()] + prefix + new_json + ';' + content[match.end():]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\n✅ Updated {updated} questions in vol2.html")
