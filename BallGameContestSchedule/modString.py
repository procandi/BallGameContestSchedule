
class modString:
	def __init__(self):
		pass
	
	def Number2ABC(self,num=0):
		num=27
		pow=26
		ans=""
		while num>=-1:
			temp=chr((num%pow)+65)
			ans+=temp
			num-=pow
			pow*=26
		
		print ans
		return ans