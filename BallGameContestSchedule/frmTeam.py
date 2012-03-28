
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
import frmTeamConfig

class frmTeam(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnDel = System.Windows.Forms.Button()
		self._btnSav = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._dgvt = System.Windows.Forms.DataGridView()
		self._tname = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._tClass = System.Windows.Forms.DataGridViewComboBoxColumn()
		self._tGood = System.Windows.Forms.DataGridViewComboBoxColumn()
		self._tschedueldate = System.Windows.Forms.DataGridViewTextBoxColumn()
		self._tsetting = System.Windows.Forms.DataGridViewButtonColumn()
		self._dgvt.BeginInit()
		self.SuspendLayout()
		# 
		# btnDel
		# 
		self._btnDel.Location = System.Drawing.Point(496, 173)
		self._btnDel.Name = "btnDel"
		self._btnDel.Size = System.Drawing.Size(55, 28)
		self._btnDel.TabIndex = 8
		self._btnDel.Text = "刪除"
		self._btnDel.UseVisualStyleBackColor = True
		self._btnDel.Click += self.BtnDelClick
		# 
		# btnSav
		# 
		self._btnSav.Location = System.Drawing.Point(8, 173)
		self._btnSav.Name = "btnSav"
		self._btnSav.Size = System.Drawing.Size(52, 28)
		self._btnSav.TabIndex = 7
		self._btnSav.Text = "存檔"
		self._btnSav.UseVisualStyleBackColor = True
		self._btnSav.Click += self.BtnSavClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(230, 176)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(100, 25)
		self._btnClose.TabIndex = 5
		self._btnClose.Text = "返回"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# dgvt
		# 
		self._dgvt.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dgvt.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
			[self._tname,
			self._tClass,
			self._tGood,
			self._tschedueldate,
			self._tsetting]))
		self._dgvt.Location = System.Drawing.Point(8, 13)
		self._dgvt.Name = "dgvt"
		self._dgvt.RowTemplate.Height = 24
		self._dgvt.Size = System.Drawing.Size(543, 154)
		self._dgvt.TabIndex = 10
		self._dgvt.CellContentClick += self.DgvtCellContentClick
		# 
		# tname
		# 
		self._tname.HeaderText = "球隊名稱"
		self._tname.Name = "tname"
		# 
		# tClass
		# 
		self._tClass.HeaderText = "組別"
		self._tClass.Items.AddRange(System.Array[System.Object](
			["龍組",
			"馬組",
			"健康組",
			"快樂組"]))
		self._tClass.Name = "tClass"
		# 
		# tGood
		# 
		self._tGood.HeaderText = "優先排賽"
		self._tGood.Items.AddRange(System.Array[System.Object](
			["皆可",
			"上午場",
			"下午場"]))
		self._tGood.Name = "tGood"
		# 
		# tschedueldate
		# 
		self._tschedueldate.HeaderText = "無法排賽日"
		self._tschedueldate.Name = "tschedueldate"
		# 
		# tsetting
		# 
		self._tsetting.HeaderText = "無法排賽日設定"
		self._tsetting.Name = "tsetting"
		self._tsetting.Text = "設定"
		# 
		# frmTeam
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(559, 217)
		self.Controls.Add(self._dgvt)
		self.Controls.Add(self._btnDel)
		self.Controls.Add(self._btnSav)
		self.Controls.Add(self._btnClose)
		self.Name = "frmTeam"
		self.Text = "設定球隊"
		self.Load += self.FrmTeamLoad
		self._dgvt.EndInit()
		self.ResumeLayout(False)

	def FrmTeamLoad(self, sender, e):
		#load file body
		file=modFile.modFile()
		result=file.readfile("teamdata.txt")
		
		#set data to datagridview
		i=0
		val=result.split("\r\n")
		for v in val:
			if v is None:
				break
			if v=="":
				break

			#make regexp to replace head, and formated data
			v=re.sub(r"team.+=","",v)
			rev=re.search(r",[^-]*",v)
			sdv=re.search(r"-.*",v)
			v=re.sub(r",.*","",v)
			
			self._dgvt.Rows.Add()
			self._dgvt.Rows[i].Cells[0].Value=v
			if rev.group(0)!="":
				revarr=rev.group(0).split(',')
				self._dgvt.Rows[i].Cells[1].Value=revarr[1].strip()
				self._dgvt.Rows[i].Cells[2].Value=revarr[2].strip()
			if sdv.group(0)!="":
				self._dgvt.Rows[i].Cells[3].Value=sdv.group(0).strip().replace("-","")
			
			i+=1
			
		pass

	def BtnSavClick(self, sender, e):
		#load data from datagridview
		i=0
		fbody=""
		for v in self._dgvt.Rows:
			if i+1==self._dgvt.Rows.Count:
				break

			fbody+="team"
			fbody+=str(i)
			fbody+="="
			fbody+=v.Cells[0].Value
			fbody+=","
			fbody+=v.Cells[1].Value
			fbody+=","
			fbody+=v.Cells[2].Value
			fbody+="-"
			if v.Cells[3].Value is None:
				fbody+=""
			else:
				fbody+=v.Cells[3].Value
			fbody+="\r\n"
			i+=1
		
		#write file body		
		file=modFile.modFile()
		file.writefile("teamdata.txt",fbody)
		
		pass

	def BtnDelClick(self, sender, e):
		self._dgvt.Rows.RemoveAt(self._dgvt.CurrentRow.Index)
		pass

	def BtnCloseClick(self, sender, e):
		self.Close()
		pass

	def DgvtCellContentClick(self, sender, e):
		#load data from datagridview
		i=0
		fbody=""
		for v in self._dgvt.Rows:
			if i+1==self._dgvt.Rows.Count:
				break

			fbody+="team"
			fbody+=str(i)
			fbody+="="
			fbody+=v.Cells[0].Value
			fbody+=","
			fbody+=v.Cells[1].Value
			fbody+=","
			fbody+=v.Cells[2].Value
			fbody+="-"
			if v.Cells[3].Value is None:
				fbody+=""
			else:
				fbody+=v.Cells[3].Value
			fbody+="\r\n"
			i+=1
		
		#write file body		
		file=modFile.modFile()
		file.writefile("teamdata.txt",fbody)
		
		teamconfig=frmTeamConfig.frmTeamConfig(self._dgvt.CurrentRow.Index,self._dgvt.Rows[self._dgvt.CurrentRow.Index].Cells[3].Value)
		teamconfig.Show()
		self.Close()
		pass