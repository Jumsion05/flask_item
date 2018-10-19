from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/center")
def center():
    return "center页面"

if __name__ == "__main__":
    app.run()
