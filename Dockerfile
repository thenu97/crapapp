FROM python:3.9

WORKDIR /app
ADD app.py index.html ./

RUN pip install redis

CMD [ "python", "app.py" ]