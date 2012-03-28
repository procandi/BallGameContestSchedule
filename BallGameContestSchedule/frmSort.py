
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

#my self module to process some question
import modFile
import modOffice
import modPublic

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
		self._pResult.SuspendLayout()
		self.SuspendLayout()
		# 
		# dtps
		# 
		self._dtps.Location = System.Drawing.Point(110, 33)
		self._dtps.Name = "dtps"
		self._dtps.Size = System.Drawing.Size(126, 22)
		self._dtps.TabIndex = 0
		# 
		# label1
		# 
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(31, 40)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(73, 20)
		self._label1.TabIndex = 1
		self._label1.Text = "賽程起始日"
		# 
		# btnHandle
		# 
		self._btnHandle.Location = System.Drawing.Point(49, 63)
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
		self._pResult.Controls.Add(self._btnRecordExcel)
		self._pResult.Controls.Add(self._btnContestExcel)
		self._pResult.Location = System.Drawing.Point(23, 109)
		self._pResult.Name = "pResult"
		self._pResult.Size = System.Drawing.Size(248, 77)
		self._pResult.TabIndex = 3
		self._pResult.Visible = False
		# 
		# btnContestExcel
		# 
		self._btnContestExcel.Location = System.Drawing.Point(26, 18)
		self._btnContestExcel.Name = "btnContestExcel"
		self._btnContestExcel.Size = System.Drawing.Size(78, 29)
		self._btnContestExcel.TabIndex = 0
		self._btnContestExcel.Text = "輸出賽程表"
		self._btnContestExcel.UseVisualStyleBackColor = True
		self._btnContestExcel.Click += self.BtnContestExcelClick
		# 
		# btnRecordExcel
		# 
		self._btnRecordExcel.Location = System.Drawing.Point(146, 17)
		self._btnRecordExcel.Name = "btnRecordExcel"
		self._btnRecordExcel.Size = System.Drawing.Size(82, 30)
		self._btnRecordExcel.TabIndex = 1
		self._btnRecordExcel.Text = "輸出成積表"
		self._btnRecordExcel.UseVisualStyleBackColor = True
		self._btnRecordExcel.Click += self.BtnRecordExcelClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(151, 63)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(100, 24)
		self._btnClose.TabIndex = 4
		self._btnClose.Text = "返回"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# frmSort
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(284, 204)
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
		self._pResult.Visible=True
		pass

	def BtnContestExcelClick(self, sender, e):
		pass

	def BtnRecordExcelClick(self, sender, e):
		pass

	def FrmSortLoad(self, sender, e):
		pass

	def BtnCloseClick(self, sender, e):
		self.Close()
		pass