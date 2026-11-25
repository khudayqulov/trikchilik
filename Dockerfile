FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY pyproject.toml README.md ./
COPY app ./app

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir .

CMD ["python", "-m", "app.main"]

