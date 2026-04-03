"""Replace vol2 arch-box img tags with compact dark inline SVGs (like vol5 style)."""
import re, json

PATH = "az305/vol2.html"
ICON_BASE = "/Users/fujiikai/Downloads/Azure_Public_Service_Icons/Icons"

BG    = "#0d1b2e"; NAVY  = "#152844"; BLUE  = "#2563eb"; LBLUE = "#93c5fd"
GRAY  = "#64748b"; LGRAY = "#94a3b8"; GREEN = "#22c55e"; LGREEN= "#86efac"
RED   = "#ef4444"; LRED  = "#fca5a5"; ARROW = "#4a9fd4"; REGION= "#1e5a8a"
ORANGE= "#f59e0b"

# ── icon helpers ────────────────────────────────────────────────────────────────
def _load_icon_inner(path, uid):
    with open(path) as f:
        raw = f.read()
    inner = re.sub(r'^<svg[^>]*>', '', raw.strip())
    inner = re.sub(r'</svg>\s*$', '', inner)
    inner = re.sub(r'id="([^"]+)"', lambda m: f'id="{uid}_{m.group(1)}"', inner)
    inner = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{uid}_{m.group(1)})', inner)
    inner = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{uid}_{m.group(1)}"', inner)
    return inner

_icon_cache = {}
def icon(rel_path, uid):
    """Return inner SVG content with unique IDs for the given icon file."""
    if rel_path not in _icon_cache:
        _icon_cache[rel_path] = open(f"{ICON_BASE}/{rel_path}").read()
    raw = _icon_cache[rel_path]
    inner = re.sub(r'^<svg[^>]*>', '', raw.strip())
    inner = re.sub(r'</svg>\s*$', '', inner)
    inner = re.sub(r'id="([^"]+)"', lambda m: f'id="{uid}_{m.group(1)}"', inner)
    inner = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{uid}_{m.group(1)})', inner)
    inner = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{uid}_{m.group(1)}"', inner)
    return inner

def embed_icon(cx, y, size, icon_inner):
    """Embed a 18x18-viewBox icon centered at cx, top at y."""
    x = cx - size // 2
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg">{icon_inner}</svg>'

def inode(x, y, w, h, icon_inner, label, sub="", tc=LBLUE, fill=NAVY, stroke=BLUE):
    """Node with icon on top, label below, optional sub-label."""
    mx = x + w // 2
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
    icon_size = 14
    if sub:
        out += embed_icon(mx, y + 5, icon_size, icon_inner)
        out += f'<text x="{mx}" y="{y + 5 + icon_size + 10}" text-anchor="middle" fill="{tc}" font-size="8" font-family="sans-serif" font-weight="bold">{label}</text>'
        out += f'<text x="{mx}" y="{y + h - 5}" text-anchor="middle" fill="{GRAY}" font-size="7" font-family="sans-serif">{sub}</text>'
    else:
        out += embed_icon(mx, y + 5, icon_size, icon_inner)
        out += f'<text x="{mx}" y="{y + 5 + icon_size + 11}" text-anchor="middle" fill="{tc}" font-size="8" font-family="sans-serif" font-weight="bold">{label}</text>'
    return out

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

# icon path constants
P_SQL    = "databases/10132-icon-service-SQL-Server.svg"
P_STOR   = "storage/10086-icon-service-Storage-Accounts.svg"
P_BLOB   = "general/10780-icon-service-Blob-Block.svg"
P_MG     = "general/10011-icon-service-Management-Groups.svg"
P_SUB    = "general/10002-icon-service-Subscriptions.svg"
P_POL    = "management + governance/10316-icon-service-Policy.svg"
P_FD     = "networking/10073-icon-service-Front-Door-and-CDN-Profiles.svg"
P_AKS    = "compute/10023-icon-service-Kubernetes-Services.svg"
P_ACR    = "containers/10105-icon-service-Container-Registries.svg"
P_SB     = "integration/10836-icon-service-Azure-Service-Bus.svg"
P_APP    = "web/10035-icon-service-App-Services.svg"
P_FUNC   = "compute/10029-icon-service-Function-Apps.svg"
P_LOGIC  = "integration/02631-icon-service-Logic-Apps.svg"
P_AGW    = "networking/10076-icon-service-Application-Gateways.svg"
P_KV     = "security/10245-icon-service-Key-Vaults.svg"
P_ADF    = "integration/10126-icon-service-Data-Factories.svg"
P_SYNAPSE= "analytics/00606-icon-service-Azure-Synapse-Analytics.svg"
P_BASTION= "networking/02422-icon-service-Bastions.svg"
P_APIM   = "integration/10042-icon-service-API-Management-Services.svg"
P_ENTRA  = "identity/10227-icon-service-Entra-Managed-Identities.svg"
P_LAW    = "monitor/00009-icon-service-Log-Analytics-Workspaces.svg"
P_APPINS = "monitor/00012-icon-service-Application-Insights.svg"
P_MON    = "monitor/00001-icon-service-Monitor.svg"
P_PE     = "other/02579-icon-service-Private-Endpoints.svg"

def _ic(path, uid): return icon(path, uid)

# ── Diagram 1: SQL監査ログ (Q1-3) ──────────────────────────────────────────────
def d1():
    p = "d1"
    W, H = 640, 185
    c = ""
    # OK cluster (East US)
    c += clust(8, 18, 295, 155, "East US — 同一リージョン", stroke=GREEN, fill="#091a10", lc=LGREEN, dash=True)
    c += inode(25,  48, 110, 52, _ic(P_SQL,  "d1sq1"), "SQL Server",    sub="East US",    tc=LBLUE)
    c += inode(170, 48, 110, 52, _ic(P_STOR, "d1st1"), "Storage Acct",  sub="East US",    tc=LBLUE)
    c += arr(135, 74, 170, 74, p, "g", color=GREEN, label="監査ログ保存", ly=44)
    # NG cluster (West/Central US)
    c += clust(337, 18, 295, 155, "West US / Central US — 異なるリージョン", stroke=RED, fill="#1a0909", lc=LRED, dash=True)
    c += inode(355, 48, 110, 52, _ic(P_SQL,  "d1sq2"), "SQL Server",    sub="West US",    tc=LGRAY,  stroke=GRAY, fill="#1a100a")
    c += inode(500, 48, 110, 52, _ic(P_STOR, "d1st2"), "Storage Acct",  sub="Central US", tc=LGRAY,  stroke=GRAY, fill="#1a100a")
    c += arr(465, 74, 500, 74, p, "r", color=RED, dash=True, label="設定不可", ly=44)
    c += f'<text x="482" y="72" text-anchor="middle" fill="{RED}" font-size="13" font-family="sans-serif" font-weight="bold">×</text>'
    return wrap(p, W, H, c)

# ── Diagram 2: 管理グループ階層 (Q9-10) ─────────────────────────────────────────
def d2():
    p = "d2"
    W, H = 640, 235
    # Icon paths
    MG_PATH  = "general/10011-icon-service-Management-Groups.svg"
    SUB_PATH = "general/10002-icon-service-Subscriptions.svg"
    POL_PATH = "management + governance/10316-icon-service-Policy.svg"

    c = ""
    # ── Row 1: Tenant Root MG (center top) ──────────────────────────────────────
    # node box: x=250, y=10, w=140, h=52  → cx=320
    c += inode(250, 10, 140, 52, icon(MG_PATH, "mg_root"), "Tenant Root MG")
    # ── Row 2: MG-A (left), MG-B (right) ────────────────────────────────────────
    # MG-A cluster: x=62, y=100, w=150, h=65
    c += clust(62, 100, 150, 65, "MG-A  (Dept A)", stroke=BLUE, fill="#0d1e35", fs=8)
    c += inode(72, 113, 130, 48, icon(MG_PATH, "mg_a"), "MG-A")
    # MG-B cluster: x=428, y=100, w=150, h=65
    c += clust(428, 100, 150, 65, "MG-B  (Dept B)", stroke=BLUE, fill="#0d1e35", fs=8)
    c += inode(438, 113, 130, 48, icon(MG_PATH, "mg_b"), "MG-B")
    # ── Row 3: Sub-A1, Sub-A2, Sub-B1, Policy ────────────────────────────────────
    # Sub-A1: x=20, y=200
    c += inode(20, 197, 98, 32, icon(SUB_PATH, "sub_a1"), "Sub-A1", tc=LGRAY, stroke=GRAY, fill="#101a28")
    # Sub-A2: x=130, y=200
    c += inode(130, 197, 98, 32, icon(SUB_PATH, "sub_a2"), "Sub-A2", tc=LGRAY, stroke=GRAY, fill="#101a28")
    # Sub-B1: x=388, y=200
    c += inode(388, 197, 98, 32, icon(SUB_PATH, "sub_b1"), "Sub-B1", tc=LGRAY, stroke=GRAY, fill="#101a28")
    # Policy: x=502, y=197
    c += inode(502, 197, 120, 32, icon(POL_PATH, "pol"), "Azure Policy", tc=ORANGE, stroke=ORANGE, fill="#1a1205")
    # ── Arrows ───────────────────────────────────────────────────────────────────
    # Root(320,62) → MG-A center(137,100)
    c += arr(295, 62, 145, 100, p)
    # Root(320,62) → MG-B center(503,100)
    c += arr(345, 62, 495, 100, p)
    # MG-A(137,165) → Sub-A1 center(69,197)
    c += arr(110, 165, 69, 197, p)
    # MG-A(137,165) → Sub-A2 center(179,197)
    c += arr(164, 165, 179, 197, p)
    # MG-B(503,165) → Sub-B1 center(437,197)
    c += arr(476, 165, 437, 197, p)
    # Root → Policy (dashed, inheritance)
    c += arr(390, 36, 502, 208, p, dash=True, color=LGRAY, label="ポリシー継承", lx=470, ly=105)
    return wrap(p, W, H, c)

# ── Diagram 3: Front Door + マルチリージョン AKS (Q12) ─────────────────────────
def d3():
    p = "d3"
    W, H = 640, 210
    c = ""
    c += inode(15, 80, 130, 52, _ic(P_FD,  "d3fd"),  "Azure Front Door", sub="グローバル LB")
    c += clust(220, 12, 170, 82, "East US",  stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += inode(230, 26, 150, 52, _ic(P_AKS, "d3ak1"), "AKS Cluster",      sub="East US")
    c += clust(220, 110, 170, 82, "West US", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += inode(230, 124, 150, 52, _ic(P_AKS,"d3ak2"), "AKS Cluster",      sub="West US")
    c += inode(455, 80, 150, 52, _ic(P_ACR, "d3acr"), "Container",        sub="Registry (共有)")
    c += arr(145, 100, 230, 52, p,  label="ルーティング", lx=185, ly=36)
    c += arr(145, 108, 230, 150, p)
    c += arr(455, 90,  380, 52, p,  dash=True, color=LGRAY, label="Image Pull", lx=418, ly=36)
    c += arr(455, 100, 380, 150, p, dash=True, color=LGRAY)
    return wrap(p, W, H, c)

# ── Diagram 4: Service Bus Pub/Sub (Q17) ───────────────────────────────────────
def d4():
    p = "d4"
    W, H = 640, 220
    c = ""
    c += inode(15, 84, 115, 52, _ic(P_APP, "d4pub"), "Publisher", sub="App Service")
    c += clust(182, 60, 130, 100, "Service Bus", stroke=BLUE, fill="#0d1e35", fs=8)
    c += inode(192, 76, 110, 52,  _ic(P_SB,   "d4sb"),  "Topic")
    c += clust(380, 18, 155, 185, "Subscribers", stroke=BLUE, fill="#0d1e35", fs=8)
    c += inode(390, 32,  135, 50, _ic(P_FUNC,  "d4f1"),  "Sub 1", sub="Functions")
    c += inode(390, 95,  135, 50, _ic(P_LOGIC, "d4l1"),  "Sub 2", sub="Logic Apps")
    c += inode(390, 158, 135, 50, _ic(P_APP,   "d4a1"),  "Sub 3", sub="App Service")
    c += arr(130, 110, 192, 102, p, label="Publish", ly=94)
    c += arr(312, 94,  390, 57, p, label="各サブへ配信", lx=348, ly=44)
    c += arr(312, 102, 390, 120, p)
    c += arr(312, 110, 390, 183, p)
    return wrap(p, W, H, c)

# ── Diagram 5: App Gateway + WAF (Q23-24) ──────────────────────────────────────
def d5():
    p = "d5"
    W, H = 640, 210
    c = ""
    c += inode(10,  80, 100, 52, _ic(P_FD,  "d5inet"), "Internet",       tc=LGRAY, fill="#0a0f1a", stroke=GRAY)
    c += inode(175, 55, 130, 52, _ic(P_AGW, "d5agw"),  "App Gateway",    sub="WAF v2", stroke="#a855f7", tc="#d8b4fe", fill="#1a0d2e")
    c += inode(175,130, 115, 52, _ic(P_KV,  "d5kv"),   "Key Vault",      sub="SSL 証明書", stroke=ORANGE, tc=ORANGE, fill="#1a1205")
    c += inode(390, 40, 130, 52, _ic(P_APP, "d5ap1"),  "App Service 1")
    c += inode(390,120, 130, 52, _ic(P_APP, "d5ap2"),  "App Service 2")
    c += arr(110, 106, 175, 81, p, label="HTTPS", ly=82)
    c += arr(305,  81, 390, 66, p, label="L7 ルーティング", lx=344, ly=52)
    c += arr(305,  92, 390, 146, p)
    c += arr(235, 145, 240, 107, p, dash=True, color=ORANGE, suf="o", label="証明書", lx=278, ly=136)
    return wrap(p, W, H, c)

# ── Diagram 6: ADF パイプライン (Q28) ──────────────────────────────────────────
def d6():
    p = "d6"
    W, H = 640, 170
    c = ""
    c += clust(8, 15, 145, 138, "On-premises", stroke=GRAY, fill="#10100a", lc=LGRAY, dash=True)
    c += inode(18, 46, 125, 52, _ic(P_SQL,    "d6sq"),  "SQL Server",   sub="オンプレミス", fill="#1a160a", stroke=GRAY, tc=LGRAY)
    c += inode(215, 60, 115, 52, _ic(P_ADF,   "d6adf"), "ADF",          sub="Self-hosted IR")
    c += clust(385, 15, 248, 138, "Azure", stroke=BLUE, fill="#0d1e35")
    c += inode(395, 46, 110, 52, _ic(P_BLOB,   "d6bl"),  "Blob Storage", sub="Staging")
    c += inode(520, 46, 105, 52, _ic(P_SYNAPSE,"d6sy"),  "Synapse DW")
    c += arr(143, 72, 215, 86, p, label="Copy via IR", ly=62)
    c += arr(330, 86, 395, 72, p, label="Stage",       ly=62)
    c += arr(505, 72, 520, 72, p, label="Load",        ly=62)
    return wrap(p, W, H, c)

# ── Diagram 7: Azure Bastion (Q42-43) ──────────────────────────────────────────
def d7():
    p = "d7"
    W, H = 640, 225
    c = ""
    c += inode(10, 86, 105, 52, _ic(P_APP,    "d7adm"), "管理者",     sub="HTTPS ブラウザ", fill="#0a0f1a", stroke=GRAY, tc=LGRAY)
    c += clust(150, 12, 480, 200, "Azure VNet", stroke=BLUE, fill="#0a1520")
    c += clust(165, 32, 175, 100, "AzureBastionSubnet", stroke=REGION, fill="#0a1020", lc="#4a9fd4", dash=True, fs=7)
    c += inode(172, 50, 160, 52, _ic(P_BASTION,"d7bas"), "Azure Bastion")
    c += clust(370, 32, 248, 168, "VM Subnet (Private)", stroke=BLUE, fill="#0d1e35", fs=7)
    c += inode(382, 50,  120, 52, _ic(P_APP,   "d7vm1"), "Windows VM",  sub="パブリックIP なし")
    c += inode(382, 130, 120, 52, _ic(P_APP,   "d7vm2"), "Linux VM",    sub="パブリックIP なし")
    c += arr(115, 112, 172, 76, p, label="HTTPS:443", lx=140, ly=76)
    c += arr(340,  76, 382, 76,  p, label="RDP", lx=360, ly=66)
    c += arr(340,  90, 382, 156, p, label="SSH", lx=356, ly=140)
    return wrap(p, W, H, c)

# ── Diagram 8: Front Door グローバル負荷分散 (Q44) ──────────────────────────────
def d8():
    p = "d8"
    W, H = 640, 210
    c = ""
    c += inode(15, 80, 145, 52, _ic(P_FD,  "d8fd"),  "Azure Front Door", sub="Anycast / Edge POP")
    c += clust(260, 8,  185, 72, "East US",    stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += inode(270, 22, 165, 50, _ic(P_APP, "d8ap1"), "App Service",      sub="East US")
    c += clust(260, 90, 185, 72, "West Europe", stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += inode(270,104, 165, 50, _ic(P_APP, "d8ap2"), "App Service",      sub="West Europe")
    c += clust(260,172, 185, 72, "SE Asia",     stroke=REGION, fill="#0a1520", lc="#4a9fd4", dash=True)
    c += inode(270,186, 165, 50, _ic(P_APP, "d8ap3"), "App Service",      sub="SE Asia")
    c += arr(160, 100, 270, 47,  p, label="最低レイテンシ", lx=212, ly=36)
    c += arr(160, 106, 270, 129, p)
    c += arr(160, 112, 270, 211, p)
    return wrap(p, W, H, c)

# ── Diagram 9: APIM + Entra ID (Q46-47) ────────────────────────────────────────
def d9():
    p = "d9"
    W, H = 640, 230
    c = ""
    c += inode(10,  95, 105, 52, _ic(P_APP,   "d9cli"),  "Client",         sub="SPA / Mobile")
    c += inode(195, 15, 115, 52, _ic(P_ENTRA, "d9eid"),  "Entra ID",       stroke="#8b5cf6", tc="#c4b5fd", fill="#13082e")
    c += inode(185, 95, 135, 52, _ic(P_APIM,  "d9apim"), "API Management")
    c += clust(408, 60, 225, 140, "Backend", stroke=BLUE, fill="#0d1e35")
    c += inode(418, 74,  120, 52, _ic(P_APP,  "d9ap1"),  "API 1",          sub="App Service")
    c += inode(418, 142, 120, 52, _ic(P_FUNC, "d9fn1"),  "API 2",          sub="Functions")
    c += arr(72,  89,  210, 41, p, label="① 認証要求",  lx=138, ly=52)
    c += arr(195, 67,  78, 107, p, dash=True, color="#8b5cf6", suf="a", label="② JWT Token", lx=130, ly=72)
    c += arr(115, 121, 185, 121, p, label="③ Bearer",  ly=112)
    c += arr(320, 108, 418, 100, p, label="④ 転送",    ly=94)
    c += arr(320, 121, 418, 168, p)
    return wrap(p, W, H, c)

# ── Diagram 10: AMPLS (Q55) ────────────────────────────────────────────────────
def d10():
    p = "d10"
    W, H = 640, 210
    c = ""
    c += clust(8, 18, 308, 172, "Azure VNet (Private)", stroke=BLUE, fill="#0a1520")
    c += inode(20,  68, 110, 52, _ic(P_APP, "d10vm"), "Azure VM",        sub="監視対象")
    c += inode(155, 68, 148, 52, _ic(P_PE,  "d10pe"), "Private Endpoint")
    c += clust(340, 10, 230, 188, "AMPLS", stroke=REGION, fill="#0a1020", lc="#4a9fd4", dash=True)
    c += inode(350, 28,  210, 52, _ic(P_LAW,    "d10law"), "Log Analytics WS")
    c += inode(350, 100, 210, 52, _ic(P_APPINS, "d10ai"),  "Application Insights")
    c += inode(550, 80,  85,  52, _ic(P_MON,    "d10mon"), "Azure Monitor",  tc=LGRAY, fill="#0d1020", stroke=GRAY)
    c += arr(130,  94, 155, 94, p)
    c += arr(303,  84, 350, 54, p, label="Private 通信", lx=324, ly=44)
    c += arr(303,  98, 350, 126, p)
    c += arr(560,  80, 595, 104, p)
    c += arr(560, 100, 595, 108, p)
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
