"""Update vol3/vol4/vol5 HTML files to embed PNG architecture diagrams."""
import json
import re

IMG_STYLE = 'width:100%;border-radius:4px;max-width:760px;'

def make_arch_box(title, filename):
    return (
        f'<div class="arch-box">'
        f'<div class="arch-title">{title}</div>'
        f'<img src="picture/{filename}.png" style="{IMG_STYLE}">'
        f'</div>'
    )

# ─── VOL3 / VOL4 mapping ───────────────────────────────────────────────────
VOL3_MAP = {
    1:  ("vol3_q01_q02_aad_eventhub_cosmos", "AAD監査ログ取り込みパイプライン（Q1-2）"),
    2:  ("vol3_q01_q02_aad_eventhub_cosmos", "AAD監査ログ取り込みパイプライン（Q1-2）"),
    5:  ("vol3_q05_q06_adf_onprem",           "オンプレ → ADF → Azure Storage（Q5-6）"),
    6:  ("vol3_q05_q06_adf_onprem",           "オンプレ → ADF → Azure Storage（Q5-6）"),
    7:  ("vol3_q07_q09_bcdr",                 "BCDR: Site Recovery + Backup（Q7-9）"),
    8:  ("vol3_q07_q09_bcdr",                 "BCDR: Site Recovery + Backup（Q7-9）"),
    9:  ("vol3_q07_q09_bcdr",                 "BCDR: Site Recovery + Backup（Q7-9）"),
    10: ("vol3_q10_aks_vm",                   "AKS マイクロサービス + VM（Q10）"),
    11: ("vol3_q11_q14_multiregion_webapp",   "マルチリージョン Web App（Q11-14）"),
    12: ("vol3_q11_q14_multiregion_webapp",   "マルチリージョン Web App（Q11-14）"),
    13: ("vol3_q11_q14_multiregion_webapp",   "マルチリージョン Web App（Q11-14）"),
    14: ("vol3_q11_q14_multiregion_webapp",   "マルチリージョン Web App（Q11-14）"),
    17: ("vol3_q17_logicapps_b2b",            "Logic Apps B2B フェデレーション（Q17）"),
    28: ("vol3_q28_vpn_azurefiles",           "ブランチ → VPN → Azure Files（Q28）"),
    31: ("vol3_q31_q34_expressroute",         "ExpressRoute ハイブリッド（Q31-34）"),
    32: ("vol3_q31_q34_expressroute",         "ExpressRoute ハイブリッド（Q31-34）"),
    33: ("vol3_q31_q34_expressroute",         "ExpressRoute ハイブリッド（Q31-34）"),
    34: ("vol3_q31_q34_expressroute",         "ExpressRoute ハイブリッド（Q31-34）"),
    36: ("vol3_q36_cosmos_synapse",           "Cosmos DB → Synapse Analytics（Q36）"),
    43: ("vol3_q43_apexcore_tm",              "ApexCore: Traffic Manager マルチリージョン（Q43）"),
    46: ("vol3_q46_q47_app_keyvault",         "App Service + Managed Identity + Key Vault（Q46-47）"),
    47: ("vol3_q46_q47_app_keyvault",         "App Service + Managed Identity + Key Vault（Q46-47）"),
    52: ("vol3_q52_appinsights",              "App Service + Application Insights（Q52）"),
}

VOL4_MAP = {
    1:  ("vol4_q01_adf_blob_sql",           "ADF ETL: Blob → SQL DB（Q1）"),
    2:  ("vol4_q02_eventhubs_adls",         "Event Hubs → Data Lake ストリーミング（Q2）"),
    11: ("vol4_q11_servicebus_fifo",        "Service Bus FIFO メッセージング（Q11）"),
    12: ("vol4_q12_multiregion_vms",        "マルチリージョン VM + Front Door（Q12）"),
    13: ("vol4_q13_app_sql_redis",          "App Service + SQL DB + Redis Cache（Q13）"),
    19: ("vol4_q19_eventhubs_capture",      "Event Hubs Capture コールドパス（Q19）"),
    23: ("vol4_q23_sql_ha_encrypt",         "SQL DB 高可用性 + 暗号化（Q23）"),
    27: ("vol4_q27_q28_vwan_expressroute",  "仮想 WAN: 4拠点 + ExpressRoute（Q27-28）"),
    28: ("vol4_q27_q28_vwan_expressroute",  "仮想 WAN: 4拠点 + ExpressRoute（Q27-28）"),
    29: ("vol4_q29_databricks_vnet",        "Databricks + VNet プライベート接続（Q29）"),
    37: ("vol4_q37_functions_aks",          "Functions → AKS 移行（Q37）"),
    42: ("vol4_q42_q43_pe_dns",             "Private Endpoint + DNS + ExpressRoute（Q42-43）"),
    43: ("vol4_q42_q43_pe_dns",             "Private Endpoint + DNS + ExpressRoute（Q42-43）"),
    50: ("vol4_q50_q51_er_globalreach",     "ExpressRoute Global Reach + Traffic Manager（Q50-51）"),
    51: ("vol4_q50_q51_er_globalreach",     "ExpressRoute Global Reach + Traffic Manager（Q50-51）"),
    54: ("vol4_q54_q55_data_pipeline",      "データパイプライン: SQL → ADF → Synapse（Q54-55）"),
    55: ("vol4_q54_q55_data_pipeline",      "データパイプライン: SQL → ADF → Synapse（Q54-55）"),
}


def update_json_vol(path, mapping):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON
    match = re.search(r'(const QUESTIONS = )(\[.*?\]);', content, re.DOTALL)
    prefix = match.group(1)
    raw    = match.group(2)
    questions = json.loads(raw)

    updated = 0
    for q in questions:
        num = q['num']
        if num not in mapping:
            continue
        fname, title = mapping[num]
        arch_box = make_arch_box(title, fname)
        exp = q.get('exp_html', '')
        # Replace <div class="arch-svg-wrap">...(svg)...</div>
        new_exp = re.sub(
            r'<div class="arch-svg-wrap">.*?</div>',
            arch_box,
            exp,
            flags=re.DOTALL
        )
        if new_exp != exp:
            q['exp_html'] = new_exp
            updated += 1

    # Serialize back with minimal whitespace
    new_json = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))
    new_content = content[:match.start()] + prefix + new_json + ';' + content[match.end():]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  Updated {updated} questions in {path}")
    return updated


# ─── VOL5 mapping ─────────────────────────────────────────────────────────
VOL5_MAP = {
    1:  ("vol5_q01_multiregion_az",       "2リージョン 4可用性ゾーン VM（Q1）"),
    3:  ("vol5_q03_q04_sql_migration",    "SQL Server → Azure SQL DB 移行 + HA（Q3-4）"),
    4:  ("vol5_q03_q04_sql_migration",    "SQL Server → Azure SQL DB 移行 + HA（Q3-4）"),
    5:  ("vol5_q05_q06_datalake",         "ペタバイト Data Lake アーキテクチャ（Q5-6）"),
    6:  ("vol5_q05_q06_datalake",         "ペタバイト Data Lake アーキテクチャ（Q5-6）"),
    16: ("vol5_q16_q17_apim",             "API Management + App Service バックエンド（Q16-17）"),
    17: ("vol5_q16_q17_apim",             "API Management + App Service バックエンド（Q16-17）"),
    22: ("vol5_q22_multitenant_saas",     "マルチテナント SaaS + Elastic Pool（Q22）"),
    23: ("vol5_q23_q24_aks_acr",          "AKS マイクロサービス + Container Registry（Q23-24）"),
    24: ("vol5_q23_q24_aks_acr",          "AKS マイクロサービス + Container Registry（Q23-24）"),
    26: ("vol5_q26_sql_alwayson_tm",      "SQL Always On + Traffic Manager DR（Q26）"),
    27: ("vol5_q27_q28_webapp_waf",       "マルチリージョン Web App + Front Door WAF（Q27-28）"),
    28: ("vol5_q27_q28_webapp_waf",       "マルチリージョン Web App + Front Door WAF（Q27-28）"),
    29: ("vol5_q29_q30_app_pe_dns",       "App Service + Private Endpoint + DNS（Q29-30）"),
    30: ("vol5_q29_q30_app_pe_dns",       "App Service + Private Endpoint + DNS（Q29-30）"),
    31: ("vol5_q31_q33_apim_vnet",        "APIM 外部 VNet モード + バックエンド VM（Q31-33）"),
    32: ("vol5_q31_q33_apim_vnet",        "APIM 外部 VNet モード + バックエンド VM（Q31-33）"),
    33: ("vol5_q31_q33_apim_vnet",        "APIM 外部 VNet モード + バックエンド VM（Q31-33）"),
    40: ("vol5_q40_ad_entra_connect",     "オンプレミス AD + Entra ID Connect 同期（Q40）"),
    42: ("vol5_q42_q43_synapse_mpe",      "Synapse Analytics + Managed Private Endpoint（Q42-43）"),
    43: ("vol5_q42_q43_synapse_mpe",      "Synapse Analytics + Managed Private Endpoint（Q42-43）"),
    49: ("vol5_q49_hybrid_monitoring",    "ハイブリッド監視: Log Analytics + Azure Arc（Q49）"),
    52: ("vol5_q52_q54_hybrid_sql_dr",    "ハイブリッド SQL Always On + DR（Q52-54）"),
    53: ("vol5_q52_q54_hybrid_sql_dr",    "ハイブリッド SQL Always On + DR（Q52-54）"),
    54: ("vol5_q52_q54_hybrid_sql_dr",    "ハイブリッド SQL Always On + DR（Q52-54）"),
}


def update_vol5(path, mapping):
    """Vol5 uses JS template literals, so we do line-based replacement."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = 0
    for qnum, (fname, title) in mapping.items():
        arch_box_html = make_arch_box(title, fname)
        # Find the question block: {num:N,
        # Then within its exp:` ... ` section, replace arch-box with SVG
        # Pattern: find exp:` ... arch-box>...<svg...>...</svg> ... `
        # We identify by question number context

        # Strategy: split by question boundaries
        # Each question starts with {num:N,
        # Find the position of {num:qnum,
        q_pattern = rf'\{{num:{qnum},'
        q_match = re.search(q_pattern, content)
        if not q_match:
            print(f"  Q{qnum}: question not found")
            continue

        q_start = q_match.start()
        # Find next question or end of QS array
        next_q = re.search(rf'\{{num:{qnum+1},', content[q_start+1:])
        q_end = (q_start + 1 + next_q.start()) if next_q else len(content)

        q_block = content[q_start:q_end]

        # Replace arch-box with SVG inside this block
        new_block = re.sub(
            r'<div class="arch-box">.*?</div>\s*</svg>\s*</div>',
            arch_box_html,
            q_block,
            flags=re.DOTALL
        )
        # Alternative pattern if the above doesn't match:
        if new_block == q_block:
            new_block = re.sub(
                r'<div class="arch-box">\s*<div class="arch-title">[^<]*</div>\s*<svg[^>]*>.*?</svg>\s*</div>',
                arch_box_html,
                q_block,
                flags=re.DOTALL
            )

        if new_block != q_block:
            content = content[:q_start] + new_block + content[q_end:]
            updated += 1
        else:
            print(f"  Q{qnum}: no SVG arch-box found (skipped)")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Updated {updated} questions in {path}")
    return updated


print("=== Updating vol3.html ===")
update_json_vol('/Users/fujiikai/SCstudy/az305/vol3.html', VOL3_MAP)

print("=== Updating vol4.html ===")
update_json_vol('/Users/fujiikai/SCstudy/az305/vol4.html', VOL4_MAP)

print("=== Updating vol5.html ===")
update_vol5('/Users/fujiikai/SCstudy/az305/vol5.html', VOL5_MAP)

print("\n✅ All HTML files updated!")
