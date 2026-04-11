"""Generate architecture diagrams for az305_v2_complete.html."""
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import (
    Firewall, VirtualNetworkGateways, PrivateEndpoint,
    DNSPrivateZones, DNSZones
)
from diagrams.azure.compute import VirtualMachine, ContainerRegistries
from diagrams.azure.security import KeyVaults
from diagrams.azure.database import SQLDatabases
from diagrams.azure.storage import StorageAccounts, BlobStorage

OUT = "/Users/fujiikai/SCstudy/az305/picture"

GRAPH = {
    "bgcolor": "white",
    "pad": "1.0",
    "splines": "ortho",
    "nodesep": "1.2",
    "ranksep": "1.6",
    "fontsize": "13",
    "fontname": "sans-serif",
}

# ── Diagram 1: Service EP vs Private EP 比較 ──────────────────────────────────
with Diagram(
    "サービスEP vs プライベートEP",
    show=False,
    filename=f"{OUT}/ep_comparison",
    direction="LR",
    graph_attr={**GRAPH, "nodesep": "1.4"},
):
    with Cluster("Service Endpoint 構成\n(パブリックIPは残存)"):
        vm_sep = VirtualMachine("VM\n(SubnetでSE有効)")
        stg_sep = StorageAccounts("Storage Account\n(パブリックIP残存)")
        vm_sep >> Edge(label="Microsoft Backbone\n経由でアクセス", color="#0078D4") >> stg_sep

    with Cluster("Private Endpoint 構成\n(パブリックIP無効化可)"):
        vm_pe = VirtualMachine("VM")
        pe_nic = PrivateEndpoint("Private Endpoint\n10.0.2.4")
        dns_z = DNSPrivateZones("Private DNS Zone\n→ 10.0.2.4")
        stg_pe = StorageAccounts("Storage Account\n(Public IP Disabled)")
        vm_pe >> Edge(label="DNS名解決", color="#FFB300", style="dashed") >> dns_z
        vm_pe >> Edge(label="プライベートIP通信", color="#7719AA") >> pe_nic
        pe_nic >> Edge(label="Private Link", color="#0078D4") >> stg_pe


# ── Diagram 2: Private Endpoint DNS 解決フロー ────────────────────────────────
with Diagram(
    "Private Endpoint — DNS解決フロー",
    show=False,
    filename=f"{OUT}/pe_dns_flow",
    direction="LR",
    graph_attr={**GRAPH, "ranksep": "1.8"},
):
    with Cluster("Azure VNet (10.0.0.0/16)"):
        with Cluster("AppSubnet"):
            vm = VirtualMachine("VM")

        with Cluster("PrivateEndpointSubnet"):
            pe = PrivateEndpoint("Private Endpoint\nNIC: 10.0.2.4")

        with Cluster("Private DNS Zone\nprivatelink.blob.core.windows.net"):
            dns = DNSPrivateZones("myaccount.blob...\n→ 10.0.2.4")

    stg = StorageAccounts("Storage Account\n(Public Access Disabled)")

    vm >> Edge(label="① DNS Query", color="#FFB300") >> dns
    dns >> Edge(label="② 10.0.2.4 を返す", color="#FFB300", style="dashed") >> vm
    vm >> Edge(label="③ プライベートIPで通信", color="#7719AA") >> pe
    pe >> Edge(label="④ Private Link経由", color="#0078D4") >> stg


# ── Diagram 3: エンタープライズ Hub-Spoke アーキテクチャ ─────────────────────
with Diagram(
    "エンタープライズ Hub-Spoke\n(金融・規制産業向け)",
    show=False,
    filename=f"{OUT}/enterprise_hub_spoke",
    direction="LR",
    graph_attr={**GRAPH, "nodesep": "1.0", "ranksep": "2.0"},
):
    with Cluster("オンプレミス"):
        onprem_vpn = VirtualNetworkGateways("ExpressRoute\n/ VPN")

    with Cluster("Hub VNet"):
        gw       = VirtualNetworkGateways("VPN / ER\nGateway")
        az_fw    = Firewall("Azure Firewall\n(強制トンネリング)")
        dns_res  = DNSZones("DNS Private\nResolver")
        hub_dns  = DNSPrivateZones("Private DNS Zones\n(KV/ACR/SQL/Storage)")
        hub_pe_kv  = PrivateEndpoint("PE → Key Vault")
        hub_pe_acr = PrivateEndpoint("PE → ACR")

    with Cluster("Spoke VNet 1  (App)"):
        vms       = VirtualMachine("VMs / VMSS")
        spoke1_pe = PrivateEndpoint("PE → SQL / Storage")

    with Cluster("Spoke VNet 2  (Data)"):
        spoke2_pe = PrivateEndpoint("PE → SQL / Storage")

    with Cluster("Azure PaaS Services\n(Public Access Disabled)"):
        kv  = KeyVaults("Key Vault")
        acr = ContainerRegistries("Container\nRegistry")
        sql = SQLDatabases("SQL Database")
        stg = StorageAccounts("Storage Account")

    # On-prem → Hub
    onprem_vpn >> Edge(label="ER / VPN", color="#00B7C3", style="dashed") >> gw

    # Hub 内部
    gw  >> az_fw
    az_fw >> dns_res
    dns_res >> hub_dns

    # Hub PE → PaaS
    hub_pe_kv  >> Edge(color="#7719AA") >> kv
    hub_pe_acr >> Edge(color="#7719AA") >> acr

    # Spoke → Hub Firewall (強制トンネリング)
    vms >> Edge(label="強制トンネリング\n(UDR→FW)", color="#D83B01", style="dashed") >> az_fw

    # Spoke PE → PaaS
    spoke1_pe >> Edge(color="#7719AA") >> sql
    spoke1_pe >> Edge(color="#7719AA") >> stg
    spoke2_pe >> Edge(color="#7719AA") >> sql
    spoke2_pe >> Edge(color="#7719AA") >> stg


print("Generated:")
for name in ["ep_comparison", "pe_dns_flow", "enterprise_hub_spoke"]:
    print(f"  {OUT}/{name}.png")
