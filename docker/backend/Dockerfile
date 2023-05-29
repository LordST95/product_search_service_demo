FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./docker/backend/starting_script.sh /usr/local/bin/starting_script.sh
RUN chmod +x /usr/local/bin/starting_script.sh
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./.env /project/.env
COPY ./src .

ENTRYPOINT ["starting_script.sh"]
