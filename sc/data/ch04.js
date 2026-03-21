const CH04_CARDS = [
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "HTTP メソッドの種類と用途",
    hint: "RESTful API でよく使う 7メソッド",
    answer: ["① GET：リソース取得", "② HEAD：ヘッダのみ取得", "③ POST：リソース作成・データ送信", "④ PUT：リソース全体更新（置換）", "⑤ PATCH：リソース部分更新", "⑥ DELETE：リソース削除", "⑦ OPTIONS：利用可能メソッドの確認（CORS プリフライト）"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "HTTP ステータスコード",
    hint: "代表的なステータスコードの意味",
    answer: ["200 OK：成功", "201 Created：作成成功", "301 Moved Permanently：恒久的リダイレクト", "302 Found：一時的リダイレクト", "400 Bad Request：リクエスト不正", "401 Unauthorized：認証が必要", "403 Forbidden：アクセス禁止", "404 Not Found：リソースなし", "500 Internal Server Error：サーバ内部エラー"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "Cookie のセキュリティ属性",
    hint: "安全な Cookie 設定に必要な属性 (5つ)",
    answer: ["① Secure：HTTPS のみで送信", "② HttpOnly：JavaScript からアクセス不可（XSS 対策）", "③ SameSite=Strict/Lax：クロスサイトリクエスト制限（CSRF 対策）", "④ Expires / Max-Age：有効期限設定", "⑤ Domain / Path：送信対象の制限"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "セキュリティ関連 HTTP レスポンスヘッダ",
    hint: "Webアプリに設定すべきセキュリティヘッダ",
    answer: ["① Strict-Transport-Security（HSTS）：HTTPS 強制", "② Content-Security-Policy（CSP）：XSS・インジェクション対策", "③ X-Frame-Options：クリックジャッキング対策（DENY/SAMEORIGIN）", "④ X-Content-Type-Options: nosniff：MIME スニッフィング防止", "⑤ Referrer-Policy：リファラ情報の制御", "⑥ Set-Cookie（Secure/HttpOnly/SameSite）"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "セッション管理のセキュリティ",
    hint: "セッションIDの安全な扱い方",
    answer: ["① セッションIDは十分にランダムで長い値にする", "② 認証成功後にセッションIDを再生成（セッションFixation 対策）", "③ HTTPS のみで送信（Secure 属性）", "④ JavaScript からアクセス禁止（HttpOnly 属性）", "⑤ CSRFトークンを使用", "⑥ ログアウト時にサーバ側でセッションを破棄"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "CORS（Cross-Origin Resource Sharing）",
    hint: "Same-Origin Policy の緩和メカニズム",
    answer: ["① Same-Origin Policy：異なるオリジンへの JS アクセスを制限", "② プリフライトリクエスト：OPTIONS メソッドで事前確認", "③ Access-Control-Allow-Origin：許可するオリジン", "④ Access-Control-Allow-Methods：許可するメソッド", "⑤ Access-Control-Allow-Headers：許可するヘッダ", "⑥ Access-Control-Allow-Credentials：Cookie 送信の許可"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "DNS の基本構成",
    hint: "名前解決の仕組みと登場人物",
    answer: ["① スタブリゾルバ：OS 内蔵のリゾルバ", "② フルリゾルバ（キャッシュサーバ）：再帰的に問い合わせ・結果をキャッシュ", "③ 権威 DNS サーバ：ゾーン情報を管理・応答", "④ ルート DNS サーバ：最上位の DNS サーバ（13系統）"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "DNS への攻撃手法",
    hint: "DNS を悪用した攻撃 (3種)",
    answer: ["① DNS キャッシュポイズニング：偽の DNS レコードをキャッシュさせる", "② DNS リフレクション攻撃（DNS amp）：送信元を詐称し大量レスポンスをターゲットに送る DDoS", "③ DNS ハイジャック：DNS サーバ自体を改ざん", "対策：DNSSEC、ランダムなソースポート、0x20 エンコーディング"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "DNSSEC",
    hint: "DNS の真正性を保証する仕組み",
    answer: ["① DNS レコードにデジタル署名（RRSIG）を付与", "② DS レコード：上位ゾーンへの信頼チェーン", "③ DNSKEY レコード：公開鍵を登録", "④ キャッシュポイズニング対策に有効", "注意：可用性攻撃（増幅）には効果なし"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "DHCP の動作フロー",
    hint: "IP アドレスを自動取得する 4ステップ",
    answer: ["① DISCOVER：クライアントがブロードキャストで DHCP サーバを探す", "② OFFER：DHCP サーバが IP アドレスを提案", "③ REQUEST：クライアントが IP アドレスを要求", "④ ACK：DHCP サーバが割り当てを確認"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "DHCP への攻撃と対策",
    hint: "DHCP を悪用する 2種の攻撃",
    answer: ["① DHCP Rogue Server Attack：偽 DHCP サーバを立て偽の IP 設定を配布", "② DHCP Starvation Attack：大量の DHCP 要求で IP アドレスを枯渇させる DoS", "対策①：DHCP スヌーピング（信頼ポート以外からの DHCP 応答を遮断）", "対策②：ポートセキュリティ（MAC アドレス数制限）", "対策③：IEEE 802.1X 認証"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "Web アプリへの主要攻撃手法",
    hint: "OWASP Top 10 の代表的な攻撃",
    answer: ["① SQL インジェクション：SQL を不正注入し DB を操作", "② XSS（クロスサイトスクリプティング）：スクリプトをページに埋め込む", "③ CSRF（クロスサイトリクエストフォージェリ）：ユーザに意図しないリクエストを実行させる", "④ ディレクトリトラバーサル：../などで意図しないファイルにアクセス", "⑤ コマンドインジェクション：OS コマンドを不正注入", "⑥ XXE（XML External Entity）：XML の外部エンティティを悪用"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "CSRF 対策",
    hint: "クロスサイトリクエストフォージェリの防御策",
    answer: ["① CSRF トークン：セッションごとにランダムなトークンを生成・検証", "② SameSite Cookie 属性：Strict/Lax でクロスサイトの Cookie 送信を制限", "③ Referer チェック：リクエスト元を確認", "④ CORS 設定：信頼できるオリジンのみ許可", "⑤ Double Submit Cookie：Cookie と本文でトークンを一致確認"]
  },
  {
    chapter: "4",
    chapterName: "第4章 サーバセキュリティ",
    term: "XSS（クロスサイトスクリプティング）の種類と対策",
    hint: "Web アプリの代表的な脆弱性",
    answer: ["種類①：反射型 XSS（Reflected）：URL パラメータのスクリプトをそのまま表示", "種類②：格納型 XSS（Stored）：DB に保存した悪意スクリプトを全ユーザに表示", "種類③：DOM-based XSS：JS の DOM 操作で発生", "対策①：出力時のエスケープ処理（HTML エンティティ化）", "対策②：Content-Security-Policy（CSP）ヘッダの設定", "対策③：HttpOnly 属性で Cookie を保護"]
  },
];
