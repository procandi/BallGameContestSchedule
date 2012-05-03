#it is a path for program know python where is.
pypath=".\python25"

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

import re

#import base python module
import sys
sys.path.append(pypath+"\lib")
import os

#my self module to process some question
import modFile

class frmSort(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._dtps = System.Windows.Forms.DateTimePicker()
		self._label1 = System.Windows.Forms.Label()
		self._btnHandle = System.Windows.Forms.Button()
		self._pResult = System.Windows.Forms.Panel()
		self._btnContestExcel = System.Windows.Forms.Button()
		self._btnRecordExcel = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._btnContestExcel2 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._cmbCount = System.Windows.Forms.ComboBox()
		self._btnRecordExcel2 = System.Windows.Forms.Button()
		self._btnRecordExcel3 = System.Windows.Forms.Button()
		self._btnRecordExcel4 = System.Windows.Forms.Button()
		self._pResult.SuspendLayout()
		self.SuspendLayout()
		# 
		# dtps
		# 
		self._dtps.Location = System.Drawing.Point(110, 24)
		self._dtps.Name = "dtps"
		self._dtps.Size = System.Drawing.Size(126, 22)
		self._dtps.TabIndex = 0
		# 
		# label1
		# 
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(31, 31)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(73, 20)
		self._label1.TabIndex = 1
		self._label1.Text = "賽程起始日"
		# 
		# btnHandle
		# 
		self._btnHandle.Location = System.Drawing.Point(49, 79)
		self._btnHandle.Name = "btnHandle"
		self._btnHandle.Size = System.Drawing.Size(96, 24)
		self._btnHandle.TabIndex = 2
		self._btnHandle.Text = "計算"
		self._btnHandle.UseVisualStyleBackColor = True
		self._btnHandle.Click += self.BtnHandleClick
		# 
		# pResult
		# 
		self._pResult.BackColor = System.Drawing.Color.Cyan
		self._pResult.Controls.Add(self._btnRecordExcel4)
		self._pResult.Controls.Add(self._btnRecordExcel3)
		self._pResult.Controls.Add(self._btnRecordExcel2)
		self._pResult.Controls.Add(self._btnContestExcel2)
		self._pResult.Controls.Add(self._btnRecordExcel)
		self._pResult.Controls.Add(self._btnContestExcel)
		self._pResult.Location = System.Drawing.Point(23, 109)
		self._pResult.Name = "pResult"
		self._pResult.Size = System.Drawing.Size(273, 155)
		self._pResult.TabIndex = 3
		self._pResult.Visible = False
		# 
		# btnContestExcel
		# 
		self._btnContestExcel.Location = System.Drawing.Point(8, 9)
		self._btnContestExcel.Name = "btnContestExcel"
		self._btnContestExcel.Size = System.Drawing.Size(114, 29)
		self._btnContestExcel.TabIndex = 0
		self._btnContestExcel.Text = "輸出龍馬組賽程表"
		self._btnContestExcel.UseVisualStyleBackColor = True
		self._btnContestExcel.Click += self.BtnContestExcelClick
		# 
		# btnRecordExcel
		# 
		self._btnRecordExcel.Location = System.Drawing.Point(8, 74)
		self._btnRecordExcel.Name = "btnRecordExcel"
		self._btnRecordExcel.Size = System.Drawing.Size(114, 30)
		self._btnRecordExcel.TabIndex = 1
		self._btnRecordExcel.Text = "輸出龍組成積表"
		self._btnRecordExcel.UseVisualStyleBackColor = True
		self._btnRecordExcel.Click += self.BtnRecordExcelClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(151, 79)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(100, 24)
		self._btnClose.TabIndex = 4
		self._btnClose.Text = "返回"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# btnContestExcel2
		# 
		self._btnContestExcel2.Location = System.Drawing.Point(128, 9)
		self._btnContestExcel2.Name = "btnContestExcel2"
		self._btnContestExcel2.Size = System.Drawing.Size(136, 29)
		self._btnContestExcel2.TabIndex = 2
		self._btnContestExcel2.Text = "輸出健康快樂組賽程表"
		self._btnContestExcel2.UseVisualStyleBackColor = True
		self._btnContestExcel2.Click += self.BtnContestExcel2Click
		# 
		# label2
		# 
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(31, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(73, 20)
		self._label2.TabIndex = 5
		self._label2.Text = "每日賽程數"
		# 
		# cmbCount
		# 
		self._cmbCount.FormattingEnabled = True
		self._cmbCount.Items.AddRange(System.Array[System.Object](
			["9",
			"10"]))
		self._cmbCount.Location = System.Drawing.Point(110, 53)
		self._cmbCount.Name = "cmbCount"
		self._cmbCount.Size = System.Drawing.Size(126, 20)
		self._cmbCount.TabIndex = 6
		self._cmbCount.Text = "9"
		# 
		# btnRecordExcel2
		# 
		self._btnRecordExcel2.Location = System.Drawing.Point(128, 74)
		self._btnRecordExcel2.Name = "btnRecordExcel2"
		self._btnRecordExcel2.Size = System.Drawing.Size(136, 30)
		self._btnRecordExcel2.TabIndex = 3
		self._btnRecordExcel2.Text = "輸出馬組成積表"
		self._btnRecordExcel2.UseVisualStyleBackColor = True
		self._btnRecordExcel2.Click += self.BtnRecordExcel2Click
		# 
		# btnRecordExcel3
		# 
		self._btnRecordExcel3.Location = System.Drawing.Point(8, 110)
		self._btnRecordExcel3.Name = "btnRecordExcel3"
		self._btnRecordExcel3.Size = System.Drawing.Size(114, 30)
		self._btnRecordExcel3.TabIndex = 4
		self._btnRecordExcel3.Text = "輸出健康組成積表"
		self._btnRecordExcel3.UseVisualStyleBackColor = True
		self._btnRecordExcel3.Click += self.BtnRecordExcel3Click
		# 
		# btnRecordExcel4
		# 
		self._btnRecordExcel4.Location = System.Drawing.Point(128, 110)
		self._btnRecordExcel4.Name = "btnRecordExcel4"
		self._btnRecordExcel4.Size = System.Drawing.Size(136, 30)
		self._btnRecordExcel4.TabIndex = 5
		self._btnRecordExcel4.Text = "輸出快樂組成積表"
		self._btnRecordExcel4.UseVisualStyleBackColor = True
		self._btnRecordExcel4.Click += self.BtnRecordExcel4Click
		# 
		# frmSort
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(317, 276)
		self.Controls.Add(self._cmbCount)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._pResult)
		self.Controls.Add(self._btnHandle)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._dtps)
		self.Name = "frmSort"
		self.Text = "frmSort"
		self.Load += self.FrmSortLoad
		self._pResult.ResumeLayout(False)
		self.ResumeLayout(False)

	def BtnHandleClick(self, sender, e):
		#write file body		
		file=modFile.modFile()
		file.writefile("datedata.txt",re.sub(r" .*","",str(self._dtps.Value)))	
		
		#write file body		
		file=modFile.modFile()
		file.writefile("countdata.txt",str(self._cmbCount.Text))	
		
		self._pResult.Visible=True
		pass

	def BtnContestExcelClick(self, sender, e):
		os.system(pypath+"\python.exe export_schedule.py")
		pass

	def BtnRecordExcelClick(self, sender, e):
		os.system(pypath+"\python.exe export_record.py")
		pass

	def FrmSortLoad(self, sender, e):
		pass

	def BtnCloseClick(self, sender, e):
		self.Close()
		pass

	def BtnContestExcel2Click(self, sender, e):
		os.system(pypath+"\python.exe export_schedule2.py")
		pass

	def BtnRecordExcel2Click(self, sender, e):
		os.system(pypath+"\python.exe export_record2.py")
		pass

	def BtnRecordExcel3Click(self, sender, e):
		os.system(pypath+"\python.exe export_record3.py")
		pass

	def BtnRecordExcel4Click(self, sender, e):
		os.system(pypath+"\python.exe export_record4.py")
		pass