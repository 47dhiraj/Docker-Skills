# linux o.s ma python version 3 vako image vanni bujaucha
FROM python:3          

#
ENV PYTHONUNBUFFERED=1

# Docker container ko working directory /app
WORKDIR /app
# local computer ko requirements.txt lai container ko requirements.txt ma lagera paste gareko
COPY requirements.txt requirements.txt
# command for upgrading pip version in the container
RUN pip3 install --upgrade pip
# command for installing all the requirements in docker container
RUN pip3 install -r requirements.txt
# copying all the files & folders in local computer to the /app directory in the container
COPY . /app

# exposing the fastapi appllication to the port 8000
EXPOSE 8000

