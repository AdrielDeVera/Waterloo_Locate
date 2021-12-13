# uguwoogoo
database = [
#NOTE THIS IS JUST FOR TESTING
	{"name":"Snorlax","human":False,"size":True},
	{"name":"Ash","human":True,"size":False}

]


def take_chance(answer, property):
	if answer == "y":
		ans = True	
	else:
		ans = False

	to_remove =[]
	for d in database:
		if d[property] != ans:
			to_remove.append(d)
	for i in to_remove:
		database.remove(i)

	if len(database)== 1:
		print("your character is "+database[0]["name"])

#asks questions for user input
#ADD VALIDATION/ERROR HANDLING
def main():
#QUESTIONS JUST FOR TESTING
  ans = input("is the ans human?")
  take_chance(ans,"human")

  ans = input("is the ans large?")
  take_chance(ans,"size")

#calls main
main()
