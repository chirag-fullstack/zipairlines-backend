FROM python:3.6

RUN apt-get update --fix-missing

WORKDIR /usr/src/app/

ADD . /usr/src/app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000