const CH09_CARDS = [
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "CSIRT の種類と役割",
    hint: "Computer Security Incident Response Team",
    answer: ["① JPCERT/CC：日本の国家レベル CSIRT（コーディネーションセンター）", "② IPA/SEC：情報処理推進機構のセキュリティセンター", "③ FIRST（Forum of IR and Security Teams）：国際的な CSIRT 連合", "④ 組織内 CSIRT：企業内のインシデント対応チーム", "⑤ NCA：日本 CSIRT 協議会"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "SOAR（Security Orchestration, Automation and Response）",
    hint: "セキュリティ運用の自動化プラットフォーム",
    answer: ["① Orchestration（オーケストレーション）：複数ツールの連携・統合", "② Automation（オートメーション）：繰り返し作業の自動化", "③ Response（レスポンス）：インシデント対応の標準化・効率化", "SIEM と組み合わせて使用し、アラート対応を自動化"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "ログ管理のポイント",
    hint: "インシデント対応で重要なログ管理",
    answer: ["① 正確な時刻記録（NTP による時刻同期）", "② WORM（Write Once Read Many）：改ざん防止", "③ ログの集中管理（SIEM への転送）", "④ 適切な保管期間（法規制に合わせる）", "⑤ バックアップ・長期保管", "⑥ アクセス制御（ログの閲覧・操作の制限）"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "OODA ループ",
    hint: "意思決定・行動のサイクル",
    answer: ["① Observe（観察）：情報・データの収集", "② Orient（状況判断）：収集情報の分析・評価", "③ Decide（意思決定）：行動方針の決定", "④ Act（行動）：決定した行動の実施", "セキュリティインシデント対応や攻撃者への対抗で活用"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "脆弱性テストの種類",
    hint: "システムの弱点を発見する手法",
    answer: ["① ペネトレーションテスト：実際に攻撃を試みてセキュリティを検証", "② 脆弱性スキャン：自動ツールで既知の脆弱性を検索", "③ SCA（Software Composition Analysis）：OSS の脆弱性を検出", "④ DAST（Dynamic Application Security Testing）：実行中アプリへのテスト", "⑤ SAST（Static Application Security Testing）：ソースコード静的解析"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "インシデント対応の基本プロセス",
    hint: "インシデント発生から収束までのフロー",
    answer: ["① 検知・トリアージ：インシデントの発見・重大度分類", "② 初動対応：影響を局限するための即時対応（隔離など）", "③ 調査・分析：侵害範囲・原因の特定（フォレンジック）", "④ 根絶：マルウェア除去・脆弱性修正", "⑤ 復旧：システムの正常復旧・監視強化", "⑥ 事後対応：再発防止策・報告書作成"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "SIEM（Security Information and Event Management）",
    hint: "ログの一元管理と脅威検知プラットフォーム",
    answer: ["① 複数システムのログを集中収集・正規化", "② リアルタイムの相関分析でインシデントを検知", "③ アラートの生成と優先度付け", "④ ダッシュボード・レポート機能", "⑤ SOAR と連携して対応を自動化", "代表製品：Splunk、IBM QRadar、Microsoft Sentinel"]
  },
  {
    chapter: "9",
    chapterName: "第9章 インシデント対応",
    term: "脅威インテリジェンスの活用",
    hint: "CTI（Cyber Threat Intelligence）",
    answer: ["① 戦略的インテリジェンス：経営層向け、攻撃者の動向・傾向", "② 戦術的インテリジェンス：TTPs（戦術・技術・手順）情報", "③ 運用的インテリジェンス：特定キャンペーン・インシデント情報", "④ 技術的インテリジェンス：IOC（Indicator of Compromise）= IP, ドメイン, ハッシュ値", "STIX/TAXII：脅威情報の標準的な共有フォーマット・プロトコル"]
  },
];
