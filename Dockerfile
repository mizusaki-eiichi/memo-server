FROM python:3.8-slim-buster

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    vim \
    locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV TZ Asia/Tokyo

COPY . /opt

RUN pip install -r /opt/requirements.txt
