
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

import re

#my self module to process some question
import modFile
import modOffice
import modPublic

#my self form
import frmTeam

class frmTeamConfig(Form):
	def __init__(self,teamindex=0,teamscheduledate=""):
		self.InitializeComponent()
		self.teamindex=teamindex
		self.teamscheduledate=teamscheduledate
	
	def InitializeComponent(self):
		self._mct = System.Windows.Forms.MonthCalendar()
		self._btnSav = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._lblDate = System.Windows.Forms.Label()
		self._btnCls = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# mct
		# 
		self._mct.Location = System.Drawing.Point(29, 7)
		self._mct.Name = "mct"
		self._mct.TabIndex = 4
		self._mct.DateSelected += self.MctDateSelected
		# 
		# btnSav
		# 
		self._btnSav.Location = System.Drawing.Point(29, 270)
		self._btnSav.Name = "btnSav"
		self._btnSav.Size = System.Drawing.Size(52, 28)
		self._btnSav.TabIndex = 9
		self._btnSav.Text = "存檔"
		self._btnSav.UseVisualStyleBackColor = True
		self._btnSav.Click += self.BtnSavClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(187, 273)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(62, 25)
		self._btnClose.TabIndex = 8
		self._btnClose.Text = "返回"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# label3
		# 
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(29, 187)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(116, 23)
		self._label3.TabIndex = 10
		self._label3.Text = "無法參與排賽的日期"
		# 
		# lblDate
		# 
		self._lblDate.ForeColor = System.Drawing.Color.White
		self._lblDate.Location = System.Drawing.Point(29, 210)
		self._lblDate.Name = "lblDate"
		self._lblDate.Size = System.Drawing.Size(220, 45)
		self._lblDate.TabIndex = 11
		self._lblDate.Text = "-"
		# 
		# btnCls
		# 
		self._btnCls.Location = System.Drawing.Point(111, 273)
		self._btnCls.Name = "btnCls"
		self._btnCls.Size = System.Drawing.Size(48, 25)
		self._btnCls.TabIndex = 12
		self._btnCls.Text = "清除"
		self._btnCls.UseVisualStyleBackColor = True
		self._btnCls.Click += self.BtnClsClick
		# 
		# frmTeamConfig
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(284, 320)
		self.Controls.Add(self._btnCls)
		self.Controls.Add(self._lblDate)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._btnSav)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._mct)
		self.Name = "frmTeamConfig"
		self.Text = "設定球隊無法參賽日期"
		self.Load += self.FrmTeamConfigLoad
		self.ResumeLayout(False)


	def BtnSavClick(self, sender, e):
		#load file body
		file=modFile.modFile()
		result=file.readfile("teamdata.txt")
		
		#add schedule date to origin data
		line=result.split("\r\n")
		fbody=""
		for v in line:
			if ("team"+str(self.teamindex)) in v:
				#only get data
				data=v.split("-")
				
				fbody+=data[0]
				fbody+=self._lblDate.Text
			else:
				fbody+=v
			fbody+="\r\n"
		
		#write file body		
		file.writefile("teamdata.txt",fbody)
		
		pass

	def BtnCloseClick(self, sender, e):
		team=frmTeam.frmTeam()
		team.Show()
		self.Close()
		
		pass

	def FrmTeamConfigLoad(self, sender, e):
		self._lblDate.Text=("-"+self.teamscheduledate)
		pass

	def MctDateSelected(self, sender, e):
		#merge date to list, or take out from list
		d=re.sub(r" .*","",str(self._mct.SelectionRange.Start.Date))
		if d in self._lblDate.Text:
			self._lblDate.Text=self._lblDate.Text.replace(d+",","")
		else:
			self._lblDate.Text+=d
			self._lblDate.Text+=","
			
		pass

	def BtnClsClick(self, sender, e):
		self._lblDate.Text="-"
		pass