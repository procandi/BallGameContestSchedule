
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

import re

#my self module to process some question
import modFile
import modOffice
import modPublic

class frmField(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnClose = System.Windows.Forms.Button()
		self._btnSav = System.Windows.Forms.Button()
		self._btnDel = System.Windows.Forms.Button()
		self._dgvf = System.Windows.Forms.DataGridView()
		self._fname = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._dgvf.BeginInit()
		self.SuspendLayout()
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(89, 177)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(100, 25)
		self._btnClose.TabIndex = 0
		self._btnClose.Text = "返回"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# btnSav
		# 
		self._btnSav.Location = System.Drawing.Point(12, 174)
		self._btnSav.Name = "btnSav"
		self._btnSav.Size = System.Drawing.Size(52, 28)
		self._btnSav.TabIndex = 2
		self._btnSav.Text = "存檔"
		self._btnSav.UseVisualStyleBackColor = True
		self._btnSav.Click += self.BtnSavClick
		# 
		# btnDel
		# 
		self._btnDel.Location = System.Drawing.Point(217, 174)
		self._btnDel.Name = "btnDel"
		self._btnDel.Size = System.Drawing.Size(55, 28)
		self._btnDel.TabIndex = 3
		self._btnDel.Text = "刪除"
		self._btnDel.UseVisualStyleBackColor = True
		self._btnDel.Click += self.BtnDelClick
		# 
		# dgvf
		# 
		self._dgvf.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dgvf.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
			[self._fname]))
		self._dgvf.Location = System.Drawing.Point(12, 14)
		self._dgvf.Name = "dgvf"
		self._dgvf.RowTemplate.Height = 24
		self._dgvf.Size = System.Drawing.Size(264, 154)
		self._dgvf.TabIndex = 11
		# 
		# fname
		# 
		self._fname.HeaderText = "球場名稱"
		self._fname.Name = "fname"
		# 
		# frmField
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(284, 217)
		self.Controls.Add(self._dgvf)
		self.Controls.Add(self._btnDel)
		self.Controls.Add(self._btnSav)
		self.Controls.Add(self._btnClose)
		self.Name = "frmField"
		self.Text = "設定球場"
		self.Load += self.FrmFieldLoad
		self._dgvf.EndInit()
		self.ResumeLayout(False)

	def FrmFieldLoad(self, sender, e):
		#load file body
		file=modFile.modFile()
		result=file.readfile("fielddata.txt")
		
		#set data to datagridview
		i=0
		val=result.split("\r\n")
		for v in val:
			if v is None:
				break
			if v=="":
				break

			#make regexp to replace heaer name
			rev=re.sub(r"field.+=","",v)
			
			self._dgvf.Rows.Add()
			self._dgvf.Rows[i].Cells[0].Value=rev
			i+=1
		
		pass

	def BtnCloseClick(self, sender, e):
		self.Close()
		pass

	def BtnSavClick(self, sender, e):
		#load data from datagridview
		i=0
		fbody=""
		for v in self._dgvf.Rows:
			if i+1==self._dgvf.Rows.Count:
				break

			fbody+="field"
			fbody+=str(i)
			fbody+="="
			fbody+=v.Cells[0].Value
			fbody+="\r\n"
			i+=1
		
		#write file body		
		file=modFile.modFile()
		file.writefile("fielddata.txt",fbody)
		
		pass

	def BtnDelClick(self, sender, e):
		self._dgvf.Rows.RemoveAt(self._dgvf.CurrentRow.Index)
		pass