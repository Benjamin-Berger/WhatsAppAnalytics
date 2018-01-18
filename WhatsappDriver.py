import ChatParser as CP
import Searcher as search

def main():
	print "Starting Whatsapp Analytics"
	fileName = "group_chat.txt"
	persons = CP.getPosts(fileName)
	heathens = search.searchCurse(persons)

	for i in persons:
		print "Name: " + persons[i].getName()
		print "Number of chats sent: " + str(persons[i].getNumLines())
		print "Number of words sent: " + str(persons[i].getNumWords())
		print "Number of curse words: " + str(heathens[i])
		# print persons[i].getPosts()
		print 



if __name__ == "__main__":
    main()