FROM python:3.9-slim

WORKDIR /app

# Tambahkan dependensi sistem yang diperlukan untuk mysqlclient
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY req.txt req.txt
RUN pip install -r req.txt

COPY ./app /app/

CMD ["python", "routes.py"]