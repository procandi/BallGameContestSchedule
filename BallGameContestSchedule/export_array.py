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


#load template and base data
userinfo=modUserInfo.modUserInfo()
userinfo.loadbaseinfo(3)
userinfo.loadtemplate()

#get begin date
begin_date = datetime.date(int(userinfo.begin_year),int(userinfo.begin_month),int(userinfo.begin_day))
delta = datetime.timedelta(days=7)
now=begin_date
#nowarr=str(now).split('-')
next=now+delta
#nextarr=str(next).split('-')

#make array
arr=modPublic.sarray()
for i in range(100):
	for j in range(100):
		arr.teamA[i][j]=""
		arr.teamB[i][j]=""
		arr.black[i][j]=False
		arr.isOver[i][j]=False

#sort game
k=0	#field number
d=0	#day numer
n=0	#round number
for i in range(userinfo.team_count):
	for j in range(userinfo.team_count):
		if i<j and userinfo.team[i].name!=userinfo.team[j].name:
			userinfo.field[k].date[d]=now
			userinfo.field[k].teamA[d][n]=userinfo.team[i].name
			userinfo.field[k].teamB[d][n]=userinfo.team[j].name

			print str(k)+" "+str(d)+" "+str(n)
			print userinfo.field[i].date[d]
			print userinfo.team[i].name + " VS " + userinfo.team[j].name
			
			#round first
			if n<count:
				n+=1	#if round is not use end, then use other round to start contest.
			else:
				if k<userinfo.field_count-1:
					n=0		#if one field all round is full, then user other fields.
					k+=1
				else:
					n=0		#if all field and all round is full, then user other days.
					d+=1
					k=0
					now=next	#update date information
					next=next+delta	
#d is need skip.#


#create excel
#office=modOffice.modOffice()
#office.create_excel_app()
#office.create_excel_workbook()
#office.create_excel_sheets()

#set row and col
#row=1
#col=1

#for i in range(d+1):    #day number
#	for j in range(userinfo.field_count):    #field number
#		#set excel title
#		v=re.sub(r"\d","",str(userinfo.field[j].date[i]))
#		if v!="":
#			office.sheet.Cells(row, col).Value=userinfo.field[j].date[i]
#			office.sheet.Cells(row, col+1).Value=userinfo.field[j].name
#		row+=1
#		
#		#set excel value
#		for k in range(count):    #round number
#			v=re.sub(r"\d","",str(userinfo.field[j].teamA[i][k]))
#			if v!="":
#				if k<3:
#					office.sheet.Cells(row, col).Value=("0"+str(k+7)+":30")
#				else:
#					office.sheet.Cells(row, col).Value=(str(k+7)+":30")
#				office.sheet.Cells(row, col+1).Value=userinfo.field[j].teamA[i][k]
#				office.sheet.Cells(row, col+2).Value=userinfo.field[j].teamB[i][k]
#				row+=1