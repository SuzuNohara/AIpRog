from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    data = json.dumps({"nodes": [{"id": 1}, {"id": 2}], "links": [{"source": 1, "target": 2}]})
    return render_template("graph.html", data=data)

app.run(debug=True)