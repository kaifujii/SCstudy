"""Generate remaining 5 architecture diagrams for az305_v2_complete.html."""
import graphviz

OUT = "/Users/fujiikai/SCstudy/az305/descriptions/img"

GRAPH_ATTRS = {
    "bgcolor": "white",
    "pad": "0.8",
    "splines": "polyline",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "fontname": "sans-serif",
    "fontsize": "12",
}

# ── Diagram 1: Service EP 動作フロー ──────────────────────────────────────────
def gen_sep_flow():
    g = graphviz.Digraph(
        "sep_flow",
        filename=f"{OUT}/sep_flow",
        format="png",
        graph_attr={**GRAPH_ATTRS, "rankdir": "LR", "pad": "0.6", "nodesep": "0.7"},
        node_attr={"fontname": "sans-serif", "fontsize": "11"},
        edge_attr={"fontname": "sans-serif", "fontsize": "10"},
    )

    with g.subgraph(name="cluster_vnet") as vnet:
        vnet.attr(label="Azure VNet  10.0.0.0/16", style="filled,rounded",
                  color="#0078D4", fillcolor="#e8f4ff", fontcolor="#0078D4",
                  fontsize="12", fontname="sans-serif bold")

        with vnet.subgraph(name="cluster_gwsubnet") as gw:
            gw.attr(label="GatewaySubnet", style="dashed,rounded",
                    color="#0078D4", fillcolor="#d0e8ff",
                    fontsize="10", fontname="sans-serif")
            gw.node("vpngw", "VPN Gateway\n/ ExpressRoute GW",
                    shape="cylinder", style="filled", fillcolor="#0078D4",
                    fontcolor="white", width="2.0")

        with vnet.subgraph(name="cluster_appsubnet") as app:
            app.attr(label="AppSubnet 10.0.1.0/24\n✓ serviceEndpoints: Microsoft.Storage",
                     style="dashed,rounded", color="#0078D4", fillcolor="#c8dfff",
                     fontsize="10", fontname="sans-serif")
            app.node("vm", "Azure VM\n10.0.1.4",
                     shape="box", style="filled,rounded", fillcolor="#0050a0",
                     fontcolor="white", width="1.6")
            app.node("rt", "有効ルートテーブル（自動追加）\nStorage Prefix → VNetSvcEndpoint\n10.0.0.0/8 → VirtualNetwork\n0.0.0.0/0 → Internet",
                     shape="note", style="filled", fillcolor="#e8ffe8",
                     fontcolor="#006000", width="3.2")

        with vnet.subgraph(name="cluster_nsg") as nsg:
            nsg.attr(label="NSG（サブネット適用推奨）", style="filled,rounded",
                     color="#ff8c00", fillcolor="#fff8e0", fontsize="10")
            nsg.node("nsg_rule", "Outbound Allow:\nServiceTag=Storage",
                     shape="note", style="filled", fillcolor="#fffacc",
                     fontcolor="#a06000", width="2.4")

    g.node("backbone", "Microsoft Global Network\n（Azureバックボーン）\nインターネット経由なし",
           shape="ellipse", style="filled,dashed", fillcolor="#e0fffe",
           color="#00B7C3", fontcolor="#007890", width="2.8")

    with g.subgraph(name="cluster_storage") as stg:
        stg.attr(label="Storage Account", style="filled,rounded",
                 color="#0078D4", fillcolor="#e8f4ff", fontsize="12")
        stg.node("stg_icon", "Azure Storage\nPublic IP: 残存\n（サービスEPはパブリックIP維持）",
                 shape="cylinder", style="filled", fillcolor="#0078D4",
                 fontcolor="white", width="2.4")
        stg.node("fw_rules", "Firewall Rules\nAllow: VNet ServiceTag\nDeny: その他",
                 shape="note", style="filled", fillcolor="#e0ffe0",
                 fontcolor="#004000", width="2.2")

    g.edge("vm", "rt", label="ルート参照", style="dashed", color="#008000")
    g.edge("vm", "backbone", label="Microsoftバックボーン経由\n（StorageへのSEルート）", color="#0078D4")
    g.edge("backbone", "stg_icon", color="#0078D4")
    g.edge("stg_icon", "fw_rules", label="Firewall\nポリシー適用", style="dashed", color="#008000")
    g.render(cleanup=True)
    print(f"Generated: {OUT}/sep_flow.png")


# ── Diagram 2: 強制トンネリング BEFORE/AFTER/COMBO ────────────────────────────
def gen_ft_comparison():
    g = graphviz.Digraph(
        "ft_comparison",
        filename=f"{OUT}/ft_comparison",
        format="png",
        graph_attr={**GRAPH_ATTRS, "rankdir": "TB", "pad": "0.5",
                    "nodesep": "0.6", "ranksep": "0.8"},
        node_attr={"fontname": "sans-serif", "fontsize": "11"},
        edge_attr={"fontname": "sans-serif", "fontsize": "10"},
    )

    # Keep 3 columns in LR using rank=same
    with g.subgraph(name="cluster_before") as b:
        b.attr(label="❌ BEFORE — 強制トンネリングなし", style="filled,rounded",
               color="#cc3300", fillcolor="#fff5f2", fontcolor="#cc3300",
               fontsize="13", fontname="sans-serif bold")
        with b.subgraph(name="cluster_b_vnet") as bv:
            bv.attr(label="Azure VNet", style="dashed,rounded",
                    color="#0078D4", fillcolor="#e8f4ff", fontsize="10")
            bv.node("b_gw", "VPN Gateway\n(BGP有効)", shape="cylinder",
                    style="filled", fillcolor="#0078D4", fontcolor="white")
            bv.node("b_vm", "Azure VM", shape="box", style="filled,rounded",
                    fillcolor="#0050a0", fontcolor="white")
            bv.node("b_route", "デフォルトルート\n0.0.0.0/0 → Internet", shape="note",
                    style="filled", fillcolor="#ffe0d8", fontcolor="#cc3300")
        b.node("b_internet", "インターネット\n（直接到達）", shape="ellipse",
               style="filled,dashed", fillcolor="#f0f0f0", fontcolor="#666666")
        b.node("b_fw", "オンプレFW\n⚠ バイパスされる!\nログ取得・検査不可",
               shape="box", style="filled,rounded", fillcolor="#ffe0d8",
               fontcolor="#cc3300", width="2.2")
        b.edge("b_vm", "b_route", style="dashed", color="#cc4400", label="参照")
        b.edge("b_vm", "b_internet", label="直接到達\nFWスキップ!", color="#cc3300", style="bold")

    with g.subgraph(name="cluster_after") as a:
        a.attr(label="✅ AFTER — 強制トンネリング有効 (UDR)", style="filled,rounded",
               color="#008000", fillcolor="#f0fff0", fontcolor="#006000",
               fontsize="13", fontname="sans-serif bold")
        with a.subgraph(name="cluster_a_vnet") as av:
            av.attr(label="Azure VNet", style="dashed,rounded",
                    color="#0078D4", fillcolor="#e8f4ff", fontsize="10")
            av.node("a_gw", "VPN GW\n(オンプレへトンネル)", shape="cylinder",
                    style="filled", fillcolor="#0078D4", fontcolor="white")
            av.node("a_vm", "Azure VM", shape="box", style="filled,rounded",
                    fillcolor="#0050a0", fontcolor="white")
            av.node("a_udr", "UDR（強制T）\n0.0.0.0/0 → VNetGW", shape="note",
                    style="filled", fillcolor="#fffacc", fontcolor="#806000")
        a.node("a_tunnel", "VPN/ER 暗号化トンネル\n→ オンプレFWへ転送",
               shape="ellipse", style="filled,dashed", fillcolor="#e0fffe",
               fontcolor="#006070", width="2.8")
        a.node("a_fw", "On-premises Firewall\n✅ 検査・ログ取得可能\n✅ Proxy/SIEM連携",
               shape="box", style="filled,rounded", fillcolor="#e0ffe0",
               fontcolor="#006000", width="2.4")
        a.edge("a_vm", "a_udr", style="dashed", color="#808000", label="参照")
        a.edge("a_vm", "a_gw", label="① Internet宛\n→ GWへ転送", color="#cc4400")
        a.edge("a_gw", "a_tunnel", label="② 強制T", color="#cc4400")
        a.edge("a_tunnel", "a_fw", label="③ FW経由", color="#008000")

    with g.subgraph(name="cluster_combo") as c:
        c.attr(label="✅ 強制T + Service EP 組み合わせ", style="filled,rounded",
               color="#806000", fillcolor="#fffdf0", fontcolor="#806000",
               fontsize="13", fontname="sans-serif bold")
        with c.subgraph(name="cluster_c_vnet") as cv:
            cv.attr(label="Azure VNet（UDR + Service EP両方）", style="dashed,rounded",
                    color="#0078D4", fillcolor="#e8f4ff", fontsize="10")
            cv.node("c_vm", "Azure VM", shape="box", style="filled,rounded",
                    fillcolor="#0050a0", fontcolor="white")
            cv.node("c_rt", "有効ルートテーブル（優先順位）\n① Storage /18 → VNetServiceEP ★最優先\n② 0.0.0.0/0 → VNetGW（強制T）\n③ 10.0.0.0/8 → VNet内部",
                    shape="note", style="filled", fillcolor="#fffacc",
                    fontcolor="#806000", width="3.8")
        c.node("c_backbone", "MSバックボーン\nStorage宛は最長マッチで\nEP経由（FW迂回）",
               shape="ellipse", style="filled,dashed", fillcolor="#e0fffe",
               fontcolor="#006070", width="2.8")
        c.node("c_fw_onprem", "オンプレFW\nInternet宛のみFW経由で検査",
               shape="box", style="filled,rounded", fillcolor="#e0ffe0",
               fontcolor="#006000", width="2.4")
        c.node("c_stg", "Storage Account\n(EP経由で直接到達)",
               shape="cylinder", style="filled", fillcolor="#0078D4",
               fontcolor="white", width="2.0")
        c.edge("c_vm", "c_rt", style="dashed", color="#808000", label="参照")
        c.edge("c_vm", "c_backbone", label="Storage宛 →\nSE経由（直接）", color="#008000")
        c.edge("c_vm", "c_fw_onprem", label="Internet宛 →\n強制T", color="#cc4400", style="dashed")
        c.edge("c_backbone", "c_stg", color="#008000")

    g.render(cleanup=True)
    print(f"Generated: {OUT}/ft_comparison.png")


# ── Diagram 3: PE DNS解決フロー（詳細）────────────────────────────────────────
def gen_pe_dns_resolution():
    g = graphviz.Digraph(
        "pe_dns_resolution",
        filename=f"{OUT}/pe_dns_resolution",
        format="png",
        graph_attr={**GRAPH_ATTRS, "rankdir": "TB", "pad": "0.5",
                    "nodesep": "0.6", "ranksep": "0.7"},
        node_attr={"fontname": "sans-serif", "fontsize": "11"},
        edge_attr={"fontname": "sans-serif", "fontsize": "9"},
    )

    # LEFT side: without DNS zone
    with g.subgraph(name="cluster_fail") as f:
        f.attr(label="❌ Private DNS Zone なし（接続失敗）", style="filled,rounded",
               color="#cc3300", fillcolor="#fff5f2", fontcolor="#cc3300",
               fontsize="13", fontname="sans-serif bold")
        f.node("f_vm", "Azure VM\n10.0.1.4", shape="box", style="filled,rounded",
               fillcolor="#0050a0", fontcolor="white")
        f.node("f_dns_q", "① DNS クエリ\nmyaccount.blob.core.windows.net は？\n→ Azure DNS (168.63.129.16) へ問い合わせ",
               shape="note", style="filled", fillcolor="#fffacc", fontcolor="#806000", width="3.5")
        f.node("f_pub_dns", "Azure Public DNS\n⚠ パブリックIPを返答\n52.xxx.xxx.xxx (Public IP)",
               shape="ellipse", style="filled", fillcolor="#f0f0f0", fontcolor="#cc3300")
        f.node("f_fail", "❌ VM → Public IP に接続しようとする\nStorage Public Access が無効なら → 接続拒否!",
               shape="box", style="filled,rounded", fillcolor="#ffe0d8",
               fontcolor="#cc3300", width="3.8")
        f.node("f_pe_unused", "PE NIC (10.0.2.5) は存在するが...\nVMはパブリックIPに接続しようとしているので\nPE は使われない!",
               shape="box", style="filled,rounded", fillcolor="#f0e0ff",
               fontcolor="#7019aa", width="3.8")
        f.edge("f_vm", "f_dns_q", style="dashed", color="#ff8c00")
        f.edge("f_dns_q", "f_pub_dns", color="#ff8c00")
        f.edge("f_pub_dns", "f_fail", label="パブリックIP返答", color="#cc3300", style="dashed")
        f.edge("f_fail", "f_pe_unused", style="dashed", color="#999999")

    # RIGHT side: with DNS zone
    with g.subgraph(name="cluster_success") as s:
        s.attr(label="✅ Private DNS Zone あり（接続成功）", style="filled,rounded",
               color="#008000", fillcolor="#f0fff0", fontcolor="#006000",
               fontsize="13", fontname="sans-serif bold")
        s.node("s_vm", "Azure VM\n10.0.1.4", shape="box", style="filled,rounded",
               fillcolor="#0050a0", fontcolor="white")
        s.node("s_dns_q", "① DNS クエリ\nmyaccount.blob.core.windows.net は？\n→ Azure DNS (168.63.129.16) へ問い合わせ",
               shape="note", style="filled", fillcolor="#fffacc", fontcolor="#806000", width="3.5")
        s.node("s_priv_dns", "Private DNS Zone が応答!\nprivatelink.blob.core.windows.net\n→ Aレコード: 10.0.2.5 (プライベートIP) を返答!",
               shape="ellipse", style="filled", fillcolor="#e0d8ff", fontcolor="#5010a0", width="3.5")
        s.node("s_success", "✅ VM → プライベートIP (10.0.2.5) に接続!\nインターネットを経由せず\nVNet内部でPE NICに到達",
               shape="box", style="filled,rounded", fillcolor="#d8ffd8",
               fontcolor="#006000", width="3.8")
        s.node("s_pe", "PE NIC (10.0.2.5)\n→ Private Link → Storage\n完全にプライベートな経路で通信成功!",
               shape="box", style="filled,rounded", fillcolor="#e0d8ff",
               fontcolor="#5010a0", width="3.8")
        s.node("s_stg", "Storage Account\n（Public Access Disabled）",
               shape="cylinder", style="filled", fillcolor="#0078D4",
               fontcolor="white", width="2.4")
        s.edge("s_vm", "s_dns_q", style="dashed", color="#ff8c00")
        s.edge("s_dns_q", "s_priv_dns", color="#ff8c00")
        s.edge("s_priv_dns", "s_success", label="プライベートIP返答", color="#008000", style="dashed")
        s.edge("s_success", "s_pe", color="#5010a0")
        s.edge("s_pe", "s_stg", label="Private Link", color="#0078D4")

    g.render(cleanup=True)
    print(f"Generated: {OUT}/pe_dns_resolution.png")


# ── Diagram 4: ハイブリッド環境DNS構成 ──────────────────────────────────────
def gen_hybrid_dns():
    g = graphviz.Digraph(
        "hybrid_dns",
        filename=f"{OUT}/hybrid_dns",
        format="png",
        graph_attr={**GRAPH_ATTRS, "rankdir": "LR", "pad": "0.6",
                    "nodesep": "0.7", "ranksep": "1.0"},
        node_attr={"fontname": "sans-serif", "fontsize": "11"},
        edge_attr={"fontname": "sans-serif", "fontsize": "9"},
    )

    with g.subgraph(name="cluster_onprem") as op:
        op.attr(label="On-premises", style="filled,rounded",
                color="#666666", fillcolor="#f0f0f0", fontcolor="#444444",
                fontsize="12", fontname="sans-serif bold")
        op.node("op_vm", "On-prem VM\nprivatelink.blob... を解決したい",
                shape="box", style="filled,rounded", fillcolor="#606060",
                fontcolor="white", width="2.4")
        op.node("op_dns", "DNS Server\nConditional Forwarder:\nprivatelink.* → Inbound EP IP",
                shape="box", style="filled,rounded", fillcolor="#808080",
                fontcolor="white", width="2.8")
        op.node("op_er", "ExpressRoute / VPN",
                shape="ellipse", style="filled,dashed", fillcolor="#e0fffe",
                fontcolor="#006070", width="2.0")
        op.edge("op_vm", "op_dns", label="DNS クエリ", color="#ff8c00", style="dashed")
        op.edge("op_dns", "op_er", label="フォワード", color="#ff8c00")

    with g.subgraph(name="cluster_hub") as hub:
        hub.attr(label="Azure Hub VNet", style="filled,rounded",
                 color="#0078D4", fillcolor="#e8f4ff", fontcolor="#0050a0",
                 fontsize="12", fontname="sans-serif bold")

        with hub.subgraph(name="cluster_resolver") as res:
            res.attr(label="DNS Private Resolver", style="filled,rounded",
                     color="#00B7C3", fillcolor="#e0fffe", fontsize="11")
            res.node("inbound_ep", "Inbound Endpoint\nIP: 10.1.0.4\n（オンプレからの受口）",
                     shape="box", style="filled,rounded", fillcolor="#00B7C3",
                     fontcolor="white", width="2.4")
            res.node("outbound_ep", "Outbound Endpoint\nオンプレゾーン → オンプレDNSへ",
                     shape="box", style="filled,rounded", fillcolor="#009faa",
                     fontcolor="white", width="2.4")

        hub.node("priv_dns_zone", "Private DNS Zone\nprivatelink.blob.core.windows.net\nA: myaccount.blob... → 10.0.2.5\n← VNetリンク（Hub VNet）",
                 shape="ellipse", style="filled", fillcolor="#d8c0ff",
                 fontcolor="#4a0090", width="3.2")

    with g.subgraph(name="cluster_spoke") as spoke:
        spoke.attr(label="Spoke VNet (App)", style="filled,rounded",
                   color="#7719AA", fillcolor="#f5e8ff", fontcolor="#5010a0",
                   fontsize="12", fontname="sans-serif bold")
        spoke.node("spoke_vm", "Azure VM\n/ App Service",
                   shape="box", style="filled,rounded", fillcolor="#0050a0",
                   fontcolor="white", width="2.0")
        spoke.node("pe_nic", "Private Endpoint NIC\n10.0.2.5",
                   shape="box", style="filled,rounded", fillcolor="#7719AA",
                   fontcolor="white", width="2.0")
        spoke.node("stg", "Storage Account\nPublic Access: Disabled",
                   shape="cylinder", style="filled", fillcolor="#0078D4",
                   fontcolor="white", width="2.2")
        spoke.node("spoke_dns_link", "Private DNS Zone リンク\n（Spoke VNetにもリンク必須!\n忘れやすいポイント）",
                   shape="note", style="filled", fillcolor="#ffe0d8",
                   fontcolor="#cc3300", width="2.8")
        spoke.edge("spoke_vm", "pe_nic", label="プライベートIP", color="#7719AA")
        spoke.edge("pe_nic", "stg", label="Private Link", color="#0078D4")

    g.edge("op_er", "inbound_ep", label="DNS フォワード\n(privatelink.*)", color="#ff8c00", style="dashed")
    g.edge("inbound_ep", "priv_dns_zone", label="クエリ解決", color="#00B7C3")
    g.edge("priv_dns_zone", "spoke_dns_link", label="ゾーンリンク", color="#7719AA", style="dashed")
    g.edge("priv_dns_zone", "inbound_ep", label="← Aレコード返答\n10.0.2.5", color="#008000", style="dashed")

    g.render(cleanup=True)
    print(f"Generated: {OUT}/hybrid_dns.png")


# ── Diagram 5: 判断ツリー（選択フローチャート）────────────────────────────────
def gen_decision_tree():
    g = graphviz.Digraph(
        "decision_tree",
        filename=f"{OUT}/decision_tree",
        format="png",
        graph_attr={
            "bgcolor": "white",
            "pad": "0.6",
            "splines": "polyline",
            "nodesep": "0.8",
            "ranksep": "0.9",
            "fontname": "sans-serif",
            "rankdir": "TB",
        },
        node_attr={"fontname": "sans-serif", "fontsize": "11"},
        edge_attr={"fontname": "sans-serif", "fontsize": "11"},
    )

    # Start
    g.node("start", "Azureネットワークセキュリティの要件",
           shape="ellipse", style="filled", fillcolor="#0078D4",
           fontcolor="white", width="3.5")

    # Q1
    g.node("q1", "インターネット宛の通信を\nFWで検査・記録したい？",
           shape="diamond", style="filled", fillcolor="#d8eeff",
           fontcolor="#004080", width="3.0", height="1.2")

    # Result: Forced Tunneling
    g.node("r_ft", "強制トンネリング\n（Forced Tunneling）\n+ Service EP との組み合わせも可",
           shape="box", style="filled,rounded", fillcolor="#d83b01",
           fontcolor="white", width="2.8")

    # Q2
    g.node("q2", "オンプレ / ピアVNetから\nもアクセスが必要？",
           shape="diamond", style="filled", fillcolor="#e8d8ff",
           fontcolor="#400080", width="3.0", height="1.2")

    # Result: Private EP (for cross-network)
    g.node("r_pe1", "プライベートエンドポイント\n（Private Endpoint）\nDNS設定必須",
           shape="box", style="filled,rounded", fillcolor="#7719AA",
           fontcolor="white", width="2.6")

    # Q3
    g.node("q3", "パブリックIPを完全\n無効化が必要？",
           shape="diamond", style="filled", fillcolor="#d8eeff",
           fontcolor="#004080", width="3.0", height="1.2")

    # Result: Private EP (public access disabled)
    g.node("r_pe2", "プライベートエンドポイント\n（Private Endpoint）\nPublic Access を無効化",
           shape="box", style="filled,rounded", fillcolor="#7719AA",
           fontcolor="white", width="2.6")

    # Result: Service EP
    g.node("r_sep", "サービスエンドポイント\n（Service Endpoint）\nコスト最小・設定が簡単",
           shape="box", style="filled,rounded", fillcolor="#0078D4",
           fontcolor="white", width="2.6")

    # Edges
    g.edge("start", "q1")
    g.edge("q1", "r_ft", label="  Yes", color="#008000", fontcolor="#008000", style="bold")
    g.edge("q1", "q2", label="  No", color="#cc3300", fontcolor="#cc3300", style="bold")
    g.edge("q2", "r_pe1", label="  Yes", color="#008000", fontcolor="#008000", style="bold")
    g.edge("q2", "q3", label="  No", color="#cc3300", fontcolor="#cc3300", style="bold")
    g.edge("q3", "r_pe2", label="  Yes", color="#008000", fontcolor="#008000", style="bold")
    g.edge("q3", "r_sep", label="  No", color="#cc3300", fontcolor="#cc3300", style="bold")

    g.render(cleanup=True)
    print(f"Generated: {OUT}/decision_tree.png")


if __name__ == "__main__":
    gen_sep_flow()
    gen_ft_comparison()
    gen_pe_dns_resolution()
    gen_hybrid_dns()
    gen_decision_tree()
    print("\nAll diagrams generated!")
