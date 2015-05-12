
from wisual import g_app
from flask import render_template

@g_app.route("/")
def index():
	return render_template('index.html')

@g_app.route("/psnr")
def computePsnr():
	return render_template('psnr.html')
	
@g_app.route("/ssim")
def computeSsim():
	return render_template('ssim.html')
