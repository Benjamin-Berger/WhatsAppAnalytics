class Person:
	def __init__(self, name, posts):
		self.name = name
		self.posts = posts
		self.numWords = 0
		self.numLines = 0

	def getName(self):
		return self.name

	def getPosts(self):
		return self.posts

	def getNumLines(self):
		return self.numLines

	def getNumWords(self):
		return self.numWords	

	def addLine(self,newLine):
		self.numWords += newLine[1]
		self.posts.append(newLine[2])
		self.numLines += 1



# friend = Person("hi", [])

# print friend.getName()