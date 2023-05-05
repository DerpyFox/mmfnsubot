FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gdal-bin libgdal-dev python3-gdal binutils libproj-dev gcc python3-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD python MMF_NSU_BOT.py