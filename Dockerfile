FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

COPY . .

RUN uv pip install --system -r requirements.txt \
    && mkdir -p storage

VOLUME ["/app/storage"]

EXPOSE 8000

CMD ["uv", "run", "./src/main.py"]