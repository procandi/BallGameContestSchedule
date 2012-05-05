# -*- coding: utf-8 -*-

#my self module to process some question
import modPublic

class modAlogorithm:
	def __init__(self):
		pass
	
	def enumarray_sub(self):
		print self.arr.isOver[0][0]
	
	def enumarray_main(self):
		#make array
		self.arr=modPublic.sarray()
		for i in range(100):
			for j in range(100):
				self.arr.teamA[i][j]=""
				self.arr.teamB[i][j]=""
				self.arr.black[i][j]=False
				self.arr.isOver[i][j]=False
		
		self.enumarray_sub()
		self.arr.isOver[0][0]=True

