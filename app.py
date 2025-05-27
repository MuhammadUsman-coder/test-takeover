from flask import Flask
app = Flask(__name__)

@app.route("/poc")
def hello():
    return "Takeover POC by SecurityReapers"

@app.route("/secrepaers")
def hello():
    return "Takeover POC by SecurityReapers"
