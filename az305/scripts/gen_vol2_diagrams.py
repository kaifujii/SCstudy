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

# Dark, compact, wide graph settings
GRAPH = {
    "bgcolor": "#0d1b2e",
    "pad": "0.25",
    "fontname": "Segoe UI",
    "fontcolor": "#c8d8f0",
    "dpi": "110",
    "ranksep": "0.5",
    "nodesep": "0.35",
    "margin": "0.2",
}
CLUSTER_ATTR = {
    "bgcolor": "#152844",
    "style": "rounded",
    "pencolor": "#2563eb",
    "fontcolor": "#93c5fd",
    "fontname": "Segoe UI",
    "fontsize": "11",
    "margin": "12",
}
REGION_ATTR = {
    "bgcolor": "#0f2233",
    "style": "rounded,dashed",
    "pencolor": "#38bdf8",
    "fontcolor": "#38bdf8",
    "fontname": "Segoe UI",
    "fontsize": "10",
    "margin": "10",
}
OK_ATTR = {
    "bgcolor": "#0d2318",
    "style": "rounded,dashed",
    "pencolor": "#22c55e",
    "fontcolor": "#86efac",
    "fontname": "Segoe UI",
    "fontsize": "10",
    "margin": "10",
}
NG_ATTR = {
    "bgcolor": "#2d1010",
    "style": "rounded,dashed",
    "pencolor": "#ef4444",
    "fontcolor": "#fca5a5",
    "fontname": "Segoe UI",
    "fontsize": "10",
    "margin": "10",
}
NODE_ATTR = {"fontcolor": "#e2e8f0", "fontsize": "10", "fontname": "Segoe UI"}
EDGE_ATTR = {"color": "#64748b", "fontcolor": "#94a3b8", "fontsize": "9", "fontname": "Segoe UI"}


# ── 1. SQL 監査ログ (Q1-3) ────────────────────────────────────────────────────
with Diagram("SQL監査ログの構成", show=False,
             filename=f"{OUTDIR}/vol2_q01_q03_sql_audit",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("East US  同一リージョン", graph_attr=OK_ATTR):
        sql1  = SQLServers("SQLsvr1\n(East US)")
        stor1 = StorageAccounts("storage1\n(East US)")
        sql1 >> Edge(label="監査ログ保存", color="#22c55e") >> stor1

    with Cluster("West US / Central US  異なるリージョン", graph_attr=NG_ATTR):
        sql2  = SQLServers("SQLsvr2\n(West US)")
        stor2 = StorageAccounts("storage2\n(Central US)")
        sql2 >> Edge(label="設定不可", color="#ef4444", style="dashed") >> stor2


# ── 2. 管理グループ階層 (Q9-10) ───────────────────────────────────────────────
with Diagram("管理グループ階層", show=False,
             filename=f"{OUTDIR}/vol2_q09_q10_mgmt_group",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    root = ManagementGroups("Tenant Root MG")
    pol  = Policy("Azure Policy\n(ポリシー継承)")
    with Cluster("MG-A (Dept A)", graph_attr=CLUSTER_ATTR):
        mga  = ManagementGroups("MG-A")
        sub1 = Subscriptions("Sub-A1")
        sub2 = Subscriptions("Sub-A2")
        mga >> [sub1, sub2]
    with Cluster("MG-B (Dept B)", graph_attr=CLUSTER_ATTR):
        mgb  = ManagementGroups("MG-B")
        sub3 = Subscriptions("Sub-B1")
        mgb >> sub3
    root >> [mga, mgb]
    root >> Edge(style="dashed", color="#94a3b8", label="継承") >> pol


# ── 3. Front Door + マルチリージョン AKS (Q12) ───────────────────────────────
with Diagram("Front Door + マルチリージョン AKS", show=False,
             filename=f"{OUTDIR}/vol2_q12_frontdoor_aks",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    fd  = FrontDoors("Azure Front Door")
    acr = ContainerRegistries("Container Registry")
    with Cluster("East US", graph_attr=REGION_ATTR):
        aks1 = KubernetesServices("AKS (East US)")
    with Cluster("West US", graph_attr=REGION_ATTR):
        aks2 = KubernetesServices("AKS (West US)")
    fd  >> Edge(label="ルーティング") >> [aks1, aks2]
    acr >> Edge(style="dashed", label="Image Pull") >> [aks1, aks2]


# ── 4. Service Bus トピック Pub/Sub (Q17) ────────────────────────────────────
with Diagram("Service Bus Pub/Sub", show=False,
             filename=f"{OUTDIR}/vol2_q17_servicebus_pubsub",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    pub = AppServices("Publisher")
    with Cluster("Service Bus Topic", graph_attr=CLUSTER_ATTR):
        topic = ServiceBus("Topic")
    with Cluster("Subscribers", graph_attr=CLUSTER_ATTR):
        s1 = FunctionApps("Sub1: Functions")
        s2 = LogicApps("Sub2: Logic Apps")
        s3 = AppServices("Sub3: App Svc")
    pub   >> Edge(label="Publish") >> topic
    topic >> Edge(label="配信") >> [s1, s2, s3]


# ── 5. Application Gateway + WAF (Q23-24) ────────────────────────────────────
with Diagram("App Gateway + WAF", show=False,
             filename=f"{OUTDIR}/vol2_q23_q24_appgw_waf",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    inet = PublicIpAddresses("Internet")
    agw  = ApplicationGateway("App GW (WAF v2)")
    kv   = KeyVaults("Key Vault\n(SSL証明書)")
    with Cluster("Backend Pool", graph_attr=CLUSTER_ATTR):
        be1 = AppServices("App Svc 1")
        be2 = AppServices("App Svc 2")
    inet >> Edge(label="HTTPS") >> agw
    kv   >> Edge(style="dashed", label="証明書") >> agw
    agw  >> Edge(label="L7 route") >> [be1, be2]


# ── 6. Azure Data Factory パイプライン (Q28) ─────────────────────────────────
with Diagram("Azure Data Factory パイプライン", show=False,
             filename=f"{OUTDIR}/vol2_q28_adf_pipeline",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("On-premises", graph_attr=CLUSTER_ATTR):
        onprem = SQLServers("SQL Server")
    adf = DataFactories("ADF (IR)")
    with Cluster("Azure", graph_attr=CLUSTER_ATTR):
        blob    = BlobStorage("Blob (Staging)")
        synapse = SynapseAnalytics("Synapse DW")
    onprem >> Edge(label="Copy via IR") >> adf
    adf    >> Edge(label="Stage")       >> blob
    blob   >> Edge(label="Load")        >> synapse


# ── 7. Azure Bastion 構成 (Q42-43) ───────────────────────────────────────────
with Diagram("Azure Bastion 構成", show=False,
             filename=f"{OUTDIR}/vol2_q42_q43_bastion",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    admin = PublicIpAddresses("管理者\n(HTTPS)")
    with Cluster("Azure VNet", graph_attr=CLUSTER_ATTR):
        with Cluster("AzureBastionSubnet", graph_attr=REGION_ATTR):
            bastion = Firewall("Azure Bastion")
        with Cluster("VM Subnet (Private)", graph_attr=CLUSTER_ATTR):
            vm1 = AppServices("Windows VM")
            vm2 = AppServices("Linux VM")
    admin   >> Edge(label="443") >> bastion
    bastion >> Edge(label="RDP/SSH") >> [vm1, vm2]


# ── 8. Azure Front Door グローバル負荷分散 (Q44) ─────────────────────────────
with Diagram("Front Door グローバル負荷分散", show=False,
             filename=f"{OUTDIR}/vol2_q44_frontdoor_global",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    fd = FrontDoors("Azure Front Door\n(Anycast)")
    with Cluster("East US", graph_attr=REGION_ATTR):
        app1 = AppServices("App Svc\n(East US)")
    with Cluster("West Europe", graph_attr=REGION_ATTR):
        app2 = AppServices("App Svc\n(West EU)")
    with Cluster("SE Asia", graph_attr=REGION_ATTR):
        app3 = AppServices("App Svc\n(SE Asia)")
    fd >> Edge(label="最低レイテンシ") >> [app1, app2, app3]


# ── 9. API Management + Entra ID (Q46-47) ────────────────────────────────────
with Diagram("API Management + Entra ID", show=False,
             filename=f"{OUTDIR}/vol2_q46_q47_apim",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    client = AppServices("Client\n(SPA/Mobile)")
    aad    = ActiveDirectory("Entra ID")
    apim   = APIManagement("API Management")
    with Cluster("Backend", graph_attr=CLUSTER_ATTR):
        be1 = AppServices("API 1 (App Svc)")
        be2 = FunctionApps("API 2 (Functions)")
    client >> Edge(label="1: 認証") >> aad
    aad    >> Edge(label="2: JWT", style="dashed") >> client
    client >> Edge(label="3: Bearer") >> apim
    apim   >> Edge(label="4: 転送") >> [be1, be2]


# ── 10. AMPLS (Q55) ───────────────────────────────────────────────────────────
with Diagram("Azure Monitor Private Link Scope", show=False,
             filename=f"{OUTDIR}/vol2_q55_ampls",
             direction="LR", graph_attr=GRAPH,
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("Azure VNet (Private)", graph_attr=CLUSTER_ATTR):
        vm = AppServices("Azure VM")
        pe = PrivateEndpoint("Private Endpoint")
        vm >> pe
    with Cluster("AMPLS", graph_attr=REGION_ATTR):
        law    = LogAnalyticsWorkspaces("Log Analytics")
        appins = ApplicationInsights("App Insights")
        mon    = Monitor("Azure Monitor")
    pe >> Edge(label="Private通信") >> [law, appins]
    [law, appins] >> mon

print("All 10 vol2 diagrams generated in az305/picture/")
