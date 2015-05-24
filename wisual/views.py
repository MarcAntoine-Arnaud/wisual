
import os
import xmltodict
from wisual import g_app
from flask import render_template, jsonify, abort

navigation = [
	{
		"caption": "New Job",
		"href" : "/job"
	},
	{
		"caption": "List Job",
		"href" : "/jobs"
	},
	{
		"caption": "View Results",
		"href" : "/results"
	}
]

analysisModes = [
	{
		"id": "psnr",
		"name": "PSNR"
	},
	{
		"id": "ssim",
		"name": "SSIM"
	},
	{
		"id": "avgpsnr",
		"name": "Average PSNR"
	},
	{
		"id": "avgssim",
		"name": "Average SSIM"
	}
]

@g_app.route("/")
def index():
	return render_template('index.html', navigation=navigation)

@g_app.route("/job")
def newJob():
	return render_template('job.html', navigation=navigation, analysisModes=analysisModes)

@g_app.route("/jobs")
def listAllJobs():
	return render_template('jobs.html', navigation=navigation)

@g_app.route("/results")
def getAllResults():
	resultsFiles = os.listdir("results")
	return render_template('results.html', navigation=navigation, resultsFiles=resultsFiles)

@g_app.route("/results/<path:resultFile>")
def getResult(resultFile):
	return render_template('result.html', navigation=navigation, resultFile=resultFile)

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
			#print f, os.path.isdir(absPath)
	except:
		abort(404)
	return jsonify({"files":files, "directories": dirs, "path":path})

@g_app.route("/results/<path:path>/data")
def getResultData(path):
	f = open( os.path.join("results", path), 'r')
	output = xmltodict.parse(f, process_namespaces=False)
	f.close()
	return jsonify(**output)
