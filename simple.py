from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>I love Barry!</h1>"

if __name__ == "__main__":
    application.run(host="localhost", port = 8000, threaded=True)
