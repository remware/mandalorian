from flask import Flask
from flask import render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mandalorian
bugs = db.bug_hunter

@app.route("/")
def index():
    return "Heipparallaa!"

@app.route("/settings")
def settings():
    return "This is configurable"

@app.route("/start")
def start():
    return "Entry point"

@app.route("/test/<int:id>")
def test(id):
    #contents = ["issues", "urls", "tracker"]
    all_bugs = bugs.find()
    return render_template("index.html", message="Welcome", items=all_bugs, bugs=id)

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/result", methods=["POST"])
def result():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    name = name=request.form["name"]
    return render_template("result.html", pizza=pizza,
                                          extras=extras,
                                          message=message,
                                          name = name)

