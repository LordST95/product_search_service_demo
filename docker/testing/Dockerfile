FROM python:3.10.0
ENV PYTHONUNBUFFERED=1

COPY ./docker/testing/starting_script.sh /usr/local/bin/starting_script.sh
RUN chmod +x /usr/local/bin/starting_script.sh
COPY requirements.txt ./project/requirements.txt
RUN pip install -r ./project/requirements.txt
COPY ./.env /project/.env
COPY ./src /project/src
COPY ./tests /project/tests

ENTRYPOINT ["starting_script.sh"]
