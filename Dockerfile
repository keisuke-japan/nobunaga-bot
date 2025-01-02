FROM python:3.12.2

# Poetryのインストール方法をpipに変更
RUN pip install poetry

# Poetryのパスを通す
ENV PATH="/root/.local/bin:${PATH}"

# Poetryがインストールされたか確認
RUN poetry --version

WORKDIR /src

# pyproject.toml と poetry.lock をコピー
COPY pyproject.toml* poetry.lock* ./


# OPENAI_API_KEYの設定
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY ${OPENAI_API_KEY}

# Poetryの設定
RUN poetry config virtualenvs.create false
RUN poetry install --no-root


# Cloud Run環境でのPORT変数を使うように変更
ENTRYPOINT [ "poetry", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8080" ]
