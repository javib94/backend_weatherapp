FROM python:3.8
  
WORKDIR /usr/src/

RUN pip install pipenv
ENV DB_URL='172.17.0.1'
ENV DB_PORT='5432'
ENV DB_NAME='online-exam'
ENV DB_USER='postgres'
ENV DB_PASSWORD='0NLIN3-ex4m'
COPY . .

RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["./bootstrap.sh" ]