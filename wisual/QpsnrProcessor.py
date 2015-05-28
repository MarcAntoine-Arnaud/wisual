import os
from qpsnr import qpsnr
from datetime import datetime

currentAppDir = os.path.dirname(__file__)

class QpsnrProcessor(object):
	def __init__(self):
		self.analysisMode = "psnr"
		self.outputFile = ""
		self.referenceVideo = ""
		self.videos = []
		self.startDate = datetime.now().isoformat()
		self.endDate = ""
		self.status = "unknown"

	def run(self):
		self.status = "processing"

		referenceVideo = os.path.join( currentAppDir, "..", "media", self.referenceVideo)
		
		processor = qpsnr.Qpsnr( str(self.outputFile), str(referenceVideo) )
		for video in self.videos:
			absPathVideo = os.path.join( currentAppDir, "..", "media", video)
			processor.addVideo( str(absPathVideo) );
		options = {}
		processor.initAnalyser( str(self.analysisMode), options );
		processor.process();
		self.status = "complete"
		self.endDate = datetime.now().isoformat()
