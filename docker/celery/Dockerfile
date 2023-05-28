FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./src .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT celery -A config worker -l INFO
