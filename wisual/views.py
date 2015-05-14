
import os
import xmltodict
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

@g_app.route("/results")
def getResultsList():
	files = os.listdir("results")
	print files
	return jsonify({"files":files})

@g_app.route("/results/<path:path>")
def getResult(path):
	f = open( os.path.join("results", path), 'r')
	output = xmltodict.parse(f, process_namespaces=False)
	f.close()
	return jsonify(**output)
