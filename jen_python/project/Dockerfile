FROM python:3.6.6

COPY project /app/
COPY project /requirements
RUN pip install -r requirements.txt
EXPOSE 8000
RUN python manage.py runserver
