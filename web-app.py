FROM registry.access.redhat.com/ubi8/python-38:1-100

WORKDIR /web-app

ADD web-app.py .

RUN pip3 install flask

EXPOSE 5000

CMD ["python3", "./web-app.py"]

[root@ip-172-31-21-153 ~]# cat web-app.py 
from flask import Flask

app = Flask(__name__)

@app.route("/charlie")
def charlie():
    return "Hello, Im Charlie!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
