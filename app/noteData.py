class note:
	typeOfC=""
	content=""

	def __init__(self,t,c):
		self.typeOfC=t
		self.content=c
		return

	def setType(self, newType):
		 self.typeOfC=newType
		 return

	def getContent(self):
		return self.content

	def getType(self):
		return self.typeOfC

a = note("t","c")
print a.getType()