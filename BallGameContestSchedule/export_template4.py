# -*- coding: utf-8 -*-

import re
import sys
import datetime
import random

import win32com.client
import win32ui

#my self module to process some question
import modUserInfo
import modOffice
import modPublic
import modFile

class export_template:
	def __init__(self):
		#load template and base data
		self.userinfo=modUserInfo.modUserInfo()
		self.userinfo.loadbaseinfo(6)
		self.userinfo.loadtemplate()

		#get begin date
		begin_date = datetime.date(int(self.userinfo.begin_year),int(self.userinfo.begin_month),int(self.userinfo.begin_day))
		self.delta = datetime.timedelta(days=7)
		self.now=begin_date
		#nowarr=str(now).split('-')
		self.next=self.now+self.delta
		#nextarr=str(next).split('-')

		#init some value
		self.flag=False

		#made 2*2 matrix array to sort
		self.arr=modPublic.sarray()
		for i in range(100):
			for j in range(100):
				self.arr.teamA[i][j]=""
				self.arr.teamB[i][j]=""
				self.arr.black[i][j]=False
				self.arr.isOver[i][j]=False
		
		#load template and set team name to template
		self.loadtemplate(str(self.userinfo.count),str(self.userinfo.team_count))
		
		#export excel
		self.export_excel()
		
		
	def export_excel(self):
		try:
			#create excel
			office=modOffice.modOffice()
			office.create_excel_app()
			office.create_excel_workbook()
			office.create_excel_sheets()
			
			#set row and col
			row=1
			col=1
			
			for i in range(self.maxd):    #day number				
				#set excel title
				if i+1==self.maxd and self.flag==True:
					office.sheet.Cells(row, col).Value="********"
					office.sheet.Cells(row, col+1).Value="********"
				else:
					v=re.sub(r"\d","",str(self.userinfo.field[0].date[i]))
					if v.strip()!="":
						office.sheet.Cells(row, col).Value=self.userinfo.field[0].date[i]
						office.sheet.Cells(row, col+1).Value=self.userinfo.field[0].name
				row+=1
				
				#set excel value
				for k in range(self.userinfo.count+1):    #round number
					v=re.sub(r"\d","",str(self.userinfo.field[0].teamA[i][k]))
					if v!="":
						if k<3:
							office.sheet.Cells(row, col).Value=("0"+str(k+7)+":30")
						else:
							office.sheet.Cells(row, col).Value=(str(k+7)+":30")
						office.sheet.Cells(row, col+1).Value=self.userinfo.field[0].teamA[i][k]
						office.sheet.Cells(row, col+2).Value=self.userinfo.field[0].teamB[i][k]
						row+=1
		except:
			raise
			
	def loadtemplate(self,round="9",count="6"):
		#load file body
		file=modFile.modFile()
		result=file.readfile("template"+round+"-"+count+".txt")
		
		#enum all result line to update to template
		line=result.split("\n")
		d=0
		k=0
		for v in line:
			v1=re.sub(r"\d","",v)
			if v1.strip()=="" and v.strip()!="":
				d=int(v)
				k=0
				
				self.userinfo.field[0].date[d]=self.now
				self.now=self.next
				self.next=self.next+self.delta
			elif v.strip()!="":
				temp=v.split("-")
				self.userinfo.field[0].teamA[d][k]=self.userinfo.team[int(temp[0])].name
				self.userinfo.field[0].teamB[d][k]=self.userinfo.team[int(temp[1])].name
				k+=1
				
		#d is need skip.#
		self.maxd=d+1
		
		
export_template()