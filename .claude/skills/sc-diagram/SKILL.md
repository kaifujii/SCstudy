---
name: sc-diagram
description: 情報セキュリティ・ネットワーク・認証プロトコルなどの技術概念を視覚的な図（Mermaid、SVG、HTMLアニメーション、ASCII）で表現する。「図を作って」「フロー図」「シーケンス図」「構成図」「アーキテクチャ図」「単語帳に使う図」「TLSの流れを図で」「XSSの仕組みを図解」「PKIを可視化」などユーザーが技術的な概念を図やビジュアルで表現したいときに必ず使用すること。情報処理安全確保支援士の単語帳・学習サイト向けの図解に特化。
version: 1.0.0
---

# セキュリティ技術図解スキル

## 概要

情報セキュリティの技術概念を、単語帳・学習サイトに埋め込みやすい形式で視覚化する。
ターゲット：暗号・認証・ネットワーク・攻撃手法・プロトコルのフロー・構成図。

## 出力形式の選択基準

| 形式 | 最適なユースケース |
|------|-----------------|
| **Mermaid.js** | プロトコルフロー、シーケンス図、状態遷移、フローチャート |
| **SVG（インライン）** | ネットワーク構成図、アーキテクチャ図、パケット構造 |
| **HTMLアニメーション** | 攻撃の進行過程、ハンドシェイクの段階的説明 |
| **ASCII art** | シンプルなパケット構造、簡易構成図 |

ユーザーが形式を指定しない場合はトピックに最適な形式を選ぶ。
単語帳サイトへの埋め込みを想定し、**自己完結したコードブロック**で出力する。

---

## 頻出トピックの図解パターン

### 暗号・PKI

- **TLS 1.3ハンドシェイク** → Mermaid sequenceDiagram（ClientHello〜Finished）
- **PKI証明書チェーン** → SVG（ルートCA → 中間CA → サーバー証明書の階層）
- **デジタル署名の流れ** → Mermaid sequenceDiagram（署名者/検証者の公開鍵・秘密鍵操作）
- **共通鍵 vs 公開鍵の比較** → SVG 2カラム比較図

### 認証・認可プロトコル

- **OAuth 2.0 Authorization Codeフロー** → Mermaid sequenceDiagram（ブラウザ/認可サーバー/リソースサーバー）
- **SAML認証フロー** → Mermaid sequenceDiagram（SP/IdP/ブラウザ）
- **FIDO2/WebAuthn** → Mermaid sequenceDiagram（登録フロー・認証フロー）
- **JWT構造** → SVG（Header.Payload.Signatureの3分割）

### ネットワークセキュリティ

- **DMZ構成** → SVG（インターネット/外部FW/DMZ/内部FW/内部LAN）
- **VPN（IPsec/SSL）** → SVG（トンネリングの概念図）
- **TCP/IPパケット構造** → ASCII or SVG（ヘッダフィールドの可視化）
- **IDS/IPS配置** → SVG（インライン配置 vs ミラーポート）

### 攻撃手法

- **SQLインジェクション** → HTMLアニメーション or Mermaid（悪意あるクエリの生成〜DB応答）
- **XSS（格納型）** → Mermaid sequenceDiagram（攻撃者/サーバー/被害者ブラウザ）
- **CSRF攻撃フロー** → Mermaid sequenceDiagram
- **中間者攻撃（MitM）** → SVG（通信の盗聴・改ざん）

---

## 出力テンプレート

### Mermaidの場合

````markdown
```mermaid
sequenceDiagram
    autonumber
    participant C as クライアント
    participant S as サーバー
    C->>S: ClientHello (サポートするTLSバージョン, 暗号スイート)
    S->>C: ServerHello (選択したパラメータ)
    ...
```
````

単語帳への埋め込み方（Mermaid.jsをCDNから読む）：
```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<div class="mermaid">
sequenceDiagram
  ...
</div>
```

### SVGの場合

```html
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <!-- ネットワーク構成要素 -->
  <!-- 色: インターネット=#ff6b6b, DMZ=#ffd93d, 内部=#6bcb77 -->
  ...
</svg>
```

### HTMLアニメーションの場合

```html
<div class="diagram-container">
  <!-- ステップごとにopacityアニメーションで段階的に表示 -->
  <style>
    .step { opacity: 0; animation: fadeIn 0.5s forwards; }
    .step:nth-child(1) { animation-delay: 0s; }
    .step:nth-child(2) { animation-delay: 1s; }
    ...
  </style>
  ...
</div>
```

---

## 単語帳サイト向けのデザイン指針

- **配色**：背景は`#1a1a2e`（ダーク）or `#f8f9fa`（ライト）に合わせる
- **フォント**：コード・技術要素は`monospace`、ラベルは`sans-serif`
- **サイズ**：カード内に収まるよう `max-width: 100%` + `viewBox`でレスポンシブに
- **コントラスト**：図の各要素に色分けし、凡例を添える
- **簡潔さ**：1図につき1概念。複雑になるなら図を分割する
- **日本語ラベル**：試験勉強用なので図中のラベルも日本語を使う

---

## 手順

### Step 1: トピック確認

指定がなければ何の図を作るか確認する。

### Step 2: 標準的な図解パターンをWeb検索で調査

**構成図・アーキテクチャ図は書き方に業界標準がある。**
オリジナリティより「見た人が即理解できる慣習的な表現」を優先するため、
図を描く前に必ずWeb検索でそのトピックの一般的な図解を調査する。

検索クエリの例：
- `"TLS handshake" sequence diagram`
- `DMZ network architecture diagram`
- `OAuth 2.0 authorization code flow diagram`
- `PKI certificate chain diagram`

調査で確認すること：
- 登場するコンポーネントの標準的な名称・略称
- 矢印の方向・ラベルの慣習（例：req/res、→/←の使い分け）
- レイアウトの定番（左右 or 上下、レイヤー構造の有無）
- よく使われるアイコン・シンボル（サーバー、クライアント、鍵マーク等）

### Step 3: 出力形式を選択

調査結果をもとに、最もそのトピックに合った形式を選ぶ（表を参照）。

### Step 4: コードを出力

コピペで即使えるレベルで出力する。

### Step 5: 補足

図の読み方・試験で問われるポイントを一言添える。
必要なら別形式バージョンも提示。
