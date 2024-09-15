# IMAGE
FROM python:3

WORKDIR /usr/src/app

RUN git clone https://github.com/GRoxo-B/flask-test.git

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./docs/app.py" ]