import ChatParser as CP

def main():
	print "Starting Whatsapp Analytics"
	fileName = "_chat.txt"
	persons = CP.getPosts(fileName)


	for i in persons:
		print persons[i].getName()
		print persons[i].getNumLines()
		print persons[i].getNumWords()
		# print persons[i].getPosts()
		print "\n"





if __name__ == "__main__":
    main()