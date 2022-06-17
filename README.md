# memo-server

## 1.概要

メモを登録するアプリとなっている。機能としては以下のようになっている。

- メモの登録機能
- 登録したメモの一覧表示機能

## 2.構成

- フロント：streamlit
- バックエンド：FastAPI
- DB：PostgreSQL

## 3.環境構築

※前提として、Dockerがインストールされていること

1. `git clone repos`
2. `cd .devcontainer`
3. `docker-compose up -d`
4. コンテナ構築後、以下のコマンドを入力
   - `./script/run.sh`
5. ブラウザで[URL](http://localhost:18501/)を入力

## 4.ディレクトリ構成

```tree
opt
├── Dockerfile
├── app
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── cruds
│   │   ├── __init__.py
│   │   └── m_memo.py
│   ├── front.py
│   ├── lib
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── schemas.py
│   └── server.py
├── database
│   ├── Dockerfile
│   └── initdb
│       └── 01_create_table.sql
└── requirements.txt
```
