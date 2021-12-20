
class questions:
    #initializes the properties of the questions class
    def __init__(self,question,choice1,choice2,choice3,choice4):
        self.question = question
        self.choice1=choice1
        self.choice2=choice2
        self.choice3=choice3
        self.choice4=choice4
#list of questions/these are temp values, actual questions will be inputted
q1 = questions("What part of campus?","north","south","west","east")
q2 = questions("What side of campus?","left","right","up","down")

#questions are put into an array/list
array = [q1,q2]
#question are iterated through the array and user answers accordingly
def ask_questions():
 #loops thru list
    for index in range(len(array)):
            value = array[index]
            q=value.question 
            c1=value.choice1
            c2=value.choice2
            c3=value.choice3
            c4=value.choice4
        
            print(q,"\n 1.",c1,"\n 2.",c2,"\n 3.",c3,"\n 4.",c4)
            ans = input("select choice: ")
            #while not loop error ensures that user inputs an actual choice 
            while not ans == c1 or ans == c2 or ans == c3 or ans == c4:
                ans = input("select choice: ")

       
#main function/structure
def main():
    
    ask_questions()

main()
