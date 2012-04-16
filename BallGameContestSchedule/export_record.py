# -*- coding: utf-8 -*-

import win32com.client
import win32ui

#my self module to process some question
import modUserInfo
import modOffice
import modPublic


#load template and base data
userinfo=modUserInfo.modUserInfo()
userinfo.loadbaseinfo()
userinfo.loadtemplate()

#create excel
office=modOffice.modOffice()
office.create_excel_app()
office.create_excel_workbook()
office.create_excel_sheets()

#set excel value
for i in range(userinfo.team_count):
	office.sheet.Cells(i+2, 1).Value=userinfo.team[i].name
	office.sheet.Cells(1, i+2).Value=userinfo.team[i].name
	office.sheet.Cells(i+2, i+2).Value="X"
	
	office.sheet.Cells(userinfo.team_count+3, i+2).Value=userinfo.team[i].name

office.sheet.Cells(userinfo.team_count+4, 1).Value="應賽".encode("big5")
office.sheet.Cells(userinfo.team_count+5, 1).Value="已賽".encode("big5")
office.sheet.Cells(userinfo.team_count+6, 1).Value="勝".encode("big5")
office.sheet.Cells(userinfo.team_count+7, 1).Value="和".encode("big5")
office.sheet.Cells(userinfo.team_count+8, 1).Value="敗".encode("big5")
office.sheet.Cells(userinfo.team_count+9, 1).Value="失分".encode("big5")
office.sheet.Cells(userinfo.team_count+10, 1).Value="得分".encode("big5")
office.sheet.Cells(userinfo.team_count+11, 1).Value="積分".encode("big5")
office.sheet.Cells(userinfo.team_count+12, 1).Value="名次".encode("big5")