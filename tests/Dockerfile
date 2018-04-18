FROM python:3.4

RUN pip3 install --upgrade pip
RUN pip3 install pika
RUN pip3 install django
RUN pip3 install circuitbreaker
RUN pip3 install rabbitmq
RUN pip3 install djangorestframework


EXPOSE 8080

WORKDIR /usr/src/app
COPY . /usr/src/app 
