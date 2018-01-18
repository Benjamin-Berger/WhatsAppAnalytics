import os

#NOTES
#lineStruct will be that of list. First element is the name. Second element is number of words written, third element is the line.

def getPosts(fileName):
	chatFile = open(fileName, 'r')

	line = chatFile.readlines()
	for i in line:
		lineInfo = extractLine(i)

			


	chatFile.close()
	return

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