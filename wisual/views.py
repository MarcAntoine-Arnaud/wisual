
import os
import uuid
import thread
import xmltodict
from wisual import g_app
from flask import (
	render_template,
	request,
	jsonify,
	abort,
)

from QpsnrProcessor import QpsnrProcessor

navigation = [
	{
		"caption": "New analyse",
		"href" : "/job",
		"icon" : "arrow-circle-right"
	},
	{
		"caption": "List analysis",
		"href" : "/jobs",
		"icon" : "history"
	},
	{
		"caption": "View Results",
		"href" : "/results",
		"icon" : "bar-chart"
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

processors = []

@g_app.route("/")
def index():
	return render_template('index.html', navigation=navigation)

@g_app.route("/job")
def newJob():
	return render_template('job.html', navigation=navigation, analysisModes=analysisModes)

@g_app.route("/jobs")
def listAllJobs():
	global processors
	return render_template('jobs.html', navigation=navigation, analysisModes=analysisModes, jobs=processors)

@g_app.route("/job", methods=["POST"])
def newAnalyse():
	global processors

	args = request.get_json()
	print args
	analysisMode = args.get( "mode", "psnr" )
	referenceVideo = args.get( "reference", None )
	videos = args.get( "videos", None )

	if referenceVideo == None or videos == None:
		abort( 400 )

	if not type( videos ) == list and len(video) > 0:
		abort( 400 )

	if not type( referenceVideo ) == unicode:
		abort( 400 )

	outputFile = os.path.join( "results", str(uuid.uuid4()) + ".xml" )

	processor = QpsnrProcessor()
	processor.analysisMode = analysisMode
	processor.outputFile = outputFile
	processor.referenceVideo = referenceVideo
	processor.videos = videos

	processors.append( processor )

	thread.start_new( processors[ len(processors) - 1 ].run, () )
	return "ok"

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
