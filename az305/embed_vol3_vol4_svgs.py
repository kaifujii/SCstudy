"""Replace vol3/vol4 <img src="picture/..."> with inline SVGs."""
import re, json

BG = "#0d1b2e"; CARD_BG = "#112240"; TEXT_LIGHT = "#c5d8ef"
TEXT_LABEL = "#7a9cbf"; ARROW = "#4a9fd4"; FONT = "Segoe UI,Arial,sans-serif"

def svg_wrap(w, h, inner, extra_defs=""):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;display:block;margin:10px auto;border-radius:10px;">\n'
        f'<rect width="{w}" height="{h}" rx="10" fill="{BG}"/>\n'
        '<defs>\n'
        '  <marker id="arr" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">'
        '<polygon points="0 0,7 2.5,0 5" fill="#4a9fd4"/></marker>\n'
        + extra_defs +
        '</defs>\n' + inner + '\n</svg>'
    )

def card(x, y, w, h, color, abbr, line1, line2=""):
    cx = x + w // 2
    t = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{CARD_BG}" stroke="{color}" stroke-width="1.5"/>\n'
        f'<rect x="{x+6}" y="{y+5}" width="{w-12}" height="24" rx="4" fill="{color}" fill-opacity="0.18"/>\n'
        f'<text x="{cx}" y="{y+21}" text-anchor="middle" font-size="11" font-weight="700" fill="{color}" font-family="{FONT}">{abbr}</text>\n'
        f'<text x="{cx}" y="{y+41}" text-anchor="middle" font-size="8.5" fill="{TEXT_LIGHT}" font-family="{FONT}">{line1}</text>\n'
    )
    if line2:
        t += f'<text x="{cx}" y="{y+52}" text-anchor="middle" font-size="8.5" fill="{TEXT_LIGHT}" font-family="{FONT}">{line2}</text>\n'
    return t

def arrow(x1, y1, x2, y2, label=""):
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ARROW}" stroke-width="1.5" marker-end="url(#arr)"/>\n'
    if label:
        mx, my = (x1+x2)//2, min(y1,y2)-5
        s += f'<text x="{mx}" y="{my}" text-anchor="middle" font-size="8" fill="{TEXT_LABEL}" font-family="{FONT}">{label}</text>\n'
    return s

def lbl(x, y, text, color=TEXT_LIGHT, size=9, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}" font-family="{FONT}">{text}</text>\n'

def region_box(x, y, w, h, label_text, color="#1e4080"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="none" stroke="{color}" stroke-width="1" stroke-dasharray="4,3"/>\n'
        + lbl(x + w//2, y+14, label_text, "#4a9fd4", 9)
    )

# ═══════════════════════════════════════════════════════════ VOL3 ══════════════

def v3_aad_eventhub_cosmos():
    """Q1-2: AAD→EventHub→Functions→CosmosDB"""
    i = ""
    i += card(30, 50, 110, 65, "#7719AA", "AAD", "Entra ID", "診断ログ")
    i += arrow(140, 82, 175, 82, "イベント出力")
    i += card(180, 50, 110, 65, "#00897B", "EH", "Event Hubs", "ストリーム")
    i += arrow(290, 82, 325, 82, "トリガー")
    i += card(330, 50, 110, 65, "#0072C6", "Fn", "Azure", "Functions")
    i += arrow(440, 82, 475, 82, "格納")
    i += card(480, 50, 110, 65, "#6264A7", "CDB", "Cosmos DB", "監査ログ保存")
    i += lbl(370, 135, "Entra ID 診断ログ → Event Hubs → Functions → Cosmos DB", "#4a9fd4", 9)
    return svg_wrap(620, 150, i)

def v3_adf_onprem():
    """Q5-6: On-prem → ADF → Azure Storage"""
    i = ""
    i += card(20, 50, 110, 65, "#E05252", "OnPrem", "オンプレ", "SQL / File")
    i += arrow(130, 82, 165, 82, "Self-hosted IR")
    i += card(170, 35, 130, 95, "#E040FB", "ADF", "Azure Data", "Factory")
    i += lbl(235, 140, "Pipeline", TEXT_LABEL, 8)
    i += arrow(300, 82, 335, 82, "Copy")
    i += card(340, 50, 110, 65, "#F97C00", "Blob", "Blob Storage", "Staging")
    i += arrow(450, 82, 485, 82, "Load")
    i += card(490, 50, 110, 65, "#0072C6", "SQL", "Azure SQL", "/ Synapse")
    i += lbl(310, 155, "Self-hosted IR がオンプレと Azure を橋渡し", "#4a9fd4", 9)
    return svg_wrap(620, 170, i)

def v3_bcdr():
    """Q7-9: BCDR Site Recovery + Backup"""
    i = ""
    i += region_box(15, 20, 260, 160, "Primary Region (East US)")
    i += card(30, 40, 110, 60, "#107C41", "VM", "Azure VM", "本番ワークロード")
    i += card(30, 115, 110, 55, "#0072C6", "DB", "SQL DB", "Primary")
    i += arrow(145, 70, 180, 50, "Site Recovery")
    i += arrow(145, 142, 180, 155, "Geo-Backup")
    i += region_box(285, 20, 260, 160, "Secondary Region (West US)")
    i += card(300, 40, 110, 60, "#107C41", "VM", "Azure VM", "DR (停止中)")
    i += card(300, 115, 110, 55, "#0072C6", "DB", "SQL DB", "Secondary")
    i += card(555, 70, 110, 55, "#F97C00", "RSV", "Recovery", "Services Vault")
    i += arrow(410, 70, 550, 82, "")
    i += lbl(370, 200, "RPO/RTO: Site Recovery=分単位, Backup=時間単位", "#4a9fd4", 9)
    return svg_wrap(680, 215, i)

def v3_aks_vm():
    """Q10: AKS + VM"""
    i = ""
    i += region_box(15, 15, 560, 180, "Azure VNet")
    i += card(30, 35, 130, 65, "#0078D4", "AKS", "AKS Cluster", "マイクロサービス")
    i += card(30, 115, 130, 65, "#107C41", "VM", "Azure VM", "レガシーサービス")
    i += arrow(160, 67, 200, 67, "内部通信")
    i += arrow(160, 147, 200, 147, "内部通信")
    i += card(205, 75, 120, 60, "#6264A7", "APIM", "API Mgmt", "統合ゲートウェイ")
    i += arrow(325, 105, 365, 105, "")
    i += card(370, 75, 120, 60, "#E040FB", "FD", "Front Door", "グローバルLB")
    i += arrow(490, 105, 530, 105, "")
    i += card(535, 75, 30, 60, "#7a9cbf", "🌐", "Users", "")
    i += lbl(290, 210, "AKS と VM を同一 VNet に配置し APIM で統合", "#4a9fd4", 9)
    return svg_wrap(590, 225, i)

def v3_multiregion_webapp():
    """Q11-14: マルチリージョン Web App"""
    i = ""
    i += card(15, 75, 90, 60, "#E040FB", "FD", "Front Door", "Global")
    i += arrow(105, 105, 140, 105, "ルーティング")
    i += region_box(145, 25, 200, 165, "East US")
    i += card(160, 45, 160, 60, "#0078D4", "App1", "App Service", "East US")
    i += card(160, 120, 160, 60, "#0072C6", "DB1", "SQL DB Primary", "East US")
    i += arrow(345, 105, 380, 105, "Geo-Replication")
    i += region_box(385, 25, 200, 165, "West US")
    i += card(400, 45, 160, 60, "#0078D4", "App2", "App Service", "West US")
    i += card(400, 120, 160, 60, "#0072C6", "DB2", "SQL DB Secondary", "West US")
    i += lbl(295, 210, "Front Door → 最低レイテンシ / フェイルオーバー自動", "#4a9fd4", 9)
    return svg_wrap(600, 225, i)

def v3_logicapps_b2b():
    """Q17: Logic Apps B2B"""
    i = ""
    i += card(15, 65, 110, 65, "#E05252", "Partner", "取引先", "B2Bパートナー")
    i += arrow(125, 97, 160, 97, "EDI/AS2")
    i += card(165, 50, 140, 95, "#E040FB", "LA", "Logic Apps", "B2B統合")
    i += lbl(235, 155, "Integration Account", TEXT_LABEL, 8)
    i += arrow(305, 97, 340, 75, "変換")
    i += arrow(305, 97, 340, 120, "通知")
    i += card(345, 45, 120, 60, "#0072C6", "SQL", "Azure SQL", "受注データ格納")
    i += card(345, 115, 120, 60, "#107C41", "SB", "Service Bus", "非同期通知")
    i += lbl(290, 195, "AS2/X12/EDIFACT 変換 → バックエンドへ自動配送", "#4a9fd4", 9)
    return svg_wrap(490, 210, i)

def v3_vpn_azurefiles():
    """Q28: Branch → VPN → Azure Files"""
    i = ""
    i += card(15, 65, 110, 65, "#7a9cbf", "Branch", "ブランチ拠点", "Windows PC")
    i += arrow(125, 97, 160, 97, "VPN S2S")
    i += card(165, 50, 130, 95, "#F97C00", "VGW", "VPN Gateway", "Azure側GW")
    i += arrow(295, 97, 330, 97, "プライベート")
    i += region_box(335, 20, 230, 155, "Azure VNet")
    i += card(350, 40, 110, 60, "#0072C6", "Files", "Azure Files", "SMBファイル共有")
    i += card(350, 115, 110, 55, "#107C41", "SA", "Storage Acct", "StorageV2")
    i += lbl(290, 190, "拠点から SMB over VPN でクラウドファイル共有にアクセス", "#4a9fd4", 9)
    return svg_wrap(590, 205, i)

def v3_expressroute():
    """Q31-34: ExpressRoute ハイブリッド"""
    i = ""
    i += card(15, 75, 110, 65, "#7a9cbf", "OnPrem", "オンプレ DC", "")
    i += arrow(125, 107, 165, 107, "専用線")
    i += card(170, 60, 130, 80, "#F97C00", "ER", "ExpressRoute", "Circuit")
    i += arrow(300, 107, 340, 107, "BGP")
    i += region_box(345, 25, 230, 165, "Azure VNet")
    i += card(360, 45, 100, 60, "#0072C6", "ERG", "ER Gateway", "GatewaySubnet")
    i += card(360, 120, 100, 55, "#107C41", "VM", "Azure VM", "バックエンド")
    i += card(480, 60, 80, 55, "#6264A7", "PE", "Private", "Endpoint")
    i += card(480, 125, 80, 55, "#E040FB", "KV", "Key Vault", "")
    i += lbl(290, 210, "ExpressRoute: 専用帯域・低レイテンシ・SLA 99.95%", "#4a9fd4", 9)
    return svg_wrap(590, 225, i)

def v3_cosmos_synapse():
    """Q36: Cosmos DB → Synapse Analytics"""
    i = ""
    i += card(20, 65, 120, 65, "#6264A7", "CDB", "Cosmos DB", "OLTP / NoSQL")
    i += arrow(140, 97, 180, 97, "Synapse Link")
    i += card(185, 50, 140, 95, "#E040FB", "SA", "Synapse", "Analytics")
    i += lbl(255, 155, "Analytical Store", TEXT_LABEL, 8)
    i += arrow(325, 97, 360, 75, "")
    i += arrow(325, 97, 360, 120, "")
    i += card(365, 45, 120, 60, "#0072C6", "Pool", "SQL Pool", "バッチ分析")
    i += card(365, 115, 120, 60, "#F97C00", "Spark", "Spark Pool", "機械学習")
    i += lbl(290, 195, "Synapse Link でETLなしリアルタイム分析 (HTAP)", "#4a9fd4", 9)
    return svg_wrap(510, 210, i)

def v3_apexcore_tm():
    """Q43: Traffic Manager マルチリージョン"""
    i = ""
    i += card(15, 75, 90, 65, "#7a9cbf", "User", "グローバル", "ユーザー")
    i += arrow(105, 107, 145, 107, "DNS")
    i += card(150, 60, 130, 80, "#E040FB", "TM", "Traffic", "Manager")
    i += arrow(280, 90, 315, 65, "")
    i += arrow(280, 107, 315, 107, "")
    i += arrow(280, 124, 315, 149, "")
    i += region_box(320, 25, 155, 90, "East US")
    i += card(335, 42, 120, 60, "#0078D4", "App1", "App Service", "East US")
    i += region_box(320, 125, 155, 90, "West EU")
    i += card(335, 140, 120, 60, "#0078D4", "App2", "App Service", "West EU")
    i += region_box(490, 75, 155, 90, "SE Asia")
    i += card(505, 90, 120, 60, "#0078D4", "App3", "App Service", "SE Asia")
    i += lbl(340, 230, "TM ルーティング: Priority / Weighted / Performance", "#4a9fd4", 9)
    return svg_wrap(660, 245, i)

def v3_app_keyvault():
    """Q46-47: App Service + Managed Identity + Key Vault"""
    i = ""
    i += card(20, 65, 130, 65, "#0078D4", "App", "App Service", "Webアプリ")
    i += lbl(85, 140, "Managed Identity", TEXT_LABEL, 8)
    i += arrow(150, 97, 190, 80, "MI認証")
    i += arrow(150, 97, 190, 115, "シークレット取得")
    i += card(195, 50, 130, 60, "#F97C00", "KV", "Key Vault", "シークレット管理")
    i += card(195, 125, 130, 55, "#7719AA", "AAD", "Entra ID", "トークン発行")
    i += arrow(325, 80, 365, 80, "接続文字列")
    i += card(370, 50, 120, 65, "#0072C6", "DB", "Azure SQL", "データベース")
    i += lbl(290, 200, "Managed Identity → パスワードレス認証・シークレット不要", "#4a9fd4", 9)
    return svg_wrap(510, 215, i)

def v3_appinsights():
    """Q52: App Service + Application Insights"""
    i = ""
    i += card(20, 65, 130, 65, "#0078D4", "App", "App Service", "Webアプリ")
    i += arrow(150, 97, 190, 97, "テレメトリ")
    i += card(195, 50, 140, 95, "#6264A7", "AI", "Application", "Insights")
    i += lbl(265, 155, "SDK自動計装", TEXT_LABEL, 8)
    i += arrow(335, 97, 375, 80, "")
    i += arrow(335, 97, 375, 115, "")
    i += card(380, 45, 120, 60, "#E040FB", "LAW", "Log Analytics", "Workspace")
    i += card(380, 115, 120, 55, "#F97C00", "Alert", "Azure Monitor", "アラート")
    i += lbl(290, 190, "リクエスト / 依存関係 / 例外 / カスタムメトリクス収集", "#4a9fd4", 9)
    return svg_wrap(520, 205, i)

# ═══════════════════════════════════════════════════════════ VOL4 ══════════════

def v4_adf_blob_sql():
    """Q1: ADF ETL Blob → SQL DB"""
    i = ""
    i += card(20, 65, 120, 65, "#F97C00", "Blob", "Blob Storage", "CSVファイル")
    i += arrow(140, 97, 180, 97, "Source")
    i += card(185, 50, 140, 95, "#E040FB", "ADF", "Azure Data", "Factory")
    i += lbl(255, 155, "Mapping Data Flow", TEXT_LABEL, 8)
    i += arrow(325, 97, 365, 97, "Sink")
    i += card(370, 65, 120, 65, "#0072C6", "SQL", "Azure SQL DB", "変換後データ")
    i += arrow(255, 50, 255, 25, "")
    i += card(190, 5, 130, 35, "#107C41", "Trigger", "スケジュール", "トリガー")
    i += lbl(290, 175, "ADF Pipeline: Source → Transform → Sink", "#4a9fd4", 9)
    return svg_wrap(520, 190, i)

def v4_eventhubs_adls():
    """Q2: Event Hubs → ADLS ストリーミング"""
    i = ""
    i += card(15, 65, 110, 65, "#7a9cbf", "IoT", "デバイス群", "テレメトリ")
    i += arrow(125, 97, 165, 97, "HTTPS/AMQP")
    i += card(170, 50, 130, 95, "#00897B", "EH", "Event Hubs", "取り込み")
    i += lbl(235, 155, "Capture 有効", TEXT_LABEL, 8)
    i += arrow(300, 97, 340, 80, "Stream")
    i += arrow(300, 97, 340, 120, "Capture")
    i += card(345, 45, 120, 60, "#6264A7", "ASA", "Stream", "Analytics")
    i += card(345, 115, 120, 60, "#F97C00", "ADLS", "Data Lake", "Storage Gen2")
    i += lbl(295, 195, "Event Hubs Capture → ADLS へ自動バッチ保存", "#4a9fd4", 9)
    return svg_wrap(490, 210, i)

def v4_servicebus_fifo():
    """Q11: Service Bus FIFO"""
    i = ""
    i += card(15, 65, 110, 65, "#107C41", "Sender", "送信者", "App Service")
    i += arrow(125, 97, 165, 97, "Send")
    i += card(170, 45, 150, 105, "#F97C00", "SB", "Service Bus", "Queue (FIFO)")
    i += lbl(245, 160, "Sessions有効", TEXT_LABEL, 8)
    i += arrow(320, 97, 360, 97, "Receive")
    i += card(365, 65, 110, 65, "#0072C6", "Receiver", "受信者", "Functions")
    i += lbl(255, 185, "Sessions = 送信順序保証 (FIFO) / Dead-letter queue", "#4a9fd4", 9)
    return svg_wrap(500, 200, i)

def v4_multiregion_vms():
    """Q12: マルチリージョン VM + Front Door"""
    i = ""
    i += card(15, 80, 85, 55, "#E040FB", "FD", "Front Door", "Global LB")
    i += arrow(100, 107, 135, 85, "")
    i += arrow(100, 107, 135, 135, "")
    i += region_box(140, 30, 190, 100, "East US")
    i += card(155, 48, 155, 65, "#107C41", "VMSS1", "VM Scale Set", "East US")
    i += region_box(140, 140, 190, 100, "West US")
    i += card(155, 158, 155, 65, "#107C41", "VMSS2", "VM Scale Set", "West US")
    i += card(350, 80, 90, 55, "#0072C6", "LB", "Load", "Balancer")
    i += arrow(330, 80, 345, 95, "")
    i += arrow(330, 180, 345, 115, "")
    i += lbl(240, 260, "Front Door → リージョン単位ルーティング → LB → VMSS", "#4a9fd4", 9)
    return svg_wrap(460, 275, i)

def v4_app_sql_redis():
    """Q13: App Service + SQL DB + Redis Cache"""
    i = ""
    i += card(15, 75, 110, 65, "#0078D4", "App", "App Service", "Webアプリ")
    i += arrow(125, 107, 165, 87, "クエリ(キャッシュミス)")
    i += arrow(125, 107, 165, 130, "キャッシュ読取")
    i += card(170, 50, 120, 65, "#0072C6", "SQL", "Azure SQL DB", "永続データ")
    i += card(170, 125, 120, 65, "#E05252", "Redis", "Azure Cache", "for Redis")
    i += arrow(170, 82, 133, 107, "結果キャッシュ")
    i += lbl(230, 210, "Cache-Aside: Redis ミス → SQL 読取 → Redis 書込", "#4a9fd4", 9)
    return svg_wrap(320, 225, i)

def v4_eventhubs_capture():
    """Q19: Event Hubs Capture コールドパス"""
    i = ""
    i += card(15, 65, 110, 65, "#7a9cbf", "Source", "イベント送信元", "")
    i += arrow(125, 97, 165, 97, "")
    i += card(170, 50, 130, 95, "#00897B", "EH", "Event Hubs", "ネームスペース")
    i += lbl(235, 155, "Capture ON", "#4a9fd4", 8)
    i += arrow(300, 80, 340, 65, "ホットパス")
    i += arrow(300, 115, 340, 130, "コールドパス")
    i += card(345, 40, 130, 55, "#6264A7", "ASA", "Stream Analytics", "リアルタイム処理")
    i += card(345, 105, 130, 55, "#F97C00", "ADLS", "Data Lake", "Storage (Avro)")
    i += arrow(475, 132, 510, 132, "バッチ分析")
    i += card(515, 105, 110, 55, "#E040FB", "Databricks", "HDInsight", "/ Databricks")
    i += lbl(330, 180, "Capture = 自動的に Avro 形式で ADLS へ保存", "#4a9fd4", 9)
    return svg_wrap(650, 195, i)

def v4_sql_ha_encrypt():
    """Q23: SQL DB 高可用性 + 暗号化"""
    i = ""
    i += region_box(15, 20, 200, 170, "Primary (East US)")
    i += card(30, 40, 165, 60, "#0072C6", "SQL-P", "SQL DB Primary", "Always Encrypted")
    i += card(30, 115, 165, 60, "#F97C00", "TDE", "TDE", "Transparent Data Enc.")
    i += arrow(215, 100, 255, 80, "Auto-Failover")
    i += arrow(215, 145, 255, 155, "Geo-Backup")
    i += region_box(260, 20, 200, 170, "Secondary (West US)")
    i += card(275, 40, 165, 60, "#0072C6", "SQL-S", "SQL DB Secondary", "読み取りレプリカ")
    i += card(275, 115, 165, 60, "#107C41", "AG", "Auto-Failover", "Group")
    i += card(480, 70, 110, 60, "#6264A7", "KV", "Key Vault", "CMK管理")
    i += lbl(285, 210, "Always Encrypted + TDE + Customer Managed Key", "#4a9fd4", 9)
    return svg_wrap(620, 225, i)

def v4_vwan_expressroute():
    """Q27-28: 仮想 WAN + ExpressRoute"""
    i = ""
    i += card(250, 10, 120, 55, "#E040FB", "vWAN", "Virtual WAN Hub", "東日本")
    i += arrow(310, 65, 310, 95, "")
    i += card(245, 100, 130, 60, "#F97C00", "ER", "ExpressRoute", "Circuit")
    i += arrow(245, 130, 185, 160, "")
    i += arrow(375, 130, 430, 160, "")
    i += card(80, 155, 100, 55, "#7a9cbf", "DC1", "東京 DC", "オンプレ")
    i += card(440, 155, 100, 55, "#7a9cbf", "DC2", "大阪 DC", "オンプレ")
    i += arrow(130, 155, 100, 100, "")
    i += arrow(490, 155, 520, 100, "")
    i += card(70, 80, 100, 55, "#0078D4", "VNet1", "VNet 東日本", "")
    i += card(500, 80, 100, 55, "#0078D4", "VNet2", "VNet 西日本", "")
    i += arrow(310, 10, 120, 107, "")
    i += arrow(310, 10, 550, 107, "")
    i += lbl(310, 235, "vWAN Hub が複数拠点・VNet・ER を一元管理", "#4a9fd4", 9)
    return svg_wrap(640, 250, i)

def v4_databricks_vnet():
    """Q29: Databricks + VNet インジェクション"""
    i = ""
    i += region_box(15, 15, 530, 185, "Azure VNet (カスタム)")
    i += region_box(30, 35, 230, 145, "Databricks VNet Injection")
    i += card(45, 55, 100, 55, "#E040FB", "Driver", "Driver Node", "Databricks")
    i += card(45, 125, 100, 55, "#E040FB", "Worker", "Worker Nodes", "Databricks")
    i += arrow(145, 82, 185, 82, "内部通信")
    i += card(190, 55, 120, 60, "#0072C6", "ADLS", "Data Lake", "Storage")
    i += card(190, 130, 120, 55, "#F97C00", "KV", "Key Vault", "シークレット")
    i += card(375, 75, 120, 60, "#6264A7", "PE", "Private Endpoint", "DNS統合")
    i += arrow(310, 85, 370, 95, "プライベート")
    i += lbl(280, 220, "VNet インジェクション → パブリックIP不要・完全プライベート通信", "#4a9fd4", 9)
    return svg_wrap(560, 235, i)

def v4_functions_aks():
    """Q37: Functions → AKS 移行"""
    i = ""
    i += card(20, 65, 130, 65, "#0072C6", "Fn", "Azure Functions", "サーバーレス(移行前)")
    i += arrow(150, 97, 190, 97, "コンテナ化")
    i += card(195, 50, 150, 95, "#0078D4", "AKS", "AKS Cluster", "移行後")
    i += lbl(270, 155, "KEDA スケーリング", TEXT_LABEL, 8)
    i += arrow(345, 97, 385, 80, "")
    i += arrow(345, 97, 385, 120, "")
    i += card(390, 45, 120, 60, "#6264A7", "ACR", "Container", "Registry")
    i += card(390, 115, 120, 60, "#107C41", "HPA", "KEDA / HPA", "オートスケール")
    i += lbl(290, 185, "Functions → AKS: KEDA でイベント駆動スケーリング維持", "#4a9fd4", 9)
    return svg_wrap(540, 200, i)

def v4_pe_dns():
    """Q42-43: Private Endpoint + DNS + ExpressRoute"""
    i = ""
    i += card(15, 75, 110, 65, "#7a9cbf", "OnPrem", "オンプレ", "クライアント")
    i += arrow(125, 107, 165, 107, "ER/VPN")
    i += region_box(170, 25, 340, 180, "Azure VNet")
    i += card(185, 45, 110, 60, "#F97C00", "VGW", "VPN/ER", "Gateway")
    i += arrow(295, 75, 335, 75, "プライベート")
    i += card(340, 45, 120, 60, "#6264A7", "PE", "Private Endpoint", "10.x.x.x")
    i += card(340, 120, 120, 55, "#E040FB", "DNS", "Private DNS", "Zone")
    i += arrow(460, 75, 500, 75, "")
    i += card(505, 45, 100, 65, "#0072C6", "SA", "Storage", "/ SQL / KV")
    i += arrow(400, 120, 400, 105, "")
    i += lbl(290, 225, "Private DNS Zone → オンプレから FQDN でプライベート解決", "#4a9fd4", 9)
    return svg_wrap(630, 240, i)

def v4_er_globalreach():
    """Q50-51: ExpressRoute Global Reach + Traffic Manager"""
    i = ""
    i += card(15, 85, 110, 60, "#7a9cbf", "DC-JP", "東京 DC", "オンプレ")
    i += arrow(125, 115, 170, 95, "ER Circuit 1")
    i += card(175, 55, 130, 80, "#F97C00", "MSEE", "MS Enterprise", "Edge (東京)")
    i += arrow(305, 95, 345, 95, "Global Reach")
    i += card(350, 55, 130, 80, "#F97C00", "MSEE", "MS Enterprise", "Edge (欧州)")
    i += arrow(480, 95, 520, 115, "ER Circuit 2")
    i += card(525, 85, 110, 60, "#7a9cbf", "DC-EU", "欧州 DC", "オンプレ")
    i += arrow(240, 55, 240, 20, "")
    i += arrow(415, 55, 415, 20, "")
    i += card(255, 5, 150, 35, "#E040FB", "TM", "Traffic Manager", "DR フェイルオーバー")
    i += lbl(320, 170, "Global Reach: 2つのERサーキットをMSバックボーン経由で接続", "#4a9fd4", 9)
    return svg_wrap(660, 185, i)

def v4_data_pipeline():
    """Q54-55: SQL → ADF → Synapse"""
    i = ""
    i += card(15, 65, 110, 65, "#0072C6", "SQL", "Azure SQL DB", "ソース")
    i += arrow(125, 97, 165, 97, "Copy Activity")
    i += card(170, 50, 140, 95, "#E040FB", "ADF", "Azure Data", "Factory")
    i += lbl(240, 155, "Mapping Data Flow", TEXT_LABEL, 8)
    i += arrow(310, 97, 350, 80, "")
    i += arrow(310, 97, 350, 120, "")
    i += card(355, 45, 130, 60, "#F97C00", "ADLS", "Data Lake", "Storage (Staging)")
    i += card(355, 115, 130, 60, "#6264A7", "Synapse", "Synapse SQL", "Pool (DWH)")
    i += arrow(485, 75, 525, 75, "分析")
    i += card(530, 45, 100, 60, "#E040FB", "PBI", "Power BI", "可視化")
    i += lbl(310, 190, "ADF → ADLS Staging → Synapse PolyBase COPY", "#4a9fd4", 9)
    return svg_wrap(650, 205, i)


# ═══════════════════════════════════════════════════════════ PATCH ═════════════

VOL3_SVG_MAP = {
    "vol3_q01_q02_aad_eventhub_cosmos":  ("AAD監査ログ取り込みパイプライン（Q1-2）",           v3_aad_eventhub_cosmos()),
    "vol3_q05_q06_adf_onprem":           ("オンプレ → ADF → Azure Storage（Q5-6）",            v3_adf_onprem()),
    "vol3_q07_q09_bcdr":                 ("BCDR: Site Recovery + Backup（Q7-9）",               v3_bcdr()),
    "vol3_q10_aks_vm":                   ("AKS マイクロサービス + VM（Q10）",                   v3_aks_vm()),
    "vol3_q11_q14_multiregion_webapp":   ("マルチリージョン Web App（Q11-14）",                 v3_multiregion_webapp()),
    "vol3_q17_logicapps_b2b":            ("Logic Apps B2B フェデレーション（Q17）",             v3_logicapps_b2b()),
    "vol3_q28_vpn_azurefiles":           ("ブランチ → VPN → Azure Files（Q28）",               v3_vpn_azurefiles()),
    "vol3_q31_q34_expressroute":         ("ExpressRoute ハイブリッド（Q31-34）",                v3_expressroute()),
    "vol3_q36_cosmos_synapse":           ("Cosmos DB → Synapse Analytics（Q36）",               v3_cosmos_synapse()),
    "vol3_q43_apexcore_tm":              ("ApexCore: Traffic Manager マルチリージョン（Q43）",  v3_apexcore_tm()),
    "vol3_q46_q47_app_keyvault":         ("App Service + Managed Identity + Key Vault（Q46-47）", v3_app_keyvault()),
    "vol3_q52_appinsights":              ("App Service + Application Insights（Q52）",           v3_appinsights()),
}

VOL4_SVG_MAP = {
    "vol4_q01_adf_blob_sql":            ("ADF ETL: Blob → SQL DB（Q1）",                       v4_adf_blob_sql()),
    "vol4_q02_eventhubs_adls":          ("Event Hubs → Data Lake ストリーミング（Q2）",         v4_eventhubs_adls()),
    "vol4_q11_servicebus_fifo":         ("Service Bus FIFO メッセージング（Q11）",              v4_servicebus_fifo()),
    "vol4_q12_multiregion_vms":         ("マルチリージョン VM + Front Door（Q12）",             v4_multiregion_vms()),
    "vol4_q13_app_sql_redis":           ("App Service + SQL DB + Redis Cache（Q13）",           v4_app_sql_redis()),
    "vol4_q19_eventhubs_capture":       ("Event Hubs Capture コールドパス（Q19）",              v4_eventhubs_capture()),
    "vol4_q23_sql_ha_encrypt":          ("SQL DB 高可用性 + 暗号化（Q23）",                    v4_sql_ha_encrypt()),
    "vol4_q27_q28_vwan_expressroute":   ("仮想 WAN: 4拠点 + ExpressRoute（Q27-28）",           v4_vwan_expressroute()),
    "vol4_q29_databricks_vnet":         ("Databricks + VNet プライベート接続（Q29）",           v4_databricks_vnet()),
    "vol4_q37_functions_aks":           ("Functions → AKS 移行（Q37）",                        v4_functions_aks()),
    "vol4_q42_q43_pe_dns":              ("Private Endpoint + DNS + ExpressRoute（Q42-43）",     v4_pe_dns()),
    "vol4_q50_q51_er_globalreach":      ("ExpressRoute Global Reach + Traffic Manager（Q50-51）", v4_er_globalreach()),
    "vol4_q54_q55_data_pipeline":       ("データパイプライン: SQL → ADF → Synapse（Q54-55）",  v4_data_pipeline()),
}

def patch_vol(path, svg_map):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'(const QUESTIONS = )(\[.*?\]);', content, re.DOTALL)
    prefix = match.group(1)
    qs = json.loads(match.group(2))
    updated = 0
    for q in qs:
        exp = q.get('exp_html', '')
        img_m = re.search(r'<img src="picture/([^"]+)\.png"[^>]*>', exp)
        if not img_m:
            continue
        fname = img_m.group(1)
        if fname not in svg_map:
            print(f"  Q{q['num']}: unknown {fname}")
            continue
        title, svg_html = svg_map[fname]
        new_exp = re.sub(
            r'<img src="picture/' + re.escape(fname) + r'\.png"[^>]*>',
            svg_html, exp, count=1
        )
        if new_exp != exp:
            q['exp_html'] = new_exp
            updated += 1
            print(f"  Q{q['num']}: ✓ {fname}")
    new_json = json.dumps(qs, ensure_ascii=False, separators=(',', ':'))
    new_content = content[:match.start()] + prefix + new_json + ';' + content[match.end():]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  → Updated {updated} questions in {path}\n")

print("=== vol3 ===")
patch_vol('/Users/fujiikai/SCstudy/az305/vol3.html', VOL3_SVG_MAP)
print("=== vol4 ===")
patch_vol('/Users/fujiikai/SCstudy/az305/vol4.html', VOL4_SVG_MAP)
print("✅ Done")
