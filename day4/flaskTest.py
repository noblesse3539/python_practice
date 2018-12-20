from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"This is my first Server!!!{type(app)}"

