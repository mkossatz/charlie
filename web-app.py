from flask import Flask

app = Flask(__name__)

@app.route("/charlie")
def charlie():
    return "Hello, Im Charlie!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
