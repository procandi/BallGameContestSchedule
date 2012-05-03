# -*- coding: utf-8 -*-

#my self module to process some question
import modFile

class modPublic:	#load template file
	def __init__(self):
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
		
class sarray:    #contest 
	def __init__(self):
		self.teamA=range(100)
		self.teamB=range(100)
		self.black=range(100)
		self.isOver=range(100)
		for i in range(100):
			self.teamA[i]=range(100)
			self.teamB[i]=range(100)
			self.black[i]=range(100)
			self.isOver[i]=range(100)