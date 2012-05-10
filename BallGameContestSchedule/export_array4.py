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

class export_array4:
	def __init__(self):
		#load template and base data
		self.userinfo=modUserInfo.modUserInfo()
		self.userinfo.loadbaseinfo(6)
		self.userinfo.loadtemplate()

		#get begin date
		begin_date = datetime.date(int(self.userinfo.begin_year),int(self.userinfo.begin_month),int(self.userinfo.begin_day))
		delta = datetime.timedelta(days=7)
		now=begin_date
		#nowarr=str(now).split('-')
		next=now+delta
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
		
		#sort game
		k=0	#field number
		d=0	#day numer
		n=0	#round number
		for i in range(self.userinfo.team_count):
			for j in range(self.userinfo.team_count):
				if i<j:
					self.userinfo.field[0].date[d]=now
					self.arr.teamA[i][j]=self.userinfo.team[i].name
					self.arr.teamB[i][j]=self.userinfo.team[j].name
					
					#round first
					if n<self.userinfo.count:
						n+=1	#if round is not use end, then use other round to start contest.
					else:
						n=0		#if all field and all round is full, then user other days.
						d+=1
						now=next	#update date information
						next=next+delta	
						
					print i,j
					print str(d)+" "+str(n)
					print self.userinfo.field[0].date[d]
					print self.userinfo.team[i].name + " VS " + self.userinfo.team[j].name
		
		
		#d is need skip.#
		self.maxd=d+1
		
		#enum array
		self.enumarray_main()
		
		
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
		
	def enumarray_sub(self,arrow,x,y,addedx,addedy,takeout,day):
		if self.arr.isOver[x][y]==False and self.arr.teamA[x][y]!="" and self.arr.teamB[x][y]!="":	#if this cell is can be choice, then save it and acount added number by arrow.
			self.arr.isOver[x][y]=True
			takeout+=1
			self.userinfo.field[0].teamA[day][takeout]=self.arr.teamA[x][y]
			self.userinfo.field[0].teamB[day][takeout]=self.arr.teamB[x][y]
			if arrow=="y":
				addedy+=1
			else:
				addedy=1
			print takeout,self.arr.teamA[x][y],self.arr.teamB[x][y]
		elif addedy>=2 and arrow=="x":	#if it is change row, then this should clear y count.
			addedy=0
		
		if takeout<self.userinfo.count and x<self.userinfo.team_count:	#if take out is not enough.
			print "in",x,y,addedx,addedy
			if addedy<2 and y<self.userinfo.team_count:	#if this row can be choice, and y is not over array length.
				self.enumarray_sub("y",x,y+1,addedx,addedy,takeout,day)
			else:	#if this row is take out more then rule, or this y is over then array length.
				self.enumarray_sub("x",x+1,0,addedx,addedy,takeout,day)
		#else:	#if x is over then array, then restart it
			#self.enumarray_sub("x",0,0,addedx,addedy,takeout,day)
	
	def enumarray_main(self):
		#output matrix
		for j in range(self.userinfo.team_count):
			for i in range(self.userinfo.team_count):
				if self.arr.isOver[i][j]==False and self.arr.teamA[i][j]!="" and self.arr.teamB[i][j]!="":
					print self.arr.teamA[i][j],"-",self.arr.teamB[i][j],",",
				else:
					print "  -   ,",
			print
			
		#enum all result util no anyone is not choice
		d=0
		while True:
			sum=0
			for i in range(self.userinfo.team_count):
				for j in range(self.userinfo.team_count):
					if self.arr.isOver[i][j]==False and self.arr.teamA[i][j]!="" and self.arr.teamB[i][j]!="":
						sum+=1
			
			if sum>=self.userinfo.count:
				self.enumarray_sub("y",0,0,0,0,0,d)
				d+=1
			else:
				self.flag=True
				t=0
				for i in range(self.userinfo.team_count):
					for j in range(self.userinfo.team_count):
						if self.arr.isOver[i][j]==False and self.arr.teamA[i][j]!="" and self.arr.teamB[i][j]!="":
							self.userinfo.field[0].teamA[d][t]=self.arr.teamA[i][j]
							self.userinfo.field[0].teamB[d][t]=self.arr.teamB[i][j]
							t+=1
							self.arr.isOver[i][j]=True
				break

export_array4()