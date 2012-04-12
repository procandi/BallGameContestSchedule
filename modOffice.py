# -*- coding: utf-8 -*-

import win32com.client
import win32ui


class modOffice:
	def __init__(self):
		pass
	
	def create_excel_app(self):
		self.app=win32com.client.Dispatch("Excel.Application")
		self.app.visible = True
	
	def create_excel_workbook(self):
		self.workbook = self.app.Workbooks.Add()
		
	def create_excel_sheets(self,sid=0,sname="default"):
		self.workbook.Sheets[sid].Name=sname
		self.sheet=self.workbook.Sheets[sid]