from flask import Flask
from flask import request
from flask import render_template
import kv
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/PUT", methods=["PUT", "POST"])
def insert():
    kh = kv.put(request.form["key"], request.form["value"])
    if kh is not None:
        return "KEY <%s> INSERTED TO (%s)\n" % (request.form["key"], kh)
    return "ERROR, KEY <%s> EXISTS\n" % request.form["key"]


@app.route("/GET/<key>", methods=["GET"])
def retrieve(key):
    if request.method == "GET":
        result = kv.get(key)
        return result
