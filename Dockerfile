FROM python:3.12.2

# Poetryのインストール
RUN pip install poetry

# Poetryのパスを通す
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /src

# pyproject.toml と poetry.lock をコピー
COPY pyproject.toml* poetry.lock* ./

# OPENAI_API_KEYの設定
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY ${OPENAI_API_KEY}

# Poetryの設定（グローバル環境にインストールする設定）
RUN poetry config virtualenvs.create false

# 依存関係のインストール (注意: まだソースコード本体はCOPYしていない)
RUN poetry install --no-root

# ここでアプリのソースコードをコピーする (例として全ファイルをコピー)
COPY . /src

# EXPOSE 8080 は必須ではないが、わかりやすいので書いてもOK
EXPOSE 8080

# 起動コマンド
ENTRYPOINT ["poetry", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8080"]