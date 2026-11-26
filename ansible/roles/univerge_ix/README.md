# univerge_ix

UNIVERGE IX2215を構築・管理するためのAnsible Roleです。

## 前提条件

- NEC UNIVERGE IX2215で実行していること

## 変数

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`univerge_ix_model`|Literal[`'ix2215'`]|⭕|モデル名|
|`univerge_ix_administrators`|list[`Administrator`]|⭕|管理者一覧|
|`univerge_ix_netmeister`|`Netmeister`|-|NetMeisterの設定|
|`univerge_ix_ntp_servers`|list[`NtpServer`]|-|NTPサーバーの同期先一覧。優先度の高い順。|
|`univerge_ix_ntp_interval`|int|-|NTPサーバーの同期間隔(秒)|
|`univerge_ix_vlans`|list[`Vlan`]|-|VLAN一覧|
|`univerge_ix_devices`|list[`Device`]|-|物理ポート一覧|
|`univerge_ix_interfaces`|list[`Interface`]|-|インターフェイス一覧|
|`univerge_ix_ipsec_tunnels`|list[`IpsecTunnel`]|-|IPsec VPN一覧|
|`univerge_ix_static_routes`|list[`StaticRoute`]|-|スタティックルート一覧|

### `Administrator`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`username`|str|⭕||
|`password_hash`|str|⭕||

### `Netmeister`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`account`|str|⭕||
|`secret`|str|⭕||
|`site_name`|str|⭕||
|`outgoing_interface`|str|⭕||

### `NtpServer`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`address`|str|⭕||

### `Vlan`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`id`|int|⭕||
|`description`|str|-|default(`''`)|
|`interface`|`VlanInterface`|-|default(`None`)|

#### `VlanInterface`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`address`|str|⭕||
|`vrf`|str|-|default(`None`)|

### `Device`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`name`|str|⭕||
|`keepalive`|`Keepalive`|-||

#### `Keepalive`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`time`|int|⭕||
|`count`|int|⭕||

### `Interface`

`Interface` = `RoutedPort` | `AccessPort` | `TrunkPort`

#### `RoutedPort`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`device`|str|⭕||
|`description`|str|-||
|`mode`|`'routed'`|⭕||
|`dhcp`|bool|-||
|`napt`|bool|-||
|`monitoring`|`Monitoring`|-||

#### `AccessPort`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`device`|str|⭕||
|`description`|str|-||
|`mode`|`'access'`|⭕||
|`vlan`|int|-||

#### `TrunkPort`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`device`|str|⭕||
|`description`|str|-||
|`mode`|`'trunk'`|⭕||
|`native_vlan`|int|-||
|`allowed_vlans`|list[int]|-||

### `IpsecTunnel`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`description`|str|-||
|`address`|str|⭕||
|`outgoing_interface`|str|⭕||
|`psk`|str|⭕|拠点間の事前共有鍵|
|`local_id`|str|⭕|自拠点の識別子|
|`remote_id`|str|⭕|接続先の識別子|
|`remote_ip`|str|-|接続先のグローバルIPアドレス|
|`vrf`|str|-|所属するVRFインスタンス|
|`monitoring`|`Monitoring`|-|監視設定|

### `StaticRoute`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`prefix`|str|⭕|A.B.C.D/<0-32>または`default`|
|`next_hop`|str|-|A.B.C.D|
|`interface`|str|-|転送先のインターフェイス名|
|`dhcp`|bool|-|dhcpで学習したゲートウェイアドレスを使うかどうか|
|`vrf`|str|-|設定先のVRFインスタンス|

### `Monitoring`

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`id`|str|⭕||
|`check_host`|str|⭕||
|`failure_action`|str|⭕||
