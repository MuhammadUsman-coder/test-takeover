from flask import Flask
app = Flask(__name__)

@app.route("/poc")
def poc():
    return "Takeover POC by SecurityReapers"

@app.route("/")
def hidden():
    return """
    <html>
        <head><title>SecurityReapers</title></head>
        <body>
            <!-- Takeover POC by SecurityReapers -->
            <p>Welcome</p>
        </body>
    </html>
    """
