FROM alpine

RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip \
        && pip2 install --upgrade pip \
          && pip2 install flask pika

ADD webLogger /opt/webLogger

EXPOSE 80
ENTRYPOINT ["python"]
CMD ["opt/webLogger/app.py"]
