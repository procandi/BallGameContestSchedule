# -*- coding: utf-8 -*-

import re

#my self module to process some question
import modFile
import modPublic

class modUserInfo:
	def __init__(self):
		pass
	
	def loadbaseinfo(self):
		#load file body
		file=modFile.modFile()
		result=file.readfile("fielddata.txt")
		
		#made field array
		self.field=range(100)
		for i in range(100):
			self.field[i]=modPublic.sfield()
			for j in range(100):
				self.field[i].date[j]=modPublic.sschedule()
				
		#add field data to origin data
		line=result.split("\r\n")
		i=0
		for v in line:
			v=re.sub(r"field.+=","",v)
			self.field[i].name=v
			i+=1
		self.field_count=i
		
		
		#load file body
		file=modFile.modFile()
		result=file.readfile("teamdata.txt")
		
		#made team struct and array
		self.team=range(100)
		for i in range(100):
			self.team[i]=modPublic.steam()
		
		#add team data to origin data
		line=result.split("\r\n")
		i=0
		for v in line:
			if v is None:
				break
			if v=="":
				break
			
			v=re.sub(r"team.+=","",v)
			vd=v.split('-')
			va0=vd[0].split(',')
			va1=vd[1].split(',')
			
			self.team[i].ingame=va0[0]
			self.team[i].name=va0[1]
			self.team[i].field=va0[2]
			self.team[i].good=va0[3]
			for j in range(100):
				if j<len(va1)-1:	#need subtract one, because date value will have one blank data.
					self.team[i].schedule[j]=va1[j]
				else:
					break
			i+=1
		self.team_count=i
		
		
		#load file body
		file=modFile.modFile()
		result=file.readfile("datedata.txt")
		
		v=result.split('/')
		self.begin_year=v[0]
		self.begin_month=v[1]
		self.begin_day=v[2]