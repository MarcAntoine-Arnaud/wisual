
from wisual import g_app
from flask import render_template, jsonify

@g_app.route("/")
def index():
	return render_template('index.html')

@g_app.route("/psnr")
def computePsnr():
	return render_template('psnr.html')
	
@g_app.route("/ssim")
def computeSsim():
	return render_template('ssim.html')
	
@g_app.route("/test")
def computeTest():
	result={'analyse':{'frame':[{'0':120},{'1':130}]}}
	return jsonify(result)
