"""Enhanced exp_html for each vol6 question."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from vol6_helpers import *
from vol6_diagrams import *

def exp_q1():
    diag = diag_q1()
    correct = blk_correct("Microsoft Entra エンタープライズ アプリケーション + アプリケーション プロキシ",
        f"<p>{svc('entra_apps','エンタープライズ アプリケーション')} は、オンプレミス・クラウド アプリの SSO・ユーザー割り当て・条件付きアクセスを設定するフレームワークです。WebApp1 をエンタープライズ アプリとして登録することで Entra ID との統合が可能になります。</p>"
        f"<p>{svc('entra_proxy','アプリケーション プロキシ')} は VPN なしでオンプレミス アプリへの安全なリモート アクセスを提供します。オンプレミスに軽量コネクタをインストールし、Entra ID 経由でリモート ユーザーが SSO アクセスできます。</p>"
        + tbl(["機能","役割","SSO提供","必須か"],
              [[svc('entra_apps','Enterprise Apps'),"アプリ登録・SSO 設定","✓","✓"],
               [svc('entra_proxy','App Proxy'),"リモート アクセス経路","✓（IWA 対応）","✓"],
               [svc('entra_ca','Conditional Access'),"アクセス条件の強化","✗","追加セキュリティ用"],
               [svc('entra_pim','PIM'),"特権ロール管理","✗","✗"]],
              "各機能の役割比較"))
    wrong = blk_wrong("Microsoft Entra PIM",
        f"{svc('entra_pim','PIM')} は Just-In-Time の特権アクセス管理ツールです。オンプレミス アプリの公開や SSO とは無関係です。")
    wrong2 = blk_wrong("条件付きアクセス ポリシー",
        f"{svc('entra_ca','条件付きアクセス')} はアクセス制御を強化しますが、アプリの公開機能や SSO 経路そのものを提供しません。Application Proxy と組み合わせて使うものです。")
    key = blk_key("Application Proxy の動作原理",
        "<p>① リモートユーザーがブラウザから Entra ID 経由でアクセス要求<br>"
        "② Entra ID がコネクタ（オンプレミス）にリクエストを転送<br>"
        "③ コネクタが WebApp1 に転送（IWA で認証）<br>"
        "VPN・ファイアウォール開放不要 ─ アウトバウンド接続のみ使用</p>")
    return exp_wrap(diag, correct, wrong, wrong2, key)

def exp_q2():
    correct = blk_correct("Blueprint は展開されたリソースとの接続を維持する",
        f"<p>Azure Blueprints は展開後もリソースとの接続を保持し、継続的なコンプライアンス追跡・更新が可能です。これが ARM テンプレートとの最大の違いです。</p>"
        + tbl(["比較項目","Azure Blueprints","ARM テンプレート"],
              [["デプロイ後の接続","✓ 接続維持・追跡","✗ 切断される"],
               ["ポリシー定義を含める","✓","✓"],
               ["ロール割り当てを含める","✓","✓（限定的）"],
               ["スコープ","管理グループ・サブスクリプション","リソース グループ"],
               ["バージョン管理","✓","✗（手動管理）"]],
              "Blueprints vs ARM テンプレート"))
    wrong = blk_wrong("ARM テンプレートは展開後もリソースとの関連性を維持する",
        "ARM テンプレートはデプロイ完了後にリソースとの接続を持ちません。テンプレートを変更してもリソースは自動更新されません。")
    wrong2 = blk_wrong("Blueprints のみが Azure Policy をサポート / Policy は ARM のみ",
        "どちらも Azure Policy を含めることができます。排他的な関係はありません。")
    key = blk_key("覚え方",
        "<p><strong>Blueprint = 設計図（完成後も管理）</strong>、ARM = 施工図（建てたら終わり）<br>"
        "試験では「継続的な接続・追跡」がキーワードです。</p>")
    return exp_wrap(correct, wrong, wrong2, key)

def exp_q3():
    correct = blk_correct("正しい（True）",
        f"<p>Azure 診断設定は最大 <strong>5 つ</strong>の異なる送信先を設定できます。</p>"
        + tbl(["送信先の種類","対応","備考"],
              [["Storage Account","✓","アーカイブ・長期保存"],
               ["Log Analytics Workspace","✓","クエリ・分析"],
               ["Event Hub","✓","リアルタイム ストリーミング"],
               ["Partner Solution","✓","サードパーティ SIEM 等"]],
              "診断設定の有効な送信先")
        + "<p>DiagConfig1（StoreAcctA + LogWS-A）はすでに 2 送信先を使用しており、EventHub-A への追加送信先を含む新しい診断設定を作成できます。</p>")
    wrong = blk_wrong("正しくない（False）",
        "Event Hub は診断設定の有効な送信先です。既存設定とは独立して別の診断設定を追加できます。上限（5件）にも達していません。")
    return exp_wrap(correct, wrong)

def exp_q4():
    correct = blk_correct("Always On 可用性グループ（Premium マネージド ディスク）＋ DNN",
        f"<p>{svc('sql_server','Always On AG')} に <strong>DNN（分散ネットワーク名）</strong>を組み合わせることで Azure Load Balancer が不要になり、フェールオーバー時間を最短化できます。</p>"
        + tbl(["方式","Load Balancer","フェールオーバー速度","コスト"],
              [["AG + DNN ✓","不要","最速（ヘルス プローブ待ち不要）","低"],
               ["AG + VNN","必要","中（LB ヘルス プローブ分遅延）","中"],
               ["FCI + VNN + Premium FS","必要","中","高（Premium FS）"],
               ["FCI + VNN + Standard FS","必要","中","低〜中"]],
              "SQL Server HA 方式の比較"))
    wrong = blk_wrong("FCI + VNN（Premium/Standard ファイル共有）",
        "FCI は Failover Cluster Instance で高可用性を提供しますが、VNN は Azure Load Balancer が必要でヘルス プローブによる追加遅延が生じます。")
    wrong2 = blk_wrong("AG + VNN",
        "Premium マネージド ディスクで高性能ですが、VNN は Load Balancer を必要とし DNN より遅延が大きくなります。")
    key = blk_key("DNN の仕組み",
        "<p>DNN はクラスターの DNS 名をすべてのノード IP にバインドします。<br>"
        "クライアントが <code>MultiSubnetFailover=True</code> を指定すると全 IP を並行試行できるため、LB のヘルス プローブ待ちが発生しません。</p>")
    return exp_wrap(correct, wrong, wrong2, key)

def exp_q5():
    diag = diag_q5()
    correct = blk_correct("Azure SQL Managed Instance ＋ 自動フェールオーバー グループ",
        f"<p>{svc('sql_mi','SQL Managed Instance')} はユーザーが開始するバックアップをサポートします（Azure SQL Database は不可）。</p>"
        f"<p>{svc('recovery','自動フェールオーバー グループ')} はクロスリージョンの自動レプリケーション + 自動フェールオーバーをフル マネージドで提供します。</p>"
        + tbl(["サービス","ユーザー バックアップ","クロスリージョン自動レプリカ","管理オーバーヘッド"],
              [[svc('sql_mi','SQL Managed Instance'),"✓","✓（FG 経由）","低"],
               [svc('sql_db','Azure SQL Database'),"✗（自動管理のみ）","✓（Active GR）","低"],
               [svc('sql_server','SQL Server on VM'),"✓","✗（手動構成）","高"]],
              "SQL サービス比較"))
    wrong = blk_wrong("SQL Server on VM",
        "ユーザー バックアップは可能ですが、リージョン間 HA の構成に多大な管理作業が必要です。")
    wrong2 = blk_wrong("Azure SQL Database / Active geo-replication / Zone-redundant",
        f"<p>{svc('sql_db','Azure SQL Database')} はユーザー開始バックアップ不可。<br>"
        f"Active geo-replication は手動フェールオーバーが必要。<br>"
        f"Zone-redundant は単一リージョン内の HA のみです。</p>")
    return exp_wrap(diag, correct, wrong, wrong2)

def exp_q6():
    correct = blk_correct("WorkloadA：Block Blob Storage（Premium、ZRS） ＋ WorkloadB：GPv2（Standard、Cool、RA-GRS）",
        tbl(["","WorkloadA","WorkloadB"],
            [["要件","最高スループット・最低レイテンシ","最低 GB 単価"],
             ["アカウント種別","Block Blob Storage","General Purpose v2"],
             ["パフォーマンス層","Premium（SSD）","Standard（HDD）"],
             ["アクセス層","N/A","Cool"],
             ["冗長性","ZRS（ゾーン冗長）","RA-GRS（読み取りアクセス付き geo 冗長）"],
             ["データセンター障害耐性","✓（ZRS = 3 ゾーン）","✓（RA-GRS = 別リージョン）"]],
            "WorkloadA vs WorkloadB ストレージ設計"))
    wrong = blk_wrong("GPv1 + LRS（WorkloadA向け）",
        "GPv1 はレガシー。LRS は単一データセンター内のみでデータセンター障害に耐性がありません。")
    key = blk_key("ストレージ アカウント種別の選び方",
        tbl(["種別","用途","Premium対応","ライフサイクル管理"],
            [["Block Blob Storage","大容量 BLOB 高速 I/O","✓","✗"],
             ["General Purpose v2","汎用（推奨）","✗","✓"],
             ["Blob Storage","BLOB 専用（レガシー）","✗","✓"],
             ["File Storage","Premium ファイル共有","✓","✗"]],
            "ストレージ アカウント種別早見表"))
    return exp_wrap(correct, wrong, key)

def exp_q7():
    diag = diag_q7()
    correct = blk_correct("Standard レベルへのアップグレード",
        f"<p>{svc('vwan','Virtual WAN')} の Basic レベルは Site-to-Site VPN のみをサポートします。<br>"
        f"{svc('expressroute','ExpressRoute')} を接続するには Standard レベルが必要です。</p>"
        + tbl(["機能","Basic","Standard"],
              [["Site-to-Site VPN","✓","✓"],
               ["ExpressRoute","✗","✓"],
               ["P2S VPN","✗","✓"],
               ["リージョン間ハブ接続","✗","✓"],
               ["Azure Firewall","✗","✓"]],
              "Virtual WAN：Basic vs Standard"))
    wrong = blk_wrong("ExpressRoute ゲートウェイのデプロイ",
        "ゲートウェイをデプロイする前に Virtual WAN を Standard にアップグレードする必要があります。Basic では ExpressRoute ゲートウェイを作成できません。")
    wrong2 = blk_wrong("Premium アドオン / 新しいハブの作成",
        "Premium アドオンは 10 超の VNet 接続やグローバル リーチが必要な場合に使用します。ハブ（EastHubA）は既に存在するため新規作成不要です。")
    return exp_wrap(diag, correct, wrong, wrong2)

def exp_q8():
    diag = diag_q8()
    correct = blk_correct("Azure Functions（Premium プラン）",
        f"<p>{svc('functions','Azure Functions Premium')} プランは <strong>VNet 統合</strong>をサポートし、プライベート IP アドレスで Azure VM 上の SQL Server に接続できます。</p>"
        + tbl(["ホスティング プラン","VNet 統合","スケーリング","コスト"],
              [["従量課金（Consumption）","✗","自動","最安（実行時のみ課金）"],
               ["Premium ✓","✓","自動","中"],
               ["Dedicated（App Service）","✓","手動/自動","高（常時課金）"],
               ["Logic Apps ISE","✓","自動","高額"]],
              "Azure Functions ホスティング プラン比較"))
    wrong = blk_wrong("従量課金プラン",
        "VNet 統合をサポートしないため、プライベート IP へのアクセスができません。コストは最安ですが要件を満たしません。")
    wrong2 = blk_wrong("Logic Apps ISE / Dedicated + Basic",
        "ISE は大幅にコストが高くなります。Dedicated + Basic は VNet 統合可能ですが、Basic プランはオートスケールや最適なパフォーマンスを提供しません。")
    return exp_wrap(diag, correct, wrong, wrong2)

def exp_q9():
    correct = blk_correct("Premium ブロック BLOB",
        f"<p>{svc('blob','Premium Block Blob')} は SSD バックアップで最高スループット・最低レイテンシを提供します。毎秒 800 リクエスト以上の要件と大容量メディア配信に最適です。</p>"
        + tbl(["ストレージ種別","スループット","レイテンシ","適した用途"],
              [["Premium Block Blob ✓","最高","最低（ms 以下）","メディア配信・高 IOPS"],
               ["Standard GPv2","中","中","汎用"],
               ["Premium File Share","高","低","SMB ファイル共有"],
               ["Premium Page Blob","高","低","VM ディスク（VHD）"]],
              "ストレージ パフォーマンス比較"))
    wrong = blk_wrong("Standard GPv2 / Premium Page Blob / Premium File Share",
        "Standard は高 IOPS 保証なし。Page Blob は VM ディスク向けランダム I/O 用。File Share は SMB ファイル共有用でメディア ストリーミングには不適。")
    return exp_wrap(correct, wrong)

def exp_q10():
    correct = blk_correct("Azure Cosmos DB",
        f"<p>{svc('cosmos','Azure Cosmos DB')} は書き込みレイテンシと スループット両方の SLA を提供する唯一の Azure データベース サービスです。</p>"
        + tbl(["サービス","書き込みレイテンシ SLA","スループット SLA","可用性 SLA"],
              [[svc('cosmos','Cosmos DB'),"✓（<10ms）","✓（プロビジョニング済み）","99.999%（マルチリージョン）"],
               [svc('sql_db','Azure SQL'),"✗","✗","99.99%"],
               ["Azure Blob Storage","✗","✗","99.9%"],
               ["ADLS Gen2","✗","✗","99.9%"]],
              "ミッション クリティカルな SLA 比較"))
    wrong = blk_wrong("Azure SQL / Blob Storage / ADLS Gen2",
        "これらのサービスは可用性の SLA は提供しますが、書き込みレイテンシやスループットの明確な SLA は保証しません。")
    key = blk_key("Cosmos DB の SLA ポイント",
        "<p>・プロビジョニング済みスループット（RU/s）で一貫した性能を保証<br>"
        "・マルチリージョン書き込みで 99.999% 可用性<br>"
        "・単一桁ミリ秒（<10ms）の書き込みレイテンシを SLA で保証</p>")
    return exp_wrap(correct, wrong, key)

def exp_q11():
    correct = blk_correct("Premium ブロック BLOB ＋ ZRS",
        tbl(["要件","選択した設計","理由"],
            [["最低読み取りレイテンシ","Premium Block Blob","SSD バックアップで最速"],
             ["最大データ回復性","ZRS（ゾーン冗長）","3 可用性ゾーンへ同期レプリカ"],
             ["1 年間の変更不可","Azure イミュータブル BLOB ポリシー","WORM ポリシー設定可"]],
            "Premium Block Blob + ZRS が要件を満たす理由"))
    wrong = blk_wrong("Standard 系（GPv1/GPv2）",
        "Standard パフォーマンスは Premium より読み取りレイテンシが高く、最低レイテンシの要件を満たしません。")
    wrong2 = blk_wrong("LRS（ローカル冗長）",
        "LRS は単一データセンター内のみのレプリケーションで、「回復性を最大化」の要件に反します。データセンター障害で全コピーが失われる可能性があります。")
    key = blk_key("Azure Storage 冗長性の比較",
        tbl(["冗長性","コピー数","保護対象","レイテンシへの影響"],
            [["LRS","3（同一DC）","ラック障害","最小"],
             ["ZRS ✓","3（異なるAZ）","データセンター障害","最小（同期）"],
             ["GRS","6（異なるリージョン）","リージョン障害","あり（非同期）"],
             ["RA-GRS","6（異なるリージョン）","リージョン障害","あり（非同期）"]],
            "冗長性オプション比較"))
    return exp_wrap(correct, wrong, wrong2, key)

def exp_q12():
    correct = blk_correct("Azure Data Factory",
        f"<p>{svc('adf','Azure Data Factory')} は ETL/ELT のフル マネージド サービスで、Blob Storage から Azure SQL Database への継続的な自動データ転送を実現します。</p>"
        + tbl(["サービス","継続転送","スケジュール","変換機能","用途"],
              [[svc('adf','ADF'),"✓","✓","✓（Data Flow）","ETL・継続的データ統合"],
               ["DMA","✗","✗","✗","1回限りのDB評価・移行"],
               ["Azure Data Box","✗","✗","✗","大量オフライン転送"],
               ["Database Migration Service","✗","✗","✗","DB一回限り移行"]],
              "データ転送サービス比較"))
    wrong = blk_wrong("DMA / Data Box / Database Migration Service",
        "これらはすべて1回限りの移行・転送向けです。継続的なデータ取り込みや定期的な ETL 処理には対応していません。")
    return exp_wrap(correct, wrong)

def exp_q13():
    correct = blk_correct("動的データ マスキング（DDM）",
        f"<p>{svc('sql_db','動的データ マスキング')} はクエリ結果レベルで PII をマスクし、非特権ユーザーが実データを閲覧できないようにします。</p>"
        + tbl(["機能","保護対象","管理者からの保護","部分開示","アプリ変更不要"],
              [["DDM ✓","クエリ結果","✗（特権ユーザーは見える）","✓（下4桁のみ等）","✓"],
               ["Always Encrypted","保存データ+転送","✓（鍵なし不可）","✗","✗（アプリ改修必要）"],
               ["TDE","保存データ","✗","✗","✓"],
               ["RBAC","アクセス権","△","✗","✓"]],
              "データ保護機能比較"))
    wrong = blk_wrong("TDE（透過的データ暗号化）",
        "TDE はデータベース全体を保存時に暗号化しますが、クエリ時に正規ユーザーが機密データを見ることを防ぎません。")
    wrong2 = blk_wrong("RBAC",
        "テーブル・データベース レベルのアクセス制御は提供しますが、特定フィールドの動的マスクには対応しません。")
    key = blk_key("DDM vs Always Encrypted",
        "<p><strong>DDM</strong>：アプリ変更不要・管理者には見える → 内部不正対策は弱い<br>"
        "<strong>Always Encrypted</strong>：アプリ側で鍵管理 → DBA・クラウド管理者にも見せない → SSN などに最適</p>")
    return exp_wrap(correct, wrong, wrong2, key)

def exp_q14():
    correct = blk_correct("General Purpose v2 ストレージ アカウントの BLOB",
        f"<p>{svc('blob','GPv2 BLOB')} は <strong>暗号化スコープ</strong>（Encryption Scopes）をサポートし、コンテナーや BLOB ごとに異なるカスタマー マネージド キー（CMK）を使用できます。</p>"
        + tbl(["ストレージ種別","CMK サポート","ユーザーごとの別キー","用途"],
              [["GPv2 BLOB ✓","✓","✓（暗号化スコープ）","汎用・アプリ データ"],
               ["ADLS Gen2","✓","△（ファイル システム単位）","ビッグ データ分析"],
               ["Premium File Share","✓","✗（共有全体のみ）","SMB ファイル共有"],
               ["GPv2 File","✓","✗","SMB ファイル共有"]],
              "ユーザーごとの暗号化キー対応比較"))
    wrong = blk_wrong("ADLS Gen2 / Premium File Share / GPv2 File",
        "ADLS Gen2 はビッグ データ分析向けでアプリ ユーザー データに最適ではありません。File Share 系はユーザーごとの CMK 設定が不可です。")
    key = blk_key("暗号化スコープ（Encryption Scopes）とは",
        "<p>GPv2 BLOB の機能で、コンテナーや個別 BLOB に異なる CMK を割り当て可能。<br>"
        "Azure Key Vault と統合して鍵をローテーション・管理できます。</p>")
    return exp_wrap(correct, wrong, key)

def exp_q15():
    correct = blk_correct("Azure Service Bus",
        f"<p>{svc('servicebus','Azure Service Bus')} は XML を含む構造化メッセージを使った非同期通信のための信頼性の高いエンタープライズ メッセージング サービスです。</p>"
        + tbl(["サービス","非同期メッセージング","XML サポート","トランザクション対応","適した用途"],
              [[svc('servicebus','Service Bus'),"✓","✓","✓","分散トランザクション・サービス間通信"],
               ["Event Hubs","✓（ストリーミング）","✓","✗","テレメトリ・ログ収集"],
               ["Event Grid","✓（イベント）","✓","✗","イベント ドリブン通知"],
               ["Storage Queue","✓","✓","✗","シンプルなキューイング"]],
              "Azure メッセージング サービス比較"))
    wrong = blk_wrong("Service Fabric / Notification Hubs / Traffic Manager",
        "Service Fabric はマイクロサービス プラットフォーム、Notification Hubs はモバイル プッシュ通知、Traffic Manager は DNS ロード バランサーです。いずれもメッセージング機能を提供しません。")
    return exp_wrap(correct, wrong)

def exp_q16():
    diag = diag_q16()
    correct = blk_correct("IP フロー確認（IP Flow Verify）",
        f"<p>{svc('nwatcher','Azure Network Watcher')} の <strong>IP フロー確認</strong>は NSG ルールに基づいて特定のトラフィックが許可・拒否されるかを即座に診断します。</p>"
        + tbl(["Network Watcher ツール","用途","パケット レベル分析"],
              [["IP Flow Verify ✓","特定トラフィックの許可/拒否確認","✓（送受信 IP・ポート指定）"],
               ["Traffic Analytics","NSG フロー ログの集計分析","✗"],
               ["Connection Monitor","接続の継続的監視","△（疎通のみ）"],
               ["Packet Capture","実際のパケットキャプチャ","✓（重い）"],
               ["Effective Routes","ルーティング確認","✗"]],
              "Network Watcher ツール比較"))
    wrong = blk_wrong("Traffic Analytics",
        "NSG フロー ログを集計・可視化しますが、特定 VM への個別パケットの許可・拒否の詳細判定はできません。")
    wrong2 = blk_wrong("Azure Advisor / VM Insights",
        "Advisor はコスト・パフォーマンス推奨サービス。VM Insights はプロセス間依存関係の可視化。いずれもパケット レベルのネットワーク診断機能はありません。")
    return exp_wrap(diag, correct, wrong, wrong2)

def exp_q17():
    diag = diag_q17()
    correct = blk_correct("VM × 2 リージョン ＋ Azure Traffic Manager",
        f"<p>{svc('vm','Azure VM')} は OS へのフル アクセスを提供し、完全な .NET Framework とカスタム依存関係のインストールが可能です。<br>"
        f"{svc('traffic_mgr','Traffic Manager')} は DNS ベースのグローバル ロード バランシングで、リージョン障害時に自動フェールオーバーします。</p>"
        + tbl(["要件","VM + Traffic Manager","VM + App Gateway","VM Scale Set","App Service（Isolated）"],
              [[".NET Full Framework","✓","✓","✓","✗（.NET Core のみ）"],
               ["OS アクセス","✓","✓","✓","✗"],
               ["リージョン冗長性","✓（マルチリージョン）","✗（単一リージョン）","✗","✗（別途構成必要）"]],
              "ステートレス Web アプリの構成比較"))
    wrong = blk_wrong("Application Gateway",
        f"{svc('app_gw','Application Gateway')} はリージョン サービスであり複数 Azure リージョンにまたがれません。リージョン冗長には Traffic Manager か Front Door が必要です。")
    wrong2 = blk_wrong("VM Scale Set / App Service（Isolated）",
        "VM Scale Set は単一リージョン内のスケーリング。App Service は OS アクセスと完全な .NET Framework をサポートしません。")
    return exp_wrap(diag, correct, wrong, wrong2)

def exp_q18():
    correct = blk_correct("アクセス レビューの構成",
        f"<p>{svc('entra_ca','Microsoft Entra アクセス レビュー')} で SecGroupA を構成することで、4 つの要件をすべて満たせます。</p>"
        + tbl(["要件","アクセス レビュー","PIM","動的グループ","Identity Protection"],
              [["3ヶ月ごとの自動実行","✓（スケジュール設定）","✗（役割専用）","✗","✗"],
               ["メンバーによる自己証明","✓","✗","✗","✗"],
               ["不要回答者の自動削除","✓","✗","✗","✗"],
               ["無応答者の自動削除","✓","✗","✗","✗"]],
              "各機能の要件対応比較"))
    wrong = blk_wrong("PIM / 動的グループ / Identity Protection",
        "PIM は特権ロール管理、動的グループは属性ベース自動管理、Identity Protection はリスク サインイン検出です。いずれも定期的なメンバーシップの人的検証には対応しません。")
    return exp_wrap(correct, wrong)

def exp_q19():
    correct = blk_correct("SKU：Premium ＋ Credential passthrough",
        f"<p>{svc('databricks','Azure Databricks Premium')} SKU のみが Credential passthrough と ACL をサポートします。</p>"
        + tbl(["SKU","Credential Passthrough","Table ACL","Unity Catalog","コスト"],
              [["Standard","✗","✗","✗","低"],
               ["Premium ✓","✓","✓","✓（オプション）","中"]],
              "Databricks SKU 比較")
        + tbl(["クラスター構成","用途","アクセス制御"],
              [["Credential passthrough ✓","ユーザー ID で ADLS にアクセス","フォルダー単位（ユーザーごと）"],
               ["Managed Identities","クラスター/WS 単位","全ユーザー共通（粒度粗）"],
               ["MLflow","実験追跡","無関係"],
               ["Photon","クエリ高速化","無関係"],
               ["Secret Scope","資格情報管理","フォルダー権限適用不可"]],
              "クラスター構成の役割"))
    wrong = blk_wrong("Standard SKU / Managed Identities",
        "Standard は Credential passthrough 非対応。Managed Identities はクラスター単位のアクセスでユーザーごとのフォルダー権限を強制できません。")
    return exp_wrap(correct, wrong)

def exp_q20():
    correct = blk_correct("Azure Service Bus トピック",
        f"<p>{svc('servicebus','Service Bus トピック')} はパブリッシュ・サブスクライブ パターンで、複数アプリが同一メッセージを独立して受信できます。サブスクリプション フィルターで各アプリは関連メッセージのみ処理可能です。</p>"
        + tbl(["方式","複数サブスクライバー","フィルタリング","メッセージ保証","適した用途"],
              [["Service Bus Topic ✓","✓（サブスクリプション）","✓（ルール/フィルター）","✓（At-least-once）","Pub/Sub・ビジネスロジック"],
               ["Service Bus Queue","✗（1対1）","✗","✓","シングル コンシューマー"],
               ["Storage Queue","✗（1対1）","✗","△","シンプルなキュー"],
               ["Event Hubs","✓（Consumer Group）","△","✓","大量ストリーミング"],
               ["Event Grid","✓","✓","△","イベント通知"]],
              "メッセージング サービス比較"))
    wrong = blk_wrong("Service Bus Queue / 複数 Storage Queue / ADF",
        "Queue は1対1のみ。複数 Queue はメッセージを手動で複製する必要があり管理オーバーヘッドが増大します。ADF はメッセージングではなくデータ統合用です。")
    return exp_wrap(correct, wrong)

def exp_q21():
    correct = blk_correct("AppOne：StoreAlpha + StoreGamma ／ AppTwo：StoreAlpha + StoreDelta",
        tbl(["ストレージ","種別","パフォーマンス","ライフサイクル管理","ファイル共有"],
            [["StoreAlpha","StorageV2","Standard","✓","✓（Standard Files）"],
             ["StoreBeta","StorageV2","Premium","✗","✗"],
             ["StoreGamma","BlobStorage","Standard","✓","✗"],
             ["StoreDelta","FileStorage","Premium","✗","✓（Premium Files）"]],
            "ストレージ アカウントの機能マトリクス")
        + "<p><strong>AppOne（ライフサイクル管理）</strong>：Standard 性能のみ対応（StoreAlpha + StoreGamma）<br>"
        "<strong>AppTwo（ファイル共有）</strong>：StorageV2 と FileStorage のみ対応（StoreAlpha + StoreDelta）</p>")
    wrong = blk_wrong("StoreBeta（Premium StorageV2）",
        "Premium パフォーマンスの StorageV2 はライフサイクル管理とファイル共有の両方をサポートしません。")
    return exp_wrap(correct, wrong)

def exp_q22():
    correct = blk_correct("Azure Blob Storage",
        f"<p>{svc('blob','Azure Blob Storage')} は大容量の非構造化データ（動画ファイルなど）の高速配信に最適です。CDN 統合・SAS による時間限定アクセス・Hot/Cool/Archive 層でコスト最適化が可能です。</p>"
        + tbl(["サービス","大容量ファイル対応","インターネット公開","コスト層","CDN統合"],
              [[svc('blob','Blob Storage'),"✓（最大 190 TB）","✓","Hot/Cool/Archive","✓"],
               ["Azure Files","✓","△（SMB/NFS）","Transaction Opt/Cool","✗"],
               ["ADLS Gen2","✓","△","N/A","✗"],
               ["Azure SQL","✗（< 1TB）","✓","N/A","✗"]],
              "動画ストレージ オプション比較"))
    wrong = blk_wrong("Azure Files / ADLS Gen2 / Azure SQL",
        "Azure Files は SMB/NFS プロトコル向けで直接インターネット配信に不向き。ADLS Gen2 は分析向け。Azure SQL は構造化データ向けで大容量ファイル格納に非効率です。")
    return exp_wrap(correct, wrong)

def exp_q23():
    correct = blk_correct("Azure SQL Database ＋ Hyperscale レベル",
        f"<p>{svc('sql_db','Azure SQL Database')} Hyperscale は最大 100 TB をサポートし、75 TB の要件を満たします。</p>"
        + tbl(["サービス/レベル","最大サイズ","スケーリング","Geo バックアップ","OLTP 最適化"],
              [[svc('sql_db','SQL DB Hyperscale ✓'),"100 TB","✓（即時スケール）","✓","✓"],
               [svc('sql_db','SQL DB General Purpose'),"4 TB","✓","✓","✓"],
               [svc('sql_db','SQL DB Business Critical'),"4 TB","✓","✓","✓"],
               [svc('sql_mi','SQL Managed Instance'),"16 TB","✓","✓","✓"],
               [svc('sql_server','SQL Server on VM'),"OS 依存","手動","手動","✓"],
               ["Azure Synapse","無制限","✓","✓","✗（OLAP向け）"]],
              "Azure SQL サービス比較（最大サイズ）"))
    wrong = blk_wrong("Azure SQL Managed Instance",
        "最大データベース サイズが 16 TB に制限されており、75 TB の要件を満たしません。")
    wrong2 = blk_wrong("Azure Synapse / Business Critical / General Purpose",
        "Synapse は OLAP 向け。Business Critical と General Purpose は最大 4 TB で 75 TB に対応しません。")
    return exp_wrap(correct, wrong, wrong2)

def exp_q24():
    correct = blk_correct("Azure Cosmos DB for NoSQL",
        f"<p>{svc('cosmos','Azure Cosmos DB for NoSQL')} は SQL API・マルチ マスター書き込み・シングル桁ミリ秒読み取りの3要件をすべて満たします。</p>"
        + tbl(["サービス","SQL クエリ","マルチリージョン書き込み","低レイテンシ読み取り"],
              [[svc('cosmos','Cosmos DB NoSQL ✓'),"✓（SQL API）","✓（マルチマスター）","✓（<10ms）"],
               [svc('sql_db','SQL DB + Active GR'),"✓","✗（読み取り専用レプリカ）","△"],
               [svc('sql_db','SQL DB Hyperscale'),"✓","✗","△"],
               ["Cosmos DB for PostgreSQL","✓","✓","△"]],
              "グローバル分散データベース比較"))
    wrong = blk_wrong("Azure SQL Database（Active geo-replication）",
        "Active geo-replication は読み取り専用のセカンダリ レプリカのみを作成します。マルチリージョンへの同時書き込みはサポートしません。")
    return exp_wrap(correct, wrong)

def exp_q25():
    correct = blk_correct("Azure Site Recovery",
        f"<p>{svc('recovery','Azure Site Recovery')} は VM レベルの自動レプリケーションと自動フェールオーバーで、15 分の RTO と 24 時間の RPO を低コストで実現します。</p>"
        + tbl(["方式","リージョン障害対応","自動復旧","RTO","コスト"],
              [[svc('recovery','Site Recovery ✓'),"✓","✓","分〜15分","低"],
               ["VM 可用性セット","✗（同一リージョン内）","✓","N/A","低"],
               ["Azure Disk Backup","✓（バックアップ）","✗（手動）","時間単位","低"],
               ["Always On AG","✓","✓（Synchronous）","秒単位","高（Enterprise）"]],
              "SQL Server DR オプション比較"))
    wrong = blk_wrong("VM 可用性セット",
        "可用性セットは単一リージョン内のハードウェア障害に対する HA を提供しますが、リージョン全体の障害には対応できません。")
    wrong2 = blk_wrong("Azure Disk Backup / Always On AG",
        "Disk Backup は手動復旧が必要で 15 分 RTO は困難。Always On AG は SQL Server Enterprise が必要で高コストです。")
    return exp_wrap(correct, wrong, wrong2)

def exp_q26():
    correct = blk_correct("Premium ストレージ層 ＋ ZRS",
        tbl(["","Premium ファイル共有（✓）","Hot / Transaction Opt."],
            [["バックアップ","SSD","HDD"],
             ["レイテンシ","最低（<1ms）","中"],
             ["IOPS","最大 100,000+","数千"],
             ["ZRS 対応","✓","✗（Transaction Opt.）"],
             ["LRS 対応","✓","✓"],
             ["GRS 対応","✗","✓"]],
            "Azure Files ストレージ層比較"))
    wrong = blk_wrong("Hot / Transaction Optimized",
        "Hot は Blob 向けのアクセス層で Azure Files には適用されません。Transaction Optimized は ZRS をサポートせず最高回復性の要件を満たしません。")
    wrong2 = blk_wrong("GRS / LRS",
        "GRS はクロスリージョンで DR 向きですが、アクティブな低レイテンシ アクセスには高レイテンシになります。LRS は単一 DC 内のみで最高回復性ではありません。")
    return exp_wrap(correct, wrong, wrong2)

def exp_q27():
    diag = diag_q27()
    correct = blk_correct("Microsoft Entra（アクセス トークンを生成する）",
        f"<p>OAuth 2.0 フローでは <strong>Microsoft Entra ID（認可サーバー）</strong> がアクセス トークンを発行します。</p>"
        + tbl(["エンティティ","OAuth 2.0 での役割","トークン生成"],
              [[svc('entra_apps','Microsoft Entra ID'),"認可サーバー（Authorization Server）","✓ 生成・発行"],
               [svc('app_svc','Web アプリ'),"クライアント（Client）","✗ 要求するのみ"],
               [svc('app_svc','Web API'),"リソース サーバー（Resource Server）","✗ 検証するのみ"]],
              "OAuth 2.0 各エンティティの役割"))
    wrong = blk_wrong("Web アプリ / Web API",
        "Web アプリはトークンを要求（クライアント）するだけで生成しません。Web API はトークンを検証・利用しますが生成しません。")
    return exp_wrap(diag, correct, wrong)

def exp_q28():
    correct = blk_correct("Web API（認可の決定を行う）",
        f"<p>OAuth 2.0 では <strong>リソース サーバー（Web API）</strong> が認可の決定を行います。受け取ったトークンのクレーム（ロール・スコープ・ユーザー ID）を検査して許可・拒否を判定します。</p>"
        + tbl(["エンティティ","認可の役割"],
              [[svc('entra_apps','Microsoft Entra ID'),"トークン発行（認可決定は行わない）"],
               [svc('app_svc','Web アプリ'),"UI レベルの制御（バックエンド API の認可は担当外）"],
               [svc('app_svc','Web API ✓'),"トークン検証 + クレーム評価 = 認可決定"]],
              "認可の責務分担"))
    wrong = blk_wrong("Microsoft Entra / Web アプリ",
        "Entra ID は ID プロバイダーでトークン発行のみ。Web アプリは UI 制御を担当しますが、API リソースへのアクセス制御は Web API の責任です。")
    return exp_wrap(correct, wrong)

def exp_q29():
    correct = blk_correct("Shared Access Signature（SAS）",
        f"<p>{svc('storage','SAS')} は開始日・有効期限・権限スコープを設定したトークンで、9 月の期間限定アクセスを安全に実装できます。</p>"
        + tbl(["SAS の種類","説明","Entra ID 連携","推奨度"],
              [["ユーザー委任 SAS","Entra ID で署名","✓","◎（最高セキュリティ）"],
               ["サービス SAS","ストレージ アカウント キーで署名","✗","○"],
               ["アカウント SAS","アカウント全体に権限","✗","△"],
               ["アクセス キー","全権限・有効期限なし","✗","✗（共有危険）"]],
              "SAS 種別比較"))
    wrong = blk_wrong("Conditional Access / アクセス キー / 証明書",
        "Conditional Access は Entra ID サインイン制御でストレージの時間限定アクセスには不可。アクセス キーは全権限付与で期限設定不可。証明書はアプリ認証用です。")
    return exp_wrap(correct, wrong)

def exp_q30():
    correct = blk_correct("Azure Data Lake Storage",
        f"<p>{svc('adls','Azure Data Lake Storage')} はイミュータブル ストレージ・匿名アクセス禁止・Microsoft Entra 連携の ACL の3要件をすべて満たします。</p>"
        + tbl(["要件","ADLS","Blob Storage","Azure Files","NetApp Files"],
              [["イミュータブル（WORM）","✓（ポリシー）","✓（コンテナー）","△","△"],
               ["匿名アクセス禁止","✓（デフォルト無効）","△（設定必要）","✓","✓"],
               ["Entra ID ACL（ファイル/Dir）","✓（POSIX ACL）","✗（RBAC のみ）","△","△"]],
              "ストレージ セキュリティ機能比較"))
    wrong = blk_wrong("Azure Blob Storage",
        "Blob Storage は RBAC によるアクセス制御をサポートしますが、POSIX スタイルの ACL でファイル・ディレクトリ単位の細粒度な Entra ID 権限管理はできません。")
    wrong2 = blk_wrong("Azure Files / Azure NetApp Files",
        "Azure Files は SMB/NFS 向けで ACL サポートは限定的。NetApp Files は高性能エンタープライズ向けですが Entra ID 連携 ACL の完全サポートがありません。")
    return exp_wrap(correct, wrong, wrong2)

def exp_q31():
    correct = blk_correct("MARS エージェント ＋ ローカル冗長ストレージ（LRS）",
        f"<p>{svc('recovery','MARS エージェント')} はオンプレミス Windows Server の全ファイル・フォルダーを Azure Recovery Services コンテナーにバックアップします。</p>"
        + tbl(["バックアップ オプション","全ファイル/フォルダー","Azure 統合","スケジュール","コスト"],
              [[svc('recovery','MARS エージェント ✓'),"✓","✓","✓（日次）","低"],
               ["Site Recovery Mobility Service","✗（VM 全体レプリカ）","✓","✓","中"],
               ["VSS","✓（スナップショット）","✗（ローカルのみ）","手動","低（スクリプト必要）"]],
              "バックアップ方式比較")
        + tbl(["冗長性","コピー数","保護","コスト","3コピー要件"],
              [["LRS ✓","3（同一 DC）","ラック障害","最安","✓"],
               ["ZRS","3（異なる AZ）","DC 障害","中","✓"],
               ["GRS","6（異なるリージョン）","リージョン障害","高","✓（過剰）"]],
              "Recovery Services コンテナーの冗長性"))
    wrong = blk_wrong("Site Recovery / VSS / GRS",
        "Site Recovery は DR・移行向け。VSS は Azure 統合なく手動管理が必要。GRS はコストが高く最小化要件に反します。")
    return exp_wrap(correct, wrong)

def exp_q32():
    correct = blk_correct("BLOB：ユーザー委任 SAS ／ ファイル共有：Microsoft Entra 資格情報",
        tbl(["","BLOB（Block Blob）","ファイル共有（SMB）"],
            [["推奨","ユーザー委任 SAS ✓","Microsoft Entra 資格情報 ✓"],
             ["共有キー不使用","✓","✓"],
             ["時間制限","✓（有効期限設定）","✓（セッション制御）"],
             ["Entra ID 連携","✓","✓"],
             ["SAS + 保存済みポリシー","✗（未対応）","N/A"],
             ["ユーザー委任 SAS + Azure Files","N/A","✗（未対応）"]],
            "ストレージ アクセス認可方式比較"))
    wrong = blk_wrong("SAS + 保存済みアクセス ポリシー",
        "保存済みアクセス ポリシーはユーザー委任 SAS と組み合わせられません。ユーザー委任 SAS 単体で要件を満たします。")
    wrong2 = blk_wrong("ファイル共有：ユーザー委任 SAS",
        "ユーザー委任 SAS は Azure Files（SMB）ではサポートされていません。Files には Microsoft Entra 資格情報を使用します。")
    return exp_wrap(correct, wrong, wrong2)

def exp_q33():
    correct = blk_correct("専用 SQL プール（ハッシュ分散テーブルへのデータ ロード）",
        f"<p>{svc('synapse','Synapse 専用 SQL プール')} はハッシュ分散テーブルをサポートし、大規模 DW ワークロードのデータ ロードと集計クエリに最適化されています。</p>"
        + tbl(["プール種別","ハッシュ分散テーブル","データ取り込み","Delta Lake 更新","適した用途"],
              [["専用 SQL プール ✓","✓","✓","✗","大規模 DW・バッチ分析"],
               ["サーバーレス Spark","✗","△","✓","Delta Lake・大規模処理"],
               ["サーバーレス SQL","✗（クエリのみ）","✗","✗","アドホック クエリ"]],
              "Synapse プール種別比較"))
    wrong = blk_wrong("サーバーレス Spark / サーバーレス SQL",
        "Spark はハッシュ分散テーブルへの直接取り込みには設計されていません。サーバーレス SQL はデータの取り込みと永続的なテーブルへの書き込みをサポートしません。")
    return exp_wrap(correct, wrong)

def exp_q34():
    correct = blk_correct("サーバーレス Apache Spark プール（Delta Lake のクエリ・更新）",
        f"<p>{svc('databricks','サーバーレス Spark プール')} は Delta Lake の実装・クエリ・更新（ACID トランザクション）をすべてサポートします。</p>"
        + tbl(["プール","Delta Lake 読み取り","Delta Lake 書き込み/更新","ACID トランザクション"],
              [["サーバーレス Spark ✓","✓","✓","✓"],
               ["専用 SQL プール","△（外部テーブル）","✗","✗"],
               ["サーバーレス SQL","✓（読み取りのみ）","✗","✗"]],
              "Delta Lake 操作対応比較"))
    wrong = blk_wrong("専用 SQL プール / サーバーレス SQL",
        "専用 SQL プールは DW 向けで Delta Lake の直接更新に適していません。サーバーレス SQL は Delta Lake の読み取りのみで更新はサポートしません。")
    return exp_wrap(correct, wrong)

def exp_q35():
    correct = blk_correct("Always Encrypted（SSN 列）",
        f"<p>{svc('kv','Always Encrypted')} はクライアント アプリが暗号化・復号を管理します。DBA やクラウド管理者はアプリが持つ鍵なしでは SSN を平文で見ることができません。</p>"
        + tbl(["機能","暗号化対象","管理者から保護","部分開示","アプリ変更"],
              [["Always Encrypted ✓","列（クライアント側）","✓（鍵なし不可）","✗","必要"],
               ["Dynamic Data Masking","クエリ結果（表示）","✗（権限付与で閲覧可）","✓","不要"],
               ["TDE","DB 全体（ページ）","✗","✗","不要"],
               ["Column Encryption","列","△","✗","必要"]],
              "データ保護機能比較（管理者保護の観点）"))
    wrong = blk_wrong("動的データ マスキング（DDM）",
        "DDM は表示をマスクしますが、適切な権限を持つ管理者はマスク解除して実データを閲覧できます。管理者からの保護には不十分です。")
    wrong2 = blk_wrong("TDE / 列の暗号化",
        "TDE はページ レベルの暗号化でクラウド管理者も復号済みデータにアクセス可能。列の暗号化は Always Encrypted と異なりアプリ管理の鍵ではなく DB 管理者が鍵を持つためです。")
    return exp_wrap(correct, wrong, wrong2)

def exp_q36():
    correct = blk_correct("動的データ マスキング（DDM）（電話番号列）",
        f"<p>{svc('sql_db','動的データ マスキング')} は SQL レイヤーで列の一部のみを表示するルールを設定できます。アプリ変更不要で電話番号の下4桁のみ表示が実現できます。</p>"
        + '<p>設定例：<code>MASKED WITH (FUNCTION = \'partial(0,"XXXX",4)\')</code> → 表示: XXXX-1234</p>"')
    wrong = blk_wrong("Always Encrypted",
        "Always Encrypted は保存・転送中の完全暗号化向けで、「下4桁のみ表示」のような部分的なデータ開示機能はありません。")
    key = blk_key("Q35 と Q36 の使い分け",
        tbl(["列","要件","最適な機能"],
            [["SSN（社会保障番号）","管理者も含め誰にも見せない","Always Encrypted"],
             ["電話番号","非特権ユーザーには下4桁のみ","Dynamic Data Masking"]],
            "機能の使い分け早見表"))
    return exp_wrap(correct, wrong, key)

def exp_q37():
    diag = diag_q37()
    correct = blk_correct("クライアント資格情報付与フロー ＋ IMDS エンドポイント",
        f"<p>{svc('entra_mi','システム割り当てマネージド ID')} を使用した App1 の認証フロー：</p>"
        + tbl(["手順","操作","エンドポイント"],
              [["①","App1 が IMDS にトークン要求","http://169.254.169.254/metadata/identity/oauth2/token"],
               ["②","IMDS が Entra ID に代わってクライアント資格情報フローを実行","自動（透過的）"],
               ["③","Entra ID がアクセス トークンを返す","Microsoft Entra（自動）"],
               ["④","App1 がトークンで KV1 のシークレットを取得","Key Vault REST API"]],
              "マネージド ID トークン取得フロー")
        + tbl(["OAuth 2.0 フロー","用途","ユーザー対話"],
              [["クライアント資格情報 ✓","サービス間認証（M2M）","不要"],
               ["認可コード","ユーザー サインインを含むアプリ","必要"],
               ["暗黙的","SPA・ブラウザー アプリ（レガシー）","必要"]],
              "OAuth 2.0 フロー比較"))
    wrong = blk_wrong("認可コード / 暗黙的フロー",
        "これらはユーザー インタラクションを必要とするフローで、VM 上でバックグラウンド実行するアプリのマシン間認証には適していません。")
    wrong2 = blk_wrong("Microsoft Entra / Microsoft Identity Platform アクセス トークン エンドポイント",
        "これらのエンドポイントは通常の OAuth フロー（サービス プリンシパルや証明書）向けです。マネージド ID の場合は IMDS 経由の方が開発作業を最小化できます。")
    return exp_wrap(diag, correct, wrong, wrong2)

def exp_q38():
    correct = blk_correct("エンタープライズ アプリケーション ＋ 条件付きアクセス ポリシー",
        f"<p>{svc('entra_apps','エンタープライズ アプリ')} で SAML SSO を設定し、{svc('entra_ca','条件付きアクセス')} で不明な場所からの MFA を強制します。</p>"
        + tbl(["要件","エンタープライズ アプリ","条件付きアクセス","PIM","ID Protection"],
              [["SAML SSO 有効化","✓（SAML 構成）","✗","✗","✗"],
               ["不明な場所からの MFA","✗","✓（場所条件）","✗","△（リスクベース）"]],
              "要件と機能の対応"))
    wrong = blk_wrong("PIM / ID Protection / Application Gateway",
        f"{svc('entra_pim','PIM')} は特権ロール管理。{svc('entra_id_prot','ID Protection')} はリスク検出。{svc('app_gw','Application Gateway')} は L7 ロード バランサー。いずれも SAML SSO や場所ベース MFA とは無関係です。")
    key = blk_key("SAML SSO 設定の流れ",
        "<p>① エンタープライズ アプリとして LOB アプリを登録<br>"
        "② SAML メタデータを交換（SP ↔ IdP）<br>"
        "③ 条件付きアクセス ポリシーで「名前付き場所以外 → MFA 必須」を設定<br>"
        "④ ユーザー割り当て・テスト</p>")
    return exp_wrap(correct, wrong, key)
