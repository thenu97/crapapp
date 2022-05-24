FROM python:3.9

WORKDIR /app
ADD app.py ./

RUN pip install redis

CMD [ "python", "app.py" ]