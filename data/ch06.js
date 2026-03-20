const CH06_CARDS = [
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "ディスク暗号化技術",
    hint: "エンドポイントのストレージ保護",
    answer: ["① BitLocker（Windows）：TPM と連携したフルディスク暗号化", "② FileVault（macOS）：macOS のフルディスク暗号化", "③ TPM（Trusted Platform Module）：暗号鍵をハードウェアで保護するチップ", "④ 暗号化アルゴリズム：AES-XTS（128/256bit）が一般的"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "EMM（Enterprise Mobility Management）の構成",
    hint: "モバイルデバイス管理の3要素",
    answer: ["① MDM（Mobile Device Management）：デバイス全体の管理（リモートワイプ・設定配布）", "② MAM（Mobile Application Management）：アプリケーションの管理・配布", "③ MCM/MEM（Mobile Content/Email Management）：コンテンツ・メール管理", "④ コンテナ化：業務データと個人データの分離"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "BYOD のセキュリティ対策",
    hint: "個人デバイスを業務利用する際のリスク管理",
    answer: ["① OS・アプリを最新の状態に保つ", "② ウイルス対策ソフトの導入", "③ 信頼できるアプリのみインストール", "④ データの暗号化", "⑤ 通信の制御（VPN 利用）", "⑥ リモートワイプ機能の有効化", "⑦ MDM によるポリシー適用"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "VPN の種類",
    hint: "仮想プライベートネットワークの主要方式",
    answer: ["① IPsec VPN：L3 でカプセル化、高セキュリティ", "② SSL/TLS VPN：ブラウザで使用可能、ポート 443", "③ PPTP：古い方式、現在は非推奨（脆弱性あり）", "④ L2TP/IPsec：L2TP をIPsecで保護", "⑤ WireGuard：新世代の高速・軽量 VPN"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "IPsec の動作モードとプロトコル",
    hint: "IPsec の AH・ESP・モード",
    answer: ["① AH（Authentication Header）：認証・完全性保証（暗号化なし）", "② ESP（Encapsulating Security Payload）：認証＋暗号化", "③ トランスポートモード：元の IP ヘッダを維持、ホスト間", "④ トンネルモード：IP パケット全体をカプセル化、GW 間", "⑤ IKE（Internet Key Exchange）：鍵交換プロトコル"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "SSH の特徴と認証方式",
    hint: "安全なリモート接続プロトコル",
    answer: ["① TCP ポート 22 番", "② パスワード認証（平文を暗号化して送信）", "③ 公開鍵認証：秘密鍵・公開鍵ペアで認証（推奨）", "④ ポートフォワーディング：他プロトコルのトンネリング", "⑤ SCP / SFTP：SSH 経由のファイル転送", "⑥ Telnet（23番・平文）の代替として使用"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "EDR（Endpoint Detection and Response）",
    hint: "エンドポイントの高度な脅威対策",
    answer: ["① エンドポイントの振る舞いを継続的に監視・記録", "② 未知のマルウェアや攻撃を検知", "③ 感染経路の調査・フォレンジック支援", "④ 自動応答（隔離・プロセス停止）", "EPP（Endpoint Protection Platform）との違い：EDR は検知・調査・対応重視"]
  },
  {
    chapter: "6",
    chapterName: "第6章 クライアントセキュリティ",
    term: "IoT のセキュリティ対策",
    hint: "IoT デバイスの主なリスクと対策",
    answer: ["① デフォルトパスワードの変更", "② ファームウェアの定期的な更新", "③ 不要なポート・サービスの無効化", "④ 通信の暗号化（TLS）", "⑤ デバイス認証（証明書・PSK）", "⑥ ネットワーク分離（VLAN・セグメンテーション）"]
  },
];
