# -*- coding: utf-8 -*-

import re
import sys
import datetime

import win32com.client
import win32ui

#my self module to process some question
import modUserInfo
import modOffice


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
			userinfo.field[i].datetag[d]=now
			userinfo.field[k].date[d].teamA[n]=userinfo.team[i].name.encode("big5")
			userinfo.field[k].date[d].teamB[n]=userinfo.team[j].name.encode("big5")

			print str(k)+" "+str(d)+" "+str(n)
			print userinfo.field[i].datetag[d]
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

#random result

#change black date

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
		office.sheet.Cells(row, col).Value=userinfo.field[j].datetag[i]
		office.sheet.Cells(row, col+1).Value=userinfo.field[j].name.encode("big5")
		row+=1
		
		for k in range(count):    #round number
			v=re.sub(r"\d","",str(userinfo.field[j].date[i].teamA[k]))
			if v!="":
				if k<3:
					office.sheet.Cells(row, col).Value=("0"+str(k+7)+":30")
				else:
					office.sheet.Cells(row, col).Value=(str(k+7)+":30")
				office.sheet.Cells(row, col+1).Value=userinfo.field[j].date[i].teamA[k]
				office.sheet.Cells(row, col+2).Value=userinfo.field[j].date[i].teamB[k]
				#office.sheet.Cells(row, col+3).Value=str(j)
				#office.sheet.Cells(row, col+4).Value=str(i)
				#office.sheet.Cells(row, col+5).Value=str(k)
				row+=1


#sheet.Cells(3, 2).AddComment()
#sheet.Cells(3, 2).Comment.Shape.Width = 150
#sheet.Cells(3, 2).Comment.Shape.Height = 160
#sheet.Cells(3, 2).Comment.Text("this is memo")