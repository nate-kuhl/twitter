FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/post.py /bots/
COPY requirements.txt /tmp
COPY data/bch_quotes.txt /data/
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "post.py"]