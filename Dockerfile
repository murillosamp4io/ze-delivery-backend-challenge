FROM python:3
RUN apt update
RUN apt upgrade -y
RUN apt install -y libgdal-dev locales

RUN locale-gen en_US.UTF-8
ENV LC_ALL='en_US.utf8'

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

RUN pip3 install GDAL==2.4.2

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/