from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    num = 100
    a = 20 + num
    return "index page"

@app.route("/center")
def center():
    num = 100
    return "center页面"

@app.route("/delete")
def delete():
    return "delete页面"

@app.route("/temp")
def func():
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run()
