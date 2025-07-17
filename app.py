from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Yosshmi's Flask DevOps App!"


if __name__ == '__main__':
    app.run(debug=True)
