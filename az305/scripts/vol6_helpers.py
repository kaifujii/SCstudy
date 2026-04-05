"""Shared helpers for vol6 HTML generation: icons, SVG, exp_html builders."""
import re, os

ICON_BASE = "/Users/fujiikai/Downloads/Azure_Public_Service_Icons/Icons"

# ── Icon paths ─────────────────────────────────────────────────────────────────
P = {
    "entra_apps":   "identity/10225-icon-service-Enterprise-Applications.svg",
    "entra_proxy":  "identity/02386-icon-service-API-Proxy.svg",
    "entra_ca":     "security/10233-icon-service-Conditional-Access.svg",
    "entra_pim":    "identity/02251-icon-service-Entra-Privleged-Identity-Management.svg",
    "entra_id_prot":"identity/10231-icon-service-Entra-ID-Protection.svg",
    "entra_mi":     "identity/10227-icon-service-Entra-Managed-Identities.svg",
    "entra_user":   "identity/10230-icon-service-Users.svg",
    "entra_cond":   "security/10233-icon-service-Conditional-Access.svg",
    "sql_db":       "databases/10130-icon-service-SQL-Database.svg",
    "sql_mi":       "databases/10136-icon-service-SQL-Managed-Instance.svg",
    "sql_server":   "databases/10132-icon-service-SQL-Server.svg",
    "azure_sql":    "databases/02390-icon-service-Azure-SQL.svg",
    "cosmos":       "databases/10121-icon-service-Azure-Cosmos-DB.svg",
    "storage":      "storage/10086-icon-service-Storage-Accounts.svg",
    "azure_files":  "storage/10400-icon-service-Azure-Fileshares.svg",
    "adls":         "storage/10090-icon-service-Data-Lake-Storage-Gen1.svg",
    "blob":         "general/10780-icon-service-Blob-Block.svg",
    "vwan":         "networking/10353-icon-service-Virtual-WANs.svg",
    "vwan_hub":     "networking/00860-icon-service-Virtual-WAN-Hub.svg",
    "expressroute": "networking/10079-icon-service-ExpressRoute-Circuits.svg",
    "traffic_mgr":  "networking/10065-icon-service-Traffic-Manager-Profiles.svg",
    "app_gw":       "networking/10076-icon-service-Application-Gateways.svg",
    "nwatcher":     "networking/10066-icon-service-Network-Watcher.svg",
    "vnet":         "networking/10061-icon-service-Virtual-Networks.svg",
    "functions":    "compute/10029-icon-service-Function-Apps.svg",
    "vm":           "compute/10021-icon-service-Virtual-Machine.svg",
    "app_svc":      "web/10035-icon-service-App-Services.svg",
    "kv":           "security/10245-icon-service-Key-Vaults.svg",
    "recovery":     "management + governance/00017-icon-service-Recovery-Services-Vaults.svg",
    "databricks":   "analytics/10787-icon-service-Azure-Databricks.svg",
    "synapse":      "analytics/00606-icon-service-Azure-Synapse-Analytics.svg",
    "servicebus":   "integration/10836-icon-service-Azure-Service-Bus.svg",
    "adf":          "integration/10126-icon-service-Data-Factories.svg",
    "law":          "monitor/00009-icon-service-Log-Analytics-Workspaces.svg",
    "appins":       "monitor/00012-icon-service-Application-Insights.svg",
    "monitor":      "monitor/00001-icon-service-Monitor.svg",
    "sub":          "general/10002-icon-service-Subscriptions.svg",
    "rg":           "general/10007-icon-service-Resource-Groups.svg",
    "event_grid":   "integration/10068-icon-service-Event-Grid-Topics.svg",
    "event_hub":    "analytics/10835-icon-service-Event-Hubs.svg",
}

_icon_cache = {}

def icon(key_or_path, uid):
    """Load SVG icon by P-key or rel path, return inner SVG content with prefixed IDs."""
    rel = P.get(key_or_path, key_or_path)
    path = f"{ICON_BASE}/{rel}"
    if path not in _icon_cache:
        try:
            with open(path, encoding='utf-8') as f:
                raw = f.read()
        except FileNotFoundError:
            return f'<rect width="18" height="18" rx="3" fill="#555"/>'
        raw = re.sub(r'<\?xml[^>]*\?>', '', raw)
        raw = re.sub(r'<!DOCTYPE[^>]*>', '', raw)
        inner = re.sub(r'<svg[^>]*>', '', raw, count=1)
        inner = re.sub(r'</svg>\s*$', '', inner).strip()
        _icon_cache[path] = inner
    inner = _icon_cache[path]
    # Prefix all IDs to avoid collisions
    ids = re.findall(r'\bid="([^"]+)"', inner)
    for id_ in set(ids):
        inner = inner.replace(f'id="{id_}"', f'id="{uid}_{id_}"')
        inner = inner.replace(f'url(#{id_})', f'url(#{uid}_{id_})')
        inner = re.sub(rf'href="#{re.escape(id_)}"', f'href="#{uid}_{id_}"', inner)
        inner = re.sub(rf'xlink:href="#{re.escape(id_)}"', f'xlink:href="#{uid}_{id_}"', inner)
    return inner

_uid_counter = [0]
def uid(prefix="ic"):
    _uid_counter[0] += 1
    return f"{prefix}_{_uid_counter[0]}"

def embed_icon(cx, cy, size, icon_inner):
    """Embed icon SVG centered at (cx, cy)."""
    x, y = cx - size // 2, cy - size // 2
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 18 18">{icon_inner}</svg>'

# ── SVG diagram wrapper ────────────────────────────────────────────────────────
DARK_BG = "#0d1b2e"
ARROW_COLOR = "#4a9fd4"
ARROW_OK = "#22c55e"
ARROW_NG = "#ef4444"
NODE_FILL = "#112240"
NODE_STROKE = "#2563eb"
LABEL_COLOR = "#c8d8f0"
SUB_COLOR = "#64748b"

def wrap(pid, W, H, content, extra_defs=""):
    """Wrap content in full SVG with dark bg and standard arrow markers."""
    defs = f"""<defs>
  <marker id="{pid}a" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{ARROW_COLOR}"/></marker>
  <marker id="{pid}g" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{ARROW_OK}"/></marker>
  <marker id="{pid}r" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{ARROW_NG}"/></marker>
  {extra_defs}
</defs>"""
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;max-width:{W}px;display:block;margin:8px auto;border-radius:8px;">'
            f'<rect width="{W}" height="{H}" rx="8" fill="{DARK_BG}"/>'
            f'{defs}{content}</svg>')

def arr(x1, y1, x2, y2, pid, mk="a", dash=False, label="", lx=None, ly=None, via=None, color=None):
    """Orthogonal arrow from (x1,y1) to (x2,y2). Uses L-bend via bx."""
    if color:
        stroke = color
        m = f'<defs><marker id="{pid}_cc" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="{color}"/></marker></defs>'
        mk_ref = f"url(#{pid}_cc)"
        extra = m
    else:
        stroke = {"a": ARROW_COLOR, "g": ARROW_OK, "r": ARROW_NG}.get(mk, ARROW_COLOR)
        mk_ref = f"url(#{pid}{mk})"
        extra = ""
    da = ' stroke-dasharray="4,3"' if dash else ''
    if x1 == x2 or y1 == y2:
        d = f"M{x1},{y1} L{x2},{y2}"
    else:
        bx = via if via is not None else x2
        d = f"M{x1},{y1} L{bx},{y1} L{bx},{y2} L{x2},{y2}"
    out = f'{extra}<path d="{d}" stroke="{stroke}" stroke-width="1.4" fill="none"{da} marker-end="{mk_ref}"/>'
    if label:
        tx = lx if lx is not None else (x1 + x2) // 2
        ty = ly if ly is not None else y1 - 5
        out += f'<text x="{tx}" y="{ty}" text-anchor="middle" fill="{SUB_COLOR}" font-size="8" font-family="sans-serif">{label}</text>'
    return out

def node(x, y, w, h, icon_key, label, sub="", stroke=None, fill=None):
    """Draw a service node box with icon (top center) and label."""
    uid_s = uid("nd")
    ic = icon(icon_key, uid_s) if icon_key else ""
    s = stroke or NODE_STROKE
    f = fill or NODE_FILL
    icon_size = 14
    icon_x = x + w // 2
    icon_y = y + 10 + icon_size // 2
    label_y = y + 10 + icon_size + 11
    sub_y = label_y + 11
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="1.5"/>'
    if ic:
        out += embed_icon(icon_x, icon_y, icon_size, ic)
    out += f'<text x="{x+w//2}" y="{label_y}" text-anchor="middle" fill="{LABEL_COLOR}" font-size="9" font-family="sans-serif" font-weight="600">{label}</text>'
    if sub:
        out += f'<text x="{x+w//2}" y="{sub_y}" text-anchor="middle" fill="{SUB_COLOR}" font-size="8" font-family="sans-serif">{sub}</text>'
    return out

def label_box(x, y, w, h, text, fill="#1a2f4a", stroke="#334e6a", color=LABEL_COLOR, font_size=9):
    """A simple labeled rectangle (cluster/region box)."""
    lines = text.split('\n')
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>'
    for i, line in enumerate(lines):
        out += f'<text x="{x+6}" y="{y+12+i*11}" fill="{color}" font-size="{font_size}" font-family="sans-serif" font-weight="600">{line}</text>'
    return out

# ── exp_html HTML helpers ──────────────────────────────────────────────────────
def svc(key, name, sz=14):
    """Inline service icon + bold name for use in HTML text."""
    u = uid("sv")
    ic = icon(key, u)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="{sz}" height="{sz}" '
            f'style="vertical-align:middle;margin-right:3px;display:inline-block">{ic}</svg>'
            f'<strong style="font-size:0.85em">{name}</strong>')

def tbl(headers, rows, caption=None):
    """Build an exp-table HTML table."""
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''
    for row in rows:
        tds = ''.join(f'<td>{c}</td>' for c in row)
        trs += f'<tr>{tds}</tr>'
    cap = f'<caption style="text-align:left;font-size:0.75rem;font-weight:700;color:#3d4966;padding:4px 0 2px">{caption}</caption>' if caption else ''
    return f'<table class="exp-table">{cap}<thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'

def blk_correct(label, body):
    return f'<div class="exp-block exp-correct"><div class="exp-block-label">✓ {label}</div><div class="exp-block-body">{body}</div></div>'

def blk_wrong(label, body):
    return f'<div class="exp-block exp-wrong"><div class="exp-block-label">✗ {label}</div><div class="exp-block-body">{body}</div></div>'

def blk_key(label, body):
    return f'<div class="exp-block exp-key"><div class="exp-block-label">💡 {label}</div><div class="exp-block-body">{body}</div></div>'

def exp_wrap(*blocks):
    return '<div class="exp-sections">' + ''.join(blocks) + '</div>'
