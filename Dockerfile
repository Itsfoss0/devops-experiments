FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN  apt update  -y && \
     apt-get install  python3-dev \
     default-libmysqlclient-dev build-essential pkg-config -y 

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
