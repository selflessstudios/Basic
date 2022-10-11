from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

print("Trying to print to AWS")

@app.route("/", methods=["GET"])
def index():
    print("Getting route index")
    return render_template("index.html")
