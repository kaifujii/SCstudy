"""SVG architecture diagrams for vol6 questions."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from vol6_helpers import *

# ── Q1: App Proxy SSO flow ────────────────────────────────────────────────────
def diag_q1():
    pid = "q1d"
    W, H = 680, 175
    parts = []
    # On-premises zone
    parts.append(label_box(10, 30, 175, 120, "On-premises", fill="#0f2233", stroke="#38bdf8", color="#38bdf8"))
    parts.append(node(20, 55, 75, 72, "vm", "WebApp1\n(IWA)", stroke="#38bdf8"))
    parts.append(node(105, 55, 72, 72, "entra_proxy", "App Proxy\nConnector", stroke="#38bdf8"))
    # Entra ID
    parts.append(node(285, 55, 90, 72, "entra_apps", "Microsoft\nEntra ID"))
    # Remote user
    parts.append(node(490, 35, 80, 70, "entra_user", "リモート\nユーザー", stroke="#22c55e"))
    # Enterprise app config
    parts.append(node(490, 115, 80, 65, "entra_apps", "Enterprise\nApplication", stroke="#7719AA"))
    # Arrows
    parts.append(arr(177, 91, 283, 91, pid, label="HTTPS\nトンネル", lx=230, ly=84))
    parts.append(arr(377, 91, 488, 70, pid, "g", label="SSO トークン", lx=432, ly=74))
    parts.append(arr(95, 91, 103, 91, pid))
    parts.append(arr(377, 91, 488, 130, pid, label="アプリ登録", lx=432, ly=135, dash=True))
    # Title
    parts.append(f'<text x="340" y="20" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">Microsoft Entra Application Proxy – SSO フロー</text>')
    return wrap(pid, W, H, ''.join(parts))

# ── Q5: SQL MI cross-region failover ─────────────────────────────────────────
def diag_q5():
    pid = "q5d"
    W, H = 680, 180
    parts = []
    # Primary region
    parts.append(label_box(10, 30, 280, 130, "プライマリ リージョン（East US）", fill="#0d2318", stroke="#22c55e", color="#86efac"))
    parts.append(node(30, 65, 90, 72, "sql_mi", "SQL\nManaged\nInstance"))
    parts.append(node(175, 65, 90, 72, "recovery", "Recovery\nServices\nVault"))
    # Auto-failover group
    parts.append(f'<rect x="310" y="78" width="60" height="24" rx="4" fill="#1e3a5f" stroke="#4a9fd4" stroke-width="1"/>')
    parts.append(f'<text x="340" y="94" text-anchor="middle" fill="#93c5fd" font-size="8" font-family="sans-serif">Auto-failover\nGroup</text>')
    # Secondary region
    parts.append(label_box(390, 30, 280, 130, "セカンダリ リージョン（West US）", fill="#1a1a0e", stroke="#f59e0b", color="#fcd34d"))
    parts.append(node(400, 65, 90, 72, "sql_mi", "SQL MI\n（読み取り専用\nレプリカ）", stroke="#f59e0b"))
    parts.append(node(545, 65, 90, 72, "recovery", "自動フェール\nオーバー先"))
    # Arrows
    parts.append(arr(120, 101, 173, 101, pid, label="自動バックアップ", lx=147, ly=95))
    parts.append(arr(267, 101, 308, 101, pid, label="", lx=288, ly=95))
    parts.append(arr(372, 101, 398, 101, pid, "g", label="自動レプリケーション", lx=385, ly=90))
    parts.append(arr(492, 101, 543, 101, pid, "g"))
    # Title
    parts.append(f'<text x="340" y="20" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">SQL Managed Instance + 自動フェールオーバー グループ</text>')
    return wrap(pid, W, H, ''.join(parts))

# ── Q7: Virtual WAN Basic → Standard + ExpressRoute ──────────────────────────
def diag_q7():
    pid = "q7d"
    W, H = 680, 195
    parts = []
    # Basic WAN (NG)
    parts.append(label_box(10, 30, 285, 145, "Basic Virtual WAN（非対応）", fill="#2d1010", stroke="#ef4444", color="#fca5a5"))
    parts.append(node(25, 60, 80, 70, "vwan", "Virtual\nWAN Basic", stroke="#ef4444", fill="#3d1515"))
    parts.append(node(125, 60, 80, 70, "vwan_hub", "EastHubA", stroke="#ef4444", fill="#3d1515"))
    parts.append(node(215, 60, 75, 70, "expressroute", "ExpressRoute", stroke="#ef4444", fill="#3d1515"))
    parts.append(f'<text x="152" y="152" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-family="sans-serif">ExpressRoute 接続不可 ✗</text>')
    parts.append(arr(107, 95, 123, 95, pid, "r"))
    parts.append(arr(207, 95, 213, 95, pid, "r", dash=True))

    # Arrow upgrade
    parts.append(f'<text x="307" y="110" text-anchor="middle" fill="#fbbf24" font-size="20" font-family="sans-serif">→</text>')
    parts.append(f'<text x="307" y="125" text-anchor="middle" fill="#fbbf24" font-size="8" font-family="sans-serif">アップグレード</text>')

    # Standard WAN (OK)
    parts.append(label_box(325, 30, 345, 145, "Standard Virtual WAN（対応）", fill="#0d2318", stroke="#22c55e", color="#86efac"))
    parts.append(node(335, 60, 80, 70, "vwan", "Virtual\nWAN Standard", stroke="#22c55e", fill="#0d2318"))
    parts.append(node(430, 60, 80, 70, "vwan_hub", "EastHubA\n(ER Gateway)", stroke="#22c55e"))
    parts.append(node(535, 60, 80, 70, "expressroute", "ExpressRoute\n回線", stroke="#22c55e"))
    parts.append(f'<text x="497" y="152" text-anchor="middle" fill="#86efac" font-size="8.5" font-family="sans-serif">ExpressRoute 接続可能 ✓</text>')
    parts.append(arr(417, 95, 428, 95, pid, "g"))
    parts.append(arr(512, 95, 533, 95, pid, "g"))

    parts.append(f'<text x="340" y="20" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">Virtual WAN：Basic vs Standard（ExpressRoute 対応）</text>')
    return wrap(pid, W, H, ''.join(parts))

# ── Q8: Functions Premium + VNet + SQL VM ─────────────────────────────────────
def diag_q8():
    pid = "q8d"
    W, H = 680, 180
    parts = []
    parts.append(f'<text x="340" y="18" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">Azure Functions Premium – VNet 統合によるプライベート接続</text>')
    # Event Grid
    parts.append(node(15, 50, 80, 70, "event_grid", "Azure\nEvent Grid"))
    # Functions Premium
    parts.append(label_box(120, 35, 155, 120, "Azure VNet", fill="#0f2233", stroke="#38bdf8", color="#38bdf8"))
    parts.append(node(130, 60, 120, 72, "functions", "Functions\n（Premium プラン）\nVNet 統合", stroke="#2563eb"))
    # SQL VM
    parts.append(node(310, 50, 85, 72, "vm", "SQL Server\non Azure VM\n（プライベート IP）", stroke="#7719AA"))
    # Internet user (for Consumption plan - NG)
    parts.append(label_box(430, 30, 235, 135, "従量課金プラン（非対応）", fill="#2d1010", stroke="#ef4444", color="#fca5a5"))
    parts.append(node(445, 55, 95, 72, "functions", "Functions\n（従量課金）\nVNet 非対応", stroke="#ef4444", fill="#3d1515"))
    parts.append(node(555, 55, 95, 72, "vm", "SQL Server\n（到達不可）", stroke="#ef4444", fill="#3d1515"))
    # Arrows
    parts.append(arr(97, 85, 128, 85, pid, label="イベント", lx=113, ly=79))
    parts.append(arr(252, 85, 308, 85, pid, "g", label="プライベート IP\nアクセス", lx=280, ly=79))
    parts.append(arr(542, 85, 553, 85, pid, "r", label="接続不可", lx=548, ly=79))
    return wrap(pid, W, H, ''.join(parts))

# ── Q16: Network Watcher IP Flow Verify ──────────────────────────────────────
def diag_q16():
    pid = "q16d"
    W, H = 680, 185
    parts = []
    parts.append(f'<text x="340" y="18" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">Azure Network Watcher – IP フロー確認の仕組み</text>')
    # Source
    parts.append(node(15, 50, 75, 70, "vm", "VM A\n（送信元）"))
    # NSG
    parts.append(label_box(115, 30, 150, 125, "NSG（ネットワーク\nセキュリティ グループ）", fill="#0f2233", stroke="#f59e0b", color="#fcd34d"))
    parts.append(f'<rect x="125" y="65" width="130" height="22" rx="4" fill="#1e3a5f" stroke="#2563eb" stroke-width="1"/>')
    parts.append(f'<text x="190" y="80" text-anchor="middle" fill="#93c5fd" font-size="8" font-family="sans-serif">許可ルール: 443 Inbound</text>')
    parts.append(f'<rect x="125" y="95" width="130" height="22" rx="4" fill="#3d1515" stroke="#ef4444" stroke-width="1"/>')
    parts.append(f'<text x="190" y="110" text-anchor="middle" fill="#fca5a5" font-size="8" font-family="sans-serif">拒否ルール: 22 Inbound</text>')
    # VM target
    parts.append(node(295, 50, 75, 70, "vm", "VM B\n（宛先）"))
    # Network Watcher
    parts.append(label_box(405, 30, 260, 145, "Azure Network Watcher", fill="#112240", stroke="#22c55e", color="#86efac"))
    parts.append(node(420, 60, 95, 72, "nwatcher", "IP フロー確認\n（IP Flow\nVerify）", stroke="#22c55e"))
    parts.append(f'<rect x="527" y="60" width="125" height="55" rx="5" fill="#0d2318" stroke="#22c55e" stroke-width="1"/>')
    parts.append(f'<text x="589" y="79" text-anchor="middle" fill="#86efac" font-size="8.5" font-family="sans-serif" font-weight="700">診断結果</text>')
    parts.append(f'<text x="589" y="94" text-anchor="middle" fill="#86efac" font-size="8" font-family="sans-serif">✓ Allow（443）</text>')
    parts.append(f'<text x="589" y="108" text-anchor="middle" fill="#fca5a5" font-size="8" font-family="sans-serif">✗ Deny（22）</text>')
    # Arrows
    parts.append(arr(92, 85, 113, 85, pid, label="パケット", lx=102, ly=79))
    parts.append(arr(267, 85, 293, 85, pid))
    parts.append(arr(335, 85, 403, 90, pid, "g", label="NSG ルール評価", lx=369, ly=84))
    parts.append(arr(517, 90, 525, 90, pid, "g"))
    return wrap(pid, W, H, ''.join(parts))

# ── Q17: Traffic Manager multi-region ─────────────────────────────────────────
def diag_q17():
    pid = "q17d"
    W, H = 680, 195
    parts = []
    parts.append(f'<text x="340" y="18" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">Azure Traffic Manager – マルチリージョン VM フェールオーバー</text>')
    # Users
    parts.append(node(15, 70, 75, 70, "entra_user", "ユーザー\n（世界中）"))
    # Traffic Manager
    parts.append(node(150, 50, 95, 85, "traffic_mgr", "Azure Traffic\nManager\n（DNS ベース）"))
    # East US
    parts.append(label_box(300, 25, 160, 145, "East US\n（プライマリ）", fill="#0d2318", stroke="#22c55e", color="#86efac"))
    parts.append(node(315, 60, 80, 70, "vm", "VM × 2\n（East US）\n.NET Full FW", stroke="#22c55e"))
    # West US
    parts.append(label_box(480, 25, 185, 145, "West US\n（フェールオーバー先）", fill="#112240", stroke="#4a9fd4", color="#93c5fd"))
    parts.append(node(510, 60, 80, 70, "vm", "VM × 2\n（West US）\n.NET Full FW"))
    # App GW (NG comparison)
    parts.append(f'<rect x="300" y="175" width="150" height="15" rx="3" fill="#2d1010" stroke="#ef4444" stroke-width="1"/>')
    parts.append(f'<text x="375" y="186" text-anchor="middle" fill="#fca5a5" font-size="8" font-family="sans-serif">✗ Application Gateway（リージョン限定）</text>')
    # Arrows
    parts.append(arr(92, 105, 148, 90, pid, label="DNS クエリ", lx=120, ly=88))
    parts.append(arr(247, 85, 313, 80, pid, "g", label="正常時", lx=280, ly=74))
    parts.append(arr(247, 100, 508, 100, pid, dash=True, label="障害時フェールオーバー", lx=378, ly=93))
    # OS access note
    parts.append(f'<text x="355" y="150" text-anchor="middle" fill="#86efac" font-size="8" font-family="sans-serif">OS アクセス可 / .NET Full FW</text>')
    parts.append(f'<text x="570" y="150" text-anchor="middle" fill="#93c5fd" font-size="8" font-family="sans-serif">OS アクセス可 / .NET Full FW</text>')
    return wrap(pid, W, H, ''.join(parts))

# ── Q27: OAuth 2.0 token flow ─────────────────────────────────────────────────
def diag_q27():
    pid = "q27d"
    W, H = 680, 185
    parts = []
    parts.append(f'<text x="340" y="18" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">OAuth 2.0 フロー：アクセス トークン生成と認可</text>')
    # User
    parts.append(node(15, 50, 75, 70, "entra_user", "サインイン\nユーザー"))
    # Web App
    parts.append(node(145, 50, 90, 70, "app_svc", "Web アプリ\n（クライアント）"))
    # Entra ID
    parts.append(node(310, 50, 90, 70, "entra_apps", "Microsoft\nEntra ID\n（認可サーバー）", stroke="#7719AA"))
    # Web API
    parts.append(node(480, 50, 90, 70, "app_svc", "Web API\n（リソース\nサーバー）", stroke="#22c55e"))
    # Token
    parts.append(f'<rect x="305" y="138" width="100" height="30" rx="4" fill="#1e3a5f" stroke="#4a9fd4"/>')
    parts.append(f'<text x="355" y="152" text-anchor="middle" fill="#93c5fd" font-size="8" font-family="sans-serif" font-weight="700">アクセス トークン</text>')
    parts.append(f'<text x="355" y="163" text-anchor="middle" fill="#64748b" font-size="7.5" font-family="sans-serif">（JWT / Bearer）</text>')
    # Step labels
    for step, x, txt in [(1, 113, "① 認証"), (2, 238, "② トークン\n要求"), (3, 405, "③ Bearer\nトークン送信")]:
        parts.append(f'<text x="{x}" y="132" text-anchor="middle" fill="#94a3b8" font-size="8" font-family="sans-serif">{txt}</text>')
    # Arrows
    parts.append(arr(92, 85, 143, 85, pid, label="", lx=118, ly=79))
    parts.append(arr(237, 85, 308, 85, pid, label="", lx=273, ly=79))
    parts.append(arr(402, 85, 478, 85, pid, "g", label="", lx=440, ly=79))
    # Token return
    parts.append(arr(355, 136, 355, 122, pid, dash=True))
    parts.append(arr(355, 120, 190, 120, pid, dash=True))
    # Authorization decision arrow
    parts.append(arr(572, 85, 572, 145, pid, dash=True, label="④ 認可判定", lx=610, ly=120))
    # Labels
    parts.append(f'<text x="355" y="98" text-anchor="middle" fill="#fcd34d" font-size="8" font-family="sans-serif">トークン生成 ★</text>')
    parts.append(f'<text x="525" y="148" text-anchor="middle" fill="#86efac" font-size="8" font-family="sans-serif">認可判定 ★</text>')
    return wrap(pid, W, H, ''.join(parts))

# ── Q37: IMDS token acquisition ───────────────────────────────────────────────
def diag_q37():
    pid = "q37d"
    W, H = 680, 185
    parts = []
    parts.append(f'<text x="340" y="18" text-anchor="middle" fill="#c8d8f0" font-size="10" font-family="sans-serif" font-weight="700">マネージド ID + IMDS によるシークレット取得フロー</text>')
    # VM1
    parts.append(label_box(10, 30, 175, 145, "Azure VM (VM1)", fill="#0f2233", stroke="#38bdf8", color="#38bdf8"))
    parts.append(node(25, 58, 80, 70, "vm", "VM1\n（System-assigned\nManaged ID）"))
    parts.append(node(115, 58, 62, 70, "entra_mi", "IMDS\n(169.254\n.169.254)"))
    # Entra ID
    parts.append(node(250, 58, 90, 70, "entra_apps", "Microsoft\nEntra ID\n（トークン発行）", stroke="#7719AA"))
    # App1
    parts.append(node(405, 35, 75, 70, "app_svc", "App1\n(ASP.NET)"))
    # Key Vault
    parts.append(node(540, 35, 90, 70, "kv", "Azure\nKey Vault\n(KV1)"))
    # Arrows
    parts.append(arr(107, 90, 113, 90, pid, label="① IMDS\nリクエスト", lx=110, ly=82))
    parts.append(arr(179, 90, 248, 90, pid, label="② MI 認証", lx=214, ly=84))
    parts.append(arr(342, 90, 403, 68, pid, "g", label="③ トークン\n返却", lx=373, ly=66))
    parts.append(arr(482, 60, 538, 60, pid, "g", label="④ シークレット取得\n（Bearer token）", lx=510, ly=52))
    # Note
    parts.append(f'<text x="340" y="160" text-anchor="middle" fill="#64748b" font-size="8" font-family="sans-serif">カスタム認証コード不要 – マネージド ID が自動的に認証を処理</text>')
    return wrap(pid, W, H, ''.join(parts))
