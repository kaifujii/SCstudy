"""Generate az305/vol6.html from parsed vol6.txt content."""
import json, re

# ── helpers ──────────────────────────────────────────────────────────────────
def exp(correct_items, wrong_items):
    """Build exp_html from lists of (label, body) tuples."""
    parts = ['<div class="exp-sections">']
    for label, body in correct_items:
        parts.append(f'<div class="exp-block exp-correct"><div class="exp-block-label">✓ {label}</div><div class="exp-block-body">{body}</div></div>')
    for label, body in wrong_items:
        parts.append(f'<div class="exp-block exp-wrong"><div class="exp-block-label">✗ {label}</div><div class="exp-block-body">{body}</div></div>')
    parts.append('</div>')
    return ''.join(parts)

def q(num, id_, domain, domain_code, domain_color, question_text, choices, correct_indices, exp_html):
    n_correct = len(correct_indices)
    cs = []
    for i, (text, _) in enumerate(choices):
        cs.append({"text": text, "is_correct": i in correct_indices})
    return {
        "num": num, "id": id_, "domain": domain, "domain_code": domain_code,
        "domain_color": domain_color, "question_text": question_text,
        "choices": cs, "correct_indices": correct_indices, "n_correct": n_correct,
        "exp_html": exp_html, "svg": ""
    }

ID = ("ID・ガバナンス", "ID", "#7719AA")
IS = ("インフラ設計", "IS", "#0072C6")
DS = ("データストレージ", "DS", "#00796B")
BC = ("ビジネス継続性", "BC", "#C50F1F")

# ── Questions ─────────────────────────────────────────────────────────────────
QUESTIONS = []

# Q1 – Entra App Proxy (multi, 2 correct)
QUESTIONS.append(q(1, "q1", *ID,
"オンプレミス環境と同期された Microsoft Entra テナントを管理しています。\n\nWebApp1 というオンプレミスの Web アプリが統合 Windows 認証（IWA）を使用しています。\nリモートワーク中のユーザーは VPN 接続なしで WebApp1 に SSO アクセスする必要があります。\n\n要件を満たす Microsoft Entra 機能を 2 つ選んでください。",
[
    ("Microsoft Entra Identity Management (PIM)", False),
    ("Microsoft Entra エンタープライズ アプリケーション", True),
    ("条件付きアクセス ポリシー", False),
    ("Microsoft Entra アプリケーション プロキシ", True),
    ("Azure Application Gateway", False),
    ("Azure Arc", False),
],
[1, 3],
exp(
    [("Microsoft Entra エンタープライズ アプリケーション",
      "オンプレミスおよびクラウドのアプリを SSO・ユーザー割り当て・条件付きアクセス向けに構成・公開するために使用します。WebApp1 をエンタープライズ アプリとして登録することで、Entra ID との統合が可能になります。"),
     ("Microsoft Entra アプリケーション プロキシ",
      "VPN なしでオンプレミス アプリへの安全なリモート アクセスを提供します。オンプレミスに軽量コネクタをインストールし、Entra ID 経由でリモート ユーザーが SSO でアクセスできます。")],
    [("Microsoft Entra Identity Management (PIM)",
      "PIM は特権ロールの Just-In-Time アクセス管理に使用します。オンプレミス アプリの公開や SSO とは無関係です。"),
     ("条件付きアクセス ポリシー",
      "アクセス制御の強化には使えますが、アプリの公開や SSO 機能そのものを提供するものではありません。"),
     ("Azure Application Gateway", "L7 ロード バランサーです。オンプレミス アプリの Entra ID 統合 SSO とは無関係です。"),
     ("Azure Arc", "ハイブリッド クラウド管理サービスです。アプリ アクセスや SSO の提供は行いません。")]
)))

# Q2 – Blueprints vs ARM
QUESTIONS.append(q(2, "q2", *ID,
"Azure Blueprints と Azure Resource Manager（ARM）テンプレートの主な違いとして正しい説明はどれですか？",
[
    ("Azure Blueprints のみが Azure Policy 定義をサポートする", False),
    ("Blueprint は展開されたリソースとの接続を維持する", True),
    ("ARM テンプレートは展開後もリソースとの継続的な関連性を維持する", False),
    ("Azure Policy 定義は ARM テンプレートを使用した場合にのみ含められる", False),
],
[1],
exp(
    [("Blueprint は展開されたリソースとの接続を維持する",
      "Azure Blueprints は展開されたリソースとの接続を維持し、継続的なコンプライアンス追跡や更新を可能にします。これが ARM テンプレートとの主な違いです。")],
    [("Azure Blueprints のみが Azure Policy 定義をサポートする",
      "ARM テンプレートも Azure Policy の割り当てを含むことができます。どちらもポリシー定義をサポートします。"),
     ("ARM テンプレートは展開後もリソースとの継続的な関連性を維持する",
      "誤りです。ARM テンプレートはデプロイ完了後にリソースとの接続を持ちません。テンプレートを変更してもリソースは自動更新されません。"),
     ("Azure Policy 定義は ARM テンプレートを使用した場合にのみ含められる",
      "Blueprints もポリシー定義・ロール割り当て・リソース グループを含むことができます。")]
)))

# Q3 – Diagnostic settings (True/False → single select)
QUESTIONS.append(q(3, "q3", *DS,
"以下のリソースが East US リージョンに展開されています：\n・StoreAcctA（Storage v1）、StoreAcctB（Storage v2）\n・LogWS-A、LogWS-B（Log Analytics ワークスペース）\n・EventHub-A（Event Hub）\n\nSalesDB（Azure SQL Database）に DiagConfig1 という診断設定を構成しました：\n  - SQLInsights ログ → StoreAcctA にアーカイブ\n  - SQLInsights ログ → LogWS-A に送信\n\n次の文は正しいですか？\n「SalesDB に追加の診断設定を作成して、SQLInsights ログを EventHub-A に送信できる」",
[
    ("正しい（True）", True),
    ("正しくない（False）", False),
],
[0],
exp(
    [("正しい（True）",
      "Azure 診断設定は最大 5 つの送信先（ストレージ アカウント、Log Analytics、Event Hub など）をサポートします。EventHub-A は有効な送信先であるため、新しい診断設定を作成して SQLInsights ログを送信できます。")],
    [("正しくない（False）",
      "Event Hub は診断設定の有効な送信先です。既存の設定（StoreAcctA + LogWS-A）とは独立して追加設定を作成できます。")]
)))

# Q4 – Always On AG with DNN
QUESTIONS.append(q(4, "q4", *IS,
"オンプレミスの SQL Server アプリを Azure VM に移行します。以下の制約を満たす高可用性 SQL Server アーキテクチャを推奨してください：\n・コストを最小限に抑える\n・SQL Server インスタンスが利用不能になった場合、最小限の遅延でフェールオーバーする",
[
    ("Always On フェールオーバー クラスター インスタンス（VNN）＋ Premium Azure ファイル共有", False),
    ("Always On 可用性グループ（Premium マネージド ディスク）＋ 分散ネットワーク名（DNN）", True),
    ("Always On フェールオーバー クラスター インスタンス（VNN）＋ Standard Azure ファイル共有", False),
    ("Always On 可用性グループ（Premium マネージド ディスク）＋ 仮想ネットワーク名（VNN）", False),
],
[1],
exp(
    [("Always On 可用性グループ（DNN）",
      "DNN（分散ネットワーク名）は Azure Load Balancer への依存を排除し、フェールオーバー時間を短縮します。クライアントが MultiSubnetFailover=True を指定するとすべてのノード IP を並行試行でき、VNN より高速なフェールオーバーが実現します。")],
    [("Always On FCI（VNN）＋ Premium ファイル共有",
      "VNN は Azure Load Balancer を必要とし、ヘルス プローブによる追加の遅延が発生します。"),
     ("Always On FCI（VNN）＋ Standard ファイル共有",
      "コストは下がりますが VNN による Load Balancer の遅延は変わりません。"),
     ("Always On AG（VNN）",
      "VNN は依然として Load Balancer を必要とし、DNN と比較してフェールオーバー時間が長くなります。")]
)))

# Q5+Q6 merged – SQL MI + Auto-failover group (multi, 2 correct)
QUESTIONS.append(q(5, "q5", *DS,
"オンプレミスの Microsoft SQL Server データベースを Azure に移行します。以下の要件を満たすソリューションを推奨してください：\n・ユーザーが開始するバックアップを許可する\n・異なる Azure リージョンの複数インスタンスへの自動レプリケーションを提供する\n・ビジネス継続性機能の構成・管理の運用オーバーヘッドを削減する\n\n最適なデプロイ サービスと、そのサービスで使用する冗長性ソリューションをそれぞれ 1 つずつ選んでください（計 2 つ）。",
[
    ("Azure SQL Managed Instance", True),
    ("Azure VM 上の SQL Server", False),
    ("Azure SQL Database シングル データベース", False),
    ("自動フェールオーバー グループ（Auto-failover group）", True),
    ("アクティブ geo レプリケーション（Active geo-replication）", False),
    ("ゾーン冗長デプロイ（Zone-redundant deployment）", False),
],
[0, 3],
exp(
    [("Azure SQL Managed Instance",
      "ユーザーが開始するバックアップをサポートします。Azure SQL Database とは異なり、手動バックアップをトリガーできます。"),
     ("自動フェールオーバー グループ",
      "複数リージョンへの自動レプリケーションと自動フェールオーバーを完全マネージドで提供します。Managed Instance と組み合わせることで、管理作業を最小限に抑えながら高可用性を実現します。")],
    [("Azure VM 上の SQL Server",
      "ユーザー バックアップは可能ですが、リージョン間の高可用性構成（可用性グループ等）に多大な管理作業が必要です。"),
     ("Azure SQL Database シングル データベース",
      "自動レプリケーションは提供しますが、ユーザーが開始するバックアップはサポートしません。"),
     ("アクティブ geo レプリケーション",
      "クロスリージョン レプリケーションを提供しますが、フェールオーバーは手動操作が必要です。また Managed Instance では使用できません。"),
     ("ゾーン冗長デプロイ",
      "単一リージョン内の高可用性を提供しますが、複数リージョンへのレプリケーションはサポートしません。")]
)))

# Q7+Q8 merged – WorkloadA and WorkloadB storage (multi, 2 correct)
QUESTIONS.append(q(6, "q6", *DS,
"WorkloadA と WorkloadB 向けに Azure Storage アカウント戦略を設計しています。\n\n設計要件：\n・WorkloadA：最高スループット・最低レイテンシのストレージが必要\n・WorkloadB：GB 単価が最も低いストレージが必要\n・両ワークロードはデータ センター障害時も可用性を維持する必要がある\n・両ワークロードは頻繁なアップロード・ダウンロード操作に最適化する\n\nWorkloadA と WorkloadB それぞれに推奨するストレージ構成を 1 つずつ選んでください（計 2 つ）。",
[
    ("WorkloadA：Blob Storage（Standard、Hot、RA-GRS）", False),
    ("WorkloadA：Block Blob Storage（Premium、ZRS）", True),
    ("WorkloadA：General Purpose v1（Premium、LRS）", False),
    ("WorkloadA：General Purpose v2（Standard、Hot、LRS）", False),
    ("WorkloadB：Blob Storage（Standard、Cool、GRS）", False),
    ("WorkloadB：Block Blob Storage（Premium、ZRS）", False),
    ("WorkloadB：General Purpose v1（Standard、RA-GRS）", False),
    ("WorkloadB：General Purpose v2（Standard、Cool、RA-GRS）", True),
],
[1, 7],
exp(
    [("WorkloadA：Block Blob Storage（Premium、ZRS）",
      "Block Blob Storage は高トランザクション レートと低レイテンシに最適化されています。Premium パフォーマンスで最小レイテンシを実現し、ZRS でデータ センター障害に対する可用性を確保します。"),
     ("WorkloadB：General Purpose v2（Standard、Cool、RA-GRS）",
      "GPv2 は最も低い GB 単価を提供します。Cool アクセス層でさらにコストを削減し、RA-GRS でクロスリージョン可用性を確保します。")],
    [("WorkloadA：Blob Storage（Standard、Hot、RA-GRS）",
      "Standard パフォーマンスでは最低レイテンシを実現できません。"),
     ("WorkloadA：General Purpose v1（Premium、LRS）",
      "GPv1 はレガシーでモダン ワークロードに最適化されていません。LRS はデータ センター障害への耐性がありません。"),
     ("WorkloadA：General Purpose v2（Standard、Hot、LRS）",
      "Standard パフォーマンスは Premium の速度に及ばず、LRS はデータ センター障害を防ぎません。"),
     ("WorkloadB：Blob Storage（Standard、Cool、GRS）",
      "GRS は RA-GRS と比較して読み取りアクセスが制限されます。GPv2 の方が柔軟性があります。"),
     ("WorkloadB：Block Blob Storage（Premium、ZRS）",
      "Premium パフォーマンスはコストを大幅に増加させ、コスト最小化の要件に反します。"),
     ("WorkloadB：General Purpose v1（Standard、RA-GRS）",
      "GPv1 は GPv2 と比較してオペレーション コストが高く、コスト最適化機能が劣ります。")]
)))

# Q9 – Virtual WAN upgrade
QUESTIONS.append(q(7, "q7", *IS,
"Basic レベルの Azure Virtual WAN「CoreWan01」を管理しています。\n\n・EastHubA（East US）\n・WestHubB（West US）\n\nEast US に既存の ExpressRoute 回線があります。この回線を CoreWan01 に関連付ける計画です。\n\nExpressRoute 回線を Virtual WAN に接続する前に、最初に実行すべき操作はどれですか？",
[
    ("CoreWan01 を Basic レベルから Standard レベルにアップグレードする", True),
    ("EastHubA に ExpressRoute ゲートウェイをデプロイする", False),
    ("East US リージョンにハブ仮想ネットワークを作成する", False),
    ("ExpressRoute 回線の ExpressRoute Premium アドオンを有効にする", False),
],
[0],
exp(
    [("Standard レベルへのアップグレード",
      "ExpressRoute は Basic Virtual WAN ではサポートされません。Standard レベルにアップグレードすることで、ExpressRoute・VPN・リージョン間ハブ接続が利用可能になります。")],
    [("ExpressRoute ゲートウェイのデプロイ",
      "ゲートウェイを作成する前に、Virtual WAN を Standard に変更する必要があります。アップグレードなしではゲートウェイを作成できません。"),
     ("ハブ仮想ネットワークの作成",
      "ハブ（EastHubA）は既に存在します。新しいハブを作成するのではなく、Virtual WAN のアップグレードが優先事項です。"),
     ("ExpressRoute Premium アドオン",
      "Premium アドオンは 10 を超える VNet 接続やグローバル リーチが必要な場合に使用します。Basic Virtual WAN の ExpressRoute 非対応を解決するものではありません。")]
)))

# Q10 – Functions Premium plan
QUESTIONS.append(q(8, "q8", *IS,
"Azure Event Grid 経由でイベントが配信されるたびにカスタム C# コードを実行するイベント ドリブン ソリューションを設計しています。\n\n要件：\n・プライベート IP アドレスを使用して Azure VM 上の SQL Server インスタンスに接続できること\n・全体的な運用コストとコンピューティング コストを最小限に抑えること\n\n使用すべき Azure サービスとホスティング オプションはどれですか？",
[
    ("Azure Functions（従量課金プラン）", False),
    ("Azure Functions（Premium プラン）", True),
    ("Azure Logic Apps（統合サービス環境）", False),
    ("Azure Functions（Dedicated プラン＋ Basic App Service プラン）", False),
    ("Azure Logic Apps（従量課金プラン）", False),
],
[1],
exp(
    [("Azure Functions（Premium プラン）",
      "Premium プランは仮想ネットワーク（VNet）統合をサポートし、プライベート IP でリソースにアクセスできます。Dedicated プランよりコスト効率が高く、スケーリングも可能です。")],
    [("Azure Functions（従量課金プラン）",
      "従量課金プランは VNet 統合をサポートしないため、プライベート IP へのアクセスができません。"),
     ("Azure Logic Apps（統合サービス環境）",
      "プライベート ネットワーク アクセスは可能ですが、Premium プランと比較して大幅にコストが高くなります。"),
     ("Azure Functions（Dedicated + Basic）",
      "VNet 統合は可能ですが、Basic App Service プランはオートスケールや最適なパフォーマンスを提供せず、コスト効率が悪いです。"),
     ("Azure Logic Apps（従量課金プラン）",
      "VNet 統合をサポートせず、プライベート IP にアクセスできません。カスタム C# コードの実行にも適していません。")]
)))

# Q11 – Premium block blobs high throughput
QUESTIONS.append(q(9, "q9", *DS,
"高スループット ワークロードを処理するストレージ ソリューションを設計しています。以下の要件を満たす必要があります：\n・毎秒 800 リクエスト以上を処理できること\n・画像・動画・音声ファイルなどの大容量マルチメディア コンテンツを保存・配信すること\n\nデプロイすべき Azure ストレージ アカウントの種類はどれですか？",
[
    ("Premium ファイル共有", False),
    ("Standard General Purpose v2", False),
    ("Premium ブロック BLOB", True),
    ("Premium ページ BLOB", False),
],
[2],
exp(
    [("Premium ブロック BLOB",
      "ブロック BLOB は大規模データ ストレージとストリーミング ワークロード（画像・動画・音声）に最適化されています。Premium パフォーマンスにより高スループットと低レイテンシが保証され、毎秒 800 リクエスト以上に対応できます。")],
    [("Premium ファイル共有",
      "SMB ベースのワークロード向けで、大容量メディア コンテンツのストリーミングには最適化されていません。"),
     ("Standard General Purpose v2",
      "コスト効率は高いですが、Standard パフォーマンスでは低レイテンシや高トランザクション レートを保証できません。"),
     ("Premium ページ BLOB",
      "VM ディスク（VHD）やランダム読み書きアクセスが必要なワークロード向けです。大容量メディアの順次ストリーミングには最適化されていません。")]
)))

# Q12 – Cosmos DB SLA
QUESTIONS.append(q(10, "q10", *DS,
"ミッション クリティカルなアプリケーションのストレージ ソリューションを設計しています。\n\n要件：\n・書き込みレイテンシの SLA を保証すること\n・スループットの SLA を保証すること\n\n推奨ストレージ ソリューションに含めるべきものはどれですか？",
[
    ("Azure SQL", False),
    ("Azure Cosmos DB", True),
    ("Azure Blob Storage", False),
    ("Azure Data Lake Storage Gen2", False),
],
[1],
exp(
    [("Azure Cosmos DB",
      "書き込みレイテンシとスループット両方の SLA を提供します。マルチリージョン レプリケーション設定時に 99.999% の可用性とシングル桁ミリ秒の書き込みを保証します。プロビジョニング済みスループットにより高負荷下でも予測可能なパフォーマンスが得られます。")],
    [("Azure SQL",
      "可用性の SLA は提供しますが、書き込みレイテンシやスループットの SLA は保証されません。"),
     ("Azure Blob Storage",
      "非構造化データ ストレージ向けで、トランザクション ワークロード向けの書き込みレイテンシ・スループット SLA がありません。"),
     ("Azure Data Lake Storage Gen2",
      "ビッグ データ分析に最適化されており、低レイテンシのトランザクション処理向けの SLA がありません。")]
)))

# Q13 – Premium block blobs ZRS immutable
QUESTIONS.append(q(11, "q11", *DS,
"新しいアプリケーション向けのストレージ ソリューションを設計しています。ビジネス クリティカルなデータを保存します。\n\n要件：\n・新しく書き込まれたデータを 1 年間変更不可にする\n・データ回復性を最大化する\n・読み取りレイテンシを最小化する\n\n推奨するストレージ ソリューションの組み合わせはどれですか？",
[
    ("Standard General Purpose v1 ＋ ZRS", False),
    ("Standard General Purpose v1 ＋ LRS", False),
    ("Standard General Purpose v2 ＋ ZRS", False),
    ("Standard General Purpose v2 ＋ LRS", False),
    ("Premium ブロック BLOB ＋ ZRS", True),
    ("Premium ブロック BLOB ＋ LRS", False),
],
[4],
exp(
    [("Premium ブロック BLOB ＋ ZRS",
      "Premium ブロック BLOB は SSD バックアップで最低読み取りレイテンシを実現します。ZRS は複数の可用性ゾーンへの同期レプリケーションにより最高の回復性を提供します。Azure イミュータブル BLOB ストレージ ポリシーで 1 年間の変更不可を設定できます。")],
    [("Standard + ZRS など他の組み合わせ",
      "Standard パフォーマンスでは Premium と比較して読み取りレイテンシが高くなります。LRS はデータ センター障害への耐性が低く、最大回復性の要件を満たしません。")]
)))

# Q14 – ADF continuous transfer
QUESTIONS.append(q(12, "q12", *DS,
"50 台のデバイスが Azure Blob Storage にパフォーマンス メトリックを継続的に書き込んでいます。このデータを Azure SQL Database に継続的に転送・分析する必要があります。\n\n推奨ソリューションに含めるべきものはどれですか？",
[
    ("Azure Data Factory", True),
    ("Data Migration Assistant（DMA）", False),
    ("Azure Data Box", False),
    ("Azure Database Migration Service", False),
],
[0],
exp(
    [("Azure Data Factory",
      "スケーラブルな自動 ETL ソリューションで、Blob Storage から Azure SQL Database への継続的なデータ移動をサポートします。増分データ移動・スケジューリング・データ フローによる変換が可能です。")],
    [("Data Migration Assistant（DMA）",
      "データベースの評価・移行ツールです。継続的なデータ移動や ETL 処理はサポートしません。"),
     ("Azure Data Box",
      "オンプレミスから Azure への大量データ転送用の物理デバイスです。継続的なデータ統合には対応していません。"),
     ("Azure Database Migration Service",
      "データベース全体の移行（1 回限りまたはダウンタイム最小）向けです。Blob Storage からの継続的なデータ取り込みには使用できません。")]
)))

# Q15 – Dynamic data masking (PII)
QUESTIONS.append(q(13, "q13", *DS,
"個人情報（PII）を含む Azure SQL Database をデプロイする予定です。認可されたユーザーのみが機密データを閲覧できるようにする必要があります。\n\nソリューションに含めるべき機能はどれですか？",
[
    ("データ検出と分類", False),
    ("透過的データ暗号化（TDE）", False),
    ("動的データ マスキング（DDM）", True),
    ("ロールベースのアクセス制御（RBAC）", False),
],
[2],
exp(
    [("動的データ マスキング（DDM）",
      "クエリ レベルで機密データをマスクし、非特権ユーザーが PII フィールドの実際の値を見られないようにします。適切な権限を持つユーザーにはマスクされていないデータへのアクセスを許可できます。")],
    [("データ検出と分類",
      "機密データの識別・分類に役立ちますが、PII へのアクセスを制限するものではありません。"),
     ("透過的データ暗号化（TDE）",
      "保存データを暗号化しますが、クエリ実行時にユーザーが機密データを閲覧することを防ぎません。"),
     ("RBAC",
      "データベースまたはテーブル レベルのアクセスを管理しますが、非特権ユーザー向けのデータの動的マスクは提供しません。")]
)))

# Q16 – Encryption scopes (blobs GPv2)
QUESTIONS.append(q(14, "q14", *DS,
"Azure Storage を使用するアプリケーションをデプロイする予定です。以下の要件を満たすストレージ アカウントが必要です：\n・複数ユーザーのデータを保存する\n・各ユーザーのデータを異なる暗号化キーで暗号化する\n・すべての保存データをカスタマー マネージド キー（CMK）で暗号化する\n\nデプロイすべきストレージの組み合わせはどれですか？",
[
    ("Azure Data Lake Storage Gen2 アカウントの BLOB", False),
    ("Premium ファイル共有ストレージ アカウントのファイル", False),
    ("General Purpose v2 ストレージ アカウントの BLOB", True),
    ("General Purpose v2 ストレージ アカウントのファイル", False),
],
[2],
exp(
    [("General Purpose v2 ストレージ アカウントの BLOB",
      "BLOB は Azure Key Vault 統合による CMK 暗号化をサポートし、暗号化スコープにより異なるコンテナーや BLOB に別々のキーを使用できます。ユーザーごとの暗号化とカスタマー マネージド キーの両要件を完全に満たします。")],
    [("Azure Data Lake Storage Gen2 の BLOB",
      "ビッグ データ分析向けに設計されており、アプリケーション ユーザー データの保存には最適ではありません。"),
     ("Premium ファイル共有",
      "ユーザーごとに異なる暗号化キーをサポートしません。ファイル共有全体に対してのみ CMK を使用できます。"),
     ("GPv2 のファイル",
      "Azure Files はユーザーごとの CMK を個別に設定する機能がありません。VM ベースのファイル共有向けに最適化されています。")]
)))

# Q17 – Service Bus
QUESTIONS.append(q(15, "q15", *IS,
"複数の Azure サービスで構成される販売アプリケーションを構築しています。各サービスはトランザクションの異なる部分（注文処理・請求・支払い・在庫管理・配送）を担当します。\n\nサービス間でトランザクション詳細を非同期で交換する必要があり、メッセージは XML 形式を使用します。\n\nこの通信モデルをサポートするために推奨する Azure サービスはどれですか？",
[
    ("Azure Service Fabric", False),
    ("Azure Notification Hubs", False),
    ("Azure Service Bus", True),
    ("Azure Traffic Manager", False),
],
[2],
exp(
    [("Azure Service Bus",
      "分散コンポーネント間の非同期通信のための信頼性の高いメッセージング プラットフォームです。XML などの構造化メッセージ形式をサポートし、注文・請求・在庫・配送などのエンタープライズ シナリオに最適です。")],
    [("Azure Service Fabric",
      "スケーラブルなマイクロサービスの構築・管理プラットフォームで、非同期メッセージング サービスではありません。"),
     ("Azure Notification Hubs",
      "モバイル デバイスへのプッシュ通知に使用します。XML メッセージの交換やバックエンド トランザクション ワークフローには適していません。"),
     ("Azure Traffic Manager",
      "DNS ベースのトラフィック ロード バランサーで、メッセージング機能を提供しません。")]
)))

# Q18-21 merged – Network Watcher / IP flow verify
QUESTIONS.append(q(16, "q16", *IS,
"オンプレミスと Azure で仮想マシンを運用しており、ExpressRoute で接続されています。一部の VM でネットワーク接続の問題が発生しています。VM に到達するパケットが許可されているか遮断されているかを検査する必要があります。\n\n次の提案のうち、要件を満たすものはどれですか？",
[
    ("Azure Network Watcher の Traffic Analytics を使用してネットワーク トラフィックを分析する", False),
    ("Azure Advisor を使用してネットワーク トラフィックを分析する", False),
    ("Azure Monitor エージェントと Dependency Agent をインストールして VM Insights でトラフィックを分析する", False),
    ("Azure Network Watcher の IP フロー確認を使用してトラフィックを分析する", True),
],
[3],
exp(
    [("IP フロー確認（IP flow verify）",
      "Azure Network Watcher の IP フロー確認は、NSG ルールに基づいて VM への特定のトラフィックが許可・拒否されているかを診断するためのツールです。送信元・宛先 IP、ポート、プロトコルを指定してテストでき、個別 VM の接続問題のトラブルシューティングに最適です。")],
    [("Traffic Analytics",
      "NSG フロー ログを基にした高レベルの分析を提供しますが、パケット レベルの可視性や個別 VM の許可・拒否の詳細は得られません。"),
     ("Azure Advisor",
      "コスト・パフォーマンス・可用性・セキュリティのベスト プラクティスを推奨するサービスです。パケット レベルのネットワーク トラフィック分析機能はありません。"),
     ("VM Insights",
      "パフォーマンス監視・依存関係マップを提供しますが、パケット レベルの解析や NSG ルールの許可・拒否の判定はできません。")]
)))

# Q22-25 merged – Stateless web app multi-region
QUESTIONS.append(q(17, "q17", *IS,
"Azure でステートレス Web アプリを実行する環境を設計しています。以下の条件を満たす必要があります：\n・完全な .NET Framework をサポートする\n・単一の Azure リージョンが利用不能になっても動作を継続する\n・管理者がカスタム依存関係をインストールするために OS にアクセスできること\n\n次の提案のうち、すべての要件を満たすものはどれですか？",
[
    ("2 つの Azure リージョンに Azure VM をデプロイし、Azure Application Gateway を使用する", False),
    ("2 つの Azure リージョンに Azure VM をデプロイし、Azure Traffic Manager プロファイルを作成する", True),
    ("自動スケーリングを使用する Azure VM スケール セットをデプロイする", False),
    ("分離 App Service プランに Web アプリをデプロイする", False),
],
[1],
exp(
    [("VM × 2 リージョン ＋ Traffic Manager",
      "2 つのリージョンへの VM デプロイでリージョン冗長性を実現します。VM は OS へのフル アクセスを提供し、完全な .NET Framework と カスタム依存関係のインストールが可能です。Traffic Manager がリージョン間の DNS ベース グローバル ロード バランシングを実現し、フェールオーバーを自動化します。")],
    [("VM × 2 リージョン ＋ Application Gateway",
      "Application Gateway はリージョン サービスであり、複数の Azure リージョンにまたがることができません。リージョン冗長性を実現するには Front Door や Traffic Manager などのグローバル ロード バランサーが必要です。"),
     ("VM スケール セット（自動スケーリング）",
      "単一リージョン内で動作し、それ自体ではリージョン障害に対応できません。複数リージョンのデプロイと Traffic Manager などが別途必要です。"),
     ("分離 App Service プラン",
      "OS へのアクセスを提供せず、カスタム依存関係のインストールができません。また完全な .NET Framework をサポートせず、自動的なリージョン冗長性もありません。")]
)))

# Q26 – Access reviews
QUESTIONS.append(q(18, "q18", *ID,
"ironclad.com という Microsoft Entra テナントに SecGroupA というセキュリティ グループ（割り当て済みメンバーシップ）があります。現在 50 名のユーザー（うち 20 名はゲスト ユーザー）が所属しています。\n\n以下の条件を満たす SecGroupA のメンバーシップ管理方法を推奨してください：\n・レビュー プロセスが 3 ヶ月ごとに自動実行される\n・各メンバーが自分のアクセスが引き続き必要かを確認できる\n・不要と回答したメンバーが自動削除される\n・レビューに応答しないメンバーも自動削除される",
[
    ("Microsoft Entra Identity Protection を有効化する", False),
    ("SecGroupA を動的ユーザー グループに変換する", False),
    ("SecGroupA のアクセス レビューを構成する", True),
    ("Microsoft Entra Privileged Identity Management（PIM）を有効化する", False),
],
[2],
exp(
    [("アクセス レビューの構成",
      "Microsoft Entra アクセス レビューを使用すると、割り当て済みグループのメンバーシップを定期的にレビューできます。3 ヶ月ごとの実行・メンバーによる自己証明・アクセス不要または無応答のユーザーの自動削除を設定できます。4 つの要件をすべて満たします。")],
    [("Microsoft Entra Identity Protection",
      "リスクベースの条件付きアクセスとユーザー リスク検出に使用します。グループ メンバーシップのレビューや証明ワークフローには使用できません。"),
     ("動的ユーザー グループへの変換",
      "動的メンバーシップはルールとユーザー属性に基づくもので、ユーザーの自己証明やアクセス レビューをサポートしません。"),
     ("Privileged Identity Management（PIM）",
      "特権ロールへの Just-In-Time アクセス管理向けです。通常のセキュリティ グループの定期的なメンバーシップ レビューには適していません。")]
)))

# Q27+Q28 merged – Databricks (multi, 2 correct)
QUESTIONS.append(q(19, "q19", *DS,
"機械学習ワークロード向けに Azure Databricks をデプロイする予定です。データ エンジニアが Azure Data Lake Storage アカウントを Databricks ファイル システム（DBFS）にマウントします。ストレージ アカウントのフォルダー レベルの権限は個々のデータ エンジニアに直接割り当てられています。\n\n以下の要件を満たす Databricks の設計にしてください：\n・データ エンジニアが明示的に許可されたストレージ フォルダーにのみアクセスできること\n・開発工数を最小限に抑えること\n・コストを最小限に抑えること\n\nDatabricks の SKU とクラスター構成からそれぞれ 1 つ選んでください（計 2 つ）。",
[
    ("SKU：Standard", False),
    ("SKU：Premium", True),
    ("クラスター構成：Credential passthrough（資格情報パススルー）", True),
    ("クラスター構成：Managed Identities（マネージド ID）", False),
    ("クラスター構成：MLflow", False),
    ("クラスター構成：Photon ランタイム", False),
    ("クラスター構成：Secret Scope（シークレット スコープ）", False),
],
[1, 2],
exp(
    [("SKU：Premium",
      "フォルダー レベルのアクセス制御に必要な Credential passthrough と ACL（アクセス制御リスト）は Databricks Premium SKU でのみ利用できます。ユーザーの Microsoft Entra ID に基づいてストレージ アクセスを適用できます。"),
     ("Credential passthrough",
      "ログイン ユーザーの ID を使用して Azure Data Lake Storage にアクセスします。ストレージ レイヤーでユーザーごとの権限が適用され、カスタム アクセス ロジックの実装なしにフォルダー レベルの制御が実現できます。")],
    [("SKU：Standard",
      "Credential passthrough や細かいアクセス制御機能がないため、ユーザーごとのフォルダー権限を強制するには独自ロジックが必要になり開発工数が増加します。"),
     ("Managed Identities",
      "クラスターまたはワークスペース レベルでアクセスを提供するため、すべてのユーザーが同じ ID を使用します。ユーザーごとのフォルダー権限の強制ができません。"),
     ("MLflow", "実験・モデルの追跡ツールです。ストレージのアクセス制御とは無関係です。"),
     ("Photon ランタイム", "クエリ パフォーマンス向上エンジンです。認証やアクセス制御の機能はありません。"),
     ("Secret Scope", "資格情報や API キーの管理ツールです。フォルダー レベルのアクセス権限を適用する機能はありません。")]
)))

# Q31 – Service Bus topic
QUESTIONS.append(q(20, "q20", *IS,
"SalesApp と ShippingApp を含む Azure サブスクリプションを管理しています。SalesApp は出荷が必要なトランザクションをストレージ キューにメッセージを入れ、ShippingApp がそれを処理しています。\n\n将来的に追加のアプリケーションが導入され、各アプリがトランザクション詳細に基づいて特定の配送リクエストのみを処理します。\n\n各アプリケーションが関連するメッセージのみを独立して受信・処理できるよう、既存のストレージ キューの代替として推奨するものはどれですか？",
[
    ("1 つの Azure Data Factory パイプライン", False),
    ("複数のストレージ アカウント キュー", False),
    ("1 つの Azure Service Bus キュー", False),
    ("1 つの Azure Service Bus トピック", True),
],
[3],
exp(
    [("Azure Service Bus トピック",
      "トピックはパブリッシュ・サブスクライブ パターンをサポートし、複数のアプリが同じメッセージ ストリームを独立してサブスクライブし、フィルターで関連するメッセージのみを受信できます。将来の複数アプリ対応に最適です。")],
    [("Azure Data Factory パイプライン",
      "データ統合・変換ワークフロー向けです。リアルタイム メッセージングやイベント ドリブン通信には適していません。"),
     ("複数のストレージ キュー",
      "各アプリにメッセージを手動で複製する必要があり、管理オーバーヘッドが増大します。ルーティングやフィルタリング機能もありません。"),
     ("Service Bus キュー",
      "1 対 1 のコンシューマー モデルです。1 つのアプリしかメッセージを受信できず、複数アプリが異なる条件で処理する要件に対応できません。")]
)))

# Q32+Q33 merged – Storage accounts AppOne/AppTwo (multi, 2 correct)
QUESTIONS.append(q(21, "q21", *DS,
"以下のストレージ アカウントを持つ Azure サブスクリプションがあります：\n\n・StoreAlpha：StorageV2、Standard パフォーマンス\n・StoreBeta：StorageV2、Premium パフォーマンス\n・StoreGamma：BlobStorage、Standard パフォーマンス\n・StoreDelta：FileStorage、Premium パフォーマンス\n\n2 つのアプリを新規デプロイします：\n・AppOne：データを異なるストレージ アクセス層間で移動するライフサイクル管理ルールが必要\n・AppTwo：Azure ファイル共有にデータを保存する必要がある\n\nAppOne と AppTwo のそれぞれに推奨するストレージ アカウントを 1 つずつ選んでください（計 2 つ）。",
[
    ("AppOne：StoreAlpha（StorageV2 Standard）のみ", False),
    ("AppOne：StoreAlpha と StoreBeta", False),
    ("AppOne：StoreAlpha と StoreGamma（StorageV2 + BlobStorage、いずれも Standard）", True),
    ("AppOne：StoreAlpha、StoreBeta、StoreGamma", False),
    ("AppTwo：StoreDelta（FileStorage Premium）のみ", False),
    ("AppTwo：StoreAlpha と StoreDelta", True),
    ("AppTwo：StoreAlpha、StoreBeta、StoreDelta", False),
],
[2, 5],
exp(
    [("AppOne：StoreAlpha と StoreGamma",
      "ライフサイクル管理は StorageV2（Standard）と BlobStorage（Standard）のみでサポートされます。StoreAlpha は StorageV2 Standard、StoreGamma は BlobStorage Standard のため両方対応。StoreBeta は StorageV2 Premium のためライフサイクル管理非対応。StoreDelta は FileStorage のため対象外。"),
     ("AppTwo：StoreAlpha と StoreDelta",
      "Azure ファイル共有は StorageV2（Standard）とFileStorage（Premium）でサポートされます。StoreAlpha（StorageV2 Standard）は標準 Azure Files をサポート。StoreDelta（FileStorage Premium）は高パフォーマンスの Premium Azure Files をサポート。StoreBeta（StorageV2 Premium）はファイル共有非対応。StoreGamma（BlobStorage）はファイル共有をサポートしません。")],
    [("その他の選択肢",
      "StoreBeta（StorageV2 Premium）はライフサイクル管理も Standard Files もサポートしません。StoreGamma（BlobStorage）はファイル共有をサポートしません。")]
)))

# Q34 – Blob Storage for video
QUESTIONS.append(q(22, "q22", *DS,
"50 MB から 15 GB のビデオ コンテンツを保存するアプリケーションをデプロイします。インターネット経由でアクセスし、証明書ベースの認証を使用します。\n\n要件：\n・最速の読み取りパフォーマンスを提供する\n・ストレージ コストを最小限に抑える\n\n選択すべきストレージ ソリューションはどれですか？",
[
    ("Azure Files", False),
    ("Azure Data Lake Storage Gen2", False),
    ("Azure Blob Storage", True),
    ("Azure SQL Database", False),
],
[2],
exp(
    [("Azure Blob Storage",
      "大容量の非構造化データ（ビデオ ファイルなど）の保存に最適化されており、ホット アクセス層・CDN 統合・高スケーラビリティで高速な読み取りパフォーマンスを実現します。HTTPS によるパブリック アクセスと SAS による証明書ベース認証をサポートし、アクセス層（ホット・クール・アーカイブ）でコストを最小化できます。")],
    [("Azure Files",
      "エンタープライズ アプリ向けのマネージド SMB/NFS ファイル共有サービスで、大規模インターネット向けコンテンツ配信には適していません。"),
     ("Azure Data Lake Storage Gen2",
      "ビッグ データ分析ワークロード向けです。ビデオ ストリーミングのパフォーマンス最適化は Blob Storage には劣ります。"),
     ("Azure SQL Database",
      "50 MB〜15 GB の大容量非構造化ファイルの保存には適しておらず、パフォーマンスとコストの両面で非効率です。")]
)))

# Q35+Q36 merged – Azure SQL DB Hyperscale (multi, 2 correct)
QUESTIONS.append(q(23, "q23", *DS,
"オンプレミスのデータベースを Azure に移行します。以下の要件を満たすデータベース プラットフォームを設計してください：\n・必要に応じてスケールアップ・スケールダウンできること\n・地理的にレプリケートされたバックアップを提供すること\n・最大 75 TB のデータベース サイズをサポートすること\n・オンライン トランザクション処理（OLTP）ワークロードに適していること\n\n最適な Azure サービスとサービス レベルをそれぞれ 1 つ選んでください（計 2 つ）。",
[
    ("Azure SQL Database", True),
    ("Azure SQL Managed Instance", False),
    ("Azure Synapse Analytics", False),
    ("Azure VM 上の SQL Server", False),
    ("サービス レベル：Hyperscale", True),
    ("サービス レベル：Business Critical", False),
    ("サービス レベル：General Purpose", False),
    ("サービス レベル：Standard", False),
],
[0, 4],
exp(
    [("Azure SQL Database",
      "動的スケーリング・組み込みの geo 冗長バックアップ・OLTP 最適化を提供するフル マネージド PaaS サービスです。Hyperscale レベルと組み合わせることで 75 TB 以上をサポートできます。"),
     ("サービス レベル：Hyperscale",
      "Azure SQL Database で唯一 100 TB までサポートする層です（75 TB の要件を満たします）。迅速な自動拡張スケーリング・geo 冗長バックアップ・高パフォーマンス OLTP をサポートします。")],
    [("Azure SQL Managed Instance",
      "最大データベース サイズが 16 TB に制限されており、75 TB の要件を満たしません。"),
     ("Azure Synapse Analytics",
      "OLAP（分析処理）向けに最適化されており、高スループットのトランザクション ワークロードには適していません。"),
     ("Azure VM 上の SQL Server",
      "大容量はサポートしますが、geo レプリケーションは組み込みではなく、カスタム構成が必要で管理オーバーヘッドが増大します。"),
     ("Business Critical / General Purpose / Standard",
      "これらのサービス レベルは 75 TB のデータベース サイズをサポートしません。")]
)))

# Q37 – Cosmos DB for NoSQL multi-write
QUESTIONS.append(q(24, "q24", *DS,
"中央のデータ ストアからユーザーにコンテンツを収集・提供するアプリケーションを構築しています。以下の要件を満たすデータベース プラットフォームを選択してください：\n・SQL ベースのクエリでデータにアクセスできること\n・複数のリージョンから同時に書き込み操作をサポートすること\n・読み取り操作の一貫した低レイテンシを保証すること\n\n推奨するデータベース ソリューションはどれですか？",
[
    ("Azure Cosmos DB for NoSQL", True),
    ("アクティブ geo レプリケーションを使用した Azure SQL Database", False),
    ("Azure SQL Database Hyperscale", False),
    ("Azure Cosmos DB for PostgreSQL", False),
],
[0],
exp(
    [("Azure Cosmos DB for NoSQL",
      "SQL API による SQL クエリ・マルチ マスター書き込み（複数リージョンへの同時書き込み）・シングル桁ミリ秒の低レイテンシ読み取りをすべて提供します。グローバル分散アプリケーションに最適です。")],
    [("アクティブ geo レプリケーションの Azure SQL Database",
      "読み取り専用レプリカのみをサポートし、マルチ マスター書き込みはできません。書き込みはプライマリ データベースに向ける必要があります。"),
     ("Azure SQL Database Hyperscale",
      "高スケーラビリティと高パフォーマンスを提供しますが、マルチ マスター書き込みやグローバルな低レイテンシ読み取りはサポートしません。"),
     ("Azure Cosmos DB for PostgreSQL",
      "複数リージョンへの書き込みはサポートしますが、NoSQL ベースのアプリケーション向けの SQL API や JSON ドキュメント ストアの柔軟性がありません。")]
)))

# Q38 – Azure Site Recovery (DR for SQL on VM)
QUESTIONS.append(q(25, "q25", *BC,
"Azure VM 上の SQL Server があり、データベースは毎晩のスケジュール バッチ ジョブで書き込まれます。以下の要件を満たすデータベースの災害復旧アプローチを選択してください：\n・Azure リージョン全体が利用不能になった場合に復旧できること\n・15 分の RTO（目標復旧時間）をサポートすること\n・24 時間の RPO（目標復旧地点）をサポートすること\n・手動操作なしで自動的に復旧すること\n・コストを最小限に抑えること\n\n推奨に含めるべきものはどれですか？",
[
    ("Azure VM 可用性セット", False),
    ("Azure ディスク バックアップ", False),
    ("Always On 可用性グループ", False),
    ("Azure Site Recovery", True),
],
[3],
exp(
    [("Azure Site Recovery",
      "リージョン障害時の Azure VM（SQL Server を含む）の災害復旧を提供します。自動復旧をサポートし 15 分の RTO 要件を満たし、スケジュール レプリケーションで 24 時間の RPO を実現します。Always On 可用性グループよりコストを低く抑えられます。")],
    [("Azure VM 可用性セット",
      "単一リージョン内のハードウェア障害に対する高可用性を提供しますが、リージョン全体の障害には対応できません。"),
     ("Azure ディスク バックアップ",
      "スナップショット ベースの保護ですが、自動復旧をサポートせず、15 分の RTO 要件を満たすことが困難です。"),
     ("Always On 可用性グループ",
      "低い RTO/RPO を実現しますが、SQL Server Enterprise エディションが必要で費用が高く、コスト最小化の要件に反します。")]
)))

# Q39+Q40 merged – Premium file shares + ZRS (multi, 2 correct)
QUESTIONS.append(q(26, "q26", *DS,
"Azure Storage アカウントをデプロイしてファイル共有をホストします。ファイル共有にはトランザクション集約型のオンプレミス アプリケーションがアクセスします。\n\n要件：\n・ファイル共有へのアクセス レイテンシを最小化すること\n・選択したストレージ層で利用可能な最高レベルの回復性を提供すること\n\nストレージ層と冗長性オプションをそれぞれ 1 つ選んでください（計 2 つ）。",
[
    ("ストレージ層：Hot", False),
    ("ストレージ層：Premium", True),
    ("ストレージ層：トランザクション最適化", False),
    ("冗長性：Geo 冗長ストレージ（GRS）", False),
    ("冗長性：ゾーン冗長ストレージ（ZRS）", True),
    ("冗長性：ローカル冗長ストレージ（LRS）", False),
],
[1, 4],
exp(
    [("Premium ストレージ層",
      "SSD バックアップで最低レイテンシと最高 IOPS を提供します。トランザクション集約型ワークロードのオンプレミス アプリに最適です。ZRS をサポートするため最高レベルの回復性も実現できます。"),
     ("ゾーン冗長ストレージ（ZRS）",
      "リージョン内の 3 つの可用性ゾーンにデータを同期レプリケーションし、データ センター レベルの障害から保護します。Premium Azure Files での最高回復性オプションです。")],
    [("Hot",
      "BLOB ストレージ向けのアクセス層で、Azure Files には適用されません。"),
     ("トランザクション最適化",
      "ファイル共有には使用できますが、Premium と比較してパフォーマンスが低く、ZRS をサポートしないため回復性も劣ります。"),
     ("GRS",
      "クロスリージョン レプリケーションはディザスター リカバリー向けで、アクティブなトランザクション アクセスには高レイテンシになります。"),
     ("LRS",
      "単一データ センター内のみのレプリケーションで、最低レベルの回復性しか提供しません。")]
)))

# Q41 – OAuth token generation (SaaS)
QUESTIONS.append(q(27, "q27", *ID,
"Microsoft Entra ID ユーザーがオンライン アンケートを作成・公開できる SaaS ソリューションを設計しています。フロントエンド Web アプリとバックエンド Web API で構成されています。\n\n要件：\n・Web アプリが OAuth 2.0 ベアラー トークンを使用してバックエンド API を呼び出すこと\n・Web アプリがアプリケーション専用 ID ではなく、サインイン ユーザーの個別 ID を使用して認証すること\n\n「アクセス トークンは _____ によって生成される」に当てはまるものを選んでください。（設問 1/2）",
[
    ("Microsoft Entra", True),
    ("Web アプリ", False),
    ("Web API", False),
    ("Azure Site Recovery", False),
],
[0],
exp(
    [("Microsoft Entra",
      "OAuth 2.0 フローでは Microsoft Entra ID（認可サーバー）がアクセス トークンを発行します。Web アプリはサインイン ユーザーの代わりに Entra ID に認証し、取得したベアラー トークンを API 呼び出しに使用します。")],
    [("Web アプリ",
      "Web アプリは OAuth 2.0 フローのクライアントとして機能し、トークンを要求しますが発行しません。"),
     ("Web API",
      "Web API はリソース サーバーとして機能し、トークンを検証しますが生成しません。"),
     ("Azure Site Recovery",
      "ディザスター リカバリー サービスであり、OAuth 認証とは無関係です。")]
)))

# Q42 – OAuth authorization decision
QUESTIONS.append(q(28, "q28", *ID,
"Microsoft Entra ID ユーザーがオンライン アンケートを作成・公開できる SaaS ソリューションを設計しています。フロントエンド Web アプリとバックエンド Web API で構成されています。\n\n要件：\n・Web アプリが OAuth 2.0 ベアラー トークンを使用してバックエンド API を呼び出すこと\n・Web アプリがアプリケーション専用 ID ではなく、サインイン ユーザーの個別 ID を使用して認証すること\n\n「認可の決定は _____ によって行われる」に当てはまるものを選んでください。（設問 2/2）",
[
    ("Microsoft Entra", False),
    ("Web アプリ", False),
    ("Web API", True),
],
[2],
exp(
    [("Web API",
      "OAuth 2.0 アーキテクチャでは、リソース サーバー（Web API）が認可の決定を行います。Web アプリから送信されたトークンを検証し、クレーム（ロール・スコープ・ユーザー ID）を検査して、内部ロジックに基づいてアクセスを許可・拒否します。")],
    [("Microsoft Entra",
      "Entra ID は ID プロバイダーおよびトークン発行者です。リソース レベルの認可決定は行わず、認証とコンセントに基づいてトークンを発行するのみです。"),
     ("Web アプリ",
      "ユーザーを認証し UI レベルのアクセス制御を行いますが、バックエンド API リソースへのアクセス制御は Web API の責任です。")]
)))

# Q43 – SAS for temporary access
QUESTIONS.append(q(29, "q29", *DS,
"複数の BLOB を持つ BLOB コンテナーを含む Azure サブスクリプションを管理しています。\n\nHR 部門の 15 名のユーザーが 9 月の 1 ヶ月間のみ BLOB にアクセスする必要があります。9 月以外のアクセスを自動的に防ぐセキュリティ アプローチを推奨してください。",
[
    ("条件付きアクセス ポリシー", False),
    ("Shared Access Signature（SAS）", True),
    ("アクセス キー", False),
    ("証明書", False),
],
[1],
exp(
    [("Shared Access Signature（SAS）",
      "特定の期間（9 月）に限定したアクセスを Azure Blob Storage リソースに付与できます。権限（読み取り・書き込みなど）・スコープ（コンテナーや BLOB）・有効期限を設定でき、ストレージ アカウント キーを共有せずに安全で柔軟な一時アクセスを実現します。")],
    [("条件付きアクセス ポリシー",
      "Microsoft Entra ID のサインイン条件に適用されるもので、Azure Storage の時間限定アクセス制御には使用できません。"),
     ("アクセス キー",
      "ストレージ アカウントへのフル アクセスを許可します。きめ細かいまたは時間限定のアクセスは提供せず、共有は推奨されません。"),
     ("証明書",
      "アプリや API のクライアント認証に使用されます。Azure Storage リソースへの一時的なアクセス制御には適していません。")]
)))

# Q44 – ADLS immutable + ACL
QUESTIONS.append(q(30, "q30", *DS,
"Azure Storage アカウントにデータ資産を保存する予定です。以下の要件を満たすストレージ ソリューションを選択してください：\n・書き込まれたデータを変更不可にすること\n・ストレージ アカウントへの匿名アクセスを禁止すること\n・Microsoft Entra と連携した ACL（アクセス制御リスト）ベースの権限をサポートすること",
[
    ("Azure Blob Storage", False),
    ("Azure Data Lake Storage", True),
    ("Azure NetApp Files", False),
    ("Azure Files", False),
],
[1],
exp(
    [("Azure Data Lake Storage",
      "イミュータブル ストレージ（ソフト削除・WORM ポリシー）で書き込み後の変更を防ぎます。デフォルトで匿名アクセスを禁止し、ディレクトリ・ファイル レベルの細かい ACL による Microsoft Entra 権限管理をサポートします。3 つの要件すべてを満たします。")],
    [("Azure Blob Storage",
      "イミュータビリティはサポートしますが、Microsoft Entra ベースの細かい ACL 権限は Azure RBAC に依存し、ADLS のようなきめ細かな制御はできません。"),
     ("Azure NetApp Files",
      "高パフォーマンスのエンタープライズ ファイル ストレージです。Microsoft Entra ACL の完全サポートが限定的で、データ資産の要件に最適ではありません。"),
     ("Azure Files",
      "汎用ファイル共有サービスです。ADLS と比較してイミュータブル ストレージが限定的で、Microsoft Entra ACL のきめ細かな制御も劣ります。")]
)))

# Q45+Q46 merged – MARS agent + LRS (multi, 2 correct)
QUESTIONS.append(q(31, "q31", *BC,
"Windows Server を実行する 20 台のオンプレミス サーバーのデータを Azure にバックアップして保護します。\n\n要件：\n・各サーバーのすべてのファイルとディレクトリをキャプチャすること\n・Azure 内にバックアップ データの 3 つのレプリカ コピーを保持すること\n・バックアップ コストを全体的に最小限に抑えること\n\nサーバーに構成するバックアップ コンポーネントとストレージ構成をそれぞれ 1 つ選んでください（計 2 つ）。",
[
    ("Azure Site Recovery Mobility Service", False),
    ("Microsoft Azure Recovery Services（MARS）エージェント", True),
    ("ボリューム シャドウ コピー サービス（VSS）", False),
    ("Geo 冗長ストレージ（GRS）", False),
    ("ローカル冗長ストレージ（LRS）", True),
    ("ゾーン冗長ストレージ（ZRS）", False),
],
[1, 4],
exp(
    [("MARS エージェント",
      "オンプレミス Windows サーバーのすべてのファイル・フォルダー・システム ステートを Azure Recovery Services コンテナーに安全にバックアップします。日次バックアップのスケジュール設定と複数コピーの保持をサポートし、コスト効率が高いです。"),
     ("ローカル冗長ストレージ（LRS）",
      "同一データ センター内に 3 つのコピーを保持するため「3 つのレプリカ コピー」の要件を満たします。GRS や ZRS と比較して最もコストが低く、バックアップ コスト最小化の要件に合致します。")],
    [("Azure Site Recovery Mobility Service",
      "VM・物理サーバーのディザスター リカバリーと移行向けです。日常的なファイル・フォルダーのバックアップには適していません。"),
     ("VSS",
      "Windows のスナップショット機能ですが、Azure へのバックアップの自動化・統合・コスト効率は MARS エージェントに劣ります。"),
     ("GRS",
      "クロスリージョン レプリケーションにより高い耐久性を提供しますが、コストが大幅に高くなります。コスト最小化の要件に反します。"),
     ("ZRS",
      "複数の可用性ゾーンにレプリケーションして高可用性を提供しますが、LRS よりコストが高くなります。")]
)))

# Q47+Q48 merged – User delegation SAS + Entra credentials (multi, 2 correct)
QUESTIONS.append(q(32, "q32", *DS,
"1 つのサブスクリプション内の複数の Azure Storage アカウントに対するアクセス認可アプローチを設計しています。\n\n構成：\n・ブロック BLOB を保存する 5 つのストレージ アカウント\n・SMB プロトコルでアクセスするファイル共有をホストする 5 つのストレージ アカウント\n\n要件：\n・可能な限り最高レベルのセキュリティを提供すること\n・共有アクセス キーを禁止すること\n・可能な限り時間制限付きアクセスをサポートすること\n\nブロック BLOB アクセスとファイル共有アクセスそれぞれに推奨するソリューションを 1 つずつ選んでください（計 2 つ）。",
[
    ("BLOB：SAS と保存済みアクセス ポリシーの組み合わせ", False),
    ("BLOB：ユーザー委任 SAS（User delegation SAS）のみ", True),
    ("BLOB：ユーザー委任 SAS と保存済みアクセス ポリシーの組み合わせ", False),
    ("ファイル共有：Microsoft Entra 資格情報", True),
    ("ファイル共有：ユーザー委任 SAS のみ", False),
    ("ファイル共有：ユーザー委任 SAS と保存済みアクセス ポリシーの組み合わせ", False),
],
[1, 3],
exp(
    [("BLOB：ユーザー委任 SAS のみ",
      "Microsoft Entra ID でサポートされ共有キーを使用しません。時間制限付きアクセスを提供し、最高レベルのセキュリティ要件を満たします。なお、保存済みアクセス ポリシーはユーザー委任 SAS でサポートされないため、組み合わせは不適切です。"),
     ("ファイル共有：Microsoft Entra 資格情報",
      "Microsoft Entra ID による ID ベースのセキュリティで共有キーを使用しません。MFA や条件付きアクセスと組み合わせることで最高レベルのセキュリティを実現します。なお、Azure Files に対してユーザー委任 SAS は使用できません。")],
    [("SAS と保存済みアクセス ポリシーの組み合わせ",
      "共有キーを使用する可能性があり、最高セキュリティの要件に反します。"),
     ("ユーザー委任 SAS と保存済みアクセス ポリシーの組み合わせ",
      "保存済みアクセス ポリシーはユーザー委任 SAS ではサポートされません。"),
     ("ファイル共有：ユーザー委任 SAS",
      "ユーザー委任 SAS は Azure Files ではサポートされていません。ID ベースのセキュリティも提供しません。")]
)))

# Q49 – Dedicated SQL pool (hash-distributed tables)
QUESTIONS.append(q(33, "q33", *DS,
"Azure Synapse Analytics と Azure Data Lake Storage Gen2 を使用するデータ分析ソリューションを設計しています。\n\n以下の要件を満たす Synapse プールを選択してください：\n「Azure Data Lake Storage からハッシュ分散テーブルにデータをロードする」\n\n（設問 1/2）",
[
    ("専用 SQL プール（Dedicated SQL pool）", True),
    ("サーバーレス Apache Spark プール", False),
    ("サーバーレス SQL プール", False),
],
[0],
exp(
    [("専用 SQL プール",
      "旧称 SQL Data Warehouse で、大規模なデータ ウェアハウス・分析タスク向けに設計されています。ハッシュ分散テーブルによりデータを複数ノードに分散し、結合・集計クエリのパフォーマンスを向上させます。データの取り込みと保存を直接サポートします。")],
    [("サーバーレス Apache Spark プール",
      "オンデマンドのデータ処理・分析向けです。ハッシュ分散テーブルへの直接取り込みには設計されていません。"),
     ("サーバーレス SQL プール",
      "Azure Data Lake のデータをクエリするためのツールですが、データの取り込みや永続的なテーブルへの書き込みはサポートしません。")]
)))

# Q50 – Serverless Spark (Delta Lake)
QUESTIONS.append(q(34, "q34", *DS,
"Azure Synapse Analytics と Azure Data Lake Storage Gen2 を使用するデータ分析ソリューションを設計しています。\n\n以下の要件を満たす Synapse プールを選択してください：\n「Delta Lake のデータを実装・クエリ・更新する」\n\n（設問 2/2）",
[
    ("専用 SQL プール（Dedicated SQL pool）", False),
    ("サーバーレス Apache Spark プール", True),
    ("サーバーレス SQL プール", False),
],
[1],
exp(
    [("サーバーレス Apache Spark プール",
      "Delta Lake のデータの実装・クエリ・更新をすべてサポートします。Scala・PySpark・.NET を使用して Delta Lake ファイルをシームレスに操作でき、ACID トランザクションもサポートします。")],
    [("専用 SQL プール",
      "分析クエリには優れていますが、Delta Lake のデータを直接更新・変更するシナリオには最適ではありません。"),
     ("サーバーレス SQL プール",
      "Delta Lake 形式のファイルをクエリできますが、データの更新はサポートしません。")]
)))

# Q51 – Always Encrypted (SSN column)
QUESTIONS.append(q(35, "q35", *DS,
"Azure SQL Managed Instance に従業員レコードが含まれています。社会保障番号（SSN）と電話番号などの機密フィールドがあります。\n\n要件：\n・ヘルプデスク チームが従業員の電話番号の下 4 桁のみを閲覧できること\n・クラウド管理者が従業員の社会保障番号を閲覧できないこと\n\n社会保障番号の列に対して有効にすべき機能はどれですか？（設問 1/2）",
[
    ("Always Encrypted（常に暗号化）", True),
    ("列の暗号化（Column encryption）", False),
    ("動的データ マスキング（DDM）", False),
    ("透過的データ暗号化（TDE）", False),
],
[0],
exp(
    [("Always Encrypted",
      "クライアント アプリケーションが暗号化・復号を処理し、データベース エンジンは暗号化されたデータのみを扱います。クラウド管理者がデータベースにアクセスしても、アプリが管理するキーなしでは SSN を平文で閲覧できません。列レベルの暗号化で最高レベルの保護を提供します。")],
    [("列の暗号化",
      "特定列を暗号化できますが、クラウド管理者からの閲覧制限に必要な細粒度はなく、Always Encrypted のようなアプリ レベルのキー管理がありません。"),
     ("動的データ マスキング（DDM）",
      "データのマスク表示は提供しますが、保存中のデータの実際の暗号化は行いません。権限を持つ管理者はマスク解除してデータを閲覧できるため、クラウド管理者からの完全な保護には不十分です。"),
     ("TDE",
      "ページ レベルでデータベース全体を暗号化しますが、特定の列の暗号化や管理者からの特定フィールドの非表示化はできません。")]
)))

# Q52 – Dynamic data masking (phone column)
QUESTIONS.append(q(36, "q36", *DS,
"Azure SQL Managed Instance に従業員レコードが含まれています。社会保障番号（SSN）と電話番号などの機密フィールドがあります。\n\n要件：\n・ヘルプデスク チームが従業員の電話番号の下 4 桁のみを閲覧できること\n・クラウド管理者が従業員の社会保障番号を閲覧できないこと\n\n電話番号の列に対して有効にすべき機能はどれですか？（設問 2/2）",
[
    ("Always Encrypted（常に暗号化）", False),
    ("列の暗号化（Column encryption）", False),
    ("動的データ マスキング（DDM）", True),
    ("透過的データ暗号化（TDE）", False),
],
[2],
exp(
    [("動的データ マスキング（DDM）",
      "機密データを非特権ユーザーに対してマスクするように設計されています。電話番号の下 4 桁のみを表示するなど、列の一部のみを表示するルールを設定できます。アプリケーションの変更は不要で、SQL Database レイヤーでマスク ルールが適用されます。")],
    [("Always Encrypted",
      "保存中・転送中のデータを暗号化しますが、電話番号の下 4 桁のみを表示するような部分的なデータ開示の機能はありません。"),
     ("列の暗号化",
      "列全体を暗号化しますが、DDM のような部分的なデータ表示はできません。"),
     ("TDE",
      "データベース全体の保存データ暗号化です。特定フィールドの部分的な表示制御には使用できません。")]
)))

# Q53+Q54 merged – Client credentials + IMDS (multi, 2 correct)
QUESTIONS.append(q(37, "q37", *ID,
"Azure Key Vault（KV1）と Windows Server 2022 Azure Edition VM（VM1）を含む Azure サブスクリプションで作業しています。\n\nVM1 に ASP.NET Core アプリ（App1）をデプロイする予定です。App1 はシステム割り当てマネージド ID を使用して KV1 のシークレットにアクセスし、カスタム開発をできるだけ少なくする必要があります。\n\nApp1 の OAuth 2.0 認証フローとトークン取得方法について、それぞれ 1 つ選んでください（計 2 つ）。",
[
    ("OAuth 2.0 フロー：認可コード付与フロー", False),
    ("OAuth 2.0 フロー：クライアント資格情報付与フロー", True),
    ("OAuth 2.0 フロー：暗黙的付与フロー", False),
    ("トークン取得元：Azure Instance Metadata Service（IMDS）エンドポイント", True),
    ("トークン取得元：Microsoft Entra の OAuth 2.0 アクセス トークン エンドポイント", False),
    ("トークン取得元：Microsoft Identity Platform の OAuth 2.0 アクセス トークン エンドポイント", False),
],
[1, 3],
exp(
    [("クライアント資格情報付与フロー",
      "VM1 のシステム割り当てマネージド ID を使用して Azure Key Vault に安全にアクセスできます。ユーザー インタラクションが不要なマシン間通信に適した OAuth 2.0 フローです。マネージド ID が認証を処理するため、コードに資格情報を明示的に記述する必要がありません。"),
     ("Azure Instance Metadata Service（IMDS）エンドポイント",
      "Azure VM の非ルーティング IP（169.254.169.254）でアクセス可能な RESTful エンドポイントです。VM のマネージド ID を使用して認証トークンを取得できます。App1 はこのエンドポイントにアクセスして KV1 へのアクセス トークンを取得します。カスタム開発が最小限で済みます。")],
    [("認可コード付与フロー",
      "ユーザー インタラクションが必要なシナリオ（Web アプリなど）向けです。システム割り当てマネージド ID のマシン間認証には適していません。"),
     ("暗黙的付与フロー",
      "ブラウザー ベースのクライアント サイド アプリ向けです。VM 上で動作する App1 には不適切で、セキュリティ リスクがあります。"),
     ("Microsoft Entra アクセス トークン エンドポイント",
      "サービス プリンシパルや証明書を使用したユーザー認証・サービス認証向けです。マネージド ID の使用で余分な開発作業が増え、要件の「最小開発」に反します。"),
     ("Microsoft Identity Platform アクセス トークン エンドポイント",
      "主にユーザー中心のシナリオや人間と機械の認証向けです。マネージド ID を持つ VM のマシン間認証には最適ではありません。")]
)))

# Q55 – Entra enterprise apps + Conditional Access for SAML SSO
QUESTIONS.append(q(38, "q38", *ID,
"オンプレミスの Active Directory と同期された Microsoft Entra テナントを管理しています。組織は内部開発の基幹業務アプリを使用しています。\n\n以下の要件を満たす認証ソリューションを設計してください：\n・アプリケーションの SAML ベースのシングルサインオン（SSO）を有効にすること\n・ユーザーが不明または不慣れな場所からサインインする場合に多要素認証（MFA）を要求すること\n\nソリューションに含めるべき 2 つの Microsoft Entra 機能はどれですか？",
[
    ("Microsoft Entra エンタープライズ アプリケーション", True),
    ("Azure Application Gateway", False),
    ("Microsoft Entra Privileged Identity Management（PIM）", False),
    ("Microsoft Entra ID Protection", False),
    ("条件付きアクセス ポリシー", True),
],
[0, 4],
exp(
    [("Microsoft Entra エンタープライズ アプリケーション",
      "SAML ベースの SSO を有効にするためのフレームワークを提供します。基幹業務アプリをエンタープライズ アプリとして統合することで、SAML SSO の構成とユーザー アクセス管理が可能になります。"),
     ("条件付きアクセス ポリシー",
      "不明な場所からのアクセス試行など特定の条件に基づいて MFA を強制できます。ユーザーの場所・デバイスのコンプライアンス・リスク レベルなどのシグナルを評価してアクセス制御を適用します。")],
    [("Azure Application Gateway",
      "L7 ロード バランサーです。SAML SSO の提供や MFA の強制は行いません。"),
     ("Microsoft Entra PIM",
      "特権ロールへの Just-In-Time アクセス管理向けです。SAML SSO の有効化や場所ベースの MFA 強制には使用しません。"),
     ("Microsoft Entra ID Protection",
      "リスクのあるサインインの検出・緩和に使用します。直接 SAML SSO を構成したり、場所に基づく MFA を強制したりするものではありません。条件付きアクセス ポリシーの方が適切です。")]
)))

# ── Count domains ──────────────────────────────────────────────────────────────
from collections import Counter
domain_counts = Counter(q["domain"] for q in QUESTIONS)
TOTAL = len(QUESTIONS)

# ── Build HTML ─────────────────────────────────────────────────────────────────
QUESTIONS_JSON = json.dumps(QUESTIONS, ensure_ascii=False, separators=(',', ':'))

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>AZ-305 練習問題集 Vol.6 – 詳細解説版</title>
<link rel="stylesheet" href="az305.css">
<style>
/* ===== VOL JUMP NAV ===== */
.vol-jump-nav {{
  background: #1a2640;
  display: flex;
  align-items: center;
  gap: 0;
  padding: 0 16px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  overflow-x: auto;
  -ms-overflow-style: none;
  scrollbar-width: none;
}}
.vol-jump-nav::-webkit-scrollbar {{ display: none; }}
.vj-link {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.72rem;
  font-weight: 600;
  color: rgba(255,255,255,0.45);
  text-decoration: none;
  padding: 7px 10px;
  border-bottom: 2px solid transparent;
  transition: color 0.15s, border-color 0.15s;
  white-space: nowrap;
  letter-spacing: 0.3px;
  display: flex;
  align-items: center;
  gap: 4px;
}}
.vj-link:hover {{ color: rgba(255,255,255,0.8); }}
.vj-link.vj-active {{
  color: #50e6ff;
  border-bottom-color: #50e6ff;
}}
.vj-home {{ padding: 7px 12px 7px 4px; }}
.vj-review {{
  margin-left: auto;
  color: rgba(255,200,0,0.7);
}}
.vj-review:hover {{ color: rgba(255,200,0,1); }}
.vj-badge {{
  background: rgba(255,200,0,0.2);
  color: rgba(255,200,0,0.9);
  border-radius: 10px;
  font-size: 0.6rem;
  font-weight: 700;
  padding: 1px 5px;
  min-width: 16px;
  text-align: center;
}}
/* ===== REVIEW BUTTON ===== */
.review-btn {{
  margin-left: auto;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  color: rgba(0,0,0,0.2);
  padding: 2px 6px;
  border-radius: 4px;
  transition: color 0.15s, background 0.15s;
  line-height: 1;
}}
.review-btn:hover {{ color: #f0c000; background: rgba(240,192,0,0.1); }}
.review-btn.review-active {{ color: #f0c000; }}
/* ===== ARCH DIAGRAM REVEAL ===== */
.arch-hidden {{ position: relative; }}
.arch-hidden > svg, .arch-hidden > div:not(.arch-reveal-overlay) {{ opacity: 0.04; pointer-events: none; filter: blur(4px); transition: opacity 0.4s, filter 0.4s; }}
.arch-reveal-overlay {{
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  background: rgba(240,242,248,0.85);
  border-radius: 8px;
  border: 1.5px dashed #c0c8d8;
}}
.arch-reveal-hint {{
  font-size: 0.75rem;
  color: #7c879c;
  font-weight: 500;
  padding: 8px 16px;
  background: rgba(255,255,255,0.9);
  border-radius: 6px;
  border: 1px solid #dde1ec;
}}
.arch-hidden.arch-revealed > svg, .arch-hidden.arch-revealed > div:not(.arch-reveal-overlay) {{ opacity: 1; filter: none; pointer-events: auto; }}
.arch-hidden.arch-revealed .arch-reveal-overlay {{ display: none; }}
</style>
</head>
<body>
<div id="studydeck-nav" class="studydeck-nav">
  <a href="../"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>StudyDeck</a>
  <span class="nav-sep">/</span>
  <span class="nav-current">AZ-305</span>
</div>

<div class="hdr">
  <div class="hdr-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
  <div>
    <div class="hdr-title">AZ-305 日本語問題集 Vol.6</div>
    <div class="hdr-sub">Azure Solutions Architect Expert – 日本語版・全{TOTAL}問</div>
  </div>
  <div class="hdr-stat">
    <strong id="hdrScore">0/{TOTAL}</strong>
    <span id="hdrPct">正解率 --％</span>
  </div>
</div>
<nav class="vol-jump-nav">
  <a href="index.html" class="vj-link vj-home" title="ホームへ">
    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
  </a>
  <a href="vol1.html" class="vj-link" id="vj1">Vol.1</a>
  <a href="vol2.html" class="vj-link" id="vj2">Vol.2</a>
  <a href="vol3.html" class="vj-link" id="vj3">Vol.3</a>
  <a href="vol4.html" class="vj-link" id="vj4">Vol.4</a>
  <a href="vol5.html" class="vj-link" id="vj5">Vol.5</a>
  <a href="vol6.html" class="vj-link" id="vj6">Vol.6</a>
  <a href="review.html" class="vj-link vj-review" id="vj-review">
    ★ 復習 <span id="vj-review-count" class="vj-badge"></span>
  </a>
</nav>

<div class="cbar">
  <span class="cbar-label">ドメイン</span>
  <button class="dbtn on" data-d="all" onclick="filterDomain('all')">全問題 ({TOTAL})</button>
  <button class="dbtn" data-d="ID・ガバナンス" onclick="filterDomain('ID・ガバナンス')">ID・ガバナンス ({domain_counts.get('ID・ガバナンス', 0)})</button>
  <button class="dbtn" data-d="インフラ設計" onclick="filterDomain('インフラ設計')">インフラ ({domain_counts.get('インフラ設計', 0)})</button>
  <button class="dbtn" data-d="データストレージ" onclick="filterDomain('データストレージ')">データストレージ ({domain_counts.get('データストレージ', 0)})</button>
  <button class="dbtn" data-d="ビジネス継続性" onclick="filterDomain('ビジネス継続性')">継続性 ({domain_counts.get('ビジネス継続性', 0)})</button>
  <div class="cbar-right">
    <label class="shuf-label"><input type="checkbox" id="chk-shuf"> 選択肢シャッフル</label>
    <div class="pb-wrap"><div class="pb" id="pbar" style="width:0%"></div></div>
    <button class="btn btn-out" onclick="resetAll()"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 .49-3.21"/></svg> リセット</button>
    <button class="btn btn-prim" onclick="showResults()"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg> 結果</button>
  </div>
</div>

<div class="qwrap" id="qwrap"></div>

<div class="modal" id="modal" onclick="modalClose(event)">
  <div class="mcard" id="mcard">
    <div class="m-icon" id="micon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="8 21 12 17 16 21"/><line x1="12" y1="17" x2="12" y2="11"/><path d="M18 6H6l1-4h10l1 4z"/><path d="M6 6c0 7 6 11 6 11s6-4 6-11"/></svg></div>
    <div class="m-score" id="mscore">--</div>
    <div class="m-pct" id="mpct">正解率</div>
    <div class="m-msg" id="mmsg"></div>
    <div class="m-domains" id="mdomains"></div>
    <div class="m-btns">
      <button class="m-btn m-btn-p" onclick="resetAll()"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 .49-3.21"/></svg> もう一度挑戦</button>
      <button class="m-btn m-btn-o" onclick="modalClose()"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> 閉じる</button>
    </div>
  </div>
</div>

<button class="scroll-top" id="scrollTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>

<script>
const QUESTIONS = {QUESTIONS_JSON};
const TOTAL = QUESTIONS.length;
const LTR = 'ABCDEFGHIJKLMNOP';
let state={{}}, filter='all', multiSel={{}}, displayChoices={{}};
function shuf(a){{for(let i=a.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}}return a;}}
function initState(){{
  const chk=document.getElementById('chk-shuf');
  const doShuf=chk&&chk.checked;
  state={{}};multiSel={{}};displayChoices={{}};
  QUESTIONS.forEach(q=>{{
    state[q.id]={{answered:false,correct:false}};
    displayChoices[q.id]=doShuf?shuf([...q.choices]):[...q.choices];
  }});
}}
function filtered(){{return filter==='all'?QUESTIONS:QUESTIONS.filter(q=>q.domain===filter);}}
function escH(s){{return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}}
function render(){{
  const qs=filtered();
  document.getElementById('qwrap').innerHTML=qs.map(q=>renderQ(q)).join('');
  qs.forEach(q=>{{if(state[q.id]?.answered)restoreQ(q);}});
  updateProgress();
}}
// ===== REVIEW SYSTEM =====
let reviewSet = new Set(JSON.parse(localStorage.getItem('az305_review_ids')||'[]'));
function toggleReview(qid, vol, num) {{
  if(reviewSet.has(qid)) {{
    reviewSet.delete(qid);
    const data = JSON.parse(localStorage.getItem('az305_review_data')||'{{}}');
    delete data[vol+'_'+qid];
    localStorage.setItem('az305_review_data', JSON.stringify(data));
  }} else {{
    reviewSet.add(qid);
    const q = QUESTIONS.find(x=>x.id===qid);
    if(q) {{
      const data = JSON.parse(localStorage.getItem('az305_review_data')||'{{}}');
      const volNum = vol.replace('vol','');
      data[vol+'_'+qid] = {{
        vol: vol, volNum: volNum, id: qid, num: q.num, domain: q.domain,
        domain_code: q.domain_code || '', domain_color: q.domain_color || '',
        question_text: q.question_text, choices: q.choices,
        correct_indices: q.correct_indices, n_correct: q.n_correct || 1,
        exp_html: q.exp_html || '', svg: q.svg || ''
      }};
      localStorage.setItem('az305_review_data', JSON.stringify(data));
    }}
  }}
  localStorage.setItem('az305_review_ids', JSON.stringify([...reviewSet]));
  const btn = document.getElementById('rbtn_'+qid);
  if(btn) btn.classList.toggle('review-active', reviewSet.has(qid));
  if(window.updateReviewBadge) updateReviewBadge();
}}
function renderQ(q){{
  const isMulti=q.n_correct>1;
  const mbadge=isMulti?`<span class="mbadge">複数選択 (${{q.n_correct}}つ)</span>`:'';
  const mhint=isMulti?`<div class="multi-hint">⚡ ${{q.n_correct}}つの選択肢を選んでください</div>`:'';
  const choices=(displayChoices[q.id]||q.choices).map((c,i)=>`<button class="cbtn" id="c_${{q.id}}_${{i}}" onclick="onChoice('${{q.id}}',${{i}})"><span class="cltr">${{LTR[i]}}</span><span>${{escH(c.text)}}</span></button>`).join('');
  const sub=isMulti?`<button class="submit-btn" id="sub_${{q.id}}" onclick="submitMulti('${{q.id}}')">回答を確定する</button>`:'';
  const archEl=q.svg?`<div class="arch-wrap arch-hidden" id="arch_${{q.id}}">${{q.svg}}<div class="arch-reveal-overlay"><span class="arch-reveal-hint">回答後にアーキテクチャ図が表示されます</span></div></div>`:'';
  return `<div class="qcard" id="card_${{q.id}}"><div class="qh"><span class="qnum">問 ${{q.num}}</span><span class="dbadge" style="background:${{q.domain_color||'#0072C6'}}">${{q.domain}}</span>${{mbadge}}<button class="review-btn ${{reviewSet.has(q.id)?'review-active':''}}" id="rbtn_${{q.id}}" onclick="toggleReview('${{q.id}}','vol6',${{q.num}})" title="復習リストに追加">★</button></div><div class="qbody"><p class="qtext">${{escH(q.question_text)}}</p></div>${{archEl}}${{mhint}}<div class="choices">${{choices}}</div>${{sub}}<div class="expanel" id="exp_${{q.id}}"><div id="rbadge_${{q.id}}"></div>${{q.exp_html}}</div></div>`;
}}
function onChoice(qid,idx){{
  if(state[qid]?.answered)return;
  const q=QUESTIONS.find(x=>x.id===qid);
  if(q.n_correct>1){{
    if(!multiSel[qid])multiSel[qid]=new Set();
    const btn=document.getElementById(`c_${{qid}}_${{idx}}`);
    if(multiSel[qid].has(idx)){{multiSel[qid].delete(idx);btn.classList.remove('multi-selected');}}
    else{{if(multiSel[qid].size>=q.n_correct)return;multiSel[qid].add(idx);btn.classList.add('multi-selected');}}
    const sub=document.getElementById(`sub_${{qid}}`);
    if(sub)sub.style.display=multiSel[qid].size>=q.n_correct?'block':'none';
  }}else{{
    state[qid]={{answered:true,correct:(displayChoices[qid]||q.choices)[idx].is_correct}};
    applyAnswer(q,[idx]);
  }}
}}
function submitMulti(qid){{
  if(state[qid]?.answered)return;
  const q=QUESTIONS.find(x=>x.id===qid);
  const sel=[...(multiSel[qid]||new Set())];
  const cset=new Set((displayChoices[qid]||q.choices).map((c,i)=>c.is_correct?i:-1).filter(i=>i>=0));
  state[qid]={{answered:true,correct:sel.length===cset.size&&sel.every(i=>cset.has(i))}};
  applyAnswer(q,sel);
}}
function applyAnswer(q,sel){{
  const sset=new Set(sel);const isOk=state[q.id].correct;
  (displayChoices[q.id]||q.choices).forEach((c,i)=>{{
    const btn=document.getElementById(`c_${{q.id}}_${{i}}`);if(!btn)return;
    btn.disabled=true;btn.classList.remove('multi-selected');
    if(sset.has(i))btn.classList.add(c.is_correct?'correct':'wrong');
    if(c.is_correct&&!sset.has(i))btn.classList.add('reveal');
  }});
  document.getElementById(`card_${{q.id}}`).classList.add(isOk?(q.n_correct>1?'multi-ok':'ok'):'ng');
  const archEl = document.getElementById('arch_'+q.id);
  if(archEl) archEl.classList.add('arch-revealed');
  document.getElementById(`rbadge_${{q.id}}`).innerHTML=isOk
    ?`<div class="rbadge ${{q.n_correct>1?'multi-ok':'ok'}}">${{q.n_correct>1?'正解！（複数選択）':'正解！'}}</div>`
    :'<div class="rbadge ng">不正解 — 解説で正解・理由を確認しましょう</div>';
  document.getElementById(`exp_${{q.id}}`).style.display='block';
  const sub=document.getElementById(`sub_${{q.id}}`);if(sub)sub.style.display='none';
  updateProgress();
  setTimeout(()=>document.getElementById(`exp_${{q.id}}`).scrollIntoView({{behavior:'smooth',block:'nearest'}}),120);
}}
function restoreQ(q){{
  const s=state[q.id];if(!s?.answered)return;
  (displayChoices[q.id]||q.choices).forEach((c,i)=>{{
    const btn=document.getElementById(`c_${{q.id}}_${{i}}`);if(!btn)return;
    btn.disabled=true;if(c.is_correct)btn.classList.add(s.correct?'correct':'reveal');
  }});
  document.getElementById(`card_${{q.id}}`).classList.add(s.correct?(q.n_correct>1?'multi-ok':'ok'):'ng');
  const exp=document.getElementById(`exp_${{q.id}}`);if(exp)exp.style.display='block';
  const badge=document.getElementById(`rbadge_${{q.id}}`);
  if(badge)badge.innerHTML=s.correct
    ?`<div class="rbadge ${{q.n_correct>1?'multi-ok':'ok'}}">${{q.n_correct>1?'正解！（複数選択）':'正解！'}}</div>`
    :'<div class="rbadge ng">不正解 — 解説で正解・理由を確認しましょう</div>';
}}
function filterDomain(d){{
  filter=d;
  document.querySelectorAll('.dbtn').forEach(b=>b.classList.toggle('on',b.dataset.d===d));
  render();window.scrollTo({{top:0}});
}}
function updateProgress(){{
  const ans=Object.values(state).filter(s=>s.answered).length;
  const cor=Object.values(state).filter(s=>s.correct).length;
  document.getElementById('pbar').style.width=(ans/TOTAL*100)+'%';
  document.getElementById('hdrScore').textContent=`${{cor}}/${{TOTAL}}`;
  document.getElementById('hdrPct').textContent=`正解率 ${{ans>0?Math.round(cor/ans*100):0}}%`;
}}
function showResults(){{
  const cor=Object.values(state).filter(s=>s.correct).length;
  const pct=Math.round(cor/TOTAL*100);
  const ds={{}};
  QUESTIONS.forEach(q=>{{
    if(!ds[q.domain])ds[q.domain]={{t:0,c:0,color:q.domain_color||'#333'}};
    ds[q.domain].t++;if(state[q.id]?.correct)ds[q.domain].c++;
  }});
  document.getElementById('mscore').textContent=`${{cor}}/${{TOTAL}}`;
  document.getElementById('mpct').textContent=`正解率 ${{pct}}%`;
  const SVG_TROPHY='<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="8 21 12 17 16 21"/><line x1="12" y1="17" x2="12" y2="11"/><path d="M18 6H6l1-4h10l1 4z"/><path d="M6 6c0 7 6 11 6 11s6-4 6-11"/></svg>';
  const SVG_UP='<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>';
  const SVG_ZAP='<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>';
  const SVG_BOOK='<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>';
  let icon=SVG_BOOK,msg='';
  if(pct>=80){{icon=SVG_TROPHY;msg='合格圏内！本番でも自信を持って！';}}
  else if(pct>=70){{icon=SVG_UP;msg='あと少し！弱点ドメインを集中的に復習しよう。';}}
  else if(pct>=50){{icon=SVG_ZAP;msg='「間違えやすいポイント」を重点的に確認しよう。';}}
  else{{icon=SVG_BOOK;msg='各解説の「なぜ正解か」「なぜ不正解か」をしっかり読もう！';}}
  document.getElementById('micon').innerHTML=icon;
  document.getElementById('mmsg').textContent=msg;
  document.getElementById('mdomains').innerHTML=Object.entries(ds).map(([d,s])=>{{
    const p=Math.round(s.c/s.t*100);
    return `<div class="m-ditem"><div class="m-dname">${{d}}</div><div class="m-dval" style="color:${{s.color}}">${{s.c}}/${{s.t}} <span style="font-size:13px;font-weight:500;color:#888">(${{p}}%)</span></div></div>`;
  }}).join('');
  document.getElementById('modal').classList.add('show');
}}
function modalClose(e){{if(!e||e.target.id==='modal')document.getElementById('modal').classList.remove('show');}}
function resetAll(){{document.getElementById('modal').classList.remove('show');initState();render();window.scrollTo({{top:0,behavior:'smooth'}});}}
window.addEventListener('scroll',()=>document.getElementById('scrollTop').classList.toggle('show',window.scrollY>400));
initState();render();

// Highlight active vol nav link
(function(){{
  const path = location.pathname;
  const m = path.match(/vol(\\d+)\\.html/);
  if(m) {{
    const el = document.getElementById('vj'+m[1]);
    if(el) el.classList.add('vj-active');
  }}
  function updateReviewBadge(){{
    const ids = JSON.parse(localStorage.getItem('az305_review_ids')||'[]');
    const badge = document.getElementById('vj-review-count');
    if(badge) badge.textContent = ids.length > 0 ? ids.length : '';
  }}
  updateReviewBadge();
  window.updateReviewBadge = updateReviewBadge;
}})();
</script>
</body>
</html>"""

if __name__ == '__main__':
    with open('az305/vol6.html', 'w', encoding='utf-8') as f:
        f.write(HTML)
    print(f"Generated az305/vol6.html with {TOTAL} questions")
    print("Domain distribution:", dict(domain_counts))
