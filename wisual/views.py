
import os

from wisual import g_app
from flask import render_template
from flask import jsonify, abort

@g_app.route("/")
def index():
	return render_template('index.html')

@g_app.route("/psnr")
def computePsnr():
	return render_template('psnr.html')

@g_app.route("/ls/<path:path>")
def ls(path):
	files = []
	dirs = []
	try:
		filesAndDirs = os.listdir("/" + path)
		for f in filesAndDirs:
			absPath = os.path.join("/" + path, f)
			if os.path.isdir( absPath ):
				dirs.append(f)
			else:
				files.append(f)
			print f, os.path.isdir(absPath)
	except:
		abort(404)
	return jsonify({"files":files, "directories": dirs, "path":path})
