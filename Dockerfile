FROM registry.access.redhat.com/ubi8/python-38:1-100

WORKDIR /web-app

ADD web-app.py .

RUN pip3 install flask

EXPOSE 5000

CMD ["python3", "./web-app.py"]
