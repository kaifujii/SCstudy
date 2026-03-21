const CH08_CARDS = [
  {
    chapter: "8",
    chapterName: "第8章 物理・ネットワーク",
    term: "VLAN の種類",
    hint: "スイッチによるネットワーク分割技術",
    answer: ["① ポート VLAN：物理ポートで VLAN を分割（アクセスポート）", "② タグ VLAN（IEEE 802.1Q）：フレームに VLAN ID タグを付与（トランクポート）", "③ VLAN ID：12bit で 4094 個まで定義可能", "効果：セキュリティセグメンテーション・ブロードキャスト制御"]
  },
  {
    chapter: "8",
    chapterName: "第8章 物理・ネットワーク",
    term: "無線 LAN 規格の比較",
    hint: "IEEE 802.11 シリーズの周波数・速度",
    answer: ["802.11b：2.4GHz、最大 11Mbps", "802.11a：5GHz、最大 54Mbps", "802.11g：2.4GHz、最大 54Mbps", "802.11n（Wi-Fi 4）：2.4/5GHz、最大 600Mbps、MIMO", "802.11ac（Wi-Fi 5）：5GHz、最大 6.93Gbps、MU-MIMO", "802.11ax（Wi-Fi 6）：2.4/5/6GHz、最大 9.6Gbps、OFDMA"]
  },
  {
    chapter: "8",
    chapterName: "第8章 物理・ネットワーク",
    term: "無線 LAN のセキュリティ規格",
    hint: "WEP・WPA・WPA2・WPA3 の違い",
    answer: ["× WEP：RC4（40〜104bit）、解読可能・廃止", "△ WPA：TKIP（RC4ベース）、暫定規格", "○ WPA2（IEEE 802.11i）：AES-CCMP（128bit）、現在も使用", "◎ WPA3：SAE（Dragonfly）で辞書攻撃耐性、192bit（Enterprise）", "IEEE 802.1X 認証と組み合わせると最強"]
  },
  {
    chapter: "8",
    chapterName: "第8章 物理・ネットワーク",
    term: "無線 LAN への攻撃手法",
    hint: "Wi-Fi 環境でよく見られる攻撃",
    answer: ["① Evil Twin（偽AP）攻撃：正規 AP と同じ SSID の偽 AP を設置して盗聴", "② ビーコン洪水：大量の Beacon フレームを送信して混乱させる", "③ 盗聴：暗号化されていない通信を傍受", "④ De-authentication 攻撃：切断フレームを偽造して強制切断", "⑤ KRACK：WPA2 の鍵再インストール脆弱性"]
  },
];
