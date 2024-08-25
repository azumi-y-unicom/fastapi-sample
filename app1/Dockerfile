FROM python:3.12.1-slim-bullseye

# Python基本設定
ENV PYTHONPATH $PYTHONPATH:/code/app
ENV TZ=Asia/Tokyo

WORKDIR /code

# ファイル構築
COPY ./app1/code /code/app
COPY ./requirements.txt /code/requirements.txt

# Pythonモジュール導入
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

# uvicorn起動コマンド　FastAPI実行のため
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# 参考情報
# https://fastapi.tiangolo.com/ja/deployment/docker/#fastapi
