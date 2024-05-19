class time():
	def __init__(self,h=0,m=0,s=0):
		self.hour=h
		self.minute=m
		self.second=s
	def __print__(self):
		return str(self.hour)+'-'+str(self.minute)+'+'+str(self.minute)
	def __add__(self,other):
		tmp = time()
		tmp.second = self.second + other.second
		tmp.minute = self.minute + other.minute + tmp.second//60
		tmp.second = tmp.second%60
		tmp.hour = self.hour + other.hour + tmp.minute//60
		tmp.minute %= 60
		return tmp
	def __sub__(self,other):
		tmp = time()
		tmp.second = self.second - other.second
		tmp.minute = self.minute - other.minute + tmp.second//60
		tmp.second = tmp.second%60
		tmp.hour = self.hour - other.hour + tmp.minute//60
		tmp.minute %= 60
		return tmp
	def __mul__(self,num):
		tmp = time()
		tmp.second = self.second*num
		tmp.minute = self.minute*num + tmp.second//60
		tmp.second = tmp.second%60
		tmp.hour = self.hour*num+ tmp.minute//60
		tmp.minute %= 60
		return tmp
		
		