# -*- coding: utf-8 -*-

#my self module to process some question
import modFile

class modPublic:	#load template file
	def __init__(self):
		pass

class sfield:	#in one field is need have those data
	def __init__(self):
		self.name=""
		self.date=range(300)
		self.teamA=range(300)
		self.teamB=range(300)
	
class steam:	#in one team is need have those data
	def __init__(self):
		self.ingame=False
		self.name=""
		self.field=""
		self.good=""
		self.schedule=range(300)
		
class sarray:    #contest 
	def __init__(self):
		self.teamA=range(300)
		self.teamB=range(300)
		self.black=range(300)
		self.isOver=range(300)
		for i in range(300):
			self.teamA[i]=range(300)
			self.teamB[i]=range(300)
			self.black[i]=range(300)
			self.isOver[i]=range(300)