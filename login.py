from flask import Flask

app = Flask(__name__)

@app.route("/login")
def login():
    return "登陆界面"

@app.route("/center")
def center():
    return "主页面"

@app.route("/jump")
def jump():
    return render_template("index.html")

if __name__ == "__main__":
  app.run()
