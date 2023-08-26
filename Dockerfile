FROM python:3.11.5-slim-bullseye

RUN apt update && apt install -y \
  libzbar0

WORKDIR /workspace

COPY ./requirements.txt /workspace
RUN pip3 install -r requirements.txt

COPY ./qrcode /usr/local/bin

ENTRYPOINT ["/usr/local/bin/qrcode"]
