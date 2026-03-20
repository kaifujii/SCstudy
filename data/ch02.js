const CH02_CARDS = [
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "X.509 証明書の主要フィールド",
    hint: "PKI デジタル証明書の構成要素",
    answer: ["① バージョン", "② シリアル番号", "③ 署名アルゴリズム", "④ 発行者（Issuer）：認証局名", "⑤ 有効期間（有効開始～有効終了）", "⑥ 主体者（Subject）：証明書の所有者", "⑦ 公開鍵", "⑧ サブジェクト代替名（SAN）：ドメイン名など"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "PKI の構成要素",
    hint: "公開鍵基盤の主要コンポーネント",
    answer: ["① CA（Certificate Authority）：証明書発行機関", "② RA（Registration Authority）：登録機関", "③ CRL（Certificate Revocation List）：失効リスト", "④ OCSP（Online Certificate Status Protocol）：オンライン失効確認", "⑤ CSR（Certificate Signing Request）：証明書署名要求"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "SSL/TLS のバージョンと推奨状況",
    hint: "廃止・非推奨・推奨の区別",
    answer: ["❌ SSL 3.0：廃止（POODLE 攻撃）", "❌ TLS 1.0 / 1.1：廃止", "✓ TLS 1.2：現在も広く使用可", "✓✓ TLS 1.3：推奨（ハンドシェイク高速化・前方秘匿性強制）"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "TLS ハンドシェイクの流れ（TLS 1.2）",
    hint: "HTTPS 接続確立の手順",
    answer: ["① Client Hello：対応暗号スイート・乱数を送信", "② Server Hello：暗号スイート決定・サーバ証明書送信", "③ ClientKeyExchange：プリマスタシークレットを送信", "④ ChangeCipherSpec：暗号化開始を通知", "⑤ Finished：双方でハンドシェイク完了を確認"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "TLS 1.3 の改良点",
    hint: "TLS 1.2 との主な違い",
    answer: ["① ハンドシェイクが 1-RTT（従来 2-RTT）", "② 0-RTT 再開（レジューム）機能", "③ 脆弱な暗号スイートを廃止（RC4, DES, 3DES, CBC等）", "④ 前方秘匿性（PFS）が必須", "⑤ ServerHello 以降を暗号化"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "HSTS（HTTP Strict Transport Security）",
    hint: "HTTPS を強制するセキュリティヘッダ",
    answer: ["① レスポンスヘッダ：Strict-Transport-Security", "② max-age：HTTPS 強制期間（秒）", "③ includeSubDomains：サブドメインにも適用", "④ preload：ブラウザ組み込みリストに登録", "効果：HTTP でアクセスされても自動的に HTTPS にリダイレクト"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "SNI と ECH",
    hint: "TLS での仮想ホスティングとプライバシー",
    answer: ["① SNI（Server Name Indication）：TLS ハンドシェイク時にホスト名を平文送信", "② ESNI（Encrypted SNI）：SNI を暗号化（非推奨→ECH に移行）", "③ ECH（Encrypted Client Hello）：Client Hello 全体を暗号化", "④ CDN 環境でよく使用される技術"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "デジタル署名の仕組み",
    hint: "送信者の正当性とデータ完全性を保証",
    answer: ["① 送信者がメッセージのハッシュ値を計算", "② 送信者の秘密鍵でハッシュ値を暗号化（=署名）", "③ メッセージと署名を送信", "④ 受信者が送信者の公開鍵で署名を復号", "⑤ 受信メッセージのハッシュ値と一致すれば正当"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "タイムスタンプ（TST）",
    hint: "電子文書の存在証明の仕組み",
    answer: ["① 送信者がドキュメントのハッシュ値を計算", "② TSA（Time Stamp Authority）にハッシュを送信", "③ TSA がハッシュ＋時刻情報に署名して TST を返却", "④ TST により「その時刻にそのデータが存在した」ことを証明"]
  },
  {
    chapter: "2",
    chapterName: "第2章 暗号技術・PKI",
    term: "共通鍵暗号と公開鍵暗号の比較",
    hint: "対称鍵 vs 非対称鍵",
    answer: ["共通鍵暗号（対称鍵）：同じ鍵で暗号化・復号。高速。AES, DES, 3DES", "公開鍵暗号（非対称鍵）：公開鍵で暗号化、秘密鍵で復号。低速。RSA, ECDSA", "ハイブリッド暗号：公開鍵で共通鍵を交換し、その後は共通鍵で通信（TLS の方式）", "代表アルゴリズム：AES（共通鍵）、RSA/ECDSA（公開鍵）、SHA-256（ハッシュ）"]
  },
];
