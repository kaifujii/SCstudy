"""
Inject real Azure SVG icons into vol2.html exp-block-body text.
Replaces existing .az-ic text badges with inline SVG icons wrapped in .az-svc spans.
"""
import re, json, os

ICONS_BASE = "/Users/fujiikai/Downloads/Azure_Public_Service_Icons/Icons"
HTML_PATH  = "az305/vol2.html"

# ── Service → SVG file path ────────────────────────────────────────────────────
ICON_FILES = {
    # Identity
    "Microsoft Entra ID":    "identity/10231-icon-service-Entra-ID-Protection.svg",
    "Entra ID":              "identity/10231-icon-service-Entra-ID-Protection.svg",
    "Azure AD":              "identity/10231-icon-service-Entra-ID-Protection.svg",
    "Managed Identity":      "identity/10227-icon-service-Managed-Identities.svg",
    "Managed Identities":    "identity/10227-icon-service-Managed-Identities.svg",
    # Compute
    "AKS":                   "compute/10023-icon-service-Kubernetes-Services.svg",
    "Azure Kubernetes Service": "compute/10023-icon-service-Kubernetes-Services.svg",
    "Azure Functions":       "compute/10029-icon-service-Function-Apps.svg",
    "Functions App":         "compute/10029-icon-service-Function-Apps.svg",
    "App Service":           "web/10035-icon-service-App-Services.svg",
    "Azure Container Registry": "containers/10105-icon-service-Container-Registries.svg",
    "ACR":                   "containers/10105-icon-service-Container-Registries.svg",
    "Azure VM":              "compute/10021-icon-service-Virtual-Machine.svg",
    "仮想マシン":             "compute/10021-icon-service-Virtual-Machine.svg",
    # Networking
    "Azure Front Door":      "networking/10073-icon-service-Front-Door-and-CDN-Profiles.svg",
    "Front Door":            "networking/10073-icon-service-Front-Door-and-CDN-Profiles.svg",
    "Application Gateway":   "networking/10076-icon-service-Application-Gateways.svg",
    "API Management":        "integration/10042-icon-service-API-Management-Services.svg",
    "APIM":                  "integration/10042-icon-service-API-Management-Services.svg",
    "Azure Traffic Manager": "networking/10065-icon-service-Traffic-Manager-Profiles.svg",
    "Traffic Manager":       "networking/10065-icon-service-Traffic-Manager-Profiles.svg",
    "Azure Bastion":         "networking/02422-icon-service-Bastions.svg",
    "VPN Gateway":           "networking/10063-icon-service-Virtual-Network-Gateways.svg",
    "ExpressRoute":          "networking/10079-icon-service-ExpressRoute-Circuits.svg",
    "Virtual WAN":           "networking/10353-icon-service-Virtual-WANs.svg",
    "vWAN":                  "networking/10353-icon-service-Virtual-WANs.svg",
    "Azure Load Balancer":   "networking/10062-icon-service-Load-Balancers.svg",
    "Load Balancer":         "networking/10062-icon-service-Load-Balancers.svg",
    "Private Endpoint":      "other/02579-icon-service-Private-Endpoints.svg",
    "Azure Firewall":        "networking/10084-icon-service-Firewalls.svg",
    "VNet":                  "networking/10061-icon-service-Virtual-Networks.svg",
    "Virtual Network":       "networking/10061-icon-service-Virtual-Networks.svg",
    "WAF":                   "networking/10362-icon-service-Web-Application-Firewall-Policies(WAF).svg",
    # Storage
    "Azure Blob Storage":    "general/10781-icon-service-Blob-Page.svg",
    "Blob Storage":          "general/10781-icon-service-Blob-Page.svg",
    "Azure Files":           "storage/10400-icon-service-Azure-Fileshares.svg",
    "Storage Account":       "storage/10086-icon-service-Storage-Accounts.svg",
    "Data Lake Storage":     "storage/10090-icon-service-Data-Lake-Storage-Gen1.svg",
    "ADLS":                  "storage/10090-icon-service-Data-Lake-Storage-Gen1.svg",
    # Databases
    "Azure SQL":             "databases/10130-icon-service-SQL-Database.svg",
    "SQL Database":          "databases/10130-icon-service-SQL-Database.svg",
    "SQL Server":            "databases/10132-icon-service-SQL-Server.svg",
    "Azure Cosmos DB":       "databases/10121-icon-service-Azure-Cosmos-DB.svg",
    "Cosmos DB":             "databases/10121-icon-service-Azure-Cosmos-DB.svg",
    "Azure Cache for Redis": "databases/10137-icon-service-Cache-Redis.svg",
    "Redis Cache":           "databases/10137-icon-service-Cache-Redis.svg",
    "Redis":                 "databases/10137-icon-service-Cache-Redis.svg",
    "Azure Synapse Analytics": "analytics/00606-icon-service-Azure-Synapse-Analytics.svg",
    "Synapse":               "analytics/00606-icon-service-Azure-Synapse-Analytics.svg",
    # Messaging & Integration
    "Azure Event Hubs":      "analytics/00039-icon-service-Event-Hubs.svg",
    "Event Hubs":            "analytics/00039-icon-service-Event-Hubs.svg",
    "Azure Service Bus":     "integration/10836-icon-service-Azure-Service-Bus.svg",
    "Service Bus":           "integration/10836-icon-service-Azure-Service-Bus.svg",
    "Azure Event Grid":      "integration/10206-icon-service-Event-Grid-Topics.svg",
    "Azure Logic Apps":      "integration/02631-icon-service-Logic-Apps.svg",
    "Logic Apps":            "integration/02631-icon-service-Logic-Apps.svg",
    "Azure Data Factory":    "databases/10126-icon-service-Data-Factories.svg",
    "Data Factory":          "databases/10126-icon-service-Data-Factories.svg",
    "ADF":                   "databases/10126-icon-service-Data-Factories.svg",
    "Azure Databricks":      "analytics/10787-icon-service-Azure-Databricks.svg",
    "Databricks":            "analytics/10787-icon-service-Azure-Databricks.svg",
    "Stream Analytics":      "analytics/00042-icon-service-Stream-Analytics-Jobs.svg",
    # Monitor
    "Azure Monitor":         "monitor/00001-icon-service-Monitor.svg",
    "Log Analytics":         "monitor/00009-icon-service-Log-Analytics-Workspaces.svg",
    "Log Analytics Workspace": "monitor/00009-icon-service-Log-Analytics-Workspaces.svg",
    "Application Insights":  "monitor/00012-icon-service-Application-Insights.svg",
    # Security
    "Azure Key Vault":       "security/10245-icon-service-Key-Vaults.svg",
    "Key Vault":             "security/10245-icon-service-Key-Vaults.svg",
    "Microsoft Defender":    "security/10241-icon-service-Microsoft-Defender-for-Cloud.svg",
    # Management
    "Management Group":      "general/10011-icon-service-Management-Groups.svg",
    "Management Groups":     "general/10011-icon-service-Management-Groups.svg",
    "Subscription":          "general/10002-icon-service-Subscriptions.svg",
    "Resource Group":        "general/10007-icon-service-Resource-Groups.svg",
    "Azure Arc":             "management + governance/00756-icon-service-Azure-Arc.svg",
    "Azure Policy":          "management + governance/10316-icon-service-Policy.svg",
    "Azure Backup":          "other/02360-icon-service-Azure-Backup-Center.svg",
    "AMPLS":                 "monitor/00009-icon-service-Log-Analytics-Workspaces.svg",
}

def load_svg(rel_path):
    """Load SVG file, strip title/xml-decl, add class="az-i", return inline-ready string."""
    full = os.path.join(ICONS_BASE, rel_path)
    if not os.path.exists(full):
        return None
    with open(full, "r", encoding="utf-8") as f:
        svg = f.read()
    # Remove XML declaration
    svg = re.sub(r'<\?xml[^>]+\?>', '', svg).strip()
    # Remove <title>...</title>
    svg = re.sub(r'<title>[^<]*</title>', '', svg)
    # Add class="az-i" to outer <svg> tag
    svg = re.sub(r'^<svg\b', '<svg class="az-i"', svg, count=1)
    return svg

# Pre-load all SVG icons
SVG_CACHE = {}
for name, rel in ICON_FILES.items():
    svg = load_svg(rel)
    if svg:
        SVG_CACHE[name] = svg
    else:
        print(f"  WARN: not found: {rel}")

def make_svc_span(name):
    svg = SVG_CACHE.get(name)
    if not svg:
        return None
    return f'<span class="az-svc">{svg}{name}</span>'

# ── Build replacement patterns (longest match first) ─────────────────────────
# Sort by length descending to avoid partial matches
REPLACEMENTS = sorted(
    [(name, make_svc_span(name)) for name in SVG_CACHE if make_svc_span(name)],
    key=lambda x: len(x[0]),
    reverse=True
)

def inject_icons(html_fragment):
    """Inject Azure SVG icons into text nodes, skipping HTML tags and <code>."""
    parts = re.split(r'(<[^>]+>)', html_fragment)
    result = []
    in_skip = 0  # skip code/pre blocks

    for part in parts:
        if part.startswith('<'):
            tl = part.lower()
            if re.match(r'<(code|pre)[\s>]', tl):   in_skip += 1
            elif re.match(r'</(code|pre)', tl):       in_skip = max(0, in_skip - 1)
            result.append(part)
        elif in_skip == 0 and part.strip():
            for name, span in REPLACEMENTS:
                if name not in part:
                    continue
                # Don't double-inject: skip if already wrapped in az-svc
                # Use word-boundary style: require non-alpha-char before and after
                part = re.sub(
                    r'(?<!\w)(' + re.escape(name) + r')(?!\w)',
                    span,
                    part
                )
            result.append(part)
        else:
            result.append(part)

    return ''.join(result)


# ── Main ──────────────────────────────────────────────────────────────────────
with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"(const QUESTIONS = )(\[.*?\]);", content, re.DOTALL)
prefix = m.group(1)
qs = json.loads(m.group(2))

total_icons = 0
for q in qs:
    exp = q.get("exp_html", "")
    if not exp:
        continue

    # Step 1: strip existing .az-ic text badges (iterative to handle any nesting depth)
    while True:
        new_exp = re.sub(r'<span class="az-ic"[^>]*>[^<]*</span>', '', exp)
        if new_exp == exp:
            break
        exp = new_exp

    # Step 2: inject real SVG icons into exp-block-body only
    def process_body(match):
        open_tag = match.group(1)
        body = match.group(2)
        close_tag = match.group(3)
        new_body = inject_icons(body)
        return open_tag + new_body + close_tag

    new_exp = re.sub(
        r'(<div class="exp-block-body">)(.*?)(</div>)',
        process_body,
        exp,
        flags=re.DOTALL
    )

    injected = new_exp.count('az-svc') - exp.count('az-svc')
    total_icons += injected
    q["exp_html"] = new_exp

new_json = json.dumps(qs, ensure_ascii=False, separators=(",", ":"))
new_content = content[:m.start()] + prefix + new_json + ";" + content[m.end():]

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Injected {total_icons} Azure SVG icons into vol2.html")
print(f"   File size: {len(new_content)//1024}KB")
