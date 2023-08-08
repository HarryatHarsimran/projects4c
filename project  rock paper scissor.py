# project 4
import random
def gamemwin (comp,user ):
    win = True
    if (comp == 1 and user == "r" ):
        win = None
        return win 
    elif (comp == 1 and user == "s" ):
        win = False
        return win  
    elif (comp == 1 and user == "p" ):
        win = True
        return win 
    elif (comp == 2 and user == "s" ):
         win = True
         return win 
    elif (comp == 2 and user == "p" ):
        win =   None
        return win
    elif (comp == 2 and user == "r" ):
        win =   False
        return win
    elif (comp == 3 and user == "r" ):
        win = True
        return win 
    elif (comp == 3 and user == "p" ):
        win = False
        return win  
    elif (comp == 3 and user == "s" ):
        win = None 
        return win
    else:
        print("do it again")    
    

print ("computer's turn: Rock , paper , Scissor ")

while True:
    user = str(input("Enter Rock (r) , paper (p), Scissor (s)"))
    comp = random.randint(1,3)
    lr=wr=0
    if(comp == 1):
        com = "Rock"
    elif( comp == 2):
        com = "paper"
    else:
        com =  "Scissor"  
    if(user == "r"):
        use = "rock"
    elif( user == "p"):
        use = "paper"
    else:
        use = "Scissor" 
    w=gamemwin(comp,user)
    if (w == None  ):
        print("game tied")
    elif(w == True):
        print("You  won the game ")
    else:
        print("You lose  game ")
    print(f"The comp chose {com} and you chose {use} \n You current score is {wr} \n Comp score is {lr}")
    ch = input("Enter q to quit or just press enter to continue ")
    if ch =="q":
        break



