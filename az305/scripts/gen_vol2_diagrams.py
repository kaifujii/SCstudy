"""Generate vol2 architecture diagrams using official Azure icons."""
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import AppServices, FunctionApps, KubernetesServices, ACR, ContainerRegistries
from diagrams.azure.network import (ApplicationGateway, FrontDoors, VirtualNetworks,
                                    VirtualNetworkGateways, PrivateEndpoint, TrafficManagerProfiles,
                                    LoadBalancers, PublicIpAddresses, Firewall)
from diagrams.azure.database import SQLDatabases, SQLServers, CosmosDb, CacheForRedis
from diagrams.azure.storage import StorageAccounts, BlobStorage
from diagrams.azure.security import KeyVaults
from diagrams.azure.monitor import LogAnalyticsWorkspaces, ApplicationInsights, Monitor
from diagrams.azure.identity import ActiveDirectory, ManagedIdentities
from diagrams.azure.integration import (APIManagement, ServiceBus, DataFactories,
                                        LogicApps, EventGridDomains)
from diagrams.azure.analytics import EventHubs, SynapseAnalytics
from diagrams.azure.general import ManagementGroups, Subscriptions, ResourceGroups
from diagrams.azure.managementgovernance import Policy, AzureArc

OUTDIR = "az305/picture"
GRAPH = {"bgcolor": "white", "pad": "0.6", "fontname": "Segoe UI"}
CLUSTER_ATTR = {"bgcolor": "#f0f4ff", "style": "rounded", "pencolor": "#3a6cbf", "fontcolor": "#1a3a6a", "fontname": "Segoe UI", "fontsize": "12"}
REGION_ATTR  = {"bgcolor": "#eaf3ff", "style": "rounded,dashed", "pencolor": "#0072C6", "fontcolor": "#0072C6", "fontname": "Segoe UI", "fontsize": "11"}
OK_ATTR      = {"bgcolor": "#e8f5e9", "style": "rounded,dashed", "pencolor": "#107C41", "fontcolor": "#107C41", "fontname": "Segoe UI", "fontsize": "11"}
NG_ATTR      = {"bgcolor": "#fdecea", "style": "rounded,dashed", "pencolor": "#c0392b", "fontcolor": "#c0392b", "fontname": "Segoe UI", "fontsize": "11"}


# ── 1. SQL 監査ログ (Q1-3) ────────────────────────────────────────────────────
with Diagram("SQL監査ログの構成", show=False,
             filename=f"{OUTDIR}/vol2_q01_q03_sql_audit",
             direction="LR", graph_attr=GRAPH):
    with Cluster("East US  ✔ 同一リージョン", graph_attr=OK_ATTR):
        sql1  = SQLServers("SQLsvr1\n(East US)")
        stor1 = StorageAccounts("storage1\n(East US)")
        sql1 >> Edge(label="監査ログ保存") >> stor1

    with Cluster("West US / Central US  ✘ 異なるリージョン", graph_attr=NG_ATTR):
        sql2  = SQLServers("SQLsvr2\n(West US)")
        stor2 = StorageAccounts("storage2\n(Central US)")
        sql2 >> Edge(label="設定不可", color="red", style="dashed") >> stor2


# ── 2. 管理グループ階層 (Q9-10) ───────────────────────────────────────────────
with Diagram("管理グループ階層", show=False,
             filename=f"{OUTDIR}/vol2_q09_q10_mgmt_group",
             direction="TB", graph_attr=GRAPH):
    root = ManagementGroups("Tenant Root\nManagement Group")
    with Cluster("MG-A", graph_attr=CLUSTER_ATTR):
        mga  = ManagementGroups("MG-A\n(Dept A)")
        sub1 = Subscriptions("Sub-A1")
        sub2 = Subscriptions("Sub-A2")
        mga >> sub1
        mga >> sub2
    with Cluster("MG-B", graph_attr=CLUSTER_ATTR):
        mgb  = ManagementGroups("MG-B\n(Dept B)")
        sub3 = Subscriptions("Sub-B1")
        mgb >> sub3
    root >> mga
    root >> mgb
    pol = Policy("Azure Policy\n(上位から継承)")
    root >> Edge(style="dashed", color="gray", label="ポリシー継承") >> pol


# ── 3. Front Door + マルチリージョン AKS (Q12) ───────────────────────────────
with Diagram("Azure Front Door + マルチリージョン AKS", show=False,
             filename=f"{OUTDIR}/vol2_q12_frontdoor_aks",
             direction="LR", graph_attr=GRAPH):
    fd = FrontDoors("Azure Front Door\n(グローバルLB)")
    with Cluster("East US", graph_attr=REGION_ATTR):
        aks1 = KubernetesServices("AKS Cluster\n(East US)")
    with Cluster("West US", graph_attr=REGION_ATTR):
        aks2 = KubernetesServices("AKS Cluster\n(West US)")
    acr = ContainerRegistries("Azure Container\nRegistry (共有)")
    fd >> Edge(label="ルーティング") >> [aks1, aks2]
    acr >> Edge(style="dashed", label="イメージ Pull") >> [aks1, aks2]


# ── 4. Service Bus トピック Pub/Sub (Q17) ────────────────────────────────────
with Diagram("Service Bus トピック (Pub/Sub)", show=False,
             filename=f"{OUTDIR}/vol2_q17_servicebus_pubsub",
             direction="LR", graph_attr=GRAPH):
    pub = AppServices("Publisher\n(App Service)")
    with Cluster("Azure Service Bus Topic", graph_attr=CLUSTER_ATTR):
        topic = ServiceBus("Topic")
    with Cluster("Subscribers", graph_attr=CLUSTER_ATTR):
        s1 = FunctionApps("Subscription 1\n→ Functions")
        s2 = LogicApps("Subscription 2\n→ Logic Apps")
        s3 = AppServices("Subscription 3\n→ App Service")
    pub >> Edge(label="Publish") >> topic
    topic >> Edge(label="各サブスクへ\nコピー配信") >> [s1, s2, s3]


# ── 5. Application Gateway + WAF (Q23-24) ────────────────────────────────────
with Diagram("Application Gateway + WAF", show=False,
             filename=f"{OUTDIR}/vol2_q23_q24_appgw_waf",
             direction="LR", graph_attr=GRAPH):
    inet = PublicIpAddresses("インターネット\nクライアント")
    agw  = ApplicationGateway("App Gateway\n(WAF v2)")
    kv   = KeyVaults("Key Vault\n(SSL証明書)")
    with Cluster("Backend Pool", graph_attr=CLUSTER_ATTR):
        be1 = AppServices("App Service 1")
        be2 = AppServices("App Service 2")
    inet >> Edge(label="HTTPS") >> agw
    kv   >> Edge(style="dashed", label="証明書取得") >> agw
    agw  >> Edge(label="L7 ルーティング") >> [be1, be2]


# ── 6. Azure Data Factory パイプライン (Q28) ─────────────────────────────────
with Diagram("Azure Data Factory パイプライン", show=False,
             filename=f"{OUTDIR}/vol2_q28_adf_pipeline",
             direction="LR", graph_attr=GRAPH):
    with Cluster("オンプレミス", graph_attr=CLUSTER_ATTR):
        onprem = SQLServers("SQL Server\n(オンプレ)")
    with Cluster("Azure Data Factory", graph_attr=CLUSTER_ATTR):
        adf = DataFactories("ADF\n(Self-hosted IR)")
    with Cluster("Azure", graph_attr=CLUSTER_ATTR):
        blob   = BlobStorage("Blob Storage\n(Staging)")
        synapse = SynapseAnalytics("Synapse / SQL\nData Warehouse")
    onprem >> Edge(label="Copy via IR") >> adf
    adf    >> Edge(label="Staging")     >> blob
    blob   >> Edge(label="Load")        >> synapse


# ── 7. Azure Bastion 構成 (Q42-43) ───────────────────────────────────────────
with Diagram("Azure Bastion 構成", show=False,
             filename=f"{OUTDIR}/vol2_q42_q43_bastion",
             direction="LR", graph_attr=GRAPH):
    admin = PublicIpAddresses("管理者\n(ブラウザ HTTPS)")
    with Cluster("Azure VNet", graph_attr=CLUSTER_ATTR):
        with Cluster("AzureBastionSubnet", graph_attr=REGION_ATTR):
            bastion = Firewall("Azure Bastion\n(マネージド)")
        with Cluster("VM Subnet (プライベート)", graph_attr=CLUSTER_ATTR):
            vm1 = AppServices("Windows VM\n(パブリックIPなし)")
            vm2 = AppServices("Linux VM\n(パブリックIPなし)")
    admin   >> Edge(label="HTTPS:443") >> bastion
    bastion >> Edge(label="RDP/SSH\n(内部通信のみ)") >> [vm1, vm2]


# ── 8. Azure Front Door グローバル負荷分散 (Q44) ─────────────────────────────
with Diagram("Azure Front Door グローバル負荷分散", show=False,
             filename=f"{OUTDIR}/vol2_q44_frontdoor_global",
             direction="LR", graph_attr=GRAPH):
    fd = FrontDoors("Azure Front Door\n(Anycast・Edge POP)")
    with Cluster("East US", graph_attr=REGION_ATTR):
        app1 = AppServices("App Service\n(East US)")
    with Cluster("West Europe", graph_attr=REGION_ATTR):
        app2 = AppServices("App Service\n(West EU)")
    with Cluster("SE Asia", graph_attr=REGION_ATTR):
        app3 = AppServices("App Service\n(SE Asia)")
    fd >> Edge(label="最低レイテンシへ\nルーティング") >> [app1, app2, app3]


# ── 9. API Management + Entra ID (Q46-47) ────────────────────────────────────
with Diagram("API Management + Entra ID", show=False,
             filename=f"{OUTDIR}/vol2_q46_q47_apim",
             direction="LR", graph_attr=GRAPH):
    client = AppServices("クライアント\n(SPA / モバイル)")
    aad    = ActiveDirectory("Microsoft\nEntra ID")
    apim   = APIManagement("API Management\n(ポリシー・認証)")
    with Cluster("Backend", graph_attr=CLUSTER_ATTR):
        be1 = AppServices("Backend API 1\n(App Service)")
        be2 = FunctionApps("Backend API 2\n(Functions)")
    client >> Edge(label="① 認証要求") >> aad
    aad    >> Edge(label="② JWT Token", style="dashed") >> client
    client >> Edge(label="③ Bearer Token") >> apim
    apim   >> Edge(label="④ 転送") >> [be1, be2]


# ── 10. AMPLS (Q55) ───────────────────────────────────────────────────────────
with Diagram("Azure Monitor Private Link Scope (AMPLS)", show=False,
             filename=f"{OUTDIR}/vol2_q55_ampls",
             direction="LR", graph_attr=GRAPH):
    with Cluster("Azure VNet (プライベート)", graph_attr=CLUSTER_ATTR):
        vm  = AppServices("Azure VM\n監視対象")
        pe  = PrivateEndpoint("Private\nEndpoint")
        vm >> pe
    with Cluster("AMPLS", graph_attr=REGION_ATTR):
        law   = LogAnalyticsWorkspaces("Log Analytics\nWorkspace")
        appins = ApplicationInsights("Application\nInsights")
        mon   = Monitor("Azure Monitor")
    pe >> Edge(label="プライベート通信\n(インターネット不使用)") >> [law, appins]
    [law, appins] >> mon

print("✅ All 10 vol2 diagrams generated in az305/picture/")
