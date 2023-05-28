FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./docker/backend/starting_script.sh /usr/local/bin/starting_script.sh
RUN chmod +x /usr/local/bin/starting_script.sh
COPY ./src .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["starting_script.sh"]








# other way 
    # + adding "command: python manage.py runserver 0.0.0.0:8000" in demo_api:
    # + deleting "starting_script.sh"

# FROM python:3.10.0
# ENV PYTHONUNBUFFERED=1
# WORKDIR /app

# # COPY ./docker/backend/starting_script.sh /usr/local/bin/starting_script.sh
# # RUN chmod +x /usr/local/bin/starting_script.sh
# COPY ./src .
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # failed
#  # django.db.utils.OperationalError: (2005, "Unknown MySQL server host 'db' (-2)")
# RUN python manage.py migrate         
