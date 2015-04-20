
from flask import Flask

g_app = Flask(__name__)

@g_app.route("/")
def index():
    return """<html>
    <head>
      <title>Wisual</title>
    </head>
    <body>
      <center><h1>Wisual</h1></center>
    </body>
    </html>
    """
