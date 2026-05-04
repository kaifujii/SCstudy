/* 技術解説書 重要用語まとめ — フラッシュカード用データ
   各 term: { term, def, section }
   section … リンク先の解説書内セクション id
*/
const DESC_TERMS = [

  /* ──────────────────────────────────────────────────
     SC_03_PKI  公開鍵基盤
  ────────────────────────────────────────────────── */
  {
    id: "pki", badge: "SC_03", title: "PKI（公開鍵基盤）",
    file: "descriptions/SC_03_PKI.html", section: "s9",
    terms: [
      { term: "PKI", section: "s1",
        def: "Public Key Infrastructure。公開鍵暗号を安全に運用するためのインフラ全体。証明書・CA・CRL・OCSP を含む。" },
      { term: "X.509", section: "s2",
        def: "デジタル証明書の構造を定義する ITU-T 規格（v3 が現在主流）。ITU-T X.509 ＝ ISO/IEC 9594-8。" },
      { term: "TBSCertificate", section: "s2",
        def: "To-Be-Signed Certificate。CA が署名する対象となる証明書の本体部分（Version〜Extensions まで）。" },
      { term: "Subject / Issuer", section: "s2",
        def: "Subject：証明書の所有者（被証明者）の DN。Issuer：証明書を発行した CA の DN。" },
      { term: "SubjectAltName（SAN）", section: "s2",
        def: "証明書が有効なドメイン名・メールアドレスのリスト拡張。現代の証明書では CN より優先される。" },
      { term: "BasicConstraints", section: "s2",
        def: "cA=TRUE で CA 証明書、FALSE でエンドエンティティ証明書を示す X.509 v3 拡張フィールド。" },
      { term: "CA（認証局）", section: "s3",
        def: "Certification Authority。証明書を発行・署名する機関。ルート CA と中間 CA がある。" },
      { term: "RA（登録局）", section: "s3",
        def: "Registration Authority。本人確認・審査を担い、CA へ発行指示を送る機関。" },
      { term: "IA（発行局）", section: "s3",
        def: "Issuing Authority。実際の証明書の生成・署名・配布を行う機関。CA と統合される場合も多い。" },
      { term: "CSR", section: "s4",
        def: "Certificate Signing Request（PKCS#10 形式）。申請者が公開鍵・DN と自己署名を CA へ提出する申請書。秘密鍵は含まない。" },
      { term: "トラストストア", section: "s5",
        def: "OS やブラウザが保持するルート CA 証明書の一覧。証明書チェーン検証の最終判断基準。" },
      { term: "PKCS#7（CMS）", section: "s6",
        def: "署名付き・暗号化データのコンテナ形式。拡張子 .p7b/.p7s。S/MIME に使用。" },
      { term: "PKCS#10", section: "s6",
        def: "CSR（証明書署名要求）の形式を定義する規格。拡張子 .csr。" },
      { term: "PKCS#11", section: "s6",
        def: "IC カード・HSM など暗号トークンへの API インタフェース定義。" },
      { term: "PKCS#12", section: "s6",
        def: "証明書と秘密鍵を暗号化してまとめるコンテナ形式。拡張子 .pfx/.p12。" },
      { term: "CP（証明書ポリシー）", section: "s7",
        def: "「どのような条件で証明書を発行するか」のポリシー文書（What）。OID で証明書に埋め込まれる。" },
      { term: "CPS（認証局運用規程）", section: "s7",
        def: "「CA が具体的にどう運用するか」を記述した手順書（How）。CP に基づいて作成。" },
      { term: "DV / OV / EV 証明書", section: "s3",
        def: "Domain Validation / Organization Validation / Extended Validation。検証の厳格さと信頼度が異なる証明書の種類。" },
      { term: "信頼チェーン", section: "s5",
        def: "ルート CA → 中間 CA → エンドエンティティ証明書へと署名で連なる信頼の連鎖。" },
      { term: "OCSP Stapling", section: "s5",
        def: "サーバが事前に OCSP レスポンスを取得し TLS ハンドシェイクに添付する手法。クライアントの照会コストを削減。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_02_FIDO  FIDO認証
  ────────────────────────────────────────────────── */
  {
    id: "fido", badge: "SC_02", title: "FIDO認証",
    file: "descriptions/SC_02_FIDO.html", section: "s11",
    terms: [
      { term: "FIDO Alliance", section: "s11",
        def: "Fast IDentity Online Alliance。FIDO の標準化団体。Google・Apple・Microsoft・主要銀行等が参加。" },
      { term: "FIDO UAF", section: "s11",
        def: "Universal Authentication Framework。パスワードレス認証規格（2014年）。生体認証・PIN のみでログイン。" },
      { term: "FIDO U2F", section: "s11",
        def: "Universal 2nd Factor。セキュリティキーによる第2要素認証規格（2014年）。パスワード＋キーの2要素。" },
      { term: "FIDO2", section: "s11",
        def: "WebAuthn（W3C）＋CTAP（FIDO Alliance）で構成される Web 認証規格（2019年）。UAF・U2F を統合。" },
      { term: "WebAuthn", section: "s2",
        def: "Web Authentication API。W3C 標準。ブラウザ〜RP サーバ間の FIDO2 プロトコル。navigator.credentials.create/get() が主要 API。" },
      { term: "CTAP", section: "s2",
        def: "Client-to-Authenticator Protocol。ブラウザ〜認証器間のプロトコル。CTAP1（旧 U2F 互換）と CTAP2（FIDO2）がある。" },
      { term: "Relying Party（RP）", section: "s3",
        def: "FIDO を利用する Web サービス・アプリ。登録時に公開鍵を保管し、認証時に署名検証を行う。" },
      { term: "rpId", section: "s3",
        def: "Relying Party ID。ドメイン名（例：bank.co.jp）。鍵ペアはこの rpId に紐付けられ、フィッシング耐性の根拠となる。" },
      { term: "Authenticator（認証器）", section: "s4",
        def: "FIDO 鍵ペアを生成・保管・署名する装置。スマートフォン（TEE/SE 使用）やハードウェアセキュリティキーが該当。" },
      { term: "TEE", section: "s4",
        def: "Trusted Execution Environment。メインOSから隔離された安全な実行環境。ARM TrustZone 等。秘密鍵の保管・署名処理を担う。" },
      { term: "SE", section: "s4",
        def: "Secure Element。物理的に分離されたセキュアな IC チップ。TEE より強固。一部のスマホやセキュリティキーに内蔵。" },
      { term: "challenge（チャレンジ）", section: "s5",
        def: "RP サーバが認証のたびに生成する使い捨て乱数（32 バイト）。同じ値は2度使われないため、リプレイ攻撃を防止する。" },
      { term: "signCount", section: "s5",
        def: "認証器が署名のたびに +1 するカウンタ。RP サーバが受信値と保存値を比較し、逆転があればクローン検知・リプレイ拒否に利用する。" },
      { term: "Attestation", section: "s6",
        def: "認証器が正規の FIDO 認定デバイスであることをメーカー証明書チェーンで証明する仕組み。登録時に RP サーバが検証する。" },
      { term: "User Verification（UV）", section: "s7",
        def: "デバイス上での本人確認（生体認証・PIN）。UV は認証器内でのみ実施され、結果のみが RP に通知される。" },
      { term: "User Presence（UP）", section: "s7",
        def: "ユーザが物理的にデバイスに触れていること（U2F の物理ボタン押下等）。リモート攻撃を防ぐ。UV より低い保証レベル。" },
      { term: "Passkeys", section: "s9",
        def: "FIDO2 の鍵ペアを OS ベンダーのクラウドで同期する仕組み。Apple iCloud/Google Password Manager/Windows Hello 等で実現。" },
      { term: "AiTM 攻撃", section: "s10",
        def: "Adversary-in-The-Middle。攻撃者が正規サイトとユーザの間でリアルタイム中継する攻撃。TOTP を突破できるが FIDO は構造的に無効化する。" },
      { term: "TOTP", section: "s11",
        def: "Time-based One-Time Password（RFC 6238）。時刻＋共有秘密鍵で OTP を生成。有効期間 30 秒。サーバに共有秘密鍵を保管するため漏洩リスクあり。" },
      { term: "authData", section: "s11",
        def: "認証器情報。rpIdHash・フラグ（UV/UP 等）・signCount・AAGUID を含むバイト列。署名対象に含まれ改ざん検知に使われる。" },
      { term: "clientDataJSON", section: "s11",
        def: "ブラウザが生成する認証リクエスト情報（type・challenge・origin 等）。署名対象に含まれ Origin の検証に使われる。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_SSL_TLS  SSL/TLS
  ────────────────────────────────────────────────── */
  {
    id: "ssl_tls", badge: "SC_03", title: "SSL/TLS プロトコル",
    file: "descriptions/SC_03_SSL_TLS.html", section: "s13",
    terms: [
      { term: "TLS / SSL", section: "s1",
        def: "Transport Layer Security / Secure Sockets Layer。TCP 上でアプリデータを暗号化。現行は TLS 1.2/1.3 のみ有効。" },
      { term: "ハンドシェイク", section: "s2",
        def: "TLS 接続確立時の暗号スイート合意・証明書交換・鍵交換のプロセス。TLS 1.2 は 2-RTT、TLS 1.3 は 1-RTT。" },
      { term: "暗号スイート", section: "s2",
        def: "鍵交換・認証・暗号化・ハッシュの組み合わせ文字列。例：TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384。" },
      { term: "ECDHE", section: "s2",
        def: "Elliptic Curve Diffie-Hellman Ephemeral。楕円曲線上の一時 DH 鍵交換。PFS を実現。TLS 1.3 では必須。" },
      { term: "PFS（前方秘匿性）", section: "s2",
        def: "Perfect Forward Secrecy。サーバ秘密鍵の漏洩が過去の通信を復号できない性質。一時鍵の使用後破棄で実現。" },
      { term: "AEAD", section: "s2",
        def: "Authenticated Encryption with Associated Data。暗号化と完全性認証を同時実行。TLS 1.3 必須。" },
      { term: "SNI", section: "s3",
        def: "Server Name Indication。ClientHello でホスト名を通知する拡張。1 IP で複数 HTTPS ドメイン運用可能。" },
      { term: "ALPN", section: "s3",
        def: "Application-Layer Protocol Negotiation。HTTP/2 等をTLS ハンドシェイク内でネゴシエーション。HTTP/2 利用に必須。" },
      { term: "0-RTT", section: "s4",
        def: "TLS 1.3 の PSK 再接続機能。初回メッセージをハンドシェイクと同時送信。リプレイ攻撃リスクあり。" },
      { term: "HSTS", section: "s5",
        def: "HTTP Strict Transport Security。Strict-Transport-Security ヘッダでブラウザに常時 HTTPS 強制を指示。SSLストリッピング対策。" },
      { term: "OCSP（TLS 文脈）", section: "s6",
        def: "Online Certificate Status Protocol。証明書の失効状態をリアルタイムで確認するプロトコル。" },
      { term: "mTLS（相互TLS）", section: "s7",
        def: "Mutual TLS。双方向証明書認証。クライアントも証明書を提示。API・マイクロサービス間認証に使用。" },
      { term: "POODLE", section: "s8",
        def: "SSL 3.0 の CBC パディング脆弱性攻撃。対策：SSL 3.0 廃止、TLS_FALLBACK_SCSV。" },
      { term: "Heartbleed", section: "s8",
        def: "OpenSSL Heartbeat 実装バグ。境界チェック不備でメモリから秘密鍵等を窃取可能。対策：OpenSSL 更新・証明書再生成。" },
      { term: "SSLストリッピング", section: "s8",
        def: "HTTP→HTTPS リダイレクトを HTTPS→HTTP に書き換えてダウングレードさせる中間者攻撃。対策：HSTS。" },
      { term: "CRIME", section: "s8",
        def: "TLS 圧縮サイズ変化で Cookie を推測するサイドチャネル攻撃。対策：TLS 圧縮無効化。" },
      { term: "ダウングレード攻撃", section: "s8",
        def: "ネゴシエーションを改ざんして古い TLS バージョンや弱い暗号スイートに強制誘導する攻撃。TLS_FALLBACK_SCSV で対策。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_SSO  シングルサインオン
  ────────────────────────────────────────────────── */
  {
    id: "sso", badge: "SC_03", title: "シングルサインオン（SSO）",
    file: "descriptions/SC_03_SSO.html", section: "s-terms",
    terms: [
      { term: "SSO", section: "s-terms",
        def: "Single Sign-On。1回の認証で複数サービスに認証なしでアクセスできる仕組み。" },
      { term: "IdP", section: "s-terms",
        def: "Identity Provider。ユーザを認証しアサーション/トークンを発行する。SAML では IdP、OIDC では OP（OpenID Provider）と呼ぶ。" },
      { term: "SP", section: "s-terms",
        def: "Service Provider。SAML で IdP のアサーションを信頼してサービスを提供する側。" },
      { term: "KDC", section: "s-terms",
        def: "Key Distribution Center。Kerberos の AS+TGS を含む認証の中心サーバ。AD のドメインコントローラが担当。" },
      { term: "TGT", section: "s-terms",
        def: "Ticket Granting Ticket。AS から発行される「フリーパス」。TGS へのアクセスに使い、ST を取得する。" },
      { term: "ST（Service Ticket）", section: "s-terms",
        def: "TGS から取得する「入場券」。個々のサービスへのアクセスに使う。" },
      { term: "SAML アサーション", section: "s-terms",
        def: "IdP がデジタル署名した XML 文書。認証・属性・認可の 3 種がある。SP に送って SSO 認可に使う。" },
      { term: "JWT", section: "s-terms",
        def: "JSON Web Token。Header.Payload.Signature の 3 部構成。OIDC の ID トークンは JWT 形式。Base64URL エンコードで暗号化ではない。" },
      { term: "ID トークン", section: "s-terms",
        def: "OIDC で発行される JWT。iss/sub/aud/exp/nonce などのクレームを含み「誰が認証されたか」を証明する。" },
      { term: "アクセストークン", section: "s-terms",
        def: "OAuth 2.0 で発行されるトークン。「何ができるか（権限）」を表す。認証情報は含まない。" },
      { term: "認可コード", section: "s-terms",
        def: "OAuth 2.0 の認可コードフローで発行される短命・1回使い切りのコード。バックエンドでアクセストークンに交換する。" },
      { term: "PKCE", section: "s-terms",
        def: "Proof Key for Code Exchange。SPA やモバイルアプリでの認可コードフロー補強策。code_verifier/code_challenge で認可コード横取りを防ぐ。" },
      { term: "フェデレーション", section: "s-terms",
        def: "異なる組織間の認証情報を相互に信頼する仕組み。SAML が典型例。" },
      { term: "Golden Ticket 攻撃", section: "s-terms",
        def: "Kerberos の KRBTGT ハッシュを奪取して任意ユーザの TGT を偽造する攻撃。AD 全体の掌握が可能。" },
      { term: "XSW 攻撃", section: "s-terms",
        def: "XML Signature Wrapping。SAML アサーションの署名範囲外に不正要素を挿入して署名検証をバイパスする攻撃。" },
      { term: "JWKS", section: "s-terms",
        def: "JSON Web Key Set。OP が公開する公開鍵セット。RP はこれを使って JWT 署名を検証する。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_PKI  ICカード認証
  ────────────────────────────────────────────────── */
  {
    id: "iccard", badge: "SC_03", title: "ICカードによる認証",
    file: "descriptions/SC_03_ICcard.html", section: "s10",
    terms: [
      { term: "APDU", section: "s10",
        def: "IC カード通信の基本データ単位。コマンド APDU（端末→カード）とレスポンス APDU（カード→端末）の対。" },
      { term: "ATR", section: "s10",
        def: "Answer to Reset。カード起動時の応答で、カード種別・対応プロトコルを通知。" },
      { term: "INTERNAL AUTHENTICATE", section: "s10",
        def: "チャレンジ値をカード内の秘密鍵で署名する APDU コマンド。チャレンジ応答認証で使用。" },
      { term: "耐タンパ性", section: "s10",
        def: "物理的な解析・改ざんに対する抵抗性。保護メッシュ・アクティブシールド・自己消去機構などで実現。" },
      { term: "SPA / DPA", section: "s10",
        def: "単純/差分電力解析。消費電力波形を解析して秘密鍵を推測するサイドチャネル攻撃。" },
      { term: "セキュアメッセージング", section: "s10",
        def: "APDU コマンドを暗号化・MAC 付加して通信路を保護する機能。通信傍受・改ざんを防ぐ。" },
      { term: "HSM", section: "s10",
        def: "Hardware Security Module。サーバ側の暗号鍵を安全に保管・使用するハードウェア。FIPS 140-2/3 で評価。" },
      { term: "ISO/IEC 7816", section: "s10",
        def: "接触型 IC カードの物理・電気・通信インタフェース規格。APDU もここで定義。" },
      { term: "ISO/IEC 14443", section: "s10",
        def: "非接触型 IC カード（13.56 MHz）の通信規格。" },
      { term: "Common Criteria（CC）", section: "s10",
        def: "IT セキュリティ製品の評価基準の国際規格（ISO/IEC 15408）。IC カードの耐タンパ評価にも使用。" },
      { term: "FIPS 140-2/3", section: "s10",
        def: "米国標準の暗号モジュール評価基準。HSM や IC カードチップの評価に使用。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_SASL  SASL認証方式
  ────────────────────────────────────────────────── */
  {
    id: "sasl", badge: "SC_03", title: "SASL認証方式",
    file: "descriptions/SC_03_SASL.html", section: "s8",
    terms: [
      { term: "SASL", section: "s8",
        def: "Simple Authentication and Security Layer。アプリ層に認証を追加するフレームワーク（RFC 4422）。認証処理自体はメカニズムが担う。" },
      { term: "ネゴシエーション", section: "s8",
        def: "SASL の最初のフェーズ。サーバが対応メカニズム一覧を通知し、クライアントが一つを選択する。" },
      { term: "nonce（SASL）", section: "s8",
        def: "Number used ONCE。毎回異なるランダム値。チャレンジ応答に使うことでリプレイ攻撃を防ぐ。" },
      { term: "SCRAM-SHA-256", section: "s8",
        def: "Salted Challenge Response Authentication Mechanism。相互認証・平文不保存・SHA-256 の3点を持つ現在の推奨方式（RFC 7677）。" },
      { term: "GSSAPI", section: "s8",
        def: "Kerberos などを SASL から呼び出すためのメカニズム名。Active Directory 環境の SSO 認証で使われる。" },
      { term: "OAUTHBEARER", section: "s8",
        def: "OAuth 2.0 の Bearer トークンを SASL 認証に使用するメカニズム（RFC 7628）。クラウドメールで拡大中。" },
      { term: "PLAIN（SASL）", section: "s8",
        def: "ユーザ名+パスワードを Base64 エンコードして送る方式。TLS 必須。Base64 は可逆変換のため単体では危険。" },
      { term: "DIGEST-MD5", section: "s8",
        def: "MD5 ハッシュを用いたチャレンジ応答方式。RFC 6331 で廃止勧告。" },
      { term: "相互認証（SASL）", section: "s8",
        def: "クライアント ↔ サーバ双方向の認証。SCRAM・GSSAPI が対応。偽サーバ検知に有効。" },
      { term: "ダウングレード攻撃（SASL）", section: "s8",
        def: "ネゴシエーション段階でメカニズム一覧を改ざんし、クライアントに弱い方式を選ばせる中間者攻撃。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_IEEERADIUS  IEEE 802.1X / RADIUS
  ────────────────────────────────────────────────── */
  {
    id: "ieee_radius", badge: "SC_03", title: "IEEE 802規格と802.1X認証",
    file: "descriptions/SC_03_IEEERADIUS.html", section: "s11",
    terms: [
      { term: "IEEE 802.1X", section: "s11",
        def: "IEEE 802.1 グループのポートベース NAC 規格。有線・無線双方に適用可能。" },
      { term: "EAPoL", section: "s11",
        def: "EAP over LAN。Ethertype 0x888E。サプリカント〜オーセンティケータ間で EAP メッセージを運ぶ L2 搬送プロトコル。" },
      { term: "Supplicant", section: "s11",
        def: "認証を要求するエンティティ（端末）。802.1X 環境で認証される側。" },
      { term: "Authenticator", section: "s11",
        def: "EAP メッセージを中継するスイッチや AP。RADIUS クライアントとして動作し、判断は認証サーバに委ねる。" },
      { term: "RADIUS", section: "s11",
        def: "RFC 2865（IETF）。AAA（認証・認可・アカウンティング）サービスを提供。UDP 1812/1813。" },
      { term: "EAP-TLS", section: "s11",
        def: "クライアント・サーバ双方の証明書による相互認証。最もセキュア（RFC 5216）。クライアント証明書が必要。" },
      { term: "PEAP", section: "s11",
        def: "外側 TLS トンネル（サーバ証明書のみ）＋内側 MSCHAPv2 等の二層構造。クライアント証明書不要。Microsoft 環境で主流。" },
      { term: "動的 VLAN", section: "s11",
        def: "RADIUS Access-Accept の Tunnel 属性でユーザごとに VLAN を自動割り当て。" },
      { term: "Controlled / Uncontrolled Port", section: "s11",
        def: "Controlled Port は認証前ブロック・認証後開放のデータ通信用。Uncontrolled Port は EAPoL のみ常時通過の認証専用。" },
      { term: "MACsec", section: "s11",
        def: "IEEE 802.1AE。L2 フレームの暗号化・完全性保護（GCM-AES）。802.1X の MKA と連携して鍵交換。" },
      { term: "WPA2-Enterprise", section: "s11",
        def: "IEEE 802.11i のエンタープライズモード。IEEE 802.1X + EAP + CCMP（AES-128）。RADIUS サーバ必須。" },
      { term: "MAB", section: "s11",
        def: "MAC Address Bypass。802.1X 非対応機器に対して MAC アドレスで認証を代替。MAC アドレス詐称に脆弱。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_HTTPS  HTTP・Webセキュリティ
  ────────────────────────────────────────────────── */
  {
    id: "https", badge: "SC_03", title: "HTTP通信・Webセキュリティ",
    file: "descriptions/SC_03_HTTPS.html", section: "s14",
    terms: [
      { term: "Cookie", section: "s14",
        def: "サーバが Set-Cookie ヘッダでクライアントに渡す小データ。以降のリクエストで Cookie ヘッダとして自動送信。" },
      { term: "HttpOnly 属性", section: "s14",
        def: "JavaScript からの Cookie アクセスを禁止する Cookie 属性。XSS による Cookie 窃取を防ぐ。" },
      { term: "Secure 属性", section: "s14",
        def: "HTTPS 接続時のみ Cookie を送信する Cookie 属性。通信経路での盗聴を防ぐ。" },
      { term: "SameSite 属性", section: "s14",
        def: "クロスサイトリクエストでの Cookie 送信を制御する属性。Strict/Lax/None。CSRF 対策。" },
      { term: "CSRF", section: "s14",
        def: "Cross-Site Request Forgery。被害者のブラウザを利用して不正リクエストを送信させる攻撃。CSRFトークン・SameSite で対策。" },
      { term: "XSS（Web セキュリティ）", section: "s14",
        def: "Cross-Site Scripting。悪意あるスクリプトを Web ページに注入し被害者ブラウザで実行させる攻撃。HttpOnly・CSP・エスケープで対策。" },
      { term: "セッション固定攻撃", section: "s14",
        def: "攻撃者がセットしたセッション ID を被害者に使用させる攻撃。ログイン後のセッション ID 再発行で対策。" },
      { term: "SOP（同一オリジンポリシー）", section: "s14",
        def: "ブラウザのデフォルトセキュリティ制約。スキーム・ホスト・ポートがすべて一致しないクロスオリジンアクセスを制限。" },
      { term: "CORS", section: "s14",
        def: "Cross-Origin Resource Sharing。サーバのレスポンスヘッダで SOP を管理された形で緩和する仕組み。" },
      { term: "HSTS（Web）", section: "s14",
        def: "HTTP Strict Transport Security。Strict-Transport-Security ヘッダでブラウザに HTTPS 強制を指示。" },
      { term: "CSP", section: "s14",
        def: "Content Security Policy。Content-Security-Policy ヘッダで XSS を軽減するリソース制限ポリシー。" },
      { term: "X-Frame-Options", section: "s14",
        def: "ページの iframe 埋め込みを制御するレスポンスヘッダ。クリックジャッキング対策。DENY/SAMEORIGIN。" },
      { term: "WAF", section: "s14",
        def: "Web Application Firewall。SQLi・XSS・パストラバーサル等の攻撃パターンをシグネチャで検知・遮断。" },
      { term: "クリックジャッキング", section: "s14",
        def: "透明な iframe で対象サイトを重ね、被害者に気づかれずにクリック操作を実行させる攻撃。X-Frame-Options で対策。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_DNS  DNSセキュリティ
  ────────────────────────────────────────────────── */
  {
    id: "dns", badge: "SC_03", title: "DNSのセキュリティ",
    file: "descriptions/SC_03_DNS.html", section: "s13",
    terms: [
      { term: "フルサービスリゾルバ", section: "s13",
        def: "再帰問い合わせを行いキャッシュする DNS サーバ。ISP・企業内に設置。キャッシュポイズニングや水攻めの標的。" },
      { term: "TTL（DNS）", section: "s13",
        def: "DNS キャッシュの有効期間（秒）。汚染時の被害継続時間に直結する。" },
      { term: "トランザクション ID（TXID）", section: "s13",
        def: "DNS クエリ・応答を照合する 16bit の識別子（65,536 通り）。カミンスキー攻撃の推測対象。" },
      { term: "ソースポートランダム化", section: "s13",
        def: "カミンスキー攻撃対策。送信元 UDP ポートをランダム化し推測空間を約 2^32 に拡大する。2008 年の緊急対策。" },
      { term: "DNSSEC", section: "s13",
        def: "DNS Security Extensions。デジタル署名で DNS 応答の完全性・真正性を保証。暗号化ではない。RFC 4033〜4035。" },
      { term: "KSK（鍵署名鍵）", section: "s13",
        def: "ZSK の DNSKEY に署名する鍵。長期間・高セキュリティで管理（年 1 回程度更新）。親ゾーンに DS レコードを登録。" },
      { term: "ZSK（ゾーン署名鍵）", section: "s13",
        def: "ゾーン内の各 RRset に署名する鍵（月 1 回程度更新）。KSK よりも頻繁にローテーション。" },
      { term: "DS レコード", section: "s13",
        def: "子ゾーンの KSK ハッシュを親ゾーンに登録するレコード。信頼チェーンの「継ぎ手」。" },
      { term: "NSEC / NSEC3", section: "s13",
        def: "DNSSEC の否定応答レコード。NSEC3 はゾーン列挙攻撃対策でハッシュ化。" },
      { term: "DoT（DNS over TLS）", section: "s13",
        def: "TCP 853 で DNS を TLS 暗号化。盗聴・通信路改ざん防止。DNSSEC と相補的。RFC 7858。" },
      { term: "DoH（DNS over HTTPS）", section: "s13",
        def: "TCP 443 で DNS を HTTPS 暗号化。プライバシー保護とファイアウォール透過の両面。RFC 8484。" },
      { term: "オープンリゾルバ", section: "s13",
        def: "外部からの再帰問い合わせに応じる DNS サーバ。リフレクション・アンプ攻撃の踏み台。廃止が基本対策。" },
      { term: "BCP38（RFC 2827）", section: "s13",
        def: "ネットワークエッジでのソース IP フィルタリング標準。IP スプーフィングを防ぎリフレクション・アンプ攻撃の根本対策。" },
      { term: "RRL（レスポンスレートリミット）", section: "s13",
        def: "DNS サーバが同一宛先への応答レートを制限する機能。アンプ・水攻め対策。BIND 9.9 以降で標準サポート。" },
      { term: "RPZ（Response Policy Zone）", section: "s13",
        def: "DNS Firewall の実装技術。ドメインベースのポリシーで悪意ある問い合わせを遮断。水攻め・マルウェア C&C 対策。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_EMAIL  電子メールセキュリティ
  ────────────────────────────────────────────────── */
  {
    id: "email", badge: "SC_03", title: "電子メールのセキュリティ",
    file: "descriptions/SC_03_EMAIL.html", section: "s12",
    terms: [
      { term: "MUA / MTA / MDA", section: "s12",
        def: "MUA：メールクライアント。MTA：サーバ間中継（Port 25）。MDA：メールボックスへの最終配送。" },
      { term: "MSA", section: "s12",
        def: "Mail Submission Agent。MUA からのメール受付・SMTP-AUTH 認証を行い MTA へ渡す。Port 587。" },
      { term: "エンベロープ", section: "s12",
        def: "SMTP 通信中の配送情報（MAIL FROM / RCPT TO）。配送後は Return-Path ヘッダに残る。SPF はここを検証。" },
      { term: "S/MIME", section: "s12",
        def: "Secure/MIME。X.509 証明書でメールを暗号化・署名する PKI ベースのエンドツーエンド暗号化。" },
      { term: "SMTP-AUTH", section: "s12",
        def: "SMTP の認証拡張（SASL）。MUA が送信サーバに ID/PW 認証してメールを送る。Port 587 必須。" },
      { term: "OP25B", section: "s12",
        def: "Outbound Port 25 Blocking。ISP が一般ユーザからの外向き Port 25 をブロック。スパム送信防止。" },
      { term: "IP25B", section: "s12",
        def: "Inbound Port 25 Blocking。受信サーバが動的 IP からの Port 25 接続を拒否。スパム受信防止。" },
      { term: "SPF", section: "s12",
        def: "Sender Policy Framework。送信ドメインの DNS TXT レコードに許可 IP を登録し受信側が照合。" },
      { term: "DKIM", section: "s12",
        def: "DomainKeys Identified Mail。送信 MTA が秘密鍵で署名し受信側が DNS 公開鍵で検証。改ざん検知も兼ねる。" },
      { term: "DMARC", section: "s12",
        def: "Domain-based Message Authentication, Reporting and Conformance。SPF/DKIM にアライメント検証とポリシー（none/quarantine/reject）を追加。" },
      { term: "アライメント（DMARC）", section: "s12",
        def: "SPF/DKIM の認証ドメインとヘッダ From ドメインとの整合性確認。なりすまし検知の核心。" },
      { term: "ARC", section: "s12",
        def: "Authenticated Received Chain。メーリングリスト等の転送で SPF/DKIM が壊れる問題に対応。転送チェーンで認証情報を引き継ぐ。" },
      { term: "STARTTLS（メール）", section: "s12",
        def: "平文の SMTP 接続を TLS 暗号化にアップグレードするコマンド。転送路の機密性を確保（エンドツーエンドではない）。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_FW  FW・IDS/IPS・WAF
  ────────────────────────────────────────────────── */
  {
    id: "fw", badge: "SC_03", title: "ファイアウォール・IDS/IPS・UTM・WAF",
    file: "descriptions/SC_03_FW.html", section: "s14",
    terms: [
      { term: "パケットフィルタリング", section: "s14",
        def: "パケットの送信元/宛先 IP・ポートなどヘッダ情報で通過を判断する FW の方式。L3/L4 で動作。" },
      { term: "ステートフルパケットインスペクション", section: "s14",
        def: "TCP コネクション状態を追跡する最も賢いパケットフィルタ。現在の主流。略称 SPI。" },
      { term: "5タプル", section: "s14",
        def: "送信元 IP・宛先 IP・送信元ポート・宛先ポート・プロトコルの 5 組。フィルタ判定の基本。" },
      { term: "サーキットレベルゲートウェイ", section: "s14",
        def: "L5 で動作。セッション確立時のみ認証し、以降は中身を見ずに中継。SOCKS が代表。" },
      { term: "アプリケーションゲートウェイ", section: "s14",
        def: "L7 で動作。HTTP や SMTP などプロトコルごとに内容を解析して中継するプロキシ型 FW。" },
      { term: "NGFW（L7 FW）", section: "s14",
        def: "アプリケーション識別・ユーザ識別・SSL 復号・IPS 等を統合した次世代 FW。" },
      { term: "デフォルト拒否（deny all）", section: "s14",
        def: "ルールリスト最後に置く「全拒否」ルール。ホワイトリスト運用の前提。" },
      { term: "DMZ", section: "s14",
        def: "Demilitarized Zone。内部 LAN とインターネットの間に置く中間領域。公開サーバを配置。" },
      { term: "UTM", section: "s14",
        def: "Unified Threat Management。FW・IDS/IPS・アンチウイルス・URL フィルタ等を統合したアプライアンス。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_CLIENT  クライアントセキュリティ
  ────────────────────────────────────────────────── */
  {
    id: "client", badge: "SC_03", title: "クライアントセキュリティ",
    file: "descriptions/SC_03_CLIENT.html", section: "s12",
    terms: [
      { term: "IPsec", section: "s12",
        def: "IP Security。L3 でIPパケットの暗号化・認証を行うプロトコルスイート。AH・ESP・IKE で構成される。" },
      { term: "AH / ESP", section: "s12",
        def: "AH：認証のみ（暗号化なし）、NAT と非互換。ESP：暗号化＋認証、NAT-T で NAT 環境でも動作。現在のIPsecの主役。" },
      { term: "SA（Security Association）", section: "s12",
        def: "IPsec の通信パラメータ（アルゴリズム・鍵・有効期限）の取り決め。一方向ごとに 1 つ。SPI で識別。" },
      { term: "IKE", section: "s12",
        def: "Internet Key Exchange。IPsec の鍵交換プロトコル。フェーズ1（IKE SA確立）・フェーズ2（IPsec SA確立）の 2 段階。UDP 500。" },
      { term: "NAT-T", section: "s12",
        def: "NAT Traversal。ESP を UDP ポート 4500 でカプセル化することで NAT 環境でも IPsec を使用可能にする仕組み。" },
      { term: "トンネルモード / トランスポートモード", section: "s12",
        def: "トンネルモード：元 IP パケット全体を暗号化（拠点間 VPN）。トランスポートモード：ホスト間でペイロードのみ暗号化。" },
      { term: "SSL-VPN（3方式）", section: "s12",
        def: "TLS（Port 443）を使う VPN。①リバースプロキシ：HTTPアプリ限定。②ポートフォワーディング：TCP アプリ。③L2フォワーディング：全プロトコル対応。" },
      { term: "SSH 公開鍵認証", section: "s12",
        def: "秘密鍵/公開鍵ペアを使用。公開鍵をサーバの authorized_keys に事前登録。チャレンジレスポンス方式で秘密鍵所持を証明。" },
      { term: "シンクライアント", section: "s12",
        def: "端末にデータや業務アプリを持たない PC。処理をサーバ側で行う。端末紛失時の情報漏洩リスクを最小化。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_02_SECURE_PROG  セキュアプログラミング
  ────────────────────────────────────────────────── */
  {
    id: "secure_prog", badge: "SC_02", title: "セキュアプログラミング",
    file: "descriptions/SC_02_SECURE_PROG.html", section: "s14",
    terms: [
      { term: "XSS（Reflected）", section: "s14",
        def: "反射型 XSS。URL パラメータにスクリプトを埋め込みその場限りで実行させる。フィッシングメールと組み合わせることが多い。" },
      { term: "XSS（Stored）", section: "s14",
        def: "蓄積型 XSS。スクリプトを DB に保存しページの全訪問者に実行させる。最も危険な XSS。" },
      { term: "XSS（DOM-based）", section: "s14",
        def: "DOM ベース型 XSS。サーバを経由せずクライアント側 JS が DOM を操作する際に発生。サーバログに痕跡が残りにくい。" },
      { term: "HTML エスケープ", section: "s14",
        def: "XSS 対策。< を &lt;、> を &gt; 等に変換して HTML タグとして解釈させない。出力時の適用が重要。" },
      { term: "CSP（セキュアプログラミング）", section: "s14",
        def: "Content Security Policy。HTTP ヘッダで許可するスクリプト発生源を制限する XSS・クリックジャッキング対策。" },
      { term: "SQLインジェクション", section: "s14",
        def: "入力値に SQL 文を混入して DB を不正操作する攻撃。情報漏洩・認証バイパス・データ削除が主な被害。" },
      { term: "プリペアドステートメント", section: "s14",
        def: "SQL 文の構造とデータを分離して実行する仕組み。SQLi の根本対策。バインドパラメータとも呼ぶ。" },
      { term: "バッファオーバーフロー", section: "s14",
        def: "確保したバッファを超えてデータを書き込みリターンアドレスを上書きし任意コードを実行させる攻撃。C/C++ で多発。" },
      { term: "ASLR", section: "s14",
        def: "Address Space Layout Randomization。メモリ配置をランダム化し BOF 攻撃者のアドレス予測を困難にする OS 保護機構。" },
      { term: "DEP/NX", section: "s14",
        def: "Data Execution Prevention / No-Execute。データ領域を実行不可にしシェルコードの実行を防ぐ BOF 対策。" },
      { term: "CSRF（セキュアプログラミング）", section: "s14",
        def: "Cross-Site Request Forgery。ログイン中ユーザのブラウザから正規サービスへ意図しないリクエストを送信させる攻撃。" },
      { term: "CSRFトークン", section: "s14",
        def: "フォームに埋め込むランダムなトークン。サーバがリクエスト時に検証することで CSRF を防ぐ根本対策。" },
      { term: "SSRF", section: "s14",
        def: "Server-Side Request Forgery。Web アプリをプロキシにしてサーバから FW 内の内部サービスへリクエストを発行させる攻撃。" },
      { term: "セッションフィクセーション", section: "s14",
        def: "ログイン前にセッション ID を固定させ認証後にそのIDを使って乗っ取る攻撃。ログイン時のセッション ID 再生成が根本対策。" },
      { term: "ディレクトリトラバーサル", section: "s14",
        def: "「../」で Web ルート外のファイルにアクセスする攻撃。realpath() による正規化・間接参照が対策。" },
      { term: "OS コマンドインジェクション", section: "s14",
        def: "シェル特殊文字（;|&&`等）で OS コマンドを追加注入しサーバを制御する攻撃。OS コマンド不使用・引数分離が対策。" },
      { term: "HTTP ヘッダインジェクション", section: "s14",
        def: "CRLF（\\r\\n）を HTTP レスポンスヘッダに注入し任意のヘッダ追加・レスポンス分割を行う攻撃。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     SC_03_OpsManagement  運用マネジメント
  ────────────────────────────────────────────────── */
  {
    id: "ops", badge: "SC_03", title: "情報セキュリティの運用マネジメント",
    file: "descriptions/SC_03_OpsManagement.html", section: "s12",
    terms: [
      { term: "ISMS", section: "s12",
        def: "Information Security Management System。ISO/IEC 27001 が要求事項、27002 が管理策の実施手引。" },
      { term: "SoA（適用宣言書）", section: "s12",
        def: "Statement of Applicability。ISO 27001 附属書 A の管理策から採用／不採用を宣言する文書。" },
      { term: "リスクアセスメント", section: "s12",
        def: "リスク特定・リスク分析・リスク評価の 3 プロセス（ISO 31000）。" },
      { term: "リスク対応の4種", section: "s12",
        def: "回避／低減／移転／保有。ISO 31000 で定義。残留リスクは経営層が受容可否を判断する。" },
      { term: "ペネトレーションテスト", section: "s12",
        def: "実際の攻撃手法で脆弱性を検証する。Black／Gray／White Box の 3 形態。" },
      { term: "ファジング", section: "s12",
        def: "異常／ランダム／変異させた入力を与えて脆弱性を発見するブラックボックステスト手法。" },
      { term: "SOC", section: "s12",
        def: "Security Operation Center。24×365 で監視・検知・分析を行う組織。" },
      { term: "CSIRT", section: "s12",
        def: "Computer Security Incident Response Team。インシデント発生時の対応組織。JPCERT/CC が国内の調整機関。" },
      { term: "SIEM", section: "s12",
        def: "Security Information and Event Management。ログを収集・正規化・相関分析し、アラートを発砲するシステム。" },
      { term: "SCAP", section: "s12",
        def: "Security Content Automation Protocol。CVE・CCE・CPE・CVSS・XCCDF・OVAL の 6 要素からなる仕様群。" },
      { term: "CVE / CVSS", section: "s12",
        def: "CVE：脆弱性の一意 ID（MITRE 採番）。CVSS：脆弱性の深刻度スコア（0.0〜10.0）。基本／現状／環境の 3 種。" },
      { term: "NIST SP 800-61", section: "s12",
        def: "インシデントハンドリングガイド。6 段階ライフサイクル（準備・検知分析・封じ込め・根絶・復旧・事後）。" },
      { term: "Chain of Custody", section: "s12",
        def: "証拠保全の連鎖。誰がいつ何を扱ったかの記録。法的証拠能力の前提。" },
      { term: "CRYPTREC", section: "s12",
        def: "Cryptography Research and Evaluation Committees。日本の暗号評価プロジェクト。電子政府推奨暗号リスト等を策定。" },
      { term: "GDPR", section: "s12",
        def: "EU の一般データ保護規則。域外適用、72 時間通知義務、最大制裁金 4% または 2,000 万€。" },
      { term: "NIST CSF", section: "s12",
        def: "NIST Cybersecurity Framework。v2.0 で 6 機能（Govern / Identify / Protect / Detect / Respond / Recover）。" },
      { term: "不正アクセス禁止法", section: "s12",
        def: "アクセス制御のあるシステムへの不正ログイン等を禁止。3 年以下懲役／100 万円以下罰金。" },
      { term: "個人情報保護法", section: "s12",
        def: "2022 改正で漏えい報告義務化、仮名加工情報新設、法人罰 1 億円以下。要配慮個人情報は取得時に本人同意が必要。" },
      { term: "不正指令電磁的記録罪", section: "s12",
        def: "刑法 168 条の 2・3。ウイルス作成・提供・供用・取得・保管を処罰。" }
    ]
  },

  /* ──────────────────────────────────────────────────
     AP_01_strategy  経営戦略・法務
  ────────────────────────────────────────────────── */
  {
    id: "ap_strategy", badge: "AP_01", title: "経営戦略・情報システム戦略と業務プロセス・法務",
    file: "descriptions/AP_01_strategy.html", section: "s14",
    terms: [
      { term: "SWOT", section: "s14",
        def: "強み・弱み・機会・脅威の 4 視点で内部・外部環境を分析する経営分析フレームワーク。" },
      { term: "5 Forces", section: "s14",
        def: "業界の収益性を 5 つの競争要因（新規参入・代替・買手・売手・既存企業）で分析。マイケル・ポーター提唱。" },
      { term: "BSC", section: "s14",
        def: "Balanced Scorecard。財務・顧客・内部ビジネスプロセス・学習と成長の 4 視点で戦略を可視化。" },
      { term: "PPM", section: "s14",
        def: "Product Portfolio Management。市場成長率×市場シェアで事業を 4 象限分類（花形・金のなる木・問題児・負け犬）。" },
      { term: "KGI / KPI / CSF", section: "s14",
        def: "KGI：最終目標値。KPI：中間指標。CSF：成功要因。CSF を達成するための KPI を設定し、KGI に向かう。" },
      { term: "EA", section: "s14",
        def: "Enterprise Architecture。BA／DA／AA／TA の 4 階層（ビジネス・データ・アプリ・テクノロジー）で IT を整理。" },
      { term: "BPR / BPM / RPA", section: "s14",
        def: "BPR：業務を抜本的に再構築。BPM：継続的に業務を改善（PDCA）。RPA：定型業務を自動化するソフトウェアボット。" },
      { term: "SOA / IaaS・PaaS・SaaS", section: "s14",
        def: "SOA：サービスの組み合わせでシステムを構築する設計思想。IaaS/PaaS/SaaS：インフラ・PF・ソフトウェアをサービスとして提供。" },
      { term: "ERP / SCM / CRM", section: "s14",
        def: "ERP：会計・人事・製造等を一元管理。SCM：供給網全体を統合管理。CRM：顧客情報・購買履歴を一元管理。" },
      { term: "RFI / RFP / SLA", section: "s14",
        def: "RFI：ベンダから情報収集。RFP：提案依頼書。SLA：サービス品質（可用性・応答時間等）に関する合意。" },
      { term: "RTO / RPO / MTPD", section: "s14",
        def: "RTO：目標復旧時間。RPO：目標復旧時点（失っていいデータ量）。MTPD：事業に致命傷を与える最大許容停止時間。" },
      { term: "BCP / BCM", section: "s14",
        def: "BCP：事業継続計画（文書）。BCM：BCP を組織に浸透させ継続改善する活動。" },
      { term: "請負 / 準委任 / 派遣", section: "s14",
        def: "請負：成果物完成の約束（指示権なし）。準委任：事務遂行の約束（善管注意義務のみ）。派遣：派遣先に指示権あり。" },
      { term: "PL法（製造物責任法）", section: "s14",
        def: "製造または加工された動産が対象。ソフト単体・データは対象外、組込機器は対象。" },
      { term: "営業秘密の 3 要件", section: "s14",
        def: "秘密管理性・有用性・非公知性（不正競争防止法 2 条 6 項）。すべて満たさないと保護されない。" },
      { term: "デジュール / デファクト / フォーラム標準", section: "s14",
        def: "デジュール：ISO 等の公的標準。デファクト：市場で広まった事実上の標準。フォーラム：業界団体策定の標準。" },
      { term: "ISO / IEC / ITU-T / IEEE / IETF", section: "s14",
        def: "ISO：国際標準化機構。IEC：電気電子分野。ITU-T：通信標準（X.509等）。IEEE：IEEE 802等。IETF：RFC発行（TCP/IP・TLS等）。" }
    ]
  }

];
