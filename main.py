from flask import Flask 

app = Flask(__name__)

class Config(object):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/python06"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True

app.config.from_object(Config)

@app.route("/")
def index():
    num = 100
    return "index page"

if __name__ == "__main__":
    app.run()
