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
userinfo.loadbaseinfo(2)
userinfo.loadtemplate()

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
			userinfo.field[k].teamA[d][n]=userinfo.team[i].name
			userinfo.field[k].teamB[d][n]=userinfo.team[j].name

			print str(k)+" "+str(d)+" "+str(n)
			print userinfo.field[i].date[d]
			print userinfo.team[i].name + " VS " + userinfo.team[j].name
			
			#field first
			#if k<userinfo.field_count:
			#	k+=1	#if field is not use end, then use other field to start contest.
			#else:
			#	if n<count:
			#		k=0		#if all field one round is full, then user other rounds.
			#		n+=1
			#	else:
			#		k=0		#if all field and all round is full, then user other days.
			#		d+=1
			#		n=0
			#		now=next	#update date information
			#		next=next+delta
			
			#round first
			if n<count:
				n+=1	#if round is not use end, then use other round to start contest.
			else:
				if k<userinfo.field_count:
					n=0		#if one field all round is full, then user other fields.
					k+=1
				else:
					n=0		#if all field and all round is full, then user other days.
					d+=1
					k=0
					now=next	#update date information
					next=next+delta					
#d is need skip.#


#random result
for m in range(100):
	#make random field, day, round
	ia=random.randint(0,d+1)
	ja=random.randint(0,userinfo.field_count)
	ka=random.randint(0,count)
	ib=random.randint(0,d+1)
	jb=random.randint(0,userinfo.field_count)
	kb=random.randint(0,count)
	
	va=re.sub(r"\d","",str(userinfo.field[ja].teamA[ia][ka]))
	vb=re.sub(r"\d","",str(userinfo.field[jb].teamA[ib][kb]))
	if va!="" and vb!="":
		#swap with random field, day, round
		t=userinfo.field[ja].teamA[ia][ka]
		userinfo.field[ja].teamA[ia][ka]=userinfo.field[jb].teamA[ib][kb]
		userinfo.field[jb].teamA[ib][kb]=t
		print "a"


#change black list date
for m in range(userinfo.team_count):	#team number
	for sche in userinfo.team[m].schedule:	#search all black list data
		if str(sche)!="":	#if this team not have any black list data, then not need to else
		
			for i in range(d+1):    #day number
				for j in range(userinfo.field_count):    #field number
					if sche==userinfo.field[j].date[i]:	#this team have black list data in this date
						
						for k in range(count):    #round number
							if userinfo.field[j].teamA[i][k]==userinfo.team[m].name:	#check team is in what's round
								#swap with last date first round
								t=userinfo.field[j].teamA[i][k]
								userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[d][0]
								userinfo.field[j].teamA[d][0]=t
								print "b"
			

#up to up, down to down
for i in range(d+1):	#day number
	for j in range(userinfo.field_count):	#field number
		
		for k in range(count):	#round number
			for e in range(userinfo.team_count):
				if userinfo.field[j].teamA[i][k]==userinfo.team[e].name:	#if this AM team name is equal this team name profile
					if userinfo.team[e].good==userinfo.AM and k>4:	#if this team favorite AM, but it is contest in PM	
						for n in range(5):	#searh this day AM
							for m in range(userinfo.team_count):	#team number
								if userinfo.field[j].teamA[i][n]==userinfo.team[m].name:	#if this AM team name is equal this team name profile
									if userinfo.team[m].good==userinfo.PM or userinfo.team[m].good==userinfo.ALL:	#and this AM team is favorite PM or ALL										
										#swap round with this team
										t=userinfo.field[j].teamA[i][k]
										userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][n]
										userinfo.field[j].teamA[i][n]=t
										print "c1"
										
					elif userinfo.team[e].good==userinfo.PM and k<5:	#if this team favorite PM, but it is contest in AM
						for n in range(5,10):	#searh this day PM
							for m in range(userinfo.team_count):	#team number
								if userinfo.field[j].teamA[i][n]==userinfo.team[m].name:	#if this AM team name is equal this team name profile
									if userinfo.team[m].good==userinfo.AM or userinfo.team[m].good==userinfo.ALL:	#and this AM team is favorite AM or ALL										
										#swap round with this team
										t=userinfo.field[j].teamA[i][k]
										userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][n]
										userinfo.field[j].teamA[i][n]=t
										print "c2"
				
				if userinfo.field[j].teamB[i][k]==userinfo.team[e].name:	#if this AM team name is equal this team name profile
					if userinfo.team[e].good==userinfo.AM and k>4:	#if this team favorite AM, but it is contest in PM	
						for n in range(5):	#searh this day AM
							for m in range(userinfo.team_count):	#team number
								if userinfo.field[j].teamB[i][n]==userinfo.team[m].name:	#if this AM team name is equal this team name profile
									if userinfo.team[m].good==userinfo.PM or userinfo.team[m].good==userinfo.ALL:	#and this AM team is favorite PM or ALL										
										#swap round with this team
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										print "c3"
					
					elif userinfo.team[e].good==userinfo.PM and k<5:	#if this team favorite PM, but it is contest in AM
						for n in range(5,10):	#searh this day PM
							for m in range(userinfo.team_count):	#team number
								if userinfo.field[j].teamB[i][n]==userinfo.team[m].name:	#if this AM team name is equal this team name profile
									if userinfo.team[m].good==userinfo.AM or userinfo.team[m].good==userinfo.ALL:	#and this AM team is favorite AM or ALL										
										#swap round with this team
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										print "c4"


#check one team in in recently three game contest
add=0
flag=False
for m in range(userinfo.team_count):	#team number
	for i in range(d+1):	#day number
		for j in range(userinfo.field_count):	#field number
			for k in range(count):	#round number
			
				if userinfo.team[m].name==userinfo.field[j].teamA[i][k]:	#if one team have in this round game contest
					add+=1
					flag=True
				elif userinfo.team[m].name==userinfo.field[j].teamB[i][k]:	#if one team have in this round game contest
					add+=1
					flag=False
					
					if add>3:	#if this team is contest with recently three game contest, then swap it with next round
						if flag==True:
							#swap round with this day first team
							t=userinfo.field[j].teamA[i][k]
							userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][0]
							userinfo.field[j].teamA[i][0]=t
							print "d1"
						else:
							#swap round with this day first team
							t=userinfo.field[j].teamB[i][k]
							userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][0]
							userinfo.field[j].teamB[i][0]=t
							print "d2"
						add=0
				
			add=0
		
		
#check one team in same time
for i in range(d+1):	#day number
	for j in range(userinfo.field_count):	#field number
		for k in range(count):	#round number
			v=re.sub(r"\d","",str(userinfo.field[j].teamA[i][k]))
			if v!="":
				if userinfo.field[j].teamA[i][k]==userinfo.field[j].teamB[i][k]:	#if this game contest is list same team, then swap it
					#swap round with this day first team
					t=userinfo.field[j].teamB[i][k]
					userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][0]
					userinfo.field[j].teamB[i][0]=t
					print "e"


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
			office.sheet.Cells(row, col+1).Value=userinfo.field[j].name
		row+=1
		
		#set excel value
		for k in range(count):    #round number
			v=re.sub(r"\d","",str(userinfo.field[j].teamA[i][k]))
			if v!="":
				if k<3:
					office.sheet.Cells(row, col).Value=("0"+str(k+7)+":30")
				else:
					office.sheet.Cells(row, col).Value=(str(k+7)+":30")
				office.sheet.Cells(row, col+1).Value=userinfo.field[j].teamA[i][k]
				office.sheet.Cells(row, col+2).Value=userinfo.field[j].teamB[i][k]
				row+=1


#sheet.Cells(3, 2).AddComment()
#sheet.Cells(3, 2).Comment.Shape.Width = 150
#sheet.Cells(3, 2).Comment.Shape.Height = 160
#sheet.Cells(3, 2).Comment.Text("this is memo")