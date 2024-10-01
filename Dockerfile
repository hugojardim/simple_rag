FROM ghcr.io/chroma-core/chroma:latest

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y curl

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["--host", "0.0.0.0", "--port", "8000"]