FROM python:3.9

RUN mkdir /flask-app
WORKDIR /flask-app
ADD . /flask-app
RUN pip install -r flask-app/requirements.txt

ENV FLASK_APP=flask-app/simple_app
ENV FLASK_ENV=development

EXPOSE 5000
CMD python -m flask run -p 5000 -h 0.0.0.0