FROM python:3

RUN apt update && apt install -y \
    wget \
    g++ \
    unixodbc \
    unixodbc-dev \
    python-dev \
    python3-requests 

RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
   