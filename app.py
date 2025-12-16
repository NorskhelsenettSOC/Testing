from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    environment = os.getenv("ENVIRONMENT", "")
    suffix = f" {environment}" if environment else ""
    return f"<h1>Hello, World!{suffix}</h1>"

if __name__ == "__main__":
    app.run(debug=True)