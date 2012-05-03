# -*- coding: utf-8 -*-

import re

#my self module to process some question
import modFile
import modPublic


class modUserInfo:
	def __init__(self):
		pass
	
	def loadtemplate(self):	
		#load template data to variant
		self.ALL="皆可".encode("big5")
		self.AM="上午場".encode("big5")
		self.PM="下午場".encode("big5")
		self.TypeA="龍組".encode("big5")
		self.TypeB="馬組".encode("big5")
		self.TypeC="健康組".encode("big5")
		self.TypdD="快樂組".encode("big5")

	def loadbaseinfo(self,type=0):
		#load file body
		file=modFile.modFile()
		result=file.readfile("fielddata.txt")
		
		#made field array
		self.field=range(100)
		for i in range(100):
			self.field[i]=modPublic.sfield()
			for j in range(100):
				self.field[i].teamA[j]=range(14)
				self.field[i].teamB[j]=range(14)
				
		#add field data to origin data
		line=result.split("\r\n")
		i=0
		for v in line:
			v=re.sub(r"field.+=","",v)
			self.field[i].name=v.encode("big5")
			if self.field[i].name!="":
				i+=1
		#if type is 0 then this is a all export
		#if type is 1 then this is a professional contest export
		#if type is 2 then this is a gernel contest export
		if type==0:
			self.field_count=i
		elif type==1:
			self.field_count=i-1
		elif type>=2:
			self.field_count=1
			t=self.field[i-2].name
			self.field[0].name=self.field[i-2].name
			self.field[0].name=t
		
		
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
			
			#class team
			if type==0 or (type==1 and (va0[2].encode("big5")=="龍組".encode("big5") or va0[2].encode("big5")=="馬組".encode("big5"))) or (type==2 and (va0[2].encode("big5")=="健康組".encode("big5") or va0[2].encode("big5")=="快樂組".encode("big5"))) or (type==3 and va0[2].encode("big5")=="龍組".encode("big5")) or (type==4 and va0[2].encode("big5")=="馬組".encode("big5")) or (type==5 and va0[2].encode("big5")=="健康組".encode("big5")) or (type==6 and va0[2].encode("big5")=="快樂組".encode("big5")):
				self.team[i].ingame=va0[0]
				self.team[i].name=va0[1].encode("big5")
				self.team[i].field=va0[2].encode("big5")
				self.team[i].good=va0[3].encode("big5")
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
		
		
		#load file body
		file=modFile.modFile()
		result=file.readfile("countdata.txt")
		
		self.count=result