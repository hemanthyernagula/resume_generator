# set base image (host OS)
FROM python:3.7.6-buster
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR ./app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python","app.py"]
