"""
Fix vol2.html:
  1. Remove duplicate standalone SVG (the old one after arch-box)
  2. Remove emoji from exp-block-label
  3. Replace ✅/❌ in tables with .tbl-ok/.tbl-ng spans
  4. Inject Azure service icon badges into exp-block-body text
"""
import re, json

# ── Azure service icon map: pattern → (bg-color, badge-text) ─────────────────
# Order matters: longer/more-specific patterns first
SERVICES = [
    # Identity
    (r'Microsoft Entra ID|Azure AD(?:FS)?|Entra ID',             '#7719AA', 'Entra'),
    # Compute
    (r'Azure Kubernetes Service|AKS',                            '#0078D4', 'AKS'),
    (r'Azure Functions?|Functions? App',                         '#0062AD', 'Fn'),
    (r'App Service(?:\s+Plan)?',                                 '#0078D4', 'App'),
    (r'Azure Container Registry|ACR',                            '#1A73E8', 'ACR'),
    (r'Azure Batch',                                             '#0072C6', 'Batch'),
    (r'Azure VM(?:SS)?|仮想マシン',                              '#107C41', 'VM'),
    # Networking
    (r'Azure Front Door',                                        '#B33AC7', 'FD'),
    (r'Application Gateway',                                     '#E74C3C', 'AGW'),
    (r'API Management(?:\s*\(APIM\))?|APIM',                    '#0072C6', 'APIM'),
    (r'Azure Traffic Manager',                                   '#B33AC7', 'TM'),
    (r'Azure Bastion',                                           '#0072C6', 'Bastion'),
    (r'VPN Gateway',                                             '#F97C00', 'VPN GW'),
    (r'ExpressRoute',                                            '#F97C00', 'ER'),
    (r'Virtual WAN|vWAN',                                        '#B33AC7', 'vWAN'),
    (r'Azure Load Balancer',                                     '#0072C6', 'LB'),
    (r'Private Endpoint',                                        '#6264A7', 'PE'),
    (r'Azure Firewall',                                          '#E74C3C', 'FW'),
    (r'Azure DDoS',                                              '#E74C3C', 'DDoS'),
    # Storage
    (r'Azure Blob Storage|Blob Storage',                         '#F97C00', 'Blob'),
    (r'Azure Files',                                             '#F97C00', 'Files'),
    (r'Storage Account',                                         '#F97C00', 'SA'),
    (r'Data Lake Storage(?:\s+Gen\d)?|ADLS',                    '#F97C00', 'ADLS'),
    # Databases
    (r'Azure SQL(?:\s+Managed Instance)?',                       '#0072C6', 'SQL'),
    (r'Azure Cosmos DB|Cosmos DB',                               '#6264A7', 'Cosmos'),
    (r'Azure Cache for Redis|Redis Cache',                       '#C41E3A', 'Redis'),
    (r'Azure Database for PostgreSQL',                           '#2D6DB5', 'PG'),
    (r'Azure Synapse Analytics|Synapse',                         '#6264A7', 'Synapse'),
    # Messaging
    (r'Azure Event Hubs?',                                       '#00897B', 'EH'),
    (r'Azure Service Bus',                                       '#F97C00', 'SB'),
    (r'Azure Event Grid',                                        '#00897B', 'EG'),
    (r'Azure Queue Storage',                                     '#F97C00', 'Queue'),
    # Integration / Analytics
    (r'Azure Data Factory|ADF',                                  '#B33AC7', 'ADF'),
    (r'Azure Databricks',                                        '#E04B00', 'Databricks'),
    (r'Azure Stream Analytics',                                  '#6264A7', 'ASA'),
    (r'Azure Logic Apps?',                                       '#B33AC7', 'LA'),
    (r'Azure HDInsight',                                         '#6264A7', 'HDI'),
    # Management / Security
    (r'Azure Monitor',                                           '#6264A7', 'Monitor'),
    (r'Log Analytics(?:\s+Workspace)?|LAW',                     '#6264A7', 'LAW'),
    (r'Application Insights',                                    '#6264A7', 'AppI'),
    (r'Azure Key Vault',                                         '#F97C00', 'KV'),
    (r'Microsoft Defender for Cloud|Defender for Cloud',        '#E74C3C', 'Defender'),
    (r'Azure Policy',                                            '#6264A7', 'Policy'),
    (r'Azure Blueprints?',                                       '#6264A7', 'Blueprint'),
    (r'Azure RBAC',                                              '#0072C6', 'RBAC'),
    (r'Azure Arc',                                               '#0072C6', 'Arc'),
    (r'Management Group',                                        '#6264A7', 'MG'),
    (r'Azure Backup',                                            '#107C41', 'Backup'),
    (r'Azure Site Recovery|ASR',                                 '#107C41', 'ASR'),
    (r'Azure AMPLS|AMPLS',                                       '#6264A7', 'AMPLS'),
]

def make_icon(color, text):
    return f'<span class="az-ic" style="background:{color}">{text}</span>'

def inject_icons(html_fragment):
    """Inject Azure icons into text nodes, skipping HTML tags and <code>."""
    parts = re.split(r'(<[^>]+>)', html_fragment)
    result = []
    in_code = 0
    for part in parts:
        if part.startswith('<'):
            tl = part.lower()
            if re.match(r'<code[\s>]', tl):  in_code += 1
            elif re.match(r'</code', tl):     in_code = max(0, in_code - 1)
            result.append(part)
        elif in_code == 0 and part.strip():
            for pattern, color, abbr in SERVICES:
                icon = make_icon(color, abbr)
                # Don't inject if icon already immediately precedes this match
                part = re.sub(
                    r'(?<!\>)(' + pattern + r')',
                    icon + r'\1',
                    part
                )
            result.append(part)
        else:
            result.append(part)
    return ''.join(result)


# ── Label emoji map ────────────────────────────────────────────────────────────
LABEL_FIXES = [
    (r'✅\s*', ''),
    (r'❌\s*', ''),
    (r'⚠️\s*', ''),
    (r'📌\s*', ''),
    (r'🔑\s*', ''),
    (r'💡\s*', ''),
    (r'📝\s*', ''),
    (r'🔴\s*', ''),
    (r'🟢\s*', ''),
    (r'⭐\s*', ''),
]

def clean_label(label_html):
    for pat, repl in LABEL_FIXES:
        label_html = re.sub(pat, repl, label_html)
    return label_html.strip()


# ── Table cell emoji → HTML spans ─────────────────────────────────────────────
def clean_table_cells(html):
    html = re.sub(r'<td([^>]*)>✅</td>',
                  r'<td\1><span class="tbl-ok">○</span></td>', html)
    html = re.sub(r'<td([^>]*)>❌</td>',
                  r'<td\1><span class="tbl-ng">—</span></td>', html)
    html = re.sub(r'<td([^>]*)>⭕</td>',
                  r'<td\1><span class="tbl-ok">○</span></td>', html)
    # Mixed-content cells: just strip the emoji
    html = re.sub(r'✅', '<span class="tbl-ok">○</span>', html)
    html = re.sub(r'❌', '<span class="tbl-ng">—</span>', html)
    return html


# ── Remove duplicate standalone SVG ───────────────────────────────────────────
def remove_duplicate_svg(exp_html):
    """
    Structure:
      <div class="arch-box">...[SVG1]</svg></div>
      <svg>[SVG2]</svg></div>          ← </div> closes outer wrapper
      <div class="exp-sections">
    Remove SVG2 (and its trailing </div> if any).
    """
    # Pattern A: arch-box-end → SVG2 → </div> → exp-sections
    result = re.sub(
        r'(</svg></div>)<svg[^>]*>.*?</svg></div>(<div class="exp-sections")',
        r'\1\2',
        exp_html, flags=re.DOTALL
    )
    if result == exp_html:
        # Pattern B: no trailing </div> before exp-sections
        result = re.sub(
            r'(</svg></div>)<svg[^>]*>.*?</svg>(<div class="exp-sections")',
            r'\1\2',
            exp_html, flags=re.DOTALL
        )
    return result


# ── Process exp_html ───────────────────────────────────────────────────────────
def process_exp(exp_html):
    # 1. Remove duplicate SVG
    exp_html = remove_duplicate_svg(exp_html)

    # 2. Clean emoji from exp-block-label
    exp_html = re.sub(
        r'(<div class="exp-block-label">)(.*?)(</div>)',
        lambda m: m.group(1) + clean_label(m.group(2)) + m.group(3),
        exp_html
    )

    # 3. Clean table emoji
    exp_html = clean_table_cells(exp_html)

    # 4. Inject Azure icons into exp-block-body divs only
    def process_body(match):
        open_tag = match.group(1)
        body = match.group(2)
        close_tag = match.group(3)
        return open_tag + inject_icons(body) + close_tag

    exp_html = re.sub(
        r'(<div class="exp-block-body">)(.*?)(</div>)',
        process_body,
        exp_html,
        flags=re.DOTALL
    )

    return exp_html


# ── Main ──────────────────────────────────────────────────────────────────────
path = 'az305/vol2.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const QUESTIONS = )(\[.*?\]);', content, re.DOTALL)
prefix = match.group(1)
qs = json.loads(match.group(2))

for q in qs:
    if 'exp_html' in q:
        q['exp_html'] = process_exp(q['exp_html'])

new_json = json.dumps(qs, ensure_ascii=False, separators=(',', ':'))
new_content = content[:match.start()] + prefix + new_json + ';' + content[match.end():]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
print("=== Verification ===")
import json as _json
m2 = re.search(r'const QUESTIONS = (\[.*?\]);', new_content, re.DOTALL)
qs2 = _json.loads(m2.group(1))
dup_svgs = [q['num'] for q in qs2 if q.get('exp_html','').count('<svg') > 1]
emojis   = sum(q.get('exp_html','').count(e) for q in qs2
               for e in ['✅','❌','⚠️','📌','🔑','💡','📝'])
icons    = sum(q.get('exp_html','').count('az-ic') for q in qs2)
print(f"Duplicate SVGs remaining: {dup_svgs or 'none'}")
print(f"Emoji remaining: {emojis}")
print(f"Azure icon injections: {icons}")
print("✅ Done")
