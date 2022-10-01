from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    print("Getting route index")
    return render_template("index.html")
