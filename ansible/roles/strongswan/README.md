# strongswan

IKEv2/IPsecによるルートベースVPNをstrongSwanで構築・管理するためのAnsible Roleです。

## 前提条件

- Debian 13で実行していること
- `systemd-networkd`で、対応するXFRMインターフェイスを作成していること

## 変数

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`strongswan_connections`|list[Conn]|⭕|接続先一覧|
|`strongswan_local_addrs`|str|⭕|自拠点のグローバルIPアドレス|
|`strongswan_local_id`|str|⭕|自拠点の識別子|

### Conn

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`name`|str|⭕|接続先の識別名|
|`if_id`|int|⭕|LinuxのXFRMインターフェイスID|
|`psk_secret`|str|⭕|拠点間の事前共有鍵|
|`remote_addrs`|str|⭕|接続先のグローバルIPアドレス|
|`remote_id`|str|⭕|接続先の識別子|
