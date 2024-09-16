# FastAPIプロジェクトについて
`./api1`と仮名で作成  
* `./api1/code`ディレクトリ　ソースファイル
* `./api1/env`ディレクトリ　 環境変数


# かんきょうについて
* fastapi
* SQLAlchemy、Alembic
* postgreSQL

# python環境
## venvによる環境構築（一回やれば不要）
```
python -m venv venv
```

## venvによる環境をアクティブ
```
.\venv\Scripts\Activate.ps1
```

## pipでFastAPI構築に必要なものをインストール
```
pip install "fastapi[all]"
pip install psycopg
pip install alembic
```


# 環境実行（初期版）
## uvicornを利用
```
python -m uvicorn app1.main:app --reload
```

# マイグレーション
* `alembic`を使用  
* alembicの利用場所は`./api1/code/models`配下

初回
```
alembic init migrations
```

# Dockerで環境を起動
## コマンド
イメージ作成
```
docker compose build --no-cache --force-rm
```

コンテナ作成＋実行
```
docker compose up
```

## 関連ファイル
- ./api1/Dockerfile  
　api1プロジェクトの環境を校正するDockerfile

- ./docker-compose.yml  
　docker-composeのファイル  

- ./requirements.txt  
　開発環境構築時のrequirements.txt　Webサーバーの構築にも利用する  
　```pip freeze > requirements.txt```で出力する  

# 参考資料
- 環境構築  
https://fastapi.tiangolo.com/ja/deployment/docker/#fastapi  



ファイル配置

PJ直下
.vscodeディレクトリ
.envディレクトリ
docker-compose.yml
requirements.txt
アプリケーションディレクトリ


Python構成がアプリケーション毎に独立している場合
.vscodeディレクトリ
.envディレクトリ
docker-compose.yml
アプリケーションディレクトリ
  ｜requirements.txt

# 環境チェック

# 

```
docker run -dit python:3.12.1-alpine3.19
 <コンテナ名>＝ brave_blackburn

docker exec brave_blackburn mkdir -p /code
docker cp ./app1/code brave_blackburn:/code/app
docker cp ./requirements.txt brave_blackburn:/code/requirements.txt
```

```
docker exec -it brave_blackburn /bin/ash

```


docker rm 