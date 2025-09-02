FROM python:3.12-slim

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

# CMD ["python", "main.py", "--action", "run_cli"]
CMD ["python", "main.py"]

# ENTRYPOINT ["python", "main.py"]
# CMD ["uv", "python", "main.py"]



# FROM python:3.12-slim

# WORKDIR /app

# # Для pip та curl (якщо потрібні)
# RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt \
#     && mkdir -p storage

# VOLUME ["/app/storage"]

# EXPOSE 8000

# CMD ["python", "main.py"]

