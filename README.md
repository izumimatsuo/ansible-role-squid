# ansible-role-squid [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-squid.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-squid)

CentOS 7 に squid を導入する ansible role です。

proxy を許可するポート

- 80
- 443

以下のいづれかの条件にマッチした場合に proxy 可能

- localhost からのアクセス
- squid_allow_ipaddr で設定した内部アドレスからのアクセス
- /etc/squid/whitelist に設定したドメインに一致するアクセス先

## 設定項目

以下の設定項目は上書き可能。

| 項目名             | デフォルト値   | 説明                 |
| ------------------ | -------------- |--------------------- |
| squid_allow_ipaddr | none           | 許可する内部アドレス |
| squid_http_port    | 3128           | squidの待受ポート    |
