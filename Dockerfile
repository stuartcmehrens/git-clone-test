FROM python:3.11.9-slim

WORKDIR /app
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv
COPY . /app

ENTRYPOINT ["uv", "run", "--", "python", "main.py"]
CMD ["--help"]
