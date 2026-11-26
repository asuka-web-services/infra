# systemd_networkd

Linuxの物理・論理ネットワークと、VPN接続のための仮想インターフェイスをsystemd_networkdで構築・管理するためのAnsible Roleです。

## 前提条件

- Debian 13で実行していること

## 変数

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`systemd_networkd_base_networks`|list[BaseNetwork]|⭕|ホストの物理・論理ネットワーク覧|
|`systemd_networkd_vpn_interfaces`|list[VpnInterface]|⭕|VPN接続のためのインターフェイス一覧|

### BaseNetwork

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`name`|str|⭕|管理名|
|`match_name`|str|⭕|対象NIC名|
|`address`|str|⭕|CIDR表記のIPアドレス|
|`dns`|str|-|DNSサーバーのIPアドレス|
|`domains`|str|-|検索ドメイン|
|`gateway`|str|-|デフォルトゲートウェイのIPアドレス|

### VpnInterface

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`name`|str|⭕|XFRMインターフェイス名|
|`if_id`|int|⭕|XFRMインターフェイスID|
|`tunnel_address`|str|⭕|CIDR表記のIPアドレス|
