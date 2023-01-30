from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'crazebots'


if __name__ == "__main__":
    app.run()
