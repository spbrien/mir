FROM python:2

WORKDIR /usr/src/app

RUN apt-get update && apt-get install wkhtmltopdf -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "mir", "dev" ]
