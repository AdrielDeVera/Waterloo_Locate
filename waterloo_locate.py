# Jaiden's waterloo_locate fork
#Class containing a constructor method for each location in the game
class locations:
    def __init__(self,name,kind,ordinalPoint, faculty, age):
        self.name=name
        self.kind =kind
        self.ordinalPoint = ordinalPoint
        self.faculty=faculty
        self.age=age
#Instantiations of the locations class to be passed into the database  
cmh = locations("claudette millar hall","academic","south east","engineering",4)
pac = locations("physical activity centre","student services","north","n/a",1)
dc = locations("davis centre","academic","north","mathematics",33)
#database containing all distinct locations in the game
database = [cmh,pac,dc]
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
  ans = input("Is your building more than 5 years old?")
  take_chance(ans,"human")

  ans = input("is the ans large?")
  take_chance(ans,"size")

#calls main
main()
