# Jaiden's waterloo_locate fork
#Class containing a constructor method for each location in the game
class locations:
    def __init__(self,name,academic,residence,studentServices,north,east,central,eng,math,sci,arts,env,ahs,age):
        self.name=name
        self.academic =academic
        self.residence = residence
        self.studentServices = studentServices
        self.north=north
        self.east=east
        self.central=central
        self.eng=eng
        self.math=math
        self.sci=sci
        self.arts=arts
        self.env=env
        self.ahs=ahs
        self.age=age
        
#Instantiations of the locations class to be passed into the database  
cmh = locations("claudette millar hall",True,False,False,False,True,False,False,False,False,False,False,False,4)
pac = locations("physical activity centre",False,False,True,True,False,False,False,False,False,False,False,False,1)
dc = locations("davis centre",True,False,False,True,True,False,False,True,False,False,False,False,33)
#database containing all distinct locations in the game
database = [cmh,pac,dc]
# Bank of questions tethered to the indices of the attributes they are related to
class questions:
    #initializes the properties of the questions class
    def __init__(self,question,relProp):
        self.question = question
        self.relProp = relProp
#list of questions/these are temp values, actual questions will be inputted
q1 = questions("Is your building located in the northern region of campus?","north")
q2 = questions("Does your building belong to the faculty of engineering?","eng")
q3 = questions("Are classes typically held in your building?","academic")
#questions are put into an array/list
array = [q1,q2,q3]
#question are iterated through the array and user answers accordingly
def ask_questions():
 #loops thru list
    index=0
    while len(database)>1:
        value = array[index]
        q=value.question 
        index+=1            
        print(q,"\n 1. yes","\n 2. no","\n 3. not sure")
        ans = input("select choice: ")
        #while not loop error ensures that user inputs an actual choice 
        while not ans == "yes" and ans == "no" and ans == "not sure":
            ans = input("Please select one of the options displayed above : ")    
        if ans =='yes': 
            i=0
            if value.relProp == "north":
                while(i<len(database) and len(database)>1 ):
                    if database[i].north!= True:
                        database.remove(database[i])
                        i-=1
                    i+=1
            elif value.relProp == "eng":
                while(i<len(database) and len(database)>1 ): 
                    
                    if database[i].eng!= True:
                        database.remove(database[i])
                        i-=1
                    i+=1
            elif value.relProp == "academic":
                while(i<len(database) and len(database)>1 ): 
                    
                    if database[i].academic!= True:
                        database.remove(database[i])
                        i-=1
                    i+=1
        elif ans =='no':    
            i=0
            if value.relProp == "north":
                while(i<len(database) and len(database)>1 ):
                   
                    if database[i].north== True: 
                        database.remove(database[i])
                        i-=1
                    i+=1
            elif value.relProp == "eng": 
                while(i<len(database) and len(database)>1 ):
                    
                    if database[i].eng== True:
                        database.remove(database[i])
                        i-=1
                    i+=1
            elif value.relProp == "academic":
                while(i<len(database) and len(database)>1 ): 
                    
                    if database[i].academic== True:
                        database.remove(database[i])
                        i-=1
                    i+=1            
    if(len(database)==1):
        print("The building you are thinking of is " +database[0].name)
            
            
    
       
#main function/structure
def main():
    
    ask_questions()

main()
