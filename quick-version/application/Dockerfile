FROM ubuntu:latest

COPY . /application
WORKDIR /application
RUN apt update\
    && apt install -y python3 python3-pip\
    && pip install -r requirements.txt
EXPOSE 9000
ENTRYPOINT [ "python3"]
CMD ["/application/app.py" ]
