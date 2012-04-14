# -*- coding: utf-8 -*-

#my self module to process some question
import modFile


class modPublic:	#load template file
	def __init__(self):
		#load file body
		file=modFile.modFile()
		result=file.readfile("template.txt")
		
		#load template data to variant
		line=result.split("\r\n")
		for v in line:
			self.ALL=v[0]
			self.AM=v[1]
			self.PM=v[2]
			self.TypeA=v[3]
			self.TypeB=v[4]
			self.TypeC=v[5]
			self.TypdD=v[6]
			break
		
		pass

class sfield:	#in one field is need have those data
	def __init__(self):
		self.name=""
		self.date=range(100)
		self.teamA=range(100)
		self.teamB=range(100)
	
class steam:	#in one team is need have those data
	def __init__(self):
		self.ingame=False
		self.name=""
		self.field=""
		self.good=""
		self.schedule=range(100)