import os
import Person as ps

#NOTES
#lineStruct will be that of list. First element is the name. Second element is number of words written, third element is the line.

persons = {}

def getPosts(fileName):
	chatFile = open(fileName, 'r')

	line = chatFile.readlines()
	for i in line:
		lineInfo = extractLine(i)

		if lineInfo != []:
			personsLine(lineInfo)


	chatFile.close()

	# for i in persons:
	# 	print persons[i].getName()
	# 	print persons[i].getNumLines()
	# 	print persons[i].getNumWords()
	# 	print persons[i].getPosts()
	# 	print "\n\n\n"
	return persons

def extractLine(line):
	lineStruct = ["", 0, ""]
	name = ""
	count = 0
	workingLine = line.split()
	for i in range(3, len(workingLine)):
		if ':' not in name:
			name += (" " + workingLine[i])
			continue
		else:
			lineStruct[1] += 1
			lineStruct[2] += (" " + workingLine[i])

	lineStruct[0] = name.strip(':').strip()
	lineStruct[2] = lineStruct[2].strip()

	if lineStruct[1] == 0:
		lineStruct = []

	return lineStruct



#TODO:
'''
make a dictionary of people
assign people to classes
'''

def personsLine(lineInfo):
	if lineInfo[0] not in persons:
		friend = ps.Person(lineInfo[0], [])
		persons[lineInfo[0]] = friend

	persons[lineInfo[0]].addLine(lineInfo)

















