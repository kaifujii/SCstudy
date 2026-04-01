"""Generate PNG architecture diagrams for vol3 questions."""
import os
from diagrams import Diagram, Cluster, Edge, Node
from diagrams.azure.compute import AppServices, FunctionApps, VirtualMachine, KubernetesServices, AKS, BatchAccounts
from diagrams.azure.network import (VirtualNetworks, Firewall, LoadBalancers, ApplicationGateway,
                                     TrafficManagerProfiles, FrontDoors, VirtualNetworkGateways,
                                     ExpressrouteCircuits, PrivateEndpoint, DNSPrivateZones)
from diagrams.azure.storage import BlobStorage, StorageAccounts, AzureFileshares, DataLakeStorage
from diagrams.azure.database import SQLDatabases, CosmosDb, CacheForRedis, SQLManagedInstances, SQLServers
from diagrams.azure.security import KeyVaults, Defender, Sentinel
from diagrams.azure.monitor import ApplicationInsights, LogAnalyticsWorkspaces, Monitor
from diagrams.azure.identity import ActiveDirectory, ManagedIdentities, ActiveDirectoryConnectHealth
from diagrams.azure.integration import ServiceBus, LogicApps, APIManagement, EventGridTopics
from diagrams.azure.analytics import EventHubs, DataFactories, AzureSynapseAnalytics, SynapseAnalytics
from diagrams.azure.migration import RecoveryServicesVaults
from diagrams.azure.general import ManagementGroups, ResourceGroups, Subscriptions
from diagrams.onprem.compute import Server

OUT = "picture"
GRAPH_ATTR = {"bgcolor": "white", "pad": "0.5", "fontname": "Arial", "splines": "ortho"}
NODE_ATTR  = {"fontname": "Arial", "fontsize": "11"}
EDGE_ATTR  = {"fontname": "Arial", "fontsize": "9"}


# ── Q1/Q2: AAD Audit → Event Hubs → Functions → Cosmos DB ──────────────────
with Diagram("AAD監査ログ取り込みパイプライン", show=False,
             filename=f"{OUT}/vol3_q01_q02_aad_eventhub_cosmos",
             direction="LR",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    aad  = ActiveDirectory("Microsoft Entra ID\n監査ログ")
    eh   = EventHubs("Event Hubs\n(サービス1)")
    fn   = FunctionApps("Azure Functions\n(サービス2)")
    cdb  = CosmosDb("Cosmos DB\nストレージ")
    aad >> Edge(label="イベント生成") >> eh >> Edge(label="転送") >> fn >> Edge(label="格納") >> cdb
print("vol3_q01_q02 done")


# ── Q5/Q6: OnPrem File Server → ADF Integration Runtime → Azure Storage ────
with Diagram("オンプレ→ADF→Azure Storage", show=False,
             filename=f"{OUT}/vol3_q05_q06_adf_onprem",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス"):
        srv  = Server("Server1\nファイルサーバー")
        ir   = Server("Self-hosted\nIntegration Runtime")
    with Cluster("Azure"):
        adf  = DataFactories("Azure Data Factory")
        stor = StorageAccounts("Azure Storage")
    srv >> Edge(style="dashed") >> ir >> Edge(label="コピー") >> adf >> Edge(label="転送") >> stor
print("vol3_q05_q06 done")


# ── Q7-Q9: BCDR – Site Recovery + Azure Backup ─────────────────────────────
with Diagram("BCDR: Site Recovery + Backup", show=False,
             filename=f"{OUT}/vol3_q07_q09_bcdr",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("プライマリ オンプレミス DC"):
        vm_sales = VirtualMachine("販売 VM")
        vm_fin   = VirtualMachine("財務 VM")
        vm_rep   = VirtualMachine("レポート VM")
    with Cluster("Recovery Services Vault"):
        rsv = RecoveryServicesVaults("RSV\n(Site Recovery\n+ Backup)")
    with Cluster("セカンダリ DC / Azure"):
        vm_dr = VirtualMachine("フェールオーバー先")
    vm_sales >> Edge(label="ASR\nレプリケーション", color="#0072C6") >> rsv
    vm_fin   >> Edge(label="Azure Backup",          color="#107C10") >> rsv
    vm_rep   >> Edge(label="Azure Backup",          color="#107C10") >> rsv
    rsv      >> Edge(label="フェールオーバー",        color="#C50F1F") >> vm_dr
print("vol3_q07_q09 done")


# ── Q10: AKS microservices + VMs in same VNet ──────────────────────────────
with Diagram("AKS マイクロサービス + VM", show=False,
             filename=f"{OUT}/vol3_q10_aks_vm",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("Azure VNet"):
        with Cluster("AKS クラスター"):
            aks  = AKS("AKS\nマイクロサービス")
            ilb  = LoadBalancers("Internal\nLoad Balancer")
        with Cluster("コンシューマー VM サブネット"):
            vm   = VirtualMachine("Consumer VM")
    vm >> Edge(label="内部アクセス") >> ilb >> aks
print("vol3_q10 done")


# ── Q11-Q14: Multi-region Web App + Traffic Manager / Front Door ───────────
with Diagram("マルチリージョン Web App", show=False,
             filename=f"{OUT}/vol3_q11_q14_multiregion_webapp",
             direction="TB",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    tm   = TrafficManagerProfiles("Traffic Manager\n(グローバル LB)")
    with Cluster("プライマリ リージョン"):
        app1 = AppServices("Web App\nインスタンス 1")
    with Cluster("セカンダリ リージョン"):
        app2 = AppServices("Web App\nインスタンス 2")
    tm >> Edge(label="ルーティング") >> app1
    tm >> Edge(label="ルーティング") >> app2
print("vol3_q11_q14 done")


# ── Q17: Logic Apps B2B (ApexCore ↔ Ironclad) ──────────────────────────────
with Diagram("Logic Apps B2B フェデレーション", show=False,
             filename=f"{OUT}/vol3_q17_logicapps_b2b",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("Ironclad テナント"):
        partner = ActiveDirectory("Ironclad\nEntra ID")
    with Cluster("ApexCore Azure"):
        la  = LogicApps("Logic Apps\n(HTTP トリガー)")
        svc = Server("オンプレミス\nWeb サービス")
    partner >> Edge(label="B2B アクセス") >> la >> Edge(label="内部呼び出し") >> svc
print("vol3_q17 done")


# ── Q28: Branch office → VPN → Azure Files ─────────────────────────────────
with Diagram("ブランチ → VPN → Azure Files", show=False,
             filename=f"{OUT}/vol3_q28_vpn_azurefiles",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("トロント ブランチ"):
        br_srv = Server("VM1\nファイル サーバー")
    with Cluster("他ブランチ オフィス"):
        users = Server("ブランチ ユーザー")
    vpng = VirtualNetworkGateways("VPN Gateway")
    with Cluster("Azure"):
        af = AzureFileshares("Azure Files\n共有ストレージ")
    users >> Edge(label="S2S VPN") >> vpng >> af
    br_srv >> Edge(style="dashed", label="移行") >> af
print("vol3_q28 done")


# ── Q31-Q34: ExpressRoute hybrid (OnPrem VMs + Azure VMs) ──────────────────
with Diagram("ExpressRoute ハイブリッド", show=False,
             filename=f"{OUT}/vol3_q31_q34_expressroute",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    with Cluster("オンプレミス DC"):
        on_vm = VirtualMachine("オンプレ VM")
    er  = ExpressrouteCircuits("ExpressRoute")
    with Cluster("Azure VNet"):
        az_vm = VirtualMachine("Azure VM")
        mon   = Monitor("Azure Monitor\nAgent")
    with Cluster("監視"):
        law = LogAnalyticsWorkspaces("Log Analytics\nWorkspace")
    on_vm >> Edge(label="専用線") >> er >> az_vm
    az_vm >> mon >> law
    on_vm >> Edge(style="dashed", label="ログ収集") >> law
print("vol3_q31_q34 done")


# ── Q36: Cosmos DB → Synapse Analytics ─────────────────────────────────────
with Diagram("Cosmos DB → Synapse Analytics", show=False,
             filename=f"{OUT}/vol3_q36_cosmos_synapse",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    cdb = CosmosDb("Cosmos DB\n(オペレーショナル)")
    with Cluster("Synapse Link"):
        link = SynapseAnalytics("Synapse Analytics\n(分析)")
    store = DataLakeStorage("Analytical Store\n(ADLS)")
    cdb >> Edge(label="Synapse Link\n自動同期", style="dashed") >> store
    store >> Edge(label="バッチ クエリ") >> link
print("vol3_q36 done")


# ── Q43: ApexCore – Traffic Manager + Multi-region App ─────────────────────
with Diagram("ApexCore: Traffic Manager マルチリージョン", show=False,
             filename=f"{OUT}/vol3_q43_apexcore_tm",
             direction="TB",
             graph_attr={**GRAPH_ATTR, "splines": "spline"},
             node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    tm = TrafficManagerProfiles("Traffic Manager")
    with Cluster("リージョン A"):
        appA = AppServices("App1\nインスタンス A")
    with Cluster("リージョン B"):
        appB = AppServices("App1\nインスタンス B")
    tm >> appA
    tm >> appB
print("vol3_q43 done")


# ── Q46/Q47: App1 + Managed Identity + Key Vault ───────────────────────────
with Diagram("App Service + Managed Identity + Key Vault", show=False,
             filename=f"{OUT}/vol3_q46_q47_app_keyvault",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    app = AppServices("App1\n(App Service)")
    mi  = ManagedIdentities("Managed Identity\n(システム割り当て)")
    kv  = KeyVaults("Key Vault\nシークレット/証明書")
    app >> Edge(label="ID利用") >> mi >> Edge(label="シークレット取得") >> kv
print("vol3_q46_q47 done")


# ── Q52: App2 + Application Insights monitoring ────────────────────────────
with Diagram("App Service + Application Insights", show=False,
             filename=f"{OUT}/vol3_q52_appinsights",
             direction="LR",
             graph_attr=GRAPH_ATTR, node_attr=NODE_ATTR, edge_attr=EDGE_ATTR):
    app = AppServices("App2\n(App Service)")
    ai  = ApplicationInsights("Application Insights\n(トランザクション追跡)")
    law = LogAnalyticsWorkspaces("Log Analytics\nWorkspace")
    app >> Edge(label="テレメトリ送信") >> ai >> Edge(label="ログ保存") >> law
print("vol3_q52 done")

print("\n✅ Vol3 diagrams generation complete!")
