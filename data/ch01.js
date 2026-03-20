const CH01_CARDS = [
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "アクセスコントロールの三要素",
    hint: "IAM の基本構成要素 (3つ)",
    answer: ["① 識別（Identification）", "② 認証（Authentication）", "③ 認可（Authorization）"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "IAM 関連用語",
    hint: "Identity and Access Management の主要概念 (6つ)",
    answer: ["① アカウンティング（Accounting）", "② AAAフレームワーク（RFC2904）", "③ シングルサインオン（SSO）・ID連携", "④ プロビジョニング機能", "⑤ IDaaS（ID as a Service）", "⑥ クレデンシャル情報"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "利用者IDの適切な運用",
    hint: "共有IDの問題と対策 (3つ)",
    answer: ["① 共有IDを使わない", "② 単独ユーザIDを定める", "③ 共有IDの廃止・利用者を特定できるIDを使用"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "認証方式の種類",
    hint: "主な認証方式 (5つ)",
    answer: ["① 単要素認証（SFA）", "② 二要素認証（2FA）", "③ 多要素認証（MFA）", "④ リスクベース認証", "⑤ ステップアップ認証"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "認証の主要素（3要素）",
    hint: "知識・所有・生体の3カテゴリ",
    answer: ["① 知識要素：何かを知っている（パスワード、PIN）", "② 所有要素：何かを持っている（スマートカード、OTP）", "③ 生体要素：何かである（指紋、顔認証）"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "バイオメトリクス認証の種類",
    hint: "生体認証の代表例 (5つ以上)",
    answer: ["① 指紋認証", "② 顔認証", "③ 虹彩認証（IRIS認識）", "④ 声紋認証", "⑤ 静脈認証", "⑥ 歩行認証"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "IEEE 802.1X 認証の構成要素",
    hint: "ネットワーク認証の登場人物 (4つ)",
    answer: ["① サプリカント（Supplicant）：認証を求める端末", "② オーセンティケータ（Authenticator）：スイッチ/AP", "③ 認証サーバ（RADIUS サーバ）", "④ EAP（Extensible Authentication Protocol）でやりとり"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "EAP の主要方式",
    hint: "IEEE 802.1X で使われる認証プロトコル",
    answer: ["① EAP-TLS：クライアント証明書による双方向認証（最も安全）", "② EAP-TTLS：サーバ証明書のみ、クライアントは多様な認証", "③ EAP-FAST：PAC（Protected Access Credential）で動作", "④ PEAP：サーバ証明書でトンネル確立後に内部認証"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "FIDO 認証",
    hint: "パスワードレス認証の標準 (5つ)",
    answer: ["① FIDO Alliance が策定した標準", "② U2F（Universal 2nd Factor）：Web ブラウザ対応の2要素", "③ UAF（Universal Authentication Framework）：パスワードレス", "④ FIDO2 = WebAuthn + CTAP", "⑤ CTAP（Client to Authenticator Protocol）：端末-認証器間"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "アクセス制御モデルの種類",
    hint: "DAC・MAC・RBAC の違い",
    answer: ["① DAC（Discretionary Access Control）任意アクセス制御：所有者が権限設定", "② MAC（Mandatory Access Control）強制アクセス制御：システムが一元管理", "③ RBAC（Role-Based Access Control）ロールベース：役割に応じた権限付与"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "シングルサインオン（SSO）の仕組み",
    hint: "主な SSO・ID連携プロトコル (4つ)",
    answer: ["① SAML（Security Assertion Markup Language）：XMLベース", "② OAuth 2.0：リソースへの認可委譲", "③ OIDC（OpenID Connect）：OAuth 2.0上の認証レイヤ", "④ SPNEGO：Kerberos を HTTP に統合"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "Kerberos 認証の構成要素",
    hint: "企業 AD 環境の認証基盤",
    answer: ["① KDC（Key Distribution Center）：AS + TGS + KDB で構成", "② AS（Authentication Server）：TGT 発行", "③ TGS（Ticket Granting Server）：サービスチケット発行", "④ レルム（Realm）：Kerberos の管理ドメイン", "⑤ ST（Service Ticket）：サービスへのアクセス許可"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "Kerberos への攻撃",
    hint: "チケット偽造攻撃の代表例",
    answer: ["① ゴールデンチケット攻撃：krbtgt アカウントのハッシュを奪取して TGT を偽造", "② シルバーチケット攻撃：サービスアカウントのハッシュで ST を偽造", "③ Pass-the-Ticket：正規チケットを盗んで再利用"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "OAuth 2.0 の登場人物",
    hint: "認可フローの4者",
    answer: ["① Resource Owner：リソースの所有者（ユーザ）", "② Client：アクセスを求めるアプリ", "③ Resource Server：保護されたリソースを持つサーバ", "④ Authorization Server：アクセストークンを発行するサーバ"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "JWT（JSON Web Token）の構造",
    hint: "3つのパートで構成",
    answer: ["① Header：アルゴリズム（alg）とトークン種別（typ）", "② Payload：クレーム情報（sub, iat, exp など）", "③ Signature：ヘッダ＋ペイロードをアルゴリズムで署名した値", "※ Base64url エンコードして . で結合"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "JWT のセキュリティ対策",
    hint: "JWT を安全に使うための注意点 (4つ)",
    answer: ["① サーバ側で alg=\"none\" を拒否する", "② XSS 対策・CSRF 対策を実施", "③ 適切な CORS 設定", "④ 有効期限（exp）を短く設定し、リフレッシュトークンを使用"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "SAML 2.0 の主要概念",
    hint: "XML ベースの認証連携 (4つ)",
    answer: ["① アサーション（Assertion）：認証・属性・認可情報を含む XML", "② SAML リクエスト：SP → IdP への認証要求", "③ SAML レスポンス：IdP → SP への認証結果", "④ SSO プロファイル：Web ブラウザ SSO が代表"]
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "パスワード攻撃の種類",
    hint: "認証を突破する主要な攻撃手法",
    answer: ["① 辞書攻撃：よく使われるパスワード辞書で試行", "② ブルートフォース攻撃：全組み合わせを試行", "③ リバースブルートフォース：1つのパスワードで多くのIDを試行", "④ パスワードスプレー攻撃：少数の一般的なパスワードで多くのアカウントを試行", "⑤ クレデンシャルスタッフィング：漏洩した ID/PW リストを使用", "⑥ レインボーテーブル攻撃：ハッシュ値を事前計算したテーブルで逆引き"]
  },
];
