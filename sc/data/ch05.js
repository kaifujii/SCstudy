const CH05_CARDS = [
  {
    chapter: "5",
    chapterName: "第5章 電子メールのセキュリティ",
    term: "SMTP コマンドの種類",
    hint: "メール送信の基本コマンド (5つ)",
    answer: ["① HELO / EHLO：サーバへの接続挨拶", "② MAIL FROM：送信元メールアドレス（エンベロープ From）", "③ RCPT TO：宛先メールアドレス", "④ DATA：メール本文の開始", "⑤ QUIT：接続終了"]
  },
  {
    chapter: "5",
    chapterName: "第5章 電子メールのセキュリティ",
    term: "メール配送の主要エージェント",
    hint: "MTA・MSA・MDA の役割",
    answer: ["① MTA（Mail Transfer Agent）：メール転送・中継（SMTP）", "② MSA（Mail Submission Agent）：メール送信受付（SMTP Port 587）", "③ MDA（Mail Delivery Agent）：メールボックスへの配送", "④ MUA（Mail User Agent）：メールクライアント", "⑤ POP3（Port 110）：メール受信（ダウンロード）", "⑥ IMAP4（Port 143）：メール受信（サーバ上管理）"]
  },
  {
    chapter: "5",
    chapterName: "第5章 電子メールのセキュリティ",
    term: "メールなりすまし対策技術",
    hint: "SPF・DKIM・DMARC の役割",
    answer: ["① SPF（Sender Policy Framework）：送信元IPアドレスを DNS の TXT レコードで検証", "② DKIM（DomainKeys Identified Mail）：秘密鍵でメールに署名、公開鍵（DNS TXT）で検証", "③ DMARC：SPF/DKIM の結果をポリシー（none/quarantine/reject）に基づき処理・レポート送信"]
  },
  {
    chapter: "5",
    chapterName: "第5章 電子メールのセキュリティ",
    term: "DKIM の仕組み",
    hint: "デジタル署名によるメール認証",
    answer: ["① 送信側メールサーバが秘密鍵でメールヘッダ・本文に署名", "② DKIM-Signature ヘッダを付与して送信", "③ 送信側 DNS の TXT レコードに公開鍵を登録（_domainkey）", "④ 受信側メールサーバが DNS から公開鍵を取得", "⑤ DKIM-Signature を検証して送信元の正当性を確認"]
  },
  {
    chapter: "5",
    chapterName: "第5章 電子メールのセキュリティ",
    term: "メール情報漏洩防止機能（DLP）",
    hint: "メールシステムでの漏洩対策機能",
    answer: ["① キーワードフィルタリング機能", "② 送信保留機能（一定時間後に送信）", "③ BCC への強制書き換え機能", "④ 管理者へのコピー送信機能", "⑤ 暗号化機能", "⑥ メールアーカイブシステム"]
  },
  {
    chapter: "5",
    chapterName: "第5章 電子メールのセキュリティ",
    term: "メールヘッダの主要フィールド",
    hint: "フォレンジックで重要なヘッダ情報",
    answer: ["① Return-Path：バウンスメールの返送先（エンベロープ From）", "② Received：メールリレーの経路記録（複数付与）", "③ From：表示上の送信者（なりすまし可能）", "④ Message-ID：メールの一意識別子", "⑤ Date：送信日時"]
  },
];
