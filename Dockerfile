
FROM python:3

WORKDIR /app

RUN apt-get update && apt-get install -y git \
    && git clone https://github.com/GRoxo-B/flask-test.git /app

WORKDIR /app/docs

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]