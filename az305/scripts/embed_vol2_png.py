"""Replace hand-crafted SVGs in vol2.html with base64-embedded PNGs (Azure icon diagrams)."""
import re, json, base64, os

PICDIR = "az305/picture"
PATH   = "az305/vol2.html"

PNG_MAP = {
    "vol2_q01_q03_sql_audit":    "SQL監査ログの構成（Q1-3）",
    "vol2_q09_q10_mgmt_group":   "管理グループ階層（Q9-10）",
    "vol2_q12_frontdoor_aks":    "Azure Front Door + マルチリージョン AKS（Q12）",
    "vol2_q17_servicebus_pubsub":"Service Bus トピック（Pub/Sub）（Q17）",
    "vol2_q23_q24_appgw_waf":    "Application Gateway + WAF アーキテクチャ（Q23-24）",
    "vol2_q28_adf_pipeline":     "Azure Data Factory パイプライン（Q28）",
    "vol2_q42_q43_bastion":      "Azure Bastion 構成（Q42-43）",
    "vol2_q44_frontdoor_global": "Azure Front Door グローバル負荷分散（Q44）",
    "vol2_q46_q47_apim":         "API Management + Entra ID（Q46-47）",
    "vol2_q55_ampls":            "Azure Monitor Private Link Scope / AMPLS（Q55）",
}

def png_to_data_uri(fname):
    path = os.path.join(PICDIR, fname + ".png")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{b64}"

def make_arch_box(title, data_uri):
    return (
        f'<div class="arch-box">'
        f'<div class="arch-title">{title}</div>'
        f'<img src="{data_uri}" style="width:100%;border-radius:6px;max-width:760px;display:block;margin:8px auto;">'
        f'</div>'
    )

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"(const QUESTIONS = )(\[.*?\]);", content, re.DOTALL)
prefix = m.group(1)
qs = json.loads(m.group(2))

updated = 0
for q in qs:
    exp = q.get("exp_html", "")
    # Find which PNG this question uses (match by title in arch-title)
    matched_key = None
    for key, title in PNG_MAP.items():
        if title in exp:
            matched_key = key
            break
    if not matched_key:
        continue

    title = PNG_MAP[matched_key]
    data_uri = png_to_data_uri(matched_key)
    new_arch = make_arch_box(title, data_uri)

    # Replace everything from arch-box start up to exp-sections
    new_exp = re.sub(
        r'<div class="arch-box">.*?(?=<div class="exp-sections")',
        new_arch,
        exp,
        count=1,
        flags=re.DOTALL
    )

    if new_exp != exp:
        q["exp_html"] = new_exp
        updated += 1
        print(f"  Q{q['num']}: embedded PNG for {matched_key}")
    else:
        print(f"  Q{q['num']}: FAILED to replace arch-box")

new_json = json.dumps(qs, ensure_ascii=False, separators=(",", ":"))
new_content = content[:m.start()] + prefix + new_json + ";" + content[m.end():]

with open(PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"\n✅ Updated {updated} questions in {PATH}")
