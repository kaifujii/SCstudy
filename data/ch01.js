const CH01_CARDS = [
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "アクセスコントロールの三要素",
    hint: "IAM の基本構成要素 (3つ)",
    answer: ["① 識別（Identification）", "② 認証（Authentication）", "③ 認可（Authorization）"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    「あなたは誰ですか？」→「本当にそうですか？」→「では何が使えますか？」という3ステップ。<br>
    すべてのアクセス制御はこの3要素の流れで成立する。試験では<strong>識別と認証の違い</strong>が特に狙われる。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔍 3要素の比較</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>要素</div><div>内容</div><div>具体例</div></div>
    <div class="ds-compare-row"><div>① 識別<br>Identification</div><div>「自分はこれだ」と名乗ること<br>本人確認は行わない</div><div>ユーザ名<br>メールアドレス</div></div>
    <div class="ds-compare-row"><div>② 認証<br>Authentication</div><div>「本当にその人か」を確認すること<br>識別情報の正当性を検証</div><div>パスワード<br>指紋・証明書</div></div>
    <div class="ds-compare-row"><div>③ 認可<br>Authorization</div><div>「何を使っていいか」権限を与えること<br>認証後に実施</div><div>ファイルRW権限<br>APIアクセス権</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">識別と認証の違いは？</div><div class="ds-qa-a">識別は「名乗るだけ」<br>認証は「本人確認」<br>識別だけでは不十分</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">認証と認可の違いは？</div><div class="ds-qa-a">認証 = 本人確認<br>認可 = 権限付与<br>認証後に認可が行われる</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">AAAの3つは？</div><div class="ds-qa-a">Authentication（認証）<br>Authorization（認可）<br>Accounting（記録・課金）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">アカウンティングとは？</div><div class="ds-qa-a">誰がいつ何をしたか<br>の記録・ログ管理<br>（課金にも使用）</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "IAM 関連用語",
    hint: "Identity and Access Management の主要概念 (6つ)",
    answer: ["① アカウンティング（Accounting）", "② AAAフレームワーク（RFC2904）", "③ シングルサインオン（SSO）・ID連携", "④ プロビジョニング機能", "⑤ IDaaS（ID as a Service）", "⑥ クレデンシャル情報"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    IAM は「誰が（Identity）何に（Access）どうアクセスできるか（Management）」を統合管理する仕組みの総称。<br>
    クラウド時代には <strong>IDaaS</strong>（クラウド型IAM）が主流になっている。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📋 主要概念の解説</div>
  <div class="ds-compare col2">
    <div class="ds-compare-head"><div>用語</div><div>内容・ポイント</div></div>
    <div class="ds-compare-row"><div>アカウンティング</div><div>誰がいつ何にアクセスしたかのログ記録。課金・監査・インシデント調査に使用</div></div>
    <div class="ds-compare-row"><div>AAAフレームワーク<br>（RFC 2904）</div><div>認証・認可・アカウンティングを統合管理する枠組み。RADIUSやTACACS+がこれを実装</div></div>
    <div class="ds-compare-row"><div>SSO・ID連携</div><div>1度のログインで複数サービスを利用可能にする仕組み。SAML・OAuth・OIDCなどで実現</div></div>
    <div class="ds-compare-row"><div>プロビジョニング</div><div>アカウント・権限の自動付与・変更・削除。デプロビジョニング = 退職時の削除・停止</div></div>
    <div class="ds-compare-row"><div>IDaaS</div><div>クラウド型のID管理サービス。例：Okta、Azure AD（Microsoft Entra ID）、Google Workspace</div></div>
    <div class="ds-compare-row"><div>クレデンシャル</div><div>認証に使う情報の総称。ID＋パスワードのセット、証明書、トークンなど</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">IDaaS の代表例は？</div><div class="ds-qa-a">Okta<br>Azure AD（Entra ID）<br>Google Workspace</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">デプロビジョニングとは？</div><div class="ds-qa-a">退職・異動時に<br>アカウント・権限を<br>停止・削除する処理</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">AAAの3つは？</div><div class="ds-qa-a">Authentication（認証）<br>Authorization（認可）<br>Accounting（記録・課金）</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "利用者IDの適切な運用",
    hint: "共有IDの問題と対策 (3つ)",
    answer: ["① 共有IDを使わない", "② 単独ユーザIDを定める", "③ 共有IDの廃止・利用者を特定できるIDを使用"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    「admin / password123 を全員で共有」は情報セキュリティの大敵。<br>
    不正があっても<strong>誰がやったかわからない</strong>ため責任追跡が不可能になる。<br>
    個人を特定できるIDを1人1つ割り当てることが基本原則。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚠️ 共有IDの問題点</div>
  <div class="ds-compare col2">
    <div class="ds-compare-head"><div>問題点</div><div>内容</div></div>
    <div class="ds-compare-row"><div>責任追跡不能</div><div>不正行為の犯人を特定できない。ログを見ても「誰が」かわからない</div></div>
    <div class="ds-compare-row"><div>最小権限原則違反</div><div>全員が全権限を持つことになり、過剰な権限付与につながる</div></div>
    <div class="ds-compare-row"><div>監査の無効化</div><div>アクセスログが監査証跡として機能しなくなる</div></div>
    <div class="ds-compare-row"><div>パスワード管理困難</div><div>退職者がいてもPW変更が困難。古い認証情報が残り続けるリスク</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">なぜ共有IDは禁止？</div><div class="ds-qa-a">不正行為者を特定できず<br>責任の所在が不明確<br>（監査が機能しない）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">最小権限の原則とは？</div><div class="ds-qa-a">業務に必要な最低限の<br>権限だけを付与すること<br>（Least Privilege）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">特権ID管理（PAM）とは？</div><div class="ds-qa-a">管理者権限を一元管理<br>払い出し・回収・<br>ログ記録を自動化</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">退職者のID対応は？</div><div class="ds-qa-a">即日アカウント無効化<br>（デプロビジョニング）<br>が必要</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "認証方式の種類",
    hint: "主な認証方式 (5つ)",
    answer: ["① 単要素認証（SFA）", "② 二要素認証（2FA）", "③ 多要素認証（MFA）", "④ リスクベース認証", "⑤ ステップアップ認証"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    認証方式は「<strong>何個の異なる種類の要素を使うか</strong>」と「<strong>状況に応じて強度を変えるか</strong>」で分類される。<br>
    現代のサービスでは MFA（多要素認証）が標準となりつつある。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ 認証方式の比較</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>方式</div><div>要素数・条件</div><div>特徴・例</div></div>
    <div class="ds-compare-row"><div>SFA（単要素認証）</div><div>1種類の要素</div><div>パスワードのみ<br>漏洩リスクが高い</div></div>
    <div class="ds-compare-row"><div>2FA（二要素認証）</div><div>2種類の異なる要素</div><div>PW ＋ SMS OTP<br>MFA の一種</div></div>
    <div class="ds-compare-row"><div>MFA（多要素認証）</div><div>2種類以上の異なる要素</div><div>PW ＋ 指紋 ＋ OTP<br>2FA も MFA に含まれる</div></div>
    <div class="ds-compare-row"><div>リスクベース認証</div><div>リスクに応じて変動</div><div>海外IPは追加認証を要求<br>普段と異なる行動で再認証</div></div>
    <div class="ds-compare-row"><div>ステップアップ認証</div><div>重要操作時に追加</div><div>高額送金・PW変更時<br>に再認証を要求</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">2FA と MFA の違いは？</div><div class="ds-qa-a">2FAは2要素、MFAは2要素以上<br>2FAはMFAの一種<br>（2FA ⊂ MFA）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">リスクベース認証の<br>判断要素は？</div><div class="ds-qa-a">IPアドレス（地域）<br>アクセス時刻<br>デバイス・行動パターン</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">同じ種類の要素を2つ<br>使うのはMFAか？</div><div class="ds-qa-a">MFAではない<br>「異なる種類」の要素を<br>組み合わせる必要がある</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "認証の主要素（3要素）",
    hint: "知識・所有・生体の3カテゴリ",
    answer: ["① 知識要素：何かを知っている（パスワード、PIN）", "② 所有要素：何かを持っている（スマートカード、OTP）", "③ 生体要素：何かである（指紋、顔認証）"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    認証の「強さ」は使う要素の数と<strong>種類（カテゴリ）</strong>で決まる。<br>
    同じカテゴリを2つ使っても多要素認証にはならない。<br>
    異なるカテゴリを組み合わせることが重要。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ 3要素の詳細比較</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>要素</div><div>具体例</div><div>長所</div><div>短所</div></div>
    <div class="ds-compare-row"><div>知識要素<br>Something<br>you know</div><div>パスワード<br>PIN<br>秘密の質問</div><div>追加コスト不要<br>いつでも変更可</div><div>忘れやすい<br>フィッシングで<br>盗まれる</div></div>
    <div class="ds-compare-row"><div>所持要素<br>Something<br>you have</div><div>スマートカード<br>OTPトークン<br>スマートフォン</div><div>フィッシング耐性<br>（物理的に必要）</div><div>紛失・盗難リスク<br>コストがかかる</div></div>
    <div class="ds-compare-row"><div>生体要素<br>Something<br>you are</div><div>指紋・顔<br>虹彩・静脈<br>声紋</div><div>忘れない<br>複製が困難</div><div>変更不可<br>漏洩が致命的<br>誤認識あり</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">PINとパスワードは<br>同じ要素？</div><div class="ds-qa-a">はい、どちらも知識要素<br>2つ組み合わせても<br>MFAにならない</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">OTPは何要素？</div><div class="ds-qa-a">所持要素<br>（スマホやトークンを<br>「持っている」から）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">生体情報が漏洩した<br>場合のリスクは？</div><div class="ds-qa-a">変更できないため致命的<br>生体情報は一生<br>使えなくなる可能性</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">2FAが有効な理由は？</div><div class="ds-qa-a">異なるカテゴリを組み合わせると<br>両方を同時に突破するのが<br>非常に困難になるため</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "バイオメトリクス認証の種類",
    hint: "生体認証の代表例 (5つ以上)",
    answer: ["① 指紋認証", "② 顔認証", "③ 虹彩認証（IRIS認識）", "④ 声紋認証", "⑤ 静脈認証", "⑥ 歩行認証"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    生体認証の精度評価には <strong>FAR（他人受入率）</strong> と <strong>FRR（本人拒否率）</strong> が使われる。<br>
    この2つはトレードオフの関係にあり、「どちらを優先するか」が設計の核心。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📊 FAR / FRR / EER の定義</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>指標</div><div>正式名</div><div>意味</div><div>低いほど</div></div>
    <div class="ds-compare-row"><div>FAR</div><div>False Acceptance Rate<br>（他人受入率）</div><div>他人を本人と<br>誤って認証する率</div><div>安全<br>（ただしFRR↑）</div></div>
    <div class="ds-compare-row"><div>FRR</div><div>False Rejection Rate<br>（本人拒否率）</div><div>本人を拒否<br>してしまう率</div><div>使いやすい<br>（ただしFAR↑）</div></div>
    <div class="ds-compare-row"><div>EER</div><div>Equal Error Rate<br>（等エラー率）</div><div>FAR＝FRRになる点<br>精度の総合評価指標</div><div>精度が高い</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔬 認証方式の比較</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>種類</div><div>精度</div><div>特徴・注意点</div></div>
    <div class="ds-compare-row"><div>虹彩認証</div><div>最高</div><div>個人差が最大、眼鏡・コンタクト影響あり</div></div>
    <div class="ds-compare-row"><div>静脈認証</div><div>高</div><div>偽造困難、死後は使用不可</div></div>
    <div class="ds-compare-row"><div>指紋認証</div><div>高</div><div>普及率高、傷・乾燥の影響あり</div></div>
    <div class="ds-compare-row"><div>顔認証</div><div>中</div><div>非接触・利便性高、変装・双子で突破の可能性</div></div>
    <div class="ds-compare-row"><div>声紋認証</div><div>中</div><div>非接触、録音による攻撃に注意</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">FAR と FRR の<br>トレードオフとは？</div><div class="ds-qa-a">FAR↓（安全）にすると<br>FRR↑（不便）になる<br>逆も然り（逆相関）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">EER とは？</div><div class="ds-qa-a">FAR と FRR が等しくなる点<br>値が小さいほど<br>認証精度が高い</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">最も精度が高い<br>生体認証は？</div><div class="ds-qa-a">虹彩認証<br>（個人差が最も大きく<br>偽造が最も困難）</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "IEEE 802.1X 認証の構成要素",
    hint: "ネットワーク認証の登場人物 (4つ)",
    answer: ["① サプリカント（Supplicant）：認証を求める端末", "② オーセンティケータ（Authenticator）：スイッチ/AP", "③ 認証サーバ（RADIUS サーバ）", "④ EAP（Extensible Authentication Protocol）でやりとり"],
    detail: `
<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    「社員証をかざさないとオフィスに入れない」仕組みのネットワーク版。<br>
    LAN ケーブルを刺したり Wi-Fi に繋いだだけでは通信できず、<strong>認証を通過した端末だけ</strong>をネットワークに入れるポートベースのアクセス制御。<br>
    企業の有線 LAN・無線 LAN で広く使われている標準規格。
  </div>
</div>

<div class="ds-section">
  <div class="ds-section-title">📡 通信の流れ（シーケンス図）</div>
  <div class="ds-diagram-card">
    <div class="ds-actors">
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#dbeafe">💻</div>
        <div class="ds-actor-name" style="color:#1e429f">サプリカント</div>
        <div class="ds-actor-sub">PC・スマホ</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#ede9fe">📡</div>
        <div class="ds-actor-name" style="color:#5b21b6">オーセンティ<br>ケータ</div>
        <div class="ds-actor-sub">スイッチ・AP</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#d1fae5">🖥️</div>
        <div class="ds-actor-name" style="color:#065f46">認証サーバ</div>
        <div class="ds-actor-sub">RADIUS</div>
      </div>
    </div>
    <div class="ds-svg-wrap">
      <svg viewBox="0 0 560 545" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'Hiragino Kaku Gothic ProN',sans-serif">
        <defs>
          <marker id="ab" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#3b82f6"/></marker>
          <marker id="ap" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#8b5cf6"/></marker>
          <marker id="ag" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#10b981"/></marker>
        </defs>
        <!-- ライフライン -->
        <line x1="88"  y1="2" x2="88"  y2="545" stroke="#bfdbfe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="280" y1="2" x2="280" y2="545" stroke="#ddd6fe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="472" y1="2" x2="472" y2="545" stroke="#a7f3d0" stroke-width="2" stroke-dasharray="6,5"/>
        <!-- 活性バー -->
        <rect x="83"  y="26" width="10" height="490" rx="3" fill="#bfdbfe" opacity="0.7"/>
        <rect x="275" y="26" width="10" height="490" rx="3" fill="#ddd6fe" opacity="0.7"/>
        <rect x="467" y="250" width="10" height="130" rx="3" fill="#a7f3d0" opacity="0.7"/>
        <!-- Step 1: S→A -->
        <circle cx="88" cy="45" r="11" fill="#1e429f"/>
        <text x="88" y="50" text-anchor="middle" font-size="11" font-weight="800" fill="white">1</text>
        <line x1="99" y1="45" x2="267" y2="45" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="183" y="36" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">LANに接続</text>
        <text x="183" y="61" text-anchor="middle" font-size="9" fill="#6b7280">EAP 以外の通信はすべて遮断される</text>
        <!-- Step 2: A→S -->
        <circle cx="280" cy="108" r="11" fill="#7c3aed"/>
        <text x="280" y="113" text-anchor="middle" font-size="11" font-weight="800" fill="white">2</text>
        <line x1="269" y1="108" x2="101" y2="108" stroke="#8b5cf6" stroke-width="2" marker-end="url(#ap)"/>
        <text x="183" y="99" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">EAP-Request / Identity</text>
        <text x="183" y="124" text-anchor="middle" font-size="9" fill="#6b7280">「あなたは誰ですか？」</text>
        <!-- Step 3: S→A -->
        <circle cx="88" cy="170" r="11" fill="#1e429f"/>
        <text x="88" y="175" text-anchor="middle" font-size="11" font-weight="800" fill="white">3</text>
        <line x1="99" y1="170" x2="267" y2="170" stroke="#3b82f6" stroke-width="2" marker-end="url(#ab)"/>
        <text x="183" y="161" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">EAP-Response / Identity</text>
        <text x="183" y="186" text-anchor="middle" font-size="9" fill="#6b7280">ユーザ名を送信（EAPOL）</text>
        <!-- Step 4: A→R -->
        <circle cx="280" cy="233" r="11" fill="#7c3aed"/>
        <text x="280" y="238" text-anchor="middle" font-size="11" font-weight="800" fill="white">4</text>
        <line x1="291" y1="233" x2="459" y2="233" stroke="#8b5cf6" stroke-width="2" marker-end="url(#ap)"/>
        <text x="376" y="224" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">RADIUS へ転送</text>
        <text x="376" y="249" text-anchor="middle" font-size="9" fill="#6b7280">EAPOL → RADIUS プロトコルに変換して中継</text>
        <!-- Step 5: R→A + relay A→S -->
        <circle cx="472" cy="295" r="11" fill="#059669"/>
        <text x="472" y="300" text-anchor="middle" font-size="11" font-weight="800" fill="white">5</text>
        <line x1="461" y1="295" x2="293" y2="295" stroke="#10b981" stroke-width="2" marker-end="url(#ag)"/>
        <line x1="267" y1="295" x2="101" y2="295" stroke="#10b981" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#ag)"/>
        <text x="183" y="286" text-anchor="middle" font-size="11" font-weight="700" fill="#065f46">チャレンジ（認証情報を要求）</text>
        <text x="183" y="311" text-anchor="middle" font-size="9" fill="#6b7280">オーセンティケータが端末へ中継 ↗（破線）</text>
        <!-- Step 6: S→A + relay A→R -->
        <circle cx="88" cy="360" r="11" fill="#1e429f"/>
        <text x="88" y="365" text-anchor="middle" font-size="11" font-weight="800" fill="white">6</text>
        <line x1="99"  y1="360" x2="267" y2="360" stroke="#3b82f6" stroke-width="2" marker-end="url(#ab)"/>
        <line x1="291" y1="360" x2="459" y2="360" stroke="#3b82f6" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#ab)"/>
        <text x="280" y="351" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">チャレンジレスポンス</text>
        <text x="280" y="376" text-anchor="middle" font-size="9" fill="#6b7280">パスワード・証明書などを送信 → 中継 → RADIUS へ</text>
        <!-- Step 7: 認証成功 -->
        <rect x="72" y="408" width="418" height="118" rx="12" fill="#f0fdf4" stroke="#6ee7b7" stroke-width="1.5"/>
        <text x="472" y="430" text-anchor="middle" font-size="9" font-weight="700" fill="#059669">RADIUS が判定</text>
        <circle cx="472" cy="448" r="11" fill="#059669"/>
        <text x="472" y="453" text-anchor="middle" font-size="11" font-weight="800" fill="white">7</text>
        <line x1="461" y1="448" x2="293" y2="448" stroke="#10b981" stroke-width="2.5" marker-end="url(#ag)"/>
        <line x1="267" y1="448" x2="101" y2="448" stroke="#10b981" stroke-width="2.5" marker-end="url(#ag)"/>
        <text x="280" y="439" text-anchor="middle" font-size="11" font-weight="800" fill="#065f46">Access-Accept</text>
        <text x="88"  y="480" text-anchor="middle" font-size="10" font-weight="800" fill="#059669">✓ ポート開放</text>
        <text x="310" y="480" text-anchor="middle" font-size="9" fill="#6b7280">スイッチがポートを開放し通信開始</text>
        <text x="310" y="497" text-anchor="middle" font-size="9" font-weight="700" fill="#dc2626">⚠️ 合否判定は RADIUS（スイッチでない）</text>
        <text x="280" y="514" text-anchor="middle" font-size="10" font-weight="700" fill="#1e429f">🎉 通信開始</text>
      </svg>
    </div>
  </div>
</div>

<div class="ds-section">
  <div class="ds-section-title">⚖️ RADIUS vs TACACS+</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>比較項目</div><div>🔵 RADIUS</div><div>🟣 TACACS+</div></div>
    <div class="ds-compare-row"><div>通信方式</div><div>UDP</div><div>TCP</div></div>
    <div class="ds-compare-row"><div>ポート番号</div><div>1812（認証）<br>1813（課金）</div><div>49</div></div>
    <div class="ds-compare-row"><div>暗号化範囲</div><div>パスワードのみ</div><div>パケット全体</div></div>
    <div class="ds-compare-row"><div>AAA の処理</div><div>認証＋認可を<br>まとめて処理</div><div>認証・認可・<br>課金を個別処理</div></div>
    <div class="ds-compare-row"><div>向いている用途</div><div>ユーザ認証<br>802.1X・VPN</div><div>ネットワーク機器<br>の管理・操作ログ</div></div>
  </div>
</div>

<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">認証の合否を<br>最終判断するのは？</div><div class="ds-qa-a">RADIUSサーバ<br>（スイッチでない）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">認証前の端末は<br>どうなる？</div><div class="ds-qa-a">EAP 以外<br>すべて遮断</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">端末↔スイッチ間の<br>プロトコルは？</div><div class="ds-qa-a">EAPOL<br>（EAP over LAN）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">スイッチ↔RADIUS間の<br>プロトコルは？</div><div class="ds-qa-a">RADIUS<br>（EAPでない）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">EAP-TLS の特徴は？</div><div class="ds-qa-a">双方向証明書<br>認証（最も安全）</div></div>
</div>
`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "EAP の主要方式",
    hint: "IEEE 802.1X で使われる認証プロトコル",
    answer: ["① EAP-TLS：クライアント証明書による双方向認証（最も安全）", "② EAP-TTLS：サーバ証明書のみ、クライアントは多様な認証", "③ EAP-FAST：PAC（Protected Access Credential）で動作", "④ PEAP：サーバ証明書でトンネル確立後に内部認証"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    EAP（Extensible Authentication Protocol）は IEEE 802.1X で使われる拡張可能な認証プロトコル。<br>
    <strong>クライアント証明書が必要かどうか</strong>がセキュリティ強度の差になる。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ EAP 方式の比較</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>方式</div><div>クライアント証明書</div><div>サーバ証明書</div><div>特徴</div></div>
    <div class="ds-compare-row"><div>EAP-TLS</div><div>✅ 必要</div><div>✅ 必要</div><div>双方向証明書認証<br>最も安全</div></div>
    <div class="ds-compare-row"><div>EAP-TTLS</div><div>❌ 不要</div><div>✅ 必要</div><div>TLSトンネル内で<br>多様な内部認証</div></div>
    <div class="ds-compare-row"><div>PEAP</div><div>❌ 不要</div><div>✅ 必要</div><div>MSCHAPv2等を<br>内部認証で使用</div></div>
    <div class="ds-compare-row"><div>EAP-FAST</div><div>❌ 不要</div><div>❌ 不要</div><div>PACという事前共有<br>キーを使用</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">最もセキュリティが<br>高いEAP方式は？</div><div class="ds-qa-a">EAP-TLS<br>（双方向証明書認証）<br>クライアント証明書が必要</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">PEAPの特徴は？</div><div class="ds-qa-a">サーバ証明書でTLSトンネルを確立<br>内部でMSCHAPv2等を使用<br>クライアント証明書は不要</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">EAP-FASTのPACとは？</div><div class="ds-qa-a">Protected Access Credential<br>事前に共有する認証情報<br>証明書の代わりに使用</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "FIDO 認証",
    hint: "パスワードレス認証の標準 (5つ)",
    answer: ["① FIDO Alliance が策定した標準", "② U2F（Universal 2nd Factor）：Web ブラウザ対応の2要素", "③ UAF（Universal Authentication Framework）：パスワードレス", "④ FIDO2 = WebAuthn + CTAP", "⑤ CTAP（Client to Authenticator Protocol）：端末-認証器間"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    FIDO は「パスワードの代わりに公開鍵暗号を使う」認証標準。<br>
    秘密鍵は端末（認証器）の中に閉じ込め、<strong>サーバにパスワードを送らない</strong>のでフィッシングが原理的に効かない。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ FIDO 規格の比較</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>規格</div><div>目的</div><div>特徴</div></div>
    <div class="ds-compare-row"><div>U2F</div><div>2要素認証の追加</div><div>パスワード＋セキュリティキー<br>既存PWと併用</div></div>
    <div class="ds-compare-row"><div>UAF</div><div>パスワードレス認証</div><div>生体認証や PIN で<br>パスワード不要</div></div>
    <div class="ds-compare-row"><div>FIDO2</div><div>Web標準のパスワードレス</div><div>WebAuthn（W3C標準）＋CTAP<br>ブラウザ・OS に標準搭載</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔑 FIDO2 認証フロー（シーケンス図）</div>
  <div class="ds-diagram-card">
    <div class="ds-actors">
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#dbeafe">🧑</div>
        <div class="ds-actor-name" style="color:#1e429f">ユーザ</div>
        <div class="ds-actor-sub">操作者</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#ede9fe">💻</div>
        <div class="ds-actor-name" style="color:#5b21b6">ブラウザ<br>/ 認証器</div>
        <div class="ds-actor-sub">CTAP/WebAuthn</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#d1fae5">🔐</div>
        <div class="ds-actor-name" style="color:#065f46">RPサーバ</div>
        <div class="ds-actor-sub">Relying Party</div>
      </div>
    </div>
    <div class="ds-svg-wrap">
      <svg viewBox="0 0 560 490" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'Hiragino Kaku Gothic ProN',sans-serif">
        <defs>
          <marker id="ab" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#3b82f6"/></marker>
          <marker id="ap" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#8b5cf6"/></marker>
          <marker id="ag" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#10b981"/></marker>
        </defs>
        <!-- ライフライン -->
        <line x1="88"  y1="2" x2="88"  y2="490" stroke="#bfdbfe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="280" y1="2" x2="280" y2="490" stroke="#ddd6fe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="472" y1="2" x2="472" y2="490" stroke="#a7f3d0" stroke-width="2" stroke-dasharray="6,5"/>
        <!-- 活性バー -->
        <rect x="83"  y="26" width="10" height="455" rx="3" fill="#bfdbfe" opacity="0.7"/>
        <rect x="275" y="26" width="10" height="455" rx="3" fill="#ddd6fe" opacity="0.7"/>
        <rect x="467" y="160" width="10" height="325" rx="3" fill="#a7f3d0" opacity="0.7"/>
        <!-- Step 1 -->
        <circle cx="88" cy="50" r="11" fill="#1e429f"/>
        <text x="88" y="55" text-anchor="middle" font-size="11" font-weight="800" fill="white">1</text>
        <line x1="99" y1="50" x2="267" y2="50" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="183" y="41" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">ログインボタン押下</text>
        <text x="183" y="66" text-anchor="middle" font-size="9" fill="#6b7280">ユーザがサービスにアクセス</text>
        <!-- Step 2 -->
        <circle cx="280" cy="113" r="11" fill="#7c3aed"/>
        <text x="280" y="118" text-anchor="middle" font-size="11" font-weight="800" fill="white">2</text>
        <line x1="291" y1="113" x2="459" y2="113" stroke="#8b5cf6" stroke-width="2" marker-end="url(#ap)"/>
        <text x="376" y="104" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">認証リクエスト</text>
        <text x="376" y="129" text-anchor="middle" font-size="9" fill="#6b7280">WebAuthn API 呼び出し</text>
        <!-- Step 3 -->
        <circle cx="472" cy="176" r="11" fill="#059669"/>
        <text x="472" y="181" text-anchor="middle" font-size="11" font-weight="800" fill="white">3</text>
        <line x1="461" y1="176" x2="293" y2="176" stroke="#10b981" stroke-width="2" marker-end="url(#ag)"/>
        <text x="376" y="167" text-anchor="middle" font-size="11" font-weight="700" fill="#065f46">チャレンジ（nonce）送信</text>
        <text x="376" y="192" text-anchor="middle" font-size="9" fill="#6b7280">ランダム値でリプレイ攻撃を防止</text>
        <!-- Step 4 -->
        <circle cx="280" cy="239" r="11" fill="#7c3aed"/>
        <text x="280" y="244" text-anchor="middle" font-size="11" font-weight="800" fill="white">4</text>
        <line x1="269" y1="239" x2="101" y2="239" stroke="#8b5cf6" stroke-width="2" marker-end="url(#ap)"/>
        <text x="183" y="230" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">生体認証を要求</text>
        <text x="183" y="255" text-anchor="middle" font-size="9" fill="#6b7280">指紋・FaceID・PINなど</text>
        <!-- Step 5 -->
        <circle cx="88" cy="302" r="11" fill="#1e429f"/>
        <text x="88" y="307" text-anchor="middle" font-size="11" font-weight="800" fill="white">5</text>
        <line x1="99" y1="302" x2="267" y2="302" stroke="#3b82f6" stroke-width="2" marker-end="url(#ab)"/>
        <text x="183" y="293" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">生体認証承認</text>
        <text x="183" y="318" text-anchor="middle" font-size="9" fill="#6b7280">認証器がアンロック</text>
        <!-- 内部処理ボックス -->
        <rect x="188" y="323" width="184" height="42" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="280" y="338" text-anchor="middle" font-size="9" font-weight="700" fill="#92400e">🔐 認証器内部処理</text>
        <text x="280" y="354" text-anchor="middle" font-size="9" fill="#92400e">秘密鍵でチャレンジに署名（鍵は外に出ない）</text>
        <!-- Step 6 -->
        <circle cx="280" cy="385" r="11" fill="#7c3aed"/>
        <text x="280" y="390" text-anchor="middle" font-size="11" font-weight="800" fill="white">6</text>
        <line x1="291" y1="385" x2="459" y2="385" stroke="#8b5cf6" stroke-width="2.5" marker-end="url(#ap)"/>
        <text x="376" y="376" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">署名済みアサーション送信</text>
        <text x="376" y="401" text-anchor="middle" font-size="9" fill="#6b7280">credential.id ＋ 署名</text>
        <!-- Step 7 成功エリア -->
        <rect x="60" y="413" width="430" height="72" rx="12" fill="#f0fdf4" stroke="#6ee7b7" stroke-width="1.5"/>
        <text x="472" y="430" text-anchor="middle" font-size="9" font-weight="700" fill="#059669">登録済み公開鍵で署名を検証</text>
        <circle cx="472" cy="448" r="11" fill="#059669"/>
        <text x="472" y="453" text-anchor="middle" font-size="11" font-weight="800" fill="white">7</text>
        <line x1="461" y1="448" x2="101" y2="448" stroke="#10b981" stroke-width="2.5" marker-end="url(#ag)"/>
        <text x="280" y="439" text-anchor="middle" font-size="11" font-weight="800" fill="#065f46">認証成功・セッション確立</text>
        <text x="88"  y="472" text-anchor="middle" font-size="10" font-weight="800" fill="#059669">✓ ログイン完了</text>
        <text x="340" y="472" text-anchor="middle" font-size="9" font-weight="700" fill="#dc2626">⚠️ パスワードはネットワークを流れない</text>
      </svg>
    </div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">FIDO2 の2つの<br>コンポーネントは？</div><div class="ds-qa-a">WebAuthn（ブラウザ-サーバ間）<br>＋<br>CTAP（ブラウザ-認証器間）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">フィッシング耐性が<br>ある理由は？</div><div class="ds-qa-a">チャレンジがドメインに紐づく<br>偽サイトでは署名が<br>RPサーバで検証失敗する</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">パスキーとは？</div><div class="ds-qa-a">FIDO2の応用<br>秘密鍵をクラウドで同期可能<br>複数デバイスで使える</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">秘密鍵はどこに？</div><div class="ds-qa-a">認証器（TPMチップ・<br>セキュリティキー等）に<br>安全に格納。外に出ない</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "アクセス制御モデルの種類",
    hint: "DAC・MAC・RBAC の違い",
    answer: ["① DAC（Discretionary Access Control）任意アクセス制御：所有者が権限設定", "② MAC（Mandatory Access Control）強制アクセス制御：システムが一元管理", "③ RBAC（Role-Based Access Control）ロールベース：役割に応じた権限付与"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    アクセス制御モデルは「<strong>誰が権限を決めるか</strong>」で分類される。<br>
    DACは所有者、MACはシステム、RBACは役割（ロール）が権限を管理する。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ アクセス制御モデルの比較</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>モデル</div><div>権限設定者</div><div>特徴</div><div>主な用途</div></div>
    <div class="ds-compare-row"><div>DAC<br>任意アクセス制御</div><div>リソースの所有者</div><div>柔軟・管理しやすい<br>所有者が自由に設定</div><div>Unix・Windowsの<br>ファイル権限</div></div>
    <div class="ds-compare-row"><div>MAC<br>強制アクセス制御</div><div>システム管理者<br>（ラベルで強制）</div><div>厳格・所有者でも<br>変更できない</div><div>政府・軍・<br>機密情報システム</div></div>
    <div class="ds-compare-row"><div>RBAC<br>ロールベース</div><div>管理者<br>（役割単位で設定）</div><div>役割変更時にロール<br>付け替えで対応可能</div><div>企業の<br>業務システム</div></div>
    <div class="ds-compare-row"><div>ABAC<br>属性ベース</div><div>ポリシーで動的制御</div><div>属性の組み合わせで<br>きめ細かい制御</div><div>クラウド・<br>ゼロトラスト</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">MACがなぜ「強制」か？</div><div class="ds-qa-a">ユーザ（所有者）が権限を<br>変更できないため<br>システムが強制する</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">RBACの利点は？</div><div class="ds-qa-a">役割変更時にロール付け替えだけで<br>対応可能（個別設定不要）<br>権限管理が効率的</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">政府・軍システムは<br>どのモデル？</div><div class="ds-qa-a">MAC（強制アクセス制御）<br>機密ラベルで強制管理<br>所有者でも変更不可</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "シングルサインオン（SSO）の仕組み",
    hint: "主な SSO・ID連携プロトコル (4つ)",
    answer: ["① SAML（Security Assertion Markup Language）：XMLベース", "② OAuth 2.0：リソースへの認可委譲", "③ OIDC（OpenID Connect）：OAuth 2.0上の認証レイヤ", "④ SPNEGO：Kerberos を HTTP に統合"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    「一度ログインすれば複数サービスをシームレスに使える」仕組み。<br>
    プロトコルによって<strong>認証（誰か）</strong>と<strong>認可（何ができるか）</strong>のどちらを主に扱うかが異なる。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ SSO プロトコルの比較</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>プロトコル</div><div>主目的</div><div>ベース技術</div><div>主な用途</div></div>
    <div class="ds-compare-row"><div>SAML 2.0</div><div>認証</div><div>XML</div><div>企業内SSO・B2B連携</div></div>
    <div class="ds-compare-row"><div>OAuth 2.0</div><div>認可</div><div>JSON/REST</div><div>APIへのアクセス委譲</div></div>
    <div class="ds-compare-row"><div>OIDC<br>（OpenID Connect）</div><div>認証＋認可</div><div>OAuth 2.0拡張<br>（IDトークン追加）</div><div>ソーシャルログイン<br>Googleログイン等</div></div>
    <div class="ds-compare-row"><div>SPNEGO</div><div>認証</div><div>Kerberos拡張</div><div>Windows AD環境<br>のWebアクセス</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">SAMLとOAuthの<br>違いは？</div><div class="ds-qa-a">SAMLは認証が主目的<br>OAuthは認可が主目的<br>OIDCはOAuthに認証を追加</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">IdP と SP とは？</div><div class="ds-qa-a">IdP = 認証するサービス<br>（Google、AD等）<br>SP = 認証を受け入れるサービス</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">OIDCのIDトークンは？</div><div class="ds-qa-a">JWT形式で発行<br>ユーザ情報（sub, nameなど）<br>が含まれる</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "Kerberos 認証の構成要素",
    hint: "企業 AD 環境の認証基盤",
    answer: ["① KDC（Key Distribution Center）：AS + TGS + KDB で構成", "② AS（Authentication Server）：TGT 発行", "③ TGS（Ticket Granting Server）：サービスチケット発行", "④ レルム（Realm）：Kerberos の管理ドメイン", "⑤ ST（Service Ticket）：サービスへのアクセス許可"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    Kerberos は「チケット」を使った認証方式。<br>
    パスワードをネットワークに流さず、<strong>TGT → ST</strong> の2段階チケットでサービスにアクセスする。<br>
    Windows Active Directory の標準認証プロトコル。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔑 Kerberos 認証フロー（シーケンス図）</div>
  <div class="ds-diagram-card">
    <div class="ds-actors">
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#dbeafe">💻</div>
        <div class="ds-actor-name" style="color:#1e429f">クライアント</div>
        <div class="ds-actor-sub">PC・端末</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#ede9fe">🏛️</div>
        <div class="ds-actor-name" style="color:#5b21b6">KDC<br>（AS＋TGS）</div>
        <div class="ds-actor-sub">認証センター</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#d1fae5">🖥️</div>
        <div class="ds-actor-name" style="color:#065f46">サービス<br>サーバ</div>
        <div class="ds-actor-sub">ファイルサーバ等</div>
      </div>
    </div>
    <div class="ds-svg-wrap">
      <svg viewBox="0 0 560 470" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'Hiragino Kaku Gothic ProN',sans-serif">
        <defs>
          <marker id="ab" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#3b82f6"/></marker>
          <marker id="ap" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#8b5cf6"/></marker>
          <marker id="ag" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#10b981"/></marker>
        </defs>
        <!-- ライフライン -->
        <line x1="88"  y1="2" x2="88"  y2="470" stroke="#bfdbfe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="280" y1="2" x2="280" y2="470" stroke="#ddd6fe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="472" y1="2" x2="472" y2="470" stroke="#a7f3d0" stroke-width="2" stroke-dasharray="6,5"/>
        <!-- 活性バー -->
        <rect x="83"  y="26" width="10" height="415" rx="3" fill="#bfdbfe" opacity="0.7"/>
        <rect x="275" y="26" width="10" height="415" rx="3" fill="#ddd6fe" opacity="0.7"/>
        <rect x="467" y="285" width="10" height="155" rx="3" fill="#a7f3d0" opacity="0.7"/>
        <!-- KDCの役割ラベル -->
        <text x="280" y="68" text-anchor="middle" font-size="8" font-weight="700" fill="#7c3aed" opacity="0.7">▼ AS フェーズ</text>
        <text x="280" y="194" text-anchor="middle" font-size="8" font-weight="700" fill="#7c3aed" opacity="0.7">▼ TGS フェーズ</text>
        <!-- Step 1: Client→KDC AS_REQ -->
        <circle cx="88" cy="80" r="11" fill="#1e429f"/>
        <text x="88" y="85" text-anchor="middle" font-size="11" font-weight="800" fill="white">1</text>
        <line x1="99" y1="80" x2="267" y2="80" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="183" y="71" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">AS_REQ（認証要求）</text>
        <text x="183" y="96" text-anchor="middle" font-size="9" fill="#6b7280">ユーザ名＋暗号化タイムスタンプ</text>
        <!-- Step 2: KDC→Client AS_REP (TGT) -->
        <circle cx="280" cy="143" r="11" fill="#7c3aed"/>
        <text x="280" y="148" text-anchor="middle" font-size="11" font-weight="800" fill="white">2</text>
        <line x1="269" y1="143" x2="101" y2="143" stroke="#8b5cf6" stroke-width="2.5" marker-end="url(#ap)"/>
        <text x="183" y="134" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">AS_REP（TGT 発行）</text>
        <text x="183" y="159" text-anchor="middle" font-size="9" fill="#6b7280">krbtgt 秘密鍵で暗号化</text>
        <!-- Step 3: Client→KDC TGS_REQ -->
        <circle cx="88" cy="206" r="11" fill="#1e429f"/>
        <text x="88" y="211" text-anchor="middle" font-size="11" font-weight="800" fill="white">3</text>
        <line x1="99" y1="206" x2="267" y2="206" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="183" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">TGS_REQ（ST 要求）</text>
        <text x="183" y="222" text-anchor="middle" font-size="9" fill="#6b7280">TGT ＋ サービス要求</text>
        <!-- Step 4: KDC→Client TGS_REP (ST) -->
        <circle cx="280" cy="269" r="11" fill="#7c3aed"/>
        <text x="280" y="274" text-anchor="middle" font-size="11" font-weight="800" fill="white">4</text>
        <line x1="269" y1="269" x2="101" y2="269" stroke="#8b5cf6" stroke-width="2.5" marker-end="url(#ap)"/>
        <text x="183" y="260" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">TGS_REP（ST 発行）</text>
        <text x="183" y="285" text-anchor="middle" font-size="9" fill="#6b7280">サービス秘密鍵で暗号化</text>
        <!-- Step 5: Client→Service AP_REQ -->
        <circle cx="88" cy="332" r="11" fill="#1e429f"/>
        <text x="88" y="337" text-anchor="middle" font-size="11" font-weight="800" fill="white">5</text>
        <line x1="99" y1="332" x2="459" y2="332" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="280" y="323" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">AP_REQ（ST を提示）</text>
        <text x="280" y="348" text-anchor="middle" font-size="9" fill="#6b7280">KDCを経由しない</text>
        <!-- Step 6 成功エリア -->
        <rect x="60" y="363" width="430" height="100" rx="12" fill="#f0fdf4" stroke="#6ee7b7" stroke-width="1.5"/>
        <text x="472" y="381" text-anchor="middle" font-size="9" font-weight="700" fill="#059669">ST を復号して検証</text>
        <circle cx="472" cy="399" r="11" fill="#059669"/>
        <text x="472" y="404" text-anchor="middle" font-size="11" font-weight="800" fill="white">6</text>
        <line x1="461" y1="399" x2="101" y2="399" stroke="#10b981" stroke-width="2.5" marker-end="url(#ag)"/>
        <text x="280" y="390" text-anchor="middle" font-size="11" font-weight="800" fill="#065f46">AP_REP（認証成功）</text>
        <text x="88"  y="423" text-anchor="middle" font-size="10" font-weight="800" fill="#059669">✓ サービス利用開始</text>
        <text x="340" y="423" text-anchor="middle" font-size="9" fill="#6b7280">パスワードは一度もネットワークを流れない</text>
        <text x="280" y="450" text-anchor="middle" font-size="9" font-weight="700" fill="#dc2626">⚠️ TGT は KDC だけが復号可能 / ST はサービスだけが復号可能</text>
      </svg>
    </div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ TGT と ST の違い</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>チケット</div><div>発行者</div><div>用途</div></div>
    <div class="ds-compare-row"><div>TGT<br>（Ticket Granting Ticket）</div><div>KDC（AS）</div><div>STを取得するための認証済み証明書<br>krbtgt鍵で暗号化</div></div>
    <div class="ds-compare-row"><div>ST<br>（Service Ticket）</div><div>KDC（TGS）</div><div>特定サービスへのアクセス許可証<br>サービスの秘密鍵で暗号化</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">TGT の役割は？</div><div class="ds-qa-a">「認証済み証明書」<br>これを使ってSTを<br>取得する</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">STがサービス秘密鍵で<br>暗号化される理由は？</div><div class="ds-qa-a">そのサービスサーバだけが<br>復号できる<br>（改ざん防止）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">リプレイ攻撃防止の<br>仕組みは？</div><div class="ds-qa-a">タイムスタンプを使用<br>時刻差5分以内のみ有効<br>（時刻同期が重要）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">レルムとは？</div><div class="ds-qa-a">Kerberosの管理ドメイン<br>AD環境では<br>ドメイン名に対応</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "Kerberos への攻撃",
    hint: "チケット偽造攻撃の代表例",
    answer: ["① ゴールデンチケット攻撃：krbtgt アカウントのハッシュを奪取して TGT を偽造", "② シルバーチケット攻撃：サービスアカウントのハッシュで ST を偽造", "③ Pass-the-Ticket：正規チケットを盗んで再利用"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    Kerberos 攻撃は「チケットの偽造・盗難」が基本。<br>
    攻撃者が <strong>krbtgt のハッシュ</strong>を入手すると、KDC 不要で任意のTGTを作成できる（最も危険）。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚔️ 主な攻撃の比較</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>攻撃名</div><div>対象チケット</div><div>必要な情報</div><div>影響範囲</div></div>
    <div class="ds-compare-row"><div>ゴールデン<br>チケット攻撃</div><div>TGT（偽造）</div><div>krbtgtの<br>NTLMハッシュ</div><div>全サービスへ<br>永続アクセス可能</div></div>
    <div class="ds-compare-row"><div>シルバー<br>チケット攻撃</div><div>ST（偽造）</div><div>サービスアカウントの<br>NTLMハッシュ</div><div>特定サービスのみ<br>（影響は限定的）</div></div>
    <div class="ds-compare-row"><div>Pass-the-Ticket</div><div>TGT/ST<br>（盗用）</div><div>メモリから<br>盗んだ正規チケット</div><div>チケットの<br>有効期限まで</div></div>
    <div class="ds-compare-row"><div>Kerberoasting</div><div>ST（オフライン<br>クラック）</div><div>低権限ユーザ権限<br>のみ</div><div>サービスアカウントの<br>PW漏洩リスク</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">ゴールデンチケット<br>対策は？</div><div class="ds-qa-a">krbtgtのパスワードを<br>定期変更（2回以上）<br>特権IDの厳格管理</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">GoldenとSilverの<br>違いは？</div><div class="ds-qa-a">Golden：TGT偽造→全サービスアクセス<br>Silver：ST偽造→特定サービスのみ<br>Goldenの方が危険</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">Kerberoastingとは？</div><div class="ds-qa-a">SPNを持つサービスアカウントの<br>STを取得しオフラインで<br>パスワードをクラックする手法</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "OAuth 2.0 の登場人物",
    hint: "認可フローの4者",
    answer: ["① Resource Owner：リソースの所有者（ユーザ）", "② Client：アクセスを求めるアプリ", "③ Resource Server：保護されたリソースを持つサーバ", "④ Authorization Server：アクセストークンを発行するサーバ"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    OAuth 2.0 は「認可の委譲」プロトコル。<br>
    「Google の情報を別のアプリに使わせる」ときに、<strong>パスワードを渡さずに</strong>アクセス権だけを委譲する仕組み。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔄 Authorization Code フロー（シーケンス図）</div>
  <div class="ds-diagram-card">
    <div class="ds-actors col4">
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#dbeafe">🧑</div>
        <div class="ds-actor-name" style="color:#1e429f">ユーザ</div>
        <div class="ds-actor-sub">Resource Owner</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#ede9fe">📱</div>
        <div class="ds-actor-name" style="color:#5b21b6">クライアント<br>App</div>
        <div class="ds-actor-sub">Client</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#fef3c7">🔑</div>
        <div class="ds-actor-name" style="color:#92400e">認可サーバ</div>
        <div class="ds-actor-sub">Auth Server</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#d1fae5">🗄️</div>
        <div class="ds-actor-name" style="color:#065f46">リソース<br>サーバ</div>
        <div class="ds-actor-sub">Resource Server</div>
      </div>
    </div>
    <div class="ds-svg-wrap">
      <svg viewBox="0 0 640 530" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'Hiragino Kaku Gothic ProN',sans-serif">
        <defs>
          <marker id="ab" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#3b82f6"/></marker>
          <marker id="ap" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#8b5cf6"/></marker>
          <marker id="ag" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#d97706"/></marker>
          <marker id="ao" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#10b981"/></marker>
        </defs>
        <!-- ライフライン: User=75, Client=225, Auth=415, Resource=575 -->
        <line x1="75"  y1="2" x2="75"  y2="530" stroke="#bfdbfe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="225" y1="2" x2="225" y2="530" stroke="#ddd6fe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="415" y1="2" x2="415" y2="530" stroke="#fde68a" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="575" y1="2" x2="575" y2="530" stroke="#a7f3d0" stroke-width="2" stroke-dasharray="6,5"/>
        <!-- 活性バー -->
        <rect x="70"  y="26" width="10" height="485" rx="3" fill="#bfdbfe" opacity="0.7"/>
        <rect x="220" y="26" width="10" height="485" rx="3" fill="#ddd6fe" opacity="0.7"/>
        <rect x="410" y="90"  width="10" height="350" rx="3" fill="#fde68a" opacity="0.7"/>
        <rect x="570" y="460" width="10" height="55"  rx="3" fill="#a7f3d0" opacity="0.7"/>
        <!-- Step 1: User→Client -->
        <circle cx="75" cy="50" r="11" fill="#1e429f"/>
        <text x="75" y="55" text-anchor="middle" font-size="11" font-weight="800" fill="white">1</text>
        <line x1="86" y1="50" x2="211" y2="50" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="150" y="41" text-anchor="middle" font-size="10" font-weight="700" fill="#1d4ed8">ログイン要求</text>
        <text x="150" y="66" text-anchor="middle" font-size="8" fill="#6b7280">「Googleでログイン」ボタン</text>
        <!-- Step 2: Client→Auth -->
        <circle cx="225" cy="113" r="11" fill="#7c3aed"/>
        <text x="225" y="118" text-anchor="middle" font-size="11" font-weight="800" fill="white">2</text>
        <line x1="236" y1="113" x2="401" y2="113" stroke="#8b5cf6" stroke-width="2" marker-end="url(#ap)"/>
        <text x="318" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#6d28d9">認可リクエスト</text>
        <text x="318" y="129" text-anchor="middle" font-size="8" fill="#6b7280">scope・redirect_uri 付き</text>
        <!-- Step 3: Auth→User -->
        <circle cx="415" cy="176" r="11" fill="#d97706"/>
        <text x="415" y="181" text-anchor="middle" font-size="11" font-weight="800" fill="white">3</text>
        <line x1="404" y1="176" x2="86" y2="176" stroke="#d97706" stroke-width="2" marker-end="url(#ag)"/>
        <text x="240" y="167" text-anchor="middle" font-size="10" font-weight="700" fill="#92400e">ログイン・同意画面</text>
        <text x="240" y="192" text-anchor="middle" font-size="8" fill="#6b7280">ブラウザにリダイレクト</text>
        <!-- Step 4: User→Auth -->
        <circle cx="75" cy="239" r="11" fill="#1e429f"/>
        <text x="75" y="244" text-anchor="middle" font-size="11" font-weight="800" fill="white">4</text>
        <line x1="86" y1="239" x2="401" y2="239" stroke="#3b82f6" stroke-width="2" marker-end="url(#ab)"/>
        <text x="240" y="230" text-anchor="middle" font-size="10" font-weight="700" fill="#1d4ed8">認証・アクセス同意</text>
        <text x="240" y="255" text-anchor="middle" font-size="8" fill="#6b7280">ユーザがPW入力＋権限に同意</text>
        <!-- Step 5: Auth→Client -->
        <circle cx="415" cy="302" r="11" fill="#d97706"/>
        <text x="415" y="307" text-anchor="middle" font-size="11" font-weight="800" fill="white">5</text>
        <line x1="404" y1="302" x2="236" y2="302" stroke="#d97706" stroke-width="2.5" marker-end="url(#ag)"/>
        <text x="318" y="293" text-anchor="middle" font-size="10" font-weight="700" fill="#92400e">認可コード発行</text>
        <text x="318" y="318" text-anchor="middle" font-size="8" fill="#6b7280">redirect_uri へリダイレクト</text>
        <!-- Step 6: Client→Auth (back channel, dashed) -->
        <circle cx="225" cy="365" r="11" fill="#7c3aed"/>
        <text x="225" y="370" text-anchor="middle" font-size="11" font-weight="800" fill="white">6</text>
        <line x1="236" y1="365" x2="401" y2="365" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="6,3" marker-end="url(#ap)"/>
        <text x="318" y="356" text-anchor="middle" font-size="10" font-weight="700" fill="#6d28d9">トークンリクエスト</text>
        <text x="318" y="381" text-anchor="middle" font-size="8" fill="#6b7280">認可コード＋client_secret（バックチャネル）</text>
        <!-- Step 7: Auth→Client -->
        <circle cx="415" cy="418" r="11" fill="#d97706"/>
        <text x="415" y="423" text-anchor="middle" font-size="11" font-weight="800" fill="white">7</text>
        <line x1="404" y1="418" x2="236" y2="418" stroke="#d97706" stroke-width="2.5" marker-end="url(#ag)"/>
        <text x="318" y="409" text-anchor="middle" font-size="10" font-weight="700" fill="#92400e">アクセストークン発行</text>
        <text x="318" y="434" text-anchor="middle" font-size="8" fill="#6b7280">＋リフレッシュトークン</text>
        <!-- Step 8: Client→Resource -->
        <rect x="55" y="452" width="535" height="72" rx="12" fill="#f0fdf4" stroke="#6ee7b7" stroke-width="1.5"/>
        <circle cx="225" cy="472" r="11" fill="#7c3aed"/>
        <text x="225" y="477" text-anchor="middle" font-size="11" font-weight="800" fill="white">8</text>
        <line x1="236" y1="472" x2="561" y2="472" stroke="#10b981" stroke-width="2.5" marker-end="url(#ao)"/>
        <text x="400" y="463" text-anchor="middle" font-size="10" font-weight="700" fill="#065f46">API 呼び出し（Bearer Token）</text>
        <text x="400" y="508" text-anchor="middle" font-size="9" font-weight="700" fill="#065f46">← リソース返却</text>
        <text x="180" y="508" text-anchor="middle" font-size="8" fill="#6b7280">⚠️ step6の破線がバックチャネル（安全の核心）</text>
      </svg>
    </div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">なぜ認可コードを<br>経由する？</div><div class="ds-qa-a">アクセストークンをURLに<br>露出させないため<br>バックチャネルで安全に交換</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">PKCE とは？</div><div class="ds-qa-a">Proof Key for Code Exchange<br>認可コードの横取り防止<br>SPAやモバイルアプリで使用</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">scope とは？</div><div class="ds-qa-a">要求するアクセス権限の範囲<br>例：read:email, write:posts<br>最小限のscopeを要求すべき</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">OAuthは認証か認可か？</div><div class="ds-qa-a">認可（Authorization）が主目的<br>認証はOIDCを使う<br>OAuth単体は認証ではない</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "JWT（JSON Web Token）の構造",
    hint: "3つのパートで構成",
    answer: ["① Header：アルゴリズム（alg）とトークン種別（typ）", "② Payload：クレーム情報（sub, iat, exp など）", "③ Signature：ヘッダ＋ペイロードをアルゴリズムで署名した値", "※ Base64url エンコードして . で結合"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    JWT は「.」で区切られた3つの Base64url エンコード文字列。<br>
    <strong>ペイロードは暗号化されていない</strong>（誰でも読める）が、署名により改ざんを検知できる。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔧 JWT の構造</div>
  <div class="ds-compare col2">
    <div class="ds-compare-head"><div>パート</div><div>内容・例</div></div>
    <div class="ds-compare-row"><div>Header<br>（ヘッダ）</div><div>アルゴリズム（alg）とトークン種別（typ）を指定<br>例：{"alg":"RS256","typ":"JWT"}</div></div>
    <div class="ds-compare-row"><div>Payload<br>（ペイロード）</div><div>クレーム情報を格納。Base64urlのみで誰でも読める<br>例：{"sub":"1234","name":"John","exp":1700000000}</div></div>
    <div class="ds-compare-row"><div>Signature<br>（署名）</div><div>Header+Payloadをアルゴリズムで署名した値<br>改ざん検知に使用（秘密鍵または共有鍵）</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📋 主要クレームの一覧</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>クレーム</div><div>意味</div><div>値の例</div></div>
    <div class="ds-compare-row"><div>sub</div><div>Subject（主体）</div><div>ユーザID</div></div>
    <div class="ds-compare-row"><div>iss</div><div>Issuer（発行者）</div><div>https://auth.example.com</div></div>
    <div class="ds-compare-row"><div>aud</div><div>Audience（受取人）</div><div>https://api.example.com</div></div>
    <div class="ds-compare-row"><div>iat</div><div>Issued At（発行時刻）</div><div>UnixTime</div></div>
    <div class="ds-compare-row"><div>exp</div><div>Expiration（有効期限）</div><div>UnixTime</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">ペイロードは<br>暗号化されている？</div><div class="ds-qa-a">いいえ。Base64urlのみ<br>誰でもデコードして読める<br>（署名はされている）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">JWSとJWEの違いは？</div><div class="ds-qa-a">JWS = 署名のみ（内容は読める）<br>JWE = 暗号化（内容は読めない）<br>通常のJWTはJWS</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">HS256とRS256の<br>違いは？</div><div class="ds-qa-a">HS256 = 共通鍵（HMAC）<br>RS256 = 公開鍵（RSA署名）<br>RS256は検証に秘密鍵不要</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "JWT のセキュリティ対策",
    hint: "JWT を安全に使うための注意点 (4つ)",
    answer: ["① サーバ側で alg=\"none\" を拒否する", "② XSS 対策・CSRF 対策を実施", "③ 適切な CORS 設定", "④ 有効期限（exp）を短く設定し、リフレッシュトークンを使用"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    JWT はステートレスで便利だが、設計ミスで重大な脆弱性につながる。<br>
    特に <strong>alg:none 攻撃</strong>と<strong>弱い秘密鍵</strong>が試験で頻出。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚔️ JWT に対する主な攻撃と対策</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>攻撃</div><div>内容</div><div>対策</div></div>
    <div class="ds-compare-row"><div>alg:none 攻撃</div><div>algを"none"に書き換えて署名検証をスキップ</div><div>サーバ側でnoneを拒否<br>algを強制指定</div></div>
    <div class="ds-compare-row"><div>弱い秘密鍵<br>クラック</div><div>HS256の短い秘密鍵を<br>オフラインでブルートフォース</div><div>256bit以上の<br>ランダムな秘密鍵を使用</div></div>
    <div class="ds-compare-row"><div>アルゴリズム<br>混同攻撃</div><div>RS256の公開鍵を<br>HS256のsecretとして利用</div><div>サーバ側でalgを<br>固定・強制指定</div></div>
    <div class="ds-compare-row"><div>XSSによる<br>トークン盗取</div><div>localStorageのJWTを<br>XSSで窃取</div><div>HttpOnly Cookieに<br>保存する</div></div>
    <div class="ds-compare-row"><div>有効期限なし</div><div>expなしで永久に有効<br>漏洩時に無効化できない</div><div>expを短く設定（15分等）<br>リフレッシュトークンを使用</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">JWTをどこに保存<br>すべき？</div><div class="ds-qa-a">HttpOnly Cookie が推奨<br>localStorageはXSSで<br>盗まれる可能性あり</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">JWTの無効化が<br>難しい理由は？</div><div class="ds-qa-a">ステートレスのため<br>サーバ側で「使用済み」を<br>管理できない</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">リフレッシュトークンの<br>役割は？</div><div class="ds-qa-a">アクセストークン失効後に<br>新しいトークンを取得<br>（再ログイン不要）</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "SAML 2.0 の主要概念",
    hint: "XML ベースの認証連携 (4つ)",
    answer: ["① アサーション（Assertion）：認証・属性・認可情報を含む XML", "② SAML リクエスト：SP → IdP への認証要求", "③ SAML レスポンス：IdP → SP への認証結果", "④ SSO プロファイル：Web ブラウザ SSO が代表"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    SAML は XML ベースの認証連携プロトコル。<br>
    IdP（認証サービス）が署名付き<strong>アサーション</strong>を発行し、SP（サービス）がそれを信頼してアクセスを許可する。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">🔄 SP-Initiated SSO フロー（シーケンス図）</div>
  <div class="ds-diagram-card">
    <div class="ds-actors">
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#dbeafe">🌐</div>
        <div class="ds-actor-name" style="color:#1e429f">ブラウザ</div>
        <div class="ds-actor-sub">ユーザ操作</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#ede9fe">🏢</div>
        <div class="ds-actor-name" style="color:#5b21b6">SP<br>（サービス）</div>
        <div class="ds-actor-sub">Service Provider</div>
      </div>
      <div class="ds-actor">
        <div class="ds-actor-icon" style="background:#fef3c7">🔑</div>
        <div class="ds-actor-name" style="color:#92400e">IdP<br>（認証）</div>
        <div class="ds-actor-sub">Identity Provider</div>
      </div>
    </div>
    <div class="ds-svg-wrap">
      <svg viewBox="0 0 560 540" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'Hiragino Kaku Gothic ProN',sans-serif">
        <defs>
          <marker id="ab" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#3b82f6"/></marker>
          <marker id="ap" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#8b5cf6"/></marker>
          <marker id="ag" markerWidth="9" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0,9 3.5,0 7" fill="#d97706"/></marker>
        </defs>
        <!-- ライフライン -->
        <line x1="88"  y1="2" x2="88"  y2="540" stroke="#bfdbfe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="280" y1="2" x2="280" y2="540" stroke="#ddd6fe" stroke-width="2" stroke-dasharray="6,5"/>
        <line x1="472" y1="2" x2="472" y2="540" stroke="#fde68a" stroke-width="2" stroke-dasharray="6,5"/>
        <!-- 活性バー -->
        <rect x="83"  y="26" width="10" height="505" rx="3" fill="#bfdbfe" opacity="0.7"/>
        <rect x="275" y="26" width="10" height="505" rx="3" fill="#ddd6fe" opacity="0.7"/>
        <rect x="467" y="160" width="10" height="370" rx="3" fill="#fde68a" opacity="0.7"/>
        <!-- Step 1: Browser→SP -->
        <circle cx="88" cy="50" r="11" fill="#1e429f"/>
        <text x="88" y="55" text-anchor="middle" font-size="11" font-weight="800" fill="white">1</text>
        <line x1="99" y1="50" x2="267" y2="50" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="183" y="41" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">リソースへアクセス</text>
        <text x="183" y="66" text-anchor="middle" font-size="9" fill="#6b7280">未認証のためアクセス不可</text>
        <!-- Step 2: SP→Browser -->
        <circle cx="280" cy="113" r="11" fill="#7c3aed"/>
        <text x="280" y="118" text-anchor="middle" font-size="11" font-weight="800" fill="white">2</text>
        <line x1="269" y1="113" x2="101" y2="113" stroke="#8b5cf6" stroke-width="2" marker-end="url(#ap)"/>
        <text x="183" y="104" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">302 リダイレクト</text>
        <text x="183" y="129" text-anchor="middle" font-size="9" fill="#6b7280">SAMLリクエスト（Base64）を付与</text>
        <!-- Step 3: Browser→IdP (long arrow over SP) -->
        <circle cx="88" cy="176" r="11" fill="#1e429f"/>
        <text x="88" y="181" text-anchor="middle" font-size="11" font-weight="800" fill="white">3</text>
        <line x1="99" y1="176" x2="459" y2="176" stroke="#3b82f6" stroke-width="2" marker-end="url(#ab)"/>
        <text x="280" y="167" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">SAMLリクエスト転送</text>
        <text x="280" y="192" text-anchor="middle" font-size="9" fill="#6b7280">ブラウザがIdPへ直接送信</text>
        <!-- Step 4: IdP→Browser (long) -->
        <circle cx="472" cy="239" r="11" fill="#d97706"/>
        <text x="472" y="244" text-anchor="middle" font-size="11" font-weight="800" fill="white">4</text>
        <line x1="461" y1="239" x2="101" y2="239" stroke="#d97706" stroke-width="2" marker-end="url(#ag)"/>
        <text x="280" y="230" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">ログイン画面を表示</text>
        <text x="280" y="255" text-anchor="middle" font-size="9" fill="#6b7280">IdPのログインページ</text>
        <!-- Step 5: Browser→IdP (long) -->
        <circle cx="88" cy="302" r="11" fill="#1e429f"/>
        <text x="88" y="307" text-anchor="middle" font-size="11" font-weight="800" fill="white">5</text>
        <line x1="99" y1="302" x2="459" y2="302" stroke="#3b82f6" stroke-width="2" marker-end="url(#ab)"/>
        <text x="280" y="293" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">認証情報を入力・送信</text>
        <!-- IdP内部処理 -->
        <rect x="380" y="315" width="180" height="42" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="470" y="330" text-anchor="middle" font-size="9" font-weight="700" fill="#92400e">🔐 IdP 内部処理</text>
        <text x="470" y="346" text-anchor="middle" font-size="9" fill="#92400e">アサーション生成・署名</text>
        <!-- Step 6: IdP→Browser (long) -->
        <circle cx="472" cy="378" r="11" fill="#d97706"/>
        <text x="472" y="383" text-anchor="middle" font-size="11" font-weight="800" fill="white">6</text>
        <line x1="461" y1="378" x2="101" y2="378" stroke="#d97706" stroke-width="2.5" marker-end="url(#ag)"/>
        <text x="280" y="369" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">SAMLレスポンス（HTTP POST）</text>
        <text x="280" y="394" text-anchor="middle" font-size="9" fill="#6b7280">署名付きアサーションをブラウザへ</text>
        <!-- Step 7: Browser→SP -->
        <circle cx="88" cy="441" r="11" fill="#1e429f"/>
        <text x="88" y="446" text-anchor="middle" font-size="11" font-weight="800" fill="white">7</text>
        <line x1="99" y1="441" x2="267" y2="441" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#ab)"/>
        <text x="183" y="432" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">SAMLレスポンス自動POST</text>
        <text x="183" y="457" text-anchor="middle" font-size="9" fill="#6b7280">HTMLフォームで自動送信</text>
        <!-- Step 8 成功エリア -->
        <rect x="60" y="468" width="430" height="66" rx="12" fill="#f0fdf4" stroke="#6ee7b7" stroke-width="1.5"/>
        <text x="280" y="484" text-anchor="middle" font-size="9" font-weight="700" fill="#059669">SPがアサーションの署名を検証</text>
        <circle cx="280" cy="502" r="11" fill="#059669"/>
        <text x="280" y="507" text-anchor="middle" font-size="11" font-weight="800" fill="white">8</text>
        <line x1="269" y1="502" x2="101" y2="502" stroke="#10b981" stroke-width="2.5" marker-end="url(#ao)"/>
        <text x="183" y="493" text-anchor="middle" font-size="10" font-weight="800" fill="#065f46">アクセス許可</text>
        <text x="88" y="525" text-anchor="middle" font-size="9" font-weight="800" fill="#059669">✓ SSO 完了</text>
      </svg>
    </div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚖️ SP-Initiated vs IdP-Initiated</div>
  <div class="ds-compare">
    <div class="ds-compare-head"><div>種別</div><div>開始者</div><div>特徴</div></div>
    <div class="ds-compare-row"><div>SP-Initiated</div><div>SP（サービス側）</div><div>ユーザがSPにアクセス→IdPへリダイレクト<br>一般的なWebアプリのSSO</div></div>
    <div class="ds-compare-row"><div>IdP-Initiated</div><div>IdP（認証側）</div><div>社内ポータルからSPへ遷移<br>SAMLリクエストなしでアサーション送信</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">アサーションとは？</div><div class="ds-qa-a">IdPが発行する<br>「認証済みです」という<br>署名付きXML文書</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">SP と IdP の違いは？</div><div class="ds-qa-a">SP = サービスプロバイダ<br>（リソース提供側）<br>IdP = アイデンティティプロバイダ（認証側）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">SAMLの主な<br>バインディングは？</div><div class="ds-qa-a">HTTPリダイレクト（SAMLリクエスト送信）<br>HTTP POST（アサーション返送）</div></div>
</div>`
  },
  {
    chapter: "1",
    chapterName: "第1章 アクセスコントロール",
    term: "パスワード攻撃の種類",
    hint: "認証を突破する主要な攻撃手法",
    answer: ["① 辞書攻撃：よく使われるパスワード辞書で試行", "② ブルートフォース攻撃：全組み合わせを試行", "③ リバースブルートフォース：1つのパスワードで多くのIDを試行", "④ パスワードスプレー攻撃：少数の一般的なパスワードで多くのアカウントを試行", "⑤ クレデンシャルスタッフィング：漏洩した ID/PW リストを使用", "⑥ レインボーテーブル攻撃：ハッシュ値を事前計算したテーブルで逆引き"],
    detail: `<div class="ds-section">
  <div class="ds-section-title">🎯 ひとことで言うと</div>
  <div class="ds-intro">
    パスワード攻撃は「<strong>オンライン攻撃</strong>（実際に試行）」と「<strong>オフライン攻撃</strong>（ハッシュを入手してクラック）」に大別。<br>
    対策も異なるため、攻撃種別ごとの対策を理解することが重要。
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">⚔️ 攻撃手法の比較</div>
  <div class="ds-compare col4">
    <div class="ds-compare-head"><div>攻撃名</div><div>種別</div><div>内容</div><div>対策</div></div>
    <div class="ds-compare-row"><div>辞書攻撃</div><div>オンライン</div><div>一般的なPWリストで試行</div><div>複雑なPW強制<br>アカウントロック</div></div>
    <div class="ds-compare-row"><div>ブルートフォース</div><div>オンライン</div><div>全組み合わせを試行</div><div>アカウントロック<br>CAPTCHA</div></div>
    <div class="ds-compare-row"><div>パスワード<br>スプレー</div><div>オンライン</div><div>少数の一般PWで多IDを試行<br>ロックを回避</div><div>MFA<br>ロックポリシー改善</div></div>
    <div class="ds-compare-row"><div>クレデンシャル<br>スタッフィング</div><div>オンライン</div><div>漏洩したID/PWリストを<br>別サービスで試行</div><div>MFA<br>パスワード使い回し禁止</div></div>
    <div class="ds-compare-row"><div>レインボー<br>テーブル</div><div>オフライン</div><div>ハッシュを事前計算した<br>テーブルで逆引き</div><div>ソルト付きハッシュ<br>（bcrypt等）</div></div>
  </div>
</div>
<div class="ds-section">
  <div class="ds-section-title">📝 試験で狙われるポイント</div>
  <div class="ds-qa-item"><div class="ds-qa-q">ソルトとは？</div><div class="ds-qa-a">パスワードにランダム値を<br>付加してからハッシュ化<br>レインボーテーブル対策</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">アカウントロックで<br>は防げない攻撃は？</div><div class="ds-qa-a">パスワードスプレー<br>（試行回数が少ないため<br>ロック閾値に達しない）</div></div>
  <div class="ds-qa-item"><div class="ds-qa-q">クレデンシャル<br>スタッフィング対策の<br>決め手は？</div><div class="ds-qa-a">MFA<br>（漏洩PW+IDが揃っても<br>突破されない）</div></div>
</div>`
  },
];
