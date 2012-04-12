# -*- coding: utf-8 -*-

import re
import sys
import datetime

import win32com.client
import win32ui

#my self module to process some question
import modUserInfo
import modOffice
import modPublic


#load base data
userinfo=modUserInfo.modUserInfo()
userinfo.loadbaseinfo()

#get begin date
begin_date = datetime.date(int(userinfo.begin_year),int(userinfo.begin_month),int(userinfo.begin_day))
delta = datetime.timedelta(days=7)
now=begin_date
#nowarr=str(now).split('-')
next=now+delta
#nextarr=str(next).split('-')

#get a day game count
count=9

#sort game
k=0	#field number
d=0	#day numer
n=0	#round number
for i in range(userinfo.team_count):
	for j in range(userinfo.team_count):
		if i<j and userinfo.team[i].name!=userinfo.team[j].name:
			userinfo.field[k].date[d]=now
			userinfo.field[k].teamA[d][n]=userinfo.team[i].name.encode("big5")
			userinfo.field[k].teamB[d][n]=userinfo.team[j].name.encode("big5")

			print str(k)+" "+str(d)+" "+str(n)
			print userinfo.field[i].date[d]
			print userinfo.team[i].name.encode("big5") + " VS " + userinfo.team[j].name.encode("big5")
			
			if k<userinfo.field_count:
				k+=1	#if field is not use end, then use other field to start contest.
			else:
				if n<count:
					k=0		#if all field one round is full, then user other rounds.
					n+=1
				else:
					k=0		#if all field and all round is full, then user other days.
					d+=1
					n=0
					now=next	#update date information
					next=next+delta							
#d is need skip.#


#random result

#change black list date
for m in range(userinfo.team_count):	#team number
	for sche in userinfo.team[m].schedule:	#search all black list data
		if str(sche)!="":	#if this team not have any black list data, then not need to else
		
			for i in range(d+1):    #day number
				for j in range(userinfo.field_count):    #field number
					if sche==userinfo.field[j].date[i]:	#this team have black list data in this date
						
						for k in range(count):    #round number
							if userinfo.field[j].teamA[i][k]==userinfo.team[m].name:	#check team is in what's round
								#swap with next date first round
								v=userinfo.field[j].teamA[i][k]
								userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i+1][k]
								userinfo.field[j].teamA[i+1][k]=t
			
			
#up to up, down to down

#check one team in same time


#create excel
office=modOffice.modOffice()
office.create_excel_app()
office.create_excel_workbook()
office.create_excel_sheets()

#set row and col
row=1
col=1

for i in range(d+1):    #day number
	for j in range(userinfo.field_count):    #field number
		#set excel title
		v=re.sub(r"\d","",str(userinfo.field[j].date[i]))
		if v!="":
			office.sheet.Cells(row, col).Value=userinfo.field[j].date[i]
			office.sheet.Cells(row, col+1).Value=userinfo.field[j].name.encode("big5")
		row+=1
		
		for k in range(count):    #round number
			v=re.sub(r"\d","",str(userinfo.field[j].teamA[i][k]))
			if v!="":
				if k<3:
					office.sheet.Cells(row, col).Value=("0"+str(k+7)+":30")
				else:
					office.sheet.Cells(row, col).Value=(str(k+7)+":30")
				office.sheet.Cells(row, col+1).Value=userinfo.field[j].teamA[i][k]
				office.sheet.Cells(row, col+2).Value=userinfo.field[j].teamB[i][k]
				#office.sheet.Cells(row, col+3).Value=str(j)
				#office.sheet.Cells(row, col+4).Value=str(i)
				#office.sheet.Cells(row, col+5).Value=str(k)
				row+=1


#sheet.Cells(3, 2).AddComment()
#sheet.Cells(3, 2).Comment.Shape.Width = 150
#sheet.Cells(3, 2).Comment.Shape.Height = 160
#sheet.Cells(3, 2).Comment.Text("this is memo")