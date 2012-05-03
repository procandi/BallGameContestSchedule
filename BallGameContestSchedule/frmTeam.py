
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

import re

#my self module to process some question
import modFile

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
		self._tshow = System.Windows.Forms.DataGridViewCheckBoxColumn()
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
		self._btnDel.Location = System.Drawing.Point(596, 571)
		self._btnDel.Name = "btnDel"
		self._btnDel.Size = System.Drawing.Size(55, 28)
		self._btnDel.TabIndex = 8
		self._btnDel.Text = "刪除"
		self._btnDel.UseVisualStyleBackColor = True
		self._btnDel.Click += self.BtnDelClick
		# 
		# btnSav
		# 
		self._btnSav.Location = System.Drawing.Point(9, 571)
		self._btnSav.Name = "btnSav"
		self._btnSav.Size = System.Drawing.Size(52, 28)
		self._btnSav.TabIndex = 7
		self._btnSav.Text = "存檔"
		self._btnSav.UseVisualStyleBackColor = True
		self._btnSav.Click += self.BtnSavClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(281, 574)
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
			[self._tshow,
			self._tname,
			self._tClass,
			self._tGood,
			self._tschedueldate,
			self._tsetting]))
		self._dgvt.Location = System.Drawing.Point(8, 13)
		self._dgvt.Name = "dgvt"
		self._dgvt.RowTemplate.Height = 24
		self._dgvt.Size = System.Drawing.Size(642, 552)
		self._dgvt.TabIndex = 10
		self._dgvt.CellContentClick += self.DgvtCellContentClick
		# 
		# tshow
		# 
		self._tshow.HeaderText = "是否列入排賽"
		self._tshow.Name = "tshow"
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
		self.ClientSize = System.Drawing.Size(660, 611)
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
			vd=v.split('-')
			va0=vd[0].split(',')

			#add data to datagridview
			self._dgvt.Rows.Add()
			if va0[1]!="":
				for j in range(4):	
					if j==0:
						if va0[j]=="1":
							self._dgvt.Rows[i].Cells[j].Value=True
						elif va0[j]=="0":
							self._dgvt.Rows[i].Cells[j].Value=False
					else:
						self._dgvt.Rows[i].Cells[j].Value=va0[j]
			
				self._dgvt.Rows[i].Cells[4].Value=vd[1]
			
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
			if v.Cells[0].Value==True:
				fbody+="1"
			elif v.Cells[0].Value==False:
				fbody+="0"
			fbody+=","
			fbody+=v.Cells[1].Value
			fbody+=","
			fbody+=v.Cells[2].Value
			fbody+=","
			fbody+=v.Cells[3].Value
			fbody+="-"
			if v.Cells[4].Value is None:
				fbody+=""
			else:
				fbody+=v.Cells[4].Value
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
		#that sure user is click configure button
		if self._dgvt.CurrentCell.ColumnIndex==5:
			#load data from datagridview
			i=0
			fbody=""
			for v in self._dgvt.Rows:
				if i+1==self._dgvt.Rows.Count:
					break
	
				fbody+="team"
				fbody+=str(i)
				fbody+="="
				if v.Cells[0].Value==True:
					fbody+="1"
				elif v.Cells[0].Value==False:
					fbody+="0"
				fbody+=","
				fbody+=v.Cells[1].Value
				fbody+=","
				fbody+=v.Cells[2].Value
				fbody+=","
				fbody+=v.Cells[3].Value
				fbody+="-"
				if v.Cells[4].Value is None:
					fbody+=""
				else:
					fbody+=v.Cells[4].Value
				fbody+="\r\n"
				i+=1
			
			#write file body		
			file=modFile.modFile()
			file.writefile("teamdata.txt",fbody)
			
			teamconfig=frmTeamConfig.frmTeamConfig(self._dgvt.CurrentRow.Index,self._dgvt.Rows[self._dgvt.CurrentRow.Index].Cells[4].Value)
			teamconfig.Show()
			self.Close()
		pass