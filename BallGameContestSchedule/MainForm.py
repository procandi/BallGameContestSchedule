import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

#my self form
import frmTeam
import frmSort
import frmField

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._btnSort = System.Windows.Forms.Button()
		self._btnField = System.Windows.Forms.Button()
		self._btnTeam = System.Windows.Forms.Button()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._panel1.Controls.Add(self._btnTeam)
		self._panel1.Controls.Add(self._btnField)
		self._panel1.Controls.Add(self._btnSort)
		self._panel1.Location = System.Drawing.Point(26, 76)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(450, 129)
		self._panel1.TabIndex = 0
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Black
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
		self._textBox1.Font = System.Drawing.Font("新細明體", 36)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(100, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(304, 58)
		self._textBox1.TabIndex = 1
		self._textBox1.Text = "賽程預排系統"
		# 
		# btnSort
		# 
		self._btnSort.Location = System.Drawing.Point(49, 31)
		self._btnSort.Name = "btnSort"
		self._btnSort.Size = System.Drawing.Size(82, 59)
		self._btnSort.TabIndex = 0
		self._btnSort.Text = "排賽程"
		self._btnSort.UseVisualStyleBackColor = True
		self._btnSort.Click += self.BtnSortClick
		# 
		# btnField
		# 
		self._btnField.Location = System.Drawing.Point(183, 31)
		self._btnField.Name = "btnField"
		self._btnField.Size = System.Drawing.Size(90, 61)
		self._btnField.TabIndex = 1
		self._btnField.Text = "設定球場"
		self._btnField.UseVisualStyleBackColor = True
		self._btnField.Click += self.BtnFieldClick
		# 
		# btnTeam
		# 
		self._btnTeam.Location = System.Drawing.Point(324, 31)
		self._btnTeam.Name = "btnTeam"
		self._btnTeam.Size = System.Drawing.Size(80, 61)
		self._btnTeam.TabIndex = 2
		self._btnTeam.Text = "設定球隊"
		self._btnTeam.UseVisualStyleBackColor = True
		self._btnTeam.Click += self.BtnTeamClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(505, 225)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._panel1)
		self.Name = "MainForm"
		self.Text = "主頁面"
		self.Load += self.MainFormLoad
		self._panel1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()

	def BtnFieldClick(self, sender, e):
		field=frmField.frmField()
		field.Show()
		pass

	def BtnTeamClick(self, sender, e):
		team=frmTeam.frmTeam()
		team.Show()
		pass

	def BtnSortClick(self, sender, e):
		sort=frmSort.frmSort()
		sort.Show()
		pass

	def MainFormLoad(self, sender, e):
		pass