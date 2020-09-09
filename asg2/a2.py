import random

file = open("movie.txt", "r") # open the file
movies_list = file.readlines() # load each line into a list
file.close() # close the file


def get_menu_option():
	print("*** Movie Title Explorer ***")
	print("r – random movie")
	print("b – begins with")
	print("f – find")
	print("s – save the last displayed movie title to your favourites")
	print("m – my favourites display")
	print("c – clear favourites")
	print("q – quit")
	op=input('command:? ')
	return op

def random_movie():
	print(random.choice(movies_list))
	return

def beginswith():
	op=input('Look for:? ')
	if op=="":
		return
		
	for item in movies_list:
		if op.upper() in item.upper():
			print (item)
	return

def find():
	op=input('Find Movie:? ')
	if op=="":
		return
	for item in movies_list:
		if op.upper() == item.upper():
			print (item)
	return

def saveFav():
	print("You called Save Fav")
	return

def clearFav():
	print("You called Clear Fav")
	return

def myFav():
	print("You called My Fav")
	return
	
while True:
	cmd = get_menu_option() # this function displays the menu and returns with a 
	if cmd == "r":
		random_movie()
	if cmd == "b":
		beginswith()
	if cmd == "f":
		find()
	if cmd == "m":
		myFav()
	if cmd == "c":
		clearFav()
	if cmd == "s":
		saveFav()
	elif cmd == "q":
		break