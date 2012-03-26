
class modFile:	
	def __init__(self,fname="template",fbody=""):
		pass
	
	def readfile(self,fname):
		result=""
		f=open(fname,"r")
		while True:
			line=f.readline()
			result+=line
			if len(line)==0:
				break
		f.close()
		return result
	
	def writefile(self,fname,fbody):
		f=open(fname,"w")
		f.write(fbody)
		f.close()
		return True