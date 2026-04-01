"""Generate PNG architecture diagrams for vol4 questions."""
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import AppServices, FunctionApps, VirtualMachine, KubernetesServices, AKS
from diagrams.azure.network import (VirtualNetworks, LoadBalancers, ApplicationGateway,
                                     TrafficManagerProfiles, FrontDoors, VirtualNetworkGateways,
                                     ExpressrouteCircuits, PrivateEndpoint, DNSPrivateZones, VirtualWans)
from diagrams.azure.storage import BlobStorage, StorageAccounts, DataLakeStorage
from diagrams.azure.database import SQLDatabases, CosmosDb, CacheForRedis, SQLServers, ElasticDatabasePools
from diagrams.azure.security import KeyVaults
from diagrams.azure.monitor import ApplicationInsights, LogAnalyticsWorkspaces, Monitor
from diagrams.azure.identity import ActiveDirectory, ManagedIdentities
from diagrams.azure.integration import ServiceBus, LogicApps, APIManagement, EventGridTopics
from diagrams.azure.analytics import EventHubs, DataFactories, AzureSynapseAnalytics, SynapseAnalytics, Databricks, AzureDatabricks
from diagrams.azure.migration import RecoveryServicesVaults
from diagrams.azure.general import StorageQueue
from diagrams.onprem.compute import Server

OUT = "picture"
GRAPH_ATTR = {"bgcolor": "white", "pad": "0.5", "fontname": "Arial", "splines": "ortho"}
NODE_ATTR  = {"fontname": "Arial", "fontsize": "11"}
EDGE_ATTR  = {"fontname": "Arial", "fontsize": "9"}


# ── Q1: ADF: Blob → SQL ETL pipeline ───────────────────────────────────────
with Diagram("ADF ETL: Blob → SQL DB", show=False,
             filename=f"{OUT}/vol4_q01_adf_blob_sql",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    blob = BlobStorage("Blob Storage\n(Webアクセスログ)")
    adf  = DataFactories("Azure Data Factory\n(変換パイプライン)")
    sql  = SQLDatabases("Azure SQL DB\n(月次レポート)")
    blob >> Edge(label="トリガー/コピー") >> adf >> Edge(label="ロード") >> sql
print("vol4_q01 done")


# ── Q2: Event Hubs → ADLS streaming ────────────────────────────────────────
with Diagram("Event Hubs → Data Lake ストリーミング", show=False,
             filename=f"{OUT}/vol4_q02_eventhubs_adls",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    eh   = EventHubs("Event Hubs\n(大量JSON取り込み)")
    cap  = BlobStorage("Event Hubs\nCapture")
    adls = DataLakeStorage("ADLS Gen2\n(日付/時刻別ディレクトリ)")
    eh >> Edge(label="Capture") >> cap >> Edge(label="自動転送") >> adls
print("vol4_q02 done")


# ── Q11: Service Bus FIFO queue ────────────────────────────────────────────
with Diagram("Service Bus FIFO メッセージング", show=False,
             filename=f"{OUT}/vol4_q11_servicebus_fifo",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    sender   = AppServices("送信コンポーネント")
    sb       = ServiceBus("Service Bus\nQueue\n(FIFO + セッション)")
    receiver = AppServices("受信コンポーネント\n(順序保証)")
    sender >> Edge(label="メッセージ送信") >> sb >> Edge(label="順序通りに処理") >> receiver
print("vol4_q11 done")


# ── Q12: Multi-VNet VMs + Front Door ───────────────────────────────────────
with Diagram("マルチリージョン VM + Front Door", show=False,
             filename=f"{OUT}/vol4_q12_multiregion_vms",
             direction="TB",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    fd = FrontDoors("Azure Front Door\n(HTTPS グローバル LB)")
    with Cluster("Central US VNet"):
        vm1 = VirtualMachine("VM1 フロントエンド")
    with Cluster("East US VNet"):
        vm2 = VirtualMachine("VM2 バックエンド")
    with Cluster("West US 2 VNet"):
        vm3 = VirtualMachine("VM3 フロントエンド")
    fd >> vm1
    fd >> vm3
    vm1 >> Edge(label="VNet Peering") >> vm2
    vm3 >> Edge(label="VNet Peering") >> vm2
print("vol4_q12 done")


# ── Q13: App Service + SQL DB + Redis Cache ────────────────────────────────
with Diagram("App Service + SQL DB + Redis Cache", show=False,
             filename=f"{OUT}/vol4_q13_app_sql_redis",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    app   = AppServices("App Service\n(マルチティア App1)")
    redis = CacheForRedis("Azure Cache\nfor Redis\n(読み取りキャッシュ)")
    sql   = SQLDatabases("Azure SQL DB\n(SQL1)")
    app >> Edge(label="キャッシュ確認") >> redis
    redis >> Edge(style="dashed", label="キャッシュミス") >> sql
    sql >> Edge(style="dashed", label="レスポンス") >> redis
print("vol4_q13 done")


# ── Q19: Event Hubs Capture コールドパス ────────────────────────────────────
with Diagram("Event Hubs Capture コールドパス", show=False,
             filename=f"{OUT}/vol4_q19_eventhubs_capture",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    app  = AppServices("アプリ\n(50,000 events/日)")
    eh   = EventHubs("Event Hubs\n(ストリーミング)")
    cap  = StorageAccounts("Capture\n(Blob/ADLS)")
    rpt  = SynapseAnalytics("レポーティング\nシステム")
    app >> Edge(label="イベント送信") >> eh
    eh >> Edge(label="Capture\n(Avro形式)") >> cap
    cap >> Edge(label="バッチ処理") >> rpt
print("vol4_q19 done")


# ── Q23: SQL DB HA + Encryption ────────────────────────────────────────────
with Diagram("SQL DB 高可用性 + 暗号化", show=False,
             filename=f"{OUT}/vol4_q23_sql_ha_encrypt",
             direction="TB",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    app = AppServices("Web アプリ\n(従業員 PII)")
    with Cluster("Azure SQL Database (ゾーン冗長)"):
        sql_p = SQLDatabases("プライマリ DB\nZone 1")
        sql_s = SQLDatabases("セカンダリ DB\nZone 2/3")
    kv  = KeyVaults("Key Vault\n(CMK for TDE)")
    app >> sql_p
    sql_p >> Edge(label="同期レプリカ") >> sql_s
    sql_p >> Edge(style="dashed", label="Column Encryption\nキー参照") >> kv
print("vol4_q23 done")


# ── Q27/Q28: 4 offices + ExpressRoute + Virtual WAN ────────────────────────
with Diagram("仮想 WAN: 4拠点 + ExpressRoute", show=False,
             filename=f"{OUT}/vol4_q27_q28_vwan_expressroute",
             direction="TB",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    vwan = VirtualWans("Azure Virtual WAN\n(Standard SKU)")
    with Cluster("ExpressRoute 接続"):
        er1 = ExpressrouteCircuits("NYC\nExpressRoute")
        er2 = ExpressrouteCircuits("SYD\nExpressRoute")
        er3 = ExpressrouteCircuits("PAR\nExpressRoute")
        er4 = ExpressrouteCircuits("JNB\nExpressRoute")
    vwan >> er1
    vwan >> er2
    vwan >> er3
    vwan >> er4
print("vol4_q27_q28 done")


# ── Q29: Databricks + VNet peering ────────────────────────────────────────
with Diagram("Databricks + VNet プライベート接続", show=False,
             filename=f"{OUT}/vol4_q29_databricks_vnet",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        on_app = Server("オンプレ アプリ")
    vpng = VirtualNetworkGateways("VPN/ExpressRoute")
    with Cluster("Azure VNet (顧客管理)"):
        pe = PrivateEndpoint("Private Endpoint")
        db = AzureDatabricks("Azure Databricks\n(VNet Injection)")
    on_app >> Edge(label="プライベート接続") >> vpng >> pe >> db
print("vol4_q29 done")


# ── Q37: AKS – Functions から移行 ──────────────────────────────────────────
with Diagram("Functions → AKS 移行", show=False,
             filename=f"{OUT}/vol4_q37_functions_aks",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    client  = AppServices("クライアント アプリ")
    with Cluster("Azure Kubernetes Service"):
        aks  = AKS("AKS クラスター\n(KEDA スケーリング)")
        fn   = FunctionApps("Functions\nコンテナー")
    eh   = EventHubs("Event Hubs\n(イベント ソース)")
    client >> aks
    aks >> fn
    eh >> Edge(label="トリガー") >> fn
print("vol4_q37 done")


# ── Q42/Q43: Private Endpoint + DNS + ExpressRoute ────────────────────────
with Diagram("Private Endpoint + DNS + ExpressRoute", show=False,
             filename=f"{OUT}/vol4_q42_q43_pe_dns",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        dns_on = Server("VM1\nDNS サーバー")
        on_cli = Server("オンプレ クライアント")
    er  = ExpressrouteCircuits("ExpressRoute")
    with Cluster("Azure VNET1"):
        pe  = PrivateEndpoint("PE1\nPrivate Endpoint")
        pdz = DNSPrivateZones("apexcore.com\nプライベート DNS")
        sql = SQLDatabases("SQLDB1")
    on_cli >> dns_on >> Edge(label="DNS転送") >> er >> pdz
    pe >> sql
    pdz >> Edge(style="dashed") >> pe
print("vol4_q42_q43 done")


# ── Q50/Q51: ExpressRoute Global Reach + Traffic Manager ──────────────────
with Diagram("ExpressRoute Global Reach + Traffic Manager", show=False,
             filename=f"{OUT}/vol4_q50_q51_er_globalreach",
             direction="LR",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("NYC DC"):
        nyc = Server("NYC\nオンプレミス DC")
    with Cluster("LA DC"):
        la  = Server("LA\nオンプレミス DC")
    with Cluster("Azure East US"):
        er_east = ExpressrouteCircuits("ExpressRoute\n(East US)")
        app_e   = AppServices("App\nEast US")
    with Cluster("Azure West US"):
        er_west = ExpressrouteCircuits("ExpressRoute\n(West US)")
        app_w   = AppServices("App\nWest US")
    tm = TrafficManagerProfiles("Traffic Manager\n(フェールオーバー)")
    nyc >> er_east
    la  >> er_west
    er_east >> Edge(label="Global Reach") >> er_west
    tm >> app_e
    tm >> app_w
print("vol4_q50_q51 done")


# ── Q54/Q55: SQL Server → ADF → Synapse → serving layer ───────────────────
with Diagram("データ パイプライン: SQL→ADF→Synapse→PowerBI", show=False,
             filename=f"{OUT}/vol4_q54_q55_data_pipeline",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        sql_on = Server("複数 SQL Server")
    adf  = DataFactories("Azure Data Factory\n(差分取り込み)")
    blob = BlobStorage("Blob Storage\n(ステージング)")
    syn  = SynapseAnalytics("Synapse Analytics\n(OLAP モデル)")
    pbi  = AppServices("Power BI /\nレポーティング")
    sql_on >> Edge(label="変更取り込み") >> adf >> blob >> syn >> Edge(label="提供") >> pbi
print("vol4_q54_q55 done")

print("\n✅ Vol4 diagrams generation complete!")
