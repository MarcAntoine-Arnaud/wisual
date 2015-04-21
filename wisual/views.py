
from wisual import g_app
from flask import render_template

@g_app.route("/")
def index():
	return render_template('index.html')

