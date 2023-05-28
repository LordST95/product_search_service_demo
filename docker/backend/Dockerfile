FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN echo "-------------"
RUN ls .
RUN echo "-------------"

COPY ./starting_script.sh /usr/local/bin/starting_script.sh
RUN chmod +x /usr/local/bin/starting_script.sh
COPY ./src .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["starting_script.sh"]
