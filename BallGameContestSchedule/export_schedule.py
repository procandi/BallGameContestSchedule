# -*- coding: utf-8 -*-

import re
import sys
import datetime

import win32com.client
import win32ui

#my self module to process some question
import modUserInfo


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
count=14

k=0	#field number
m=0	#day numer
n=0	#round number
for i in range(userinfo.team_count):
	for j in range(userinfo.team_count):
		if i<j and userinfo.team[i].name!=userinfo.team[j].name:
			userinfo.field[i].datetag[m]=now
			userinfo.field[k].date[m].teamA[n]=userinfo.team[i]
			userinfo.field[k].date[m].teamB[n]=userinfo.team[j]
			
			if k<userinfo.field_count:
				k+=1	#if field is not use end, then use other field to start contest.
			else:
				if n<count:
					k=0		#if all field one round is full, then user other rounds.
					n+=1
				else:
					k=0		#if all field and all round is full, then user other days.
					m+=1
					n=0
					now=next	#update date information
					next=next+delta					
			
			print userinfo.field[i].datetag[m]
			print userinfo.team[i].name.encode("big5") + " VS " + userinfo.team[j].name.encode("big5")

#app = win32com.client.Dispatch("Excel.Application")
#app.visible = True
#workbook = app.Workbooks.Add()
#workbook.Sheets[0].Name = "test"
#sheet = workbook.Sheets[0]
#sheet.Range("A1").Value = ("this is A1"+userinfo.field[1].encode("big5"))
#sheet.Cells(3, 2).Value = "Hi Alarm"  #==B3
#sheet.Cells(3, 2).AddComment()
#sheet.Cells(3, 2).Comment.Shape.Width = 150
#sheet.Cells(3, 2).Comment.Shape.Height = 160
#sheet.Cells(3, 2).Comment.Text("this is memo")
