"""Replace vol2 arch-box img tags with compact dark inline SVGs (like vol5 style)."""
import re, json

PATH = "az305/vol2.html"

BG    = "#0d1b2e"; NAVY  = "#152844"; BLUE  = "#2563eb"; LBLUE = "#93c5fd"
GRAY  = "#64748b"; LGRAY = "#94a3b8"; GREEN = "#22c55e"; LGREEN= "#86efac"
RED   = "#ef4444"; LRED  = "#fca5a5"; ARROW = "#4a9fd4"; REGION= "#1e5a8a"
ORANGE= "#f59e0b"

# ── helpers ────────────────────────────────────────────────────────────────────
def mk_defs(pid):
    return (f'<defs>'
            f'<marker id="{pid}a" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{ARROW}"/></marker>'
            f'<marker id="{pid}g" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{GREEN}"/></marker>'
            f'<marker id="{pid}r" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{RED}"/></marker>'
            f'<marker id="{pid}o" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{ORANGE}"/></marker>'
            f'</defs>')

def node(x, y, w, h, label, sub="", tc=LBLUE, fill=NAVY, stroke=BLUE):
    mx = x + w // 2
    lines = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
    if sub:
        lines += f'<text x="{mx}" y="{y + h//2 - 2}" text-anchor="middle" fill="{tc}" font-size="9" font-family="sans-serif" font-weight="bold">{label}</text>'
        lines += f'<text x="{mx}" y="{y + h//2 + 10}" text-anchor="middle" fill="{GRAY}" font-size="8" font-family="sans-serif">{sub}</text>'
    else:
        lines += f'<text x="{mx}" y="{y + h//2 + 4}" text-anchor="middle" fill="{tc}" font-size="9" font-family="sans-serif" font-weight="bold">{label}</text>'
    return lines

def clust(x, y, w, h, label="", stroke=BLUE, fill="none", lc=None, dash=False, fs=8):
    lc = lc or stroke
    da = ' stroke-dasharray="5,3"' if dash else ''
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.2"{da}/>'
    if label:
        out += f'<text x="{x+6}" y="{y+10}" fill="{lc}" font-size="{fs}" font-family="sans-serif" font-weight="bold">{label}</text>'
    return out

def arr(x1, y1, x2, y2, pid, suf="a", color=None, dash=False, label="", lx=None, ly=None):
    color = color or ARROW
    da = ' stroke-dasharray="4,3"' if dash else ''
    out = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.3"{da} marker-end="url(#{pid}{suf})"/>'
    if label:
        tx = lx if lx is not None else (x1+x2)//2
        ty = ly if ly is not None else min(y1,y2) - 4 if y1!=y2 else y1 - 5
        out += f'<text x="{tx}" y="{ty}" text-anchor="middle" fill="{LGRAY}" font-size="8" font-family="sans-serif">{label}</text>'
    return out

def txt(x, y, s, color=LGRAY, size=8, anchor="middle", bold=False):
    fw = ' font-weight="bold"' if bold else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{color}" font-size="{size}" font-family="sans-serif"{fw}>{s}</text>'

def wrap(pid, W, H, content):
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;max-width:{W}px;display:block;border-radius:8px;">'
            f'<rect width="{W}" height="{H}" rx="8" fill="{BG}"/>'
            + mk_defs(pid) + content + '</svg>')

# ── Diagram 1: SQL監査ログ (Q1-3) ──────────────────────────────────────────────
def d1():
    p = "d1"
    W, H = 640, 165
    c = ""
    # OK cluster (East US)
    c += clust(8, 22, 295, 130, "East US — 同一リージョン", stroke=GREEN, fill="#091a10", lc=LGREEN, dash=True)
    c += node(25, 65, 100, 36, "SQL Server", "East US")
    c += node(175, 65, 100, 36, "Storage Acct", "East US")
    c += arr(125, 83, 175, 83, p, "g", color=GREEN, label="監査ログ保存", ly=58)
    # NG cluster (West/Central US)
    c += clust(337, 22, 295, 130, "West US / Central US — 異なるリージョン", stroke=RED, fill="#1a0909", lc=LRED, dash=True)
    c += node(355, 65, 100, 36, "SQL Server", "West US")
    c += node(505, 65, 100, 36, "Storage Acct", "Central US")
    c += arr(455, 83, 505, 83, p, "r", color=RED, dash=True, label="設定不可", ly=58)
    # X mark
    c += f'<text x="480" y="80" text-anchor="middle" fill="{RED}" font-size="14" font-family="sans-serif" font-weight="bold">×</text>'
    return wrap(p, W, H, c)

# ── Diagram 2: 管理グループ階層 (Q9-10) ─────────────────────────────────────────
def d2():
    p = "d2"
    W, H = 640, 195
    c = ""
    # Root MG
    c += node(20, 80, 100, 36, "Tenant Root MG", tc=LBLUE)
    # MG-A cluster
    c += clust(155, 18, 120, 95, "MG-A (Dept A)", stroke=BLUE, dash=False, fs=8)
    c += node(165, 32, 100, 32, "MG-A")
    # Sub-A1, Sub-A2
    c += clust(310, 8, 100, 50, "", stroke=BLUE)
    c += node(315, 15, 88, 28, "Sub-A1", tc=LGRAY)
    c += clust(310, 68, 100, 50, "", stroke=BLUE)
    c += node(315, 75, 88, 28, "Sub-A2", tc=LGRAY)
    # MG-B cluster
    c += clust(155, 128, 120, 55, "MG-B (Dept B)", stroke=BLUE, dash=False, fs=8)
    c += node(165, 142, 100, 32, "MG-B")
    # Sub-B1
    c += clust(310, 128, 100, 55, "", stroke=BLUE)
    c += node(315, 142, 88, 32, "Sub-B1", tc=LGRAY)
    # Policy
    c += node(470, 80, 100, 36, "Azure Policy", sub="ポリシー継承", stroke=ORANGE, fill="#1a1209", tc=ORANGE)
    # Arrows: Root → MG-A, MG-B
    c += arr(120, 95, 155, 48, p, label="", color=ARROW)
    c += arr(120, 100, 155, 158, p, label="")
    # MG-A → Sub-A1, Sub-A2
    c += arr(265, 48, 315, 29, p)
    c += arr(265, 48, 315, 89, p)
    # MG-B → Sub-B1
    c += arr(265, 158, 315, 158, p)
    # Root → Policy (dashed)
    c += arr(120, 98, 470, 98, p, dash=True, color=LGRAY, label="ポリシー継承", ly=90)
    return wrap(p, W, H, c)

# ── Diagram 3: Front Door + マルチリージョン AKS (Q12) ─────────────────────────
def d3():
    p = "d3"
    W, H = 640, 175
    c = ""
    # Front Door
    c += node(20, 70, 115, 36, "Azure Front Door", sub="グローバル LB")
    # East US cluster + AKS
    c += clust(215, 15, 160, 65, "East US", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += node(225, 30, 140, 36, "AKS Cluster", sub="East US")
    # West US cluster + AKS
    c += clust(215, 95, 160, 65, "West US", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += node(225, 110, 140, 36, "AKS Cluster", sub="West US")
    # Container Registry
    c += node(440, 70, 130, 36, "Container", sub="Registry (共有)")
    # Arrows: FD → AKS East, West
    c += arr(135, 82, 225, 48, p, label="ルーティング", lx=178, ly=28)
    c += arr(135, 88, 225, 128, p)
    # ACR → AKS (dashed)
    c += arr(440, 80, 365, 48, p, dash=True, color=LGRAY, label="Image Pull", lx=405, ly=28)
    c += arr(440, 90, 365, 128, p, dash=True, color=LGRAY)
    return wrap(p, W, H, c)

# ── Diagram 4: Service Bus Pub/Sub (Q17) ───────────────────────────────────────
def d4():
    p = "d4"
    W, H = 640, 185
    c = ""
    # Publisher
    c += node(20, 75, 100, 36, "Publisher", sub="App Service")
    # Service Bus Topic cluster
    c += clust(175, 55, 120, 75, "Service Bus", stroke=BLUE, fill="#0d1e35", fs=8)
    c += node(185, 72, 100, 36, "Topic")
    # Subscribers
    c += clust(370, 18, 140, 145, "Subscribers", stroke=BLUE, fill="#0d1e35", fs=8)
    c += node(380, 32, 120, 32, "Sub 1", sub="Functions")
    c += node(380, 80, 120, 32, "Sub 2", sub="Logic Apps")
    c += node(380, 128, 120, 32, "Sub 3", sub="App Service")
    # Arrows
    c += arr(120, 93, 185, 90, p, label="Publish", ly=82)
    c += arr(285, 82, 380, 48, p, label="各サブへ配信", lx=330, ly=38)
    c += arr(285, 90, 380, 96, p)
    c += arr(285, 98, 380, 144, p)
    return wrap(p, W, H, c)

# ── Diagram 5: App Gateway + WAF (Q23-24) ──────────────────────────────────────
def d5():
    p = "d5"
    W, H = 640, 175
    c = ""
    c += node(15, 68, 90, 36, "Internet", tc=LGRAY, fill="#0a0f1a", stroke=GRAY)
    c += node(175, 68, 120, 36, "App Gateway", sub="WAF v2", stroke="#a855f7", tc="#d8b4fe", fill="#1a0d2e")
    c += node(380, 35, 110, 36, "App Service 1")
    c += node(380, 100, 110, 36, "App Service 2")
    c += node(175, 128, 100, 32, "Key Vault", sub="SSL 証明書", stroke="#f59e0b", tc=ORANGE, fill="#1a1205")
    # Arrows
    c += arr(105, 86, 175, 86, p, label="HTTPS", ly=78)
    c += arr(295, 76, 380, 53, p, label="L7 ルーティング", lx=335, ly=40)
    c += arr(295, 86, 380, 118, p)
    c += arr(225, 128, 235, 104, p, dash=True, color=ORANGE, suf="o", label="証明書", lx=270, ly=118)
    return wrap(p, W, H, c)

# ── Diagram 6: ADF パイプライン (Q28) ──────────────────────────────────────────
def d6():
    p = "d6"
    W, H = 640, 148
    c = ""
    # OnPrem cluster
    c += clust(8, 20, 130, 108, "On-premises", stroke=GRAY, fill="#10100a", lc=LGRAY, dash=True)
    c += node(18, 50, 110, 36, "SQL Server", sub="オンプレミス", fill="#1a160a", stroke=GRAY, tc=LGRAY)
    # ADF
    c += node(210, 55, 100, 36, "ADF", sub="Self-hosted IR")
    # Azure cluster
    c += clust(368, 20, 260, 108, "Azure", stroke=BLUE, fill="#0d1e35", dash=False)
    c += node(378, 50, 100, 36, "Blob Storage", sub="Staging")
    c += node(530, 50, 88, 36, "Synapse DW")
    # Arrows
    c += arr(128, 68, 210, 73, p, label="Copy via IR", ly=58)
    c += arr(310, 73, 378, 68, p, label="Stage", ly=58)
    c += arr(478, 68, 530, 68, p, label="Load", ly=58)
    return wrap(p, W, H, c)

# ── Diagram 7: Azure Bastion (Q42-43) ──────────────────────────────────────────
def d7():
    p = "d7"
    W, H = 640, 195
    c = ""
    c += node(15, 80, 90, 36, "管理者", sub="HTTPS ブラウザ", fill="#0a0f1a", stroke=GRAY, tc=LGRAY)
    # VNet outer cluster
    c += clust(145, 15, 480, 165, "Azure VNet", stroke=BLUE, fill="#0a1520", dash=False)
    # Bastion Subnet
    c += clust(160, 35, 160, 70, "AzureBastionSubnet", stroke=REGION, fill="#0a1020", lc="#4a9fd4", dash=True, fs=7)
    c += node(168, 52, 144, 36, "Azure Bastion")
    # VM Subnet
    c += clust(355, 35, 255, 135, "VM Subnet (Private)", stroke=BLUE, fill="#0d1e35", fs=7)
    c += node(370, 55, 120, 36, "Windows VM", sub="パブリックIP なし")
    c += node(370, 110, 120, 36, "Linux VM", sub="パブリックIP なし")
    # Arrows
    c += arr(105, 98, 168, 70, p, label="HTTPS:443", lx=135, ly=72)
    c += arr(312, 62, 370, 73, p, label="RDP", lx=340, ly=58)
    c += arr(312, 72, 370, 128, p, label="SSH", lx=337, ly=115)
    return wrap(p, W, H, c)

# ── Diagram 8: Front Door グローバル負荷分散 (Q44) ──────────────────────────────
def d8():
    p = "d8"
    W, H = 640, 175
    c = ""
    c += node(20, 70, 130, 36, "Azure Front Door", sub="Anycast / Edge POP")
    # 3 regions
    c += clust(260, 12, 155, 55, "East US", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += node(270, 25, 135, 35, "App Service", sub="East US")
    c += clust(260, 77, 155, 55, "West Europe", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += node(270, 90, 135, 35, "App Service", sub="West Europe")
    c += clust(260, 142, 155, 55, "SE Asia", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += node(270, 155, 135, 35, "App Service", sub="SE Asia")
    # Arrow labels
    c += arr(150, 85, 270, 42, p, label="最低レイテンシ", lx=208, ly=32)
    c += arr(150, 88, 270, 107, p)
    c += arr(150, 92, 270, 172, p)
    # Note
    c += txt(450, 170, "レイテンシ最小リージョンへ自動ルーティング", GRAY, 8)
    return wrap(p, W, H, c)

# ── Diagram 9: APIM + Entra ID (Q46-47) ────────────────────────────────────────
def d9():
    p = "d9"
    W, H = 640, 195
    c = ""
    c += node(15, 88, 90, 36, "Client", sub="SPA / Mobile")
    c += node(185, 18, 100, 36, "Entra ID", stroke="#8b5cf6", tc="#c4b5fd", fill="#13082e")
    c += node(185, 88, 120, 36, "API Management")
    # Backend cluster
    c += clust(400, 55, 230, 110, "Backend", stroke=BLUE, fill="#0d1e35")
    c += node(415, 70, 120, 36, "API 1", sub="App Service")
    c += node(415, 125, 120, 36, "API 2", sub="Functions")
    # Arrows numbered
    c += arr(60, 82, 185, 36, p, label="① 認証要求", lx=120, ly=46)
    c += arr(185, 54, 70, 88, p, dash=True, color="#8b5cf6", suf="a", label="② JWT Token", lx=115, ly=60)
    c += arr(105, 106, 185, 106, p, label="③ Bearer", ly=97)
    c += arr(305, 93, 415, 88, p, label="④ 転送", ly=82)
    c += arr(305, 106, 415, 143, p)
    return wrap(p, W, H, c)

# ── Diagram 10: AMPLS (Q55) ────────────────────────────────────────────────────
def d10():
    p = "d10"
    W, H = 640, 175
    c = ""
    # VNet cluster
    c += clust(8, 20, 280, 135, "Azure VNet (Private)", stroke=BLUE, fill="#0a1520", dash=False)
    c += node(22, 65, 90, 36, "Azure VM", sub="監視対象")
    c += node(150, 65, 120, 36, "Private Endpoint")
    # AMPLS cluster
    c += clust(330, 12, 210, 150, "AMPLS", stroke=REGION, fill="#0a1020", lc="#4a9fd4", dash=True)
    c += node(345, 35, 175, 36, "Log Analytics WS")
    c += node(345, 90, 175, 36, "Application Insights")
    # Monitor
    c += node(560, 65, 72, 36, "Azure Monitor", tc=LGRAY, fill="#0d1020", stroke=GRAY)
    # Arrows
    c += arr(112, 83, 150, 83, p, label="", )
    c += arr(270, 76, 345, 53, p, label="Private 通信", lx=305, ly=42)
    c += arr(270, 90, 345, 108, p)
    c += arr(520, 53, 560, 76, p)
    c += arr(520, 108, 560, 90, p)
    return wrap(p, W, H, c)

SVGS = {
    "SQL監査ログの構成（Q1-3）":                        d1(),
    "管理グループ階層（Q9-10）":                         d2(),
    "Azure Front Door + マルチリージョン AKS（Q12）":    d3(),
    "Service Bus トピック（Pub/Sub）（Q17）":            d4(),
    "Application Gateway + WAF アーキテクチャ（Q23-24）":d5(),
    "Azure Data Factory パイプライン（Q28）":            d6(),
    "Azure Bastion 構成（Q42-43）":                     d7(),
    "Azure Front Door グローバル負荷分散（Q44）":        d8(),
    "API Management + Entra ID（Q46-47）":              d9(),
    "Azure Monitor Private Link Scope / AMPLS（Q55）":  d10(),
}

# ── Embed into vol2.html ────────────────────────────────────────────────────────
with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"(const QUESTIONS = )(\[.*?\]);", content, re.DOTALL)
prefix = m.group(1)
qs = json.loads(m.group(2))

updated = 0
for q in qs:
    exp = q.get("exp_html", "")
    matched_title = None
    for title in SVGS:
        if title in exp:
            matched_title = title
            break
    if not matched_title:
        continue
    svg_html = (f'<div class="arch-box">'
                f'<div class="arch-title">{matched_title}</div>'
                f'{SVGS[matched_title]}'
                f'</div>')
    new_exp = re.sub(
        r'<div class="arch-box">.*?(?=<div class="exp-sections")',
        svg_html,
        exp, count=1, flags=re.DOTALL
    )
    if new_exp != exp:
        q["exp_html"] = new_exp
        updated += 1
        print(f"  Q{q['num']}: embedded SVG for «{matched_title[:30]}»")

new_json = json.dumps(qs, ensure_ascii=False, separators=(",", ":"))
new_content = content[:m.start()] + prefix + new_json + ";" + content[m.end():]

with open(PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"\nDone: updated {updated} questions in {PATH}")
