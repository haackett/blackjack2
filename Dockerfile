FROM python:3

WORKDIR /app

COPY requirements.txt ./

#RUN pip install -r requirements.txt

EXPOSE 80:80

COPY . /app

RUN python -m unittest discover .