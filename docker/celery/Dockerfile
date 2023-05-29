FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./.env /.env
COPY ./src .

ENTRYPOINT celery -A config worker -l INFO
