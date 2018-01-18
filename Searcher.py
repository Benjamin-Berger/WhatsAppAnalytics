import Person as ps

# def searchWord(word,line):
# 	return line.count(word)

# def searchLines(word,lines):
# 	count = 0
# 	for i in lines:
# 		count += searchWord(word, i)
# 	return count

# def searchPerson(word,person):
# 	count = searchLines(word,person.getPosts


curses = ["fuck", "shit", "bull", "crap", "hell", "cunt", "goodness"]

def searchCurse(persons):
	heathens = {}
	for i in persons:
		heathens[i] = sum(persons[i].getMass().count(x) for x in curses)

	return heathens