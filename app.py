from flask import Flask, render_template
from data import data, parse_homework

app = Flask(__name__)

groups = data()
tasks = parse_homework()


@app.route("/")
def home():
    return render_template("home.html", groups=groups)


@app.route("/groups/<string:id>/")
def schedule(id):
    for group in groups:
        if group["id"] == id:
            return render_template("schedule_tmp.html", group=group)


@app.route("/groups/hw/<string:id>/")
def homework(id):
    for group in groups:
        if group["id"] == id:
            return render_template("hw_tmp.html", group=group)


@app.route("/groups/hw/<string:id>/<string:title>")
def task(id, title):
    ref = tasks[id][title]
    for group in groups:
        if group["id"] == id:
            return render_template("task.html", group=group, ref=ref)  

if __name__ == "__main__":
    app.run(debug=True)
