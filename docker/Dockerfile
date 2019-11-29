FROM alpine:3.10

# set variable to help prevent issues with log output
ENV PYTHONUNBUFFERED=1

# copy in example handlers file
COPY handlers.py /handlers.py

RUN apk add --no-cache gcc=8.3.0-r0 python3=3.7.5-r1 python3-dev=3.7.5-r1 musl-dev=1.1.22-r3 && pip3 install --upgrade pip --no-cache kopf==0.23.2 kubernetes==10.0.1 jinja2==2.10.3

CMD kopf run --standalone --verbose /handlers.py
