FROM python:3.12.2

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY ${OPENAI_API_KEY}
RUN poetry config virtualenvs.create false
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi




ENTRYPOINT [ "poetry", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--reload" ]