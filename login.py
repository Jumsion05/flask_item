from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    num = 100
    a = 20 + num
    return "index page"

if __name__ == "__main__":
    app.run()
