
import sys

class modFile:	
	def __init__(self):
		pass
	
	def readfile(self,fname="template"):
		sys.setdefaultencoding("utf-8")
		
		result=""
		f=open(fname,"r")
		while True:
			line=f.readline()
			result+=line
			if len(line)==0:
				break
		f.close()
		return result
	
	def writefile(self,fname="template",fbody=""):
		sys.setdefaultencoding("utf-8")
		
		f=open(fname,"w")
		f.write(fbody)
		f.close()
		return True