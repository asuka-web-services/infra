# firewall

サーバーをルーター化するためのAnsible Roleです。

## 前提条件

- Debian 13で実行していること

## 変数

|変数名|型|必須|説明|
|:-|:-|:-|:-|
|`firewall_enable_ip_forward`|bool|⭕|パケット転送許可|
|`firewall_nat_outgoing_interface`|str|⭕|WANポート|
