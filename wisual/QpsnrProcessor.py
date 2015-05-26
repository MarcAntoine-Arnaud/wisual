
from qpsnr import qpsnr

class QpsnrProcessor(object):
	def __init__(self):
		self.analysisMode = "psnr"
		self.outputFile = ""
		self.referenceVideo = ""
		self.videos = []

	def run(self):
		processor = qpsnr.Qpsnr( str(self.outputFile), str(self.referenceVideo) )
		for video in self.videos:
			processor.addVideo( str(video) );
		options = {}
		processor.initAnalyser( str(self.analysisMode), options );
		processor.process();
