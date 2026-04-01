"""Generate PNG architecture diagrams for vol5 questions."""
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import AppServices, FunctionApps, VirtualMachine, KubernetesServices, AKS, ContainerRegistries
from diagrams.azure.network import (VirtualNetworks, LoadBalancers, ApplicationGateway, Firewall,
                                     TrafficManagerProfiles, FrontDoors, VirtualNetworkGateways,
                                     ExpressrouteCircuits, PrivateEndpoint, DNSPrivateZones)
from diagrams.azure.storage import BlobStorage, StorageAccounts, DataLakeStorage, AzureFileshares
from diagrams.azure.database import SQLDatabases, CosmosDb, CacheForRedis, SQLServers, ElasticDatabasePools
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.monitor import ApplicationInsights, LogAnalyticsWorkspaces, Monitor
from diagrams.azure.identity import ActiveDirectory, ManagedIdentities, EntraConnect
from diagrams.azure.integration import ServiceBus, LogicApps, APIManagement
from diagrams.azure.analytics import EventHubs, DataFactories, AzureSynapseAnalytics, SynapseAnalytics
from diagrams.azure.migration import RecoveryServicesVaults
from diagrams.azure.general import ManagementGroups, Subscriptions, ResourceGroups
from diagrams.onprem.compute import Server

OUT = "picture"
GRAPH_ATTR = {"bgcolor": "white", "pad": "0.5", "fontname": "Arial", "splines": "ortho"}
NODE_ATTR  = {"fontname": "Arial", "fontsize": "11"}
EDGE_ATTR  = {"fontname": "Arial", "fontsize": "9"}


# ── Q1: 2リージョン × 4AZ VM デプロイ ─────────────────────────────────────
with Diagram("2リージョン 4可用性ゾーン VM デプロイ", show=False,
             filename=f"{OUT}/vol5_q01_multiregion_az",
             direction="LR",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("East Japan (リージョン1)\nVNet 1"):
        vm1 = VirtualMachine("VM 群\nAZ-1")
        vm2 = VirtualMachine("VM 群\nAZ-2")
    with Cluster("West Japan (リージョン2)\nVNet 2"):
        vm3 = VirtualMachine("VM 群\nAZ-3")
        vm4 = VirtualMachine("VM 群\nAZ-4")
    VirtualNetworks("VNet Peering") >> Edge(style="dashed")
    vm1 - vm2
    vm3 - vm4
print("vol5_q01 done")


# ── Q3/Q4: SQL Server → Azure SQL DB 移行 (読み取りレプリカ) ──────────────
with Diagram("SQL Server → Azure SQL DB 移行 + HA", show=False,
             filename=f"{OUT}/vol5_q03_q04_sql_migration",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        sql_on = Server("SQL Server\n(SQL1)")
    dms = DataFactories("Database Migration\nService")
    with Cluster("Azure SQL DB\n(Business Critical)"):
        sql_p  = SQLDatabases("プライマリ レプリカ")
        sql_r1 = SQLDatabases("読み取り専用\nレプリカ 1")
        sql_r2 = SQLDatabases("読み取り専用\nレプリカ 2")
    sql_on >> Edge(label="移行") >> dms >> sql_p
    sql_p >> Edge(label="自動同期") >> sql_r1
    sql_p >> Edge(label="自動同期") >> sql_r2
print("vol5_q03_q04 done")


# ── Q5/Q6: ペタバイト規模 Data Lake Architecture ───────────────────────────
with Diagram("ペタバイト Data Lake アーキテクチャ", show=False,
             filename=f"{OUT}/vol5_q05_q06_datalake",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    src  = Server("多様なデータ ソース\n(構造化/半構造化/非構造化)")
    adls = DataLakeStorage("ADLS Gen2\n(ペタバイト規模)")
    ade  = SynapseAnalytics("Azure Data Explorer\n(KQL クエリ)")
    syn  = AzureSynapseAnalytics("Synapse Analytics\n(分析)")
    src >> Edge(label="取り込み") >> adls
    adls >> ade
    adls >> syn
print("vol5_q05_q06 done")


# ── Q16/Q17: APIM + App Service backend ────────────────────────────────────
with Diagram("API Management + App Service バックエンド", show=False,
             filename=f"{OUT}/vol5_q16_q17_apim",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    partner = Server("外部パートナー")
    apim    = APIManagement("Azure API Management\n(レート制限 / 認証)")
    app     = AppServices("App Service\nバックエンド")
    partner >> Edge(label="HTTPS") >> apim >> Edge(label="プロキシ") >> app
print("vol5_q16_q17 done")


# ── Q22: Multi-tenant SaaS + Elastic Pool ──────────────────────────────────
with Diagram("マルチテナント SaaS + Elastic Pool", show=False,
             filename=f"{OUT}/vol5_q22_multitenant_saas",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    users = Server("複数テナント ユーザー")
    app   = AppServices("SaaS アプリ\n(App Service)")
    with Cluster("Azure SQL\nElastic Pool"):
        db1 = SQLDatabases("テナント DB 1")
        db2 = SQLDatabases("テナント DB 2")
        db3 = SQLDatabases("テナント DB N")
    users >> app
    app >> db1
    app >> db2
    app >> db3
print("vol5_q22 done")


# ── Q23/Q24: AKS microservices + Container Registry ───────────────────────
with Diagram("AKS マイクロサービス + Container Registry", show=False,
             filename=f"{OUT}/vol5_q23_q24_aks_acr",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    acr  = ContainerRegistries("Azure Container\nRegistry (ACR)")
    with Cluster("Azure Kubernetes Service"):
        aks  = AKS("AKS クラスター")
        svc1 = FunctionApps("マイクロサービス A")
        svc2 = FunctionApps("マイクロサービス B")
    acr >> Edge(label="イメージ プル") >> aks
    aks >> svc1
    aks >> svc2
print("vol5_q23_q24 done")


# ── Q26: SQL Always On + Traffic Manager (マルチリージョン) ───────────────
with Diagram("SQL Always On + Traffic Manager DR", show=False,
             filename=f"{OUT}/vol5_q26_sql_alwayson_tm",
             direction="LR",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    tm = TrafficManagerProfiles("Traffic Manager\n(フェールオーバー)")
    with Cluster("East US VNet"):
        vm1_p = VirtualMachine("VM\nプライマリ レプリカ")
        lb1   = LoadBalancers("ILB Listener")
    with Cluster("West US VNet"):
        vm2_s = VirtualMachine("VM\nセカンダリ レプリカ")
        lb2   = LoadBalancers("ILB Listener")
    tm >> lb1
    tm >> lb2
    vm1_p >> Edge(label="Always On\n同期") >> vm2_s
print("vol5_q26 done")


# ── Q27/Q28: Multi-region Web App + App Gateway WAF ───────────────────────
with Diagram("マルチリージョン Web App + Front Door + WAF", show=False,
             filename=f"{OUT}/vol5_q27_q28_webapp_waf",
             direction="TB",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    fd   = FrontDoors("Azure Front Door\n(グローバル LB / WAF)")
    with Cluster("リージョン A"):
        app_a = AppServices("Web App A")
    with Cluster("リージョン B"):
        app_b = AppServices("Web App B")
    fd >> app_a
    fd >> app_b
print("vol5_q27_q28 done")


# ── Q29/Q30: App Service + SQL DB + Private Endpoint + DNS ────────────────
with Diagram("App Service + Private Endpoint + DNS", show=False,
             filename=f"{OUT}/vol5_q29_q30_app_pe_dns",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    app = AppServices("WebApp1\n(App Service\nVNet Integration)")
    pe  = PrivateEndpoint("PE1\nPrivate Endpoint")
    dns = DNSPrivateZones("プライベート DNS\nゾーン")
    sql = SQLDatabases("DB1\n(Azure SQL DB)")
    app >> Edge(label="VNet 経由") >> pe
    pe >> sql
    dns >> Edge(style="dashed", label="名前解決") >> pe
print("vol5_q29_q30 done")


# ── Q31/Q32/Q33: APIM + VNet + VM (外部モード) ────────────────────────────
with Diagram("APIM 外部 VNet モード + バックエンド VM", show=False,
             filename=f"{OUT}/vol5_q31_q33_apim_vnet",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    client = Server("外部クライアント")
    with Cluster("VNet1"):
        with Cluster("ProdSubnet (APIM)"):
            apim = APIManagement("API Management\n(外部 VNet モード)")
        with Cluster("Subnet1"):
            vm1  = VirtualMachine("VM1")
            vm2  = VirtualMachine("VM2")
    client >> Edge(label="インターネット") >> apim
    apim >> vm1
    apim >> vm2
print("vol5_q31_q33 done")


# ── Q40: OnPrem AD + Entra Connect ──────────────────────────────────────────
with Diagram("オンプレミス AD + Entra ID Connect 同期", show=False,
             filename=f"{OUT}/vol5_q40_ad_entra_connect",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        ad_on = Server("AD DS\ncorp.ironclad.com")
    conn  = EntraConnect("Microsoft Entra\nConnect")
    entra = ActiveDirectory("Microsoft Entra ID\n(Azure AD)")
    with Cluster("Azure リソース"):
        res   = AppServices("Azure リソース\n(RBAC 割り当て)")
    ad_on >> Edge(label="同期") >> conn >> entra >> res
print("vol5_q40 done")


# ── Q42/Q43: Synapse + Managed Private Endpoint → ADLS ───────────────────
with Diagram("Synapse Analytics + Managed Private Endpoint", show=False,
             filename=f"{OUT}/vol5_q42_q43_synapse_mpe",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    syn  = AzureSynapseAnalytics("Synapse Analytics\nワークスペース")
    mpe  = PrivateEndpoint("Managed\nPrivate Endpoint")
    adls = DataLakeStorage("ADLS Gen2\n(機密データ)")
    blob = BlobStorage("Azure Blob\nStorage")
    syn >> Edge(label="安全なアクセス") >> mpe
    mpe >> adls
    mpe >> blob
print("vol5_q42_q43 done")


# ── Q49: ハイブリッド監視 (Log Analytics + Azure Arc) ─────────────────────
with Diagram("ハイブリッド監視: Log Analytics + Azure Arc", show=False,
             filename=f"{OUT}/vol5_q49_hybrid_monitoring",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        on_vm  = VirtualMachine("オンプレ VM\n(Azure Arc 登録)")
    with Cluster("Azure"):
        az_vm  = VirtualMachine("Azure VM")
    ama  = Monitor("Azure Monitor\nAgent (AMA)")
    law  = LogAnalyticsWorkspaces("Log Analytics\nWorkspace")
    on_vm >> ama
    az_vm >> ama
    ama >> Edge(label="ログ送信") >> law
print("vol5_q49 done")


# ── Q52/Q53/Q54: ハイブリッド SQL Server Always On DR ─────────────────────
with Diagram("ハイブリッド SQL Always On + DR", show=False,
             filename=f"{OUT}/vol5_q52_q54_hybrid_sql_dr",
             direction="LR",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス DC"):
        sql_on = Server("SQL Server\nプライマリ")
    vpng = VirtualNetworkGateways("VPN / ExpressRoute")
    with Cluster("Azure (DR リージョン)"):
        sql_az = VirtualMachine("SQL Server VM\nセカンダリ (DR)")
        rsv    = RecoveryServicesVaults("Recovery Services\nVault")
    sql_on >> Edge(label="Always On\nレプリケーション") >> vpng >> sql_az
    sql_on >> Edge(style="dashed", label="Azure Backup") >> rsv
print("vol5_q52_q54 done")

print("\n✅ Vol5 diagrams generation complete!")
