# ansible-role-squid

CentOS 7 に squid を導入する ansible role です。

proxy を許可するポート

- 80
- 443

## 設定項目

以下の設定項目は上書き可能。

| 項目名          | デフォルト値   | 説明                 |
| --------------- | -------------- |--------------------- |
| squid_allow_ip  | 192.168.0.0/16 | 許可する内部アドレス |
| squid_http_port | 3128           | squidの待受ポート    |
