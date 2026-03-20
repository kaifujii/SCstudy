const CH03_CARDS = [
  {
    chapter: "3",
    chapterName: "第3章 ネットワークセキュリティ",
    term: "ファイアウォールの種類と特徴",
    hint: "各世代のファイアウォール方式",
    answer: ["① パケットフィルタリング型：IP/ポートで制御、高速", "② ステートフルインスペクション：接続状態を管理", "③ アプリケーションゲートウェイ（プロキシ）型：L7まで検査", "④ WAF（Web Application Firewall）：HTTP の内容を検査", "⑤ 次世代FW（NGFW）：IPS・アプリ識別・SSL復号を統合"]
  },
  {
    chapter: "3",
    chapterName: "第3章 ネットワークセキュリティ",
    term: "フィルタリングルールの方式",
    hint: "ホワイトリスト vs ブラックリスト",
    answer: ["① ホワイトリスト（許可リスト）：許可するものだけ定義、デフォルト拒否。安全性が高い", "② ブラックリスト（拒否リスト）：拒否するものだけ定義、デフォルト許可。使いやすいが漏れが生じやすい", "推奨：ホワイトリスト方式"]
  },
  {
    chapter: "3",
    chapterName: "第3章 ネットワークセキュリティ",
    term: "IDS / IPS の違い",
    hint: "検知と防御の違い",
    answer: ["① IDS（Intrusion Detection System）：不正侵入を検知・通報のみ", "② IPS（Intrusion Prevention System）：検知＋自動的に遮断・防御", "③ NIDS（Network-based IDS）：ネットワークトラフィックを監視", "④ HIDS（Host-based IDS）：ホスト上のログ・ファイルを監視", "⑤ 検知方式：シグネチャ型（既知）・アノマリ型（異常）"]
  },
];
