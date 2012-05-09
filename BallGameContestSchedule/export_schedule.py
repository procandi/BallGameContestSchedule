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
userinfo.loadbaseinfo(1)
userinfo.loadtemplate()

#get begin date
begin_date = datetime.date(int(userinfo.begin_year),int(userinfo.begin_month),int(userinfo.begin_day))
delta = datetime.timedelta(days=7)
now=begin_date
#nowarr=str(now).split('-')
next=now+delta
#nextarr=str(next).split('-')

#get a day game count
count=int(userinfo.count)

#get maxinum day
#dmax=((userinfo.team_count+1)*userinfo.team_count)/2
#dmax/=3    #because may one team will game contest over three per day
oneteam1=(userinfo.team_count-1)/3
oneteam2=(count*userinfo.field_count)/userinfo.team_count
dmax=int(oneteam1*oneteam2)

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
			#if k<userinfo.field_count-1:
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
			#if n<count:
			#	n+=1	#if round is not use end, then use other round to start contest.
			#else:
			#	if k<userinfo.field_count-1:
			#		n=0		#if one field all round is full, then user other fields.
			#		k+=1
			#	else:
			#		n=0		#if all field and all round is full, then user other days.
			#		d+=1
			#		k=0
			#		now=next	#update date information
			#		next=next+delta	

			#day first
			if d<dmax:
				d+=1
				now=next	#update date information
				next=next+delta    #if day is not use end, then use other date to start contest.
			else:
				if n<count:
					n+=1
					d=0		#if one day all is full, then user other round.
					now=begin_date
					next=now+delta
				else:
					n=0		#if all day and all round is full, then user other fields.
					d=0
					k+=1
					now=begin_date
					next=now+delta
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
		t=userinfo.field[ja].teamB[ia][ka]
		userinfo.field[ja].teamB[ia][ka]=userinfo.field[jb].teamB[ib][kb]
		userinfo.field[jb].teamB[ib][kb]=t
		print "random",ia,ja,ka,ib,jb,kb


#change black list date
#for m in range(userinfo.team_count):	#team number
#	for sche in userinfo.team[m].schedule:	#search all black list data
#		if str(sche)!="":	#if this team not have any black list data, then not need to else
#		
#			for i in range(d+1):    #day number
#				for j in range(userinfo.field_count):    #field number
#					if sche==userinfo.field[j].date[i]:	#this team have black list data in this date
#						
#						for k in range(count):    #round number
#							if userinfo.field[j].teamA[i][k]==userinfo.team[m].name:	#check team is in what's round
#								#swap with last date first round
#								t=userinfo.field[j].teamA[i][k]
#								userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[d][0]
#								userinfo.field[j].teamA[d][0]=t
#								print "black"
			

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
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										print "class1",j,i,k,j,i,n
										
					elif userinfo.team[e].good==userinfo.PM and k<5:	#if this team favorite PM, but it is contest in AM
						for n in range(5,10):	#searh this day PM
							for m in range(userinfo.team_count):	#team number
								if userinfo.field[j].teamA[i][n]==userinfo.team[m].name:	#if this AM team name is equal this team name profile
									if userinfo.team[m].good==userinfo.AM or userinfo.team[m].good==userinfo.ALL:	#and this AM team is favorite AM or ALL										
										#swap round with this team
										t=userinfo.field[j].teamA[i][k]
										userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][n]
										userinfo.field[j].teamA[i][n]=t
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										print "class2",j,i,k,j,i,n
				
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
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										print "class3",j,i,k,j,i,n
					
					elif userinfo.team[e].good==userinfo.PM and k<5:	#if this team favorite PM, but it is contest in AM
						for n in range(5,10):	#searh this day PM
							for m in range(userinfo.team_count):	#team number
								if userinfo.field[j].teamB[i][n]==userinfo.team[m].name:	#if this AM team name is equal this team name profile
									if userinfo.team[m].good==userinfo.AM or userinfo.team[m].good==userinfo.ALL:	#and this AM team is favorite AM or ALL										
										#swap round with this team
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										t=userinfo.field[j].teamB[i][k]
										userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][n]
										userinfo.field[j].teamB[i][n]=t
										print "class4",j,i,k,j,i,n



#check one team in in recently three game contest
addA=0
addB=0
flag=False
for m in range(userinfo.team_count):	#team number
	for i in range(d+1):	#day number
		for j in range(userinfo.field_count):	#field number
			for k in range(count):	#round number
			
				if userinfo.team[m].name==userinfo.field[j].teamA[i][k]:	#if one team have in this round game contest
					addA+=1
					addB=0
				elif userinfo.team[m].name==userinfo.field[j].teamB[i][k]:	#if one team have in this round game contest
					addA=0
					addB+=1
				else:
					addA=0
					addB=0
					
				if addA>=3:	#if this team is contest with recently three game contest, then swap it with next round
					#swap round with this day first team
					t=userinfo.field[j].teamA[i][k]
					userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][0]
					userinfo.field[j].teamA[i][0]=t
					t=userinfo.field[j].teamB[i][k]
					userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[d][0]
					userinfo.field[j].teamB[d][0]=t
					print "recently1",j,i,k
				
					addA=0
					
				elif addB>=3:	#if this team is contest with recently three game contest, then swap it with next round
					#swap round with this day first team
					t=userinfo.field[j].teamA[i][k]
					userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][0]
					userinfo.field[j].teamA[i][0]=t
					t=userinfo.field[j].teamB[i][k]
					userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[d][0]
					userinfo.field[j].teamB[d][0]=t
					print "recently2",j,i,k
					
					addB>=0
				
			addA=0
			addB=0


#check one team in in one day game contest more then three
addA=0
addB=0
flag=False
for m in range(userinfo.team_count):	#team number
	for i in range(d+1):	#day number
		for j in range(userinfo.field_count):	#field number
			for k in range(count):	#round number
			
				if userinfo.team[m].name==userinfo.field[j].teamA[i][k]:	#if one team have in this round game contest
					addA+=1
					print userinfo.team[m].name,"a"
				elif userinfo.team[m].name==userinfo.field[j].teamB[i][k]:	#if one team have in this round game contest
					addB+=1
					print userinfo.team[m].name,"b"
					
				if addA>=3:	#if this team is contest with recently three game contest, then swap it with last day someone round
					n=0
					while userinfo.team[m].name==userinfo.field[d].teamA[i][n]:	
						n+=1
						
					#swap round with last day someone team
					t=userinfo.field[j].teamA[i][k]
					userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[d][n]
					userinfo.field[j].teamA[d][n]=t
					t=userinfo.field[j].teamB[i][k]
					userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[d][n]
					userinfo.field[j].teamB[d][n]=t
					addA-=1
					print "more then three per day 1",m,j,i,k,j,d,n
					
				elif addB>=3:	#if this team is contest with recently three game contest, then swap it with last day someone round
					n=0
					while userinfo.team[m].name==userinfo.field[d].teamB[i][n]:	
						n+=1
					
					#swap round with last day someone team
					t=userinfo.field[j].teamA[i][k]
					userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[d][n]
					userinfo.field[j].teamA[d][n]=t
					t=userinfo.field[j].teamB[i][k]
					userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[d][n]
					userinfo.field[j].teamB[d][n]=t
					addB-=1
					print "more then three per day 2",m,j,i,k,j,d,n
					
		addA=0
		addB=0			
			
#check one team in same time
#for i in range(d+1):	#day number
#	for j in range(userinfo.field_count):	#field number
#		for k in range(count):	#round number
#			v=re.sub(r"\d","",str(userinfo.field[j].teamA[i][k]))
#			if v!="":
#				if userinfo.field[j].teamA[i][k]==userinfo.field[j].teamB[i][k]:	#if this game contest is list same team, then swap it
#					#swap round with this day first team
#					t=userinfo.field[j].teamA[i][k]
#					userinfo.field[j].teamA[i][k]=userinfo.field[j].teamA[i][0]
#					userinfo.field[j].teamA[i][0]=t
#					t=userinfo.field[j].teamB[i][k]
#					userinfo.field[j].teamB[i][k]=userinfo.field[j].teamB[i][0]
#					userinfo.field[j].teamB[i][0]=t
#					print "sametime"


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