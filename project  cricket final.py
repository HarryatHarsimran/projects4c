                        #PROJECT 1
#program starting
import random
def toss(u,c):
    win=None
    if u in [1,2,3,4,5,6] :
        sum=u+c
        if (sum%2==0 and usereo=="e") or (sum%2!=0 and usereo=="o"):
            win = True
            return win
        elif (sum%2==0 and usereo=="o" ) or (sum%2!=0 and usereo=="e"):
            win=False
            return win

        else:
            win= 0
            return win

    else: 
        win = 0
        return win
userscore=0
cscore=0
while True:
    
    usereo=input("Enter odd(o) or even (e) \n :")
    compeo=random.randint(1,2)
    if  compeo== 1:
        comp="odd"
    elif compeo ==2:
        comp="even"
    if  usereo== "o":
        user="odd"
    elif usereo == "e":
        user="even"
    u=int(input("Enter your no. btw 1-6 \n : "))
    c=random.randint(1,6)
    t=toss(u,c)
    if (t == True):
        print(f"User won, \n You chose {user}\t while the comp chose {comp} \n You chose {u} and com chose {c}")
        ch = int(input("Enter 1 for batting or 2 for bowling "))
        if ch== 1:
            print("user Turn to Bat \n Choose a no.btw 1-6 for runs ")
            while True:
                ur1b=int(input("Enter 1-6  "))
                cd=random.randint(1,6)
                if ur1b>6 or ur1b ==' ':
                    print("Enter number only in 1-6")
                    continue
                if ur1b!= cd:
                    userscore +=ur1b
                    print(f"User scored {ur1b} run, Total runs ={userscore} ")
            
                if cd == ur1b:
 
                    print(f"you are out and your score is {userscore} ")
            
                    t=userscore+1
                    print(f"Comp Turn to Bat and his target is {t} and ")
                    
                    cscore=0
                    while True:
                        ur1bo=int(input("Enter 1-6  "))
                        cb=random.randint(1,6)

                        if ur1bo>6 or ur1bo ==' ':
                            print("Enter number only in 1-6")
                            continue
                        if ur1bo!= cb:
                            cscore +=cb
                            print(f"Comp scored {cb} run, Total runs ={cscore} ")
                        if cscore>t :
                            print("Comp won the game ")
                            break
                        if cb == ur1bo:
                            print(f"Comp is Out and he scored {cscore}  ")
                            if cscore<t:
                                print("User Won and Comp Lose")
                                break
                            elif cscore == userscore:
                                print("Match is drawn ,please rerun the programm")
                                break
        if ch ==2  :
            print("Comp Turn to Bat  ")
            while True:

                ur2bo=int(input("Enter 1-6  "))
                cb=random.randint(1,6)
                if ur2bo>6 or ur2bo ==' ':
                    print("Enter number only in 1-6")
                    continue
                if ur2bo!= cb:
                    cscore +=cb
                    print(f"Comp scored {cb} run, Total runs ={cscore} ")
            
                if cb == ur2bo:
                    print(f"Comp is Out and he scored {cscore}  ")
                
                    t=cscore+1 
                    print("User Turn to Bat  ")  
                    
                    while True:
                        ur2ba=int(input("Enter 1-6  "))
                        cb1=random.randint(1,6)

                        if ur2ba>6 or ur2ba ==' ':
                            print("Enter number only in 1-6")
                            continue
                        if ur2ba!= cb1:
                            userscore +=ur2ba
                            print(f"Player scored {ur2ba} and his current score is {userscore}")
                        if userscore>t:
                                print("User Won and CompLose")
                                break
                        if ur2ba == cb:
                            print("Player out ")
                            
                            if userscore<t:
                                print("Comp Won  and User Lose")
                                break
                            elif cscore == userscore:
                                print("Match is drawn ,please rerun the programm")
                                break 
    elif (t== 0) :
        print("Please renter value or redo the toss ")
    elif (t == False):
        print(f"Comp won, \n You chose {user}\t while the comp chose {comp} \n You chose {u} and com chose {c}")    
        comch=random.randint(1,2)
        ch1 = None
        if comch == 1:
            ch1 = "Bat"
            print("Comp Turn to Bat  ")
            while True:

                ur2bo=int(input("Enter 1-6  "))
                cb=random.randint(1,6)
                if ur2bo>6 or ur2bo ==' ':
                    print("Enter number only in 1-6")
                    continue
                if ur2bo!= cb:
                    cscore +=cb
                    print(f"Comp scored {cb} run, Total runs ={cscore} ")
            
                if cb == ur2bo:
                    print(f"Comp is Out and he scored {cscore}  ")
                
                    t=cscore+1 
                    print("User Turn to Bat  ")
                    while True : 
                        ur2ba=int(input("Enter 1-6  "))
                        cb=random.randint(1,6)
                        if ur2ba>6 or ur2ba ==' ':
                            print("Enter number only in 1-6")
                            continue
                        if ur2ba!= cb:
                            userscore +=ur2ba
                        print(f"Player scored {ur2ba} and his current score is {userscore}")
                        if userscore>t:
                            print("User Won and CompLose")
                            break
                        if ur2ba == cb:
                            print("Player out ")
                    
                        if userscore<t:
                            print("Comp Won Won and User Lose")
                            break
                        elif cscore == userscore:
                            print("Match is drawn ,please rerun the programm")
                            break
        elif comch == 2:
            ch1 = "Bowl"
            print("user Turn to Bat \n Choose a no.btw 1-6 for runs ")
            while True:
                ur1b=int(input("Enter 1-6  "))
                cd=random.randint(1,6)
                if ur1b>6 or ur1b ==' ':
                    print("Enter number only in 1-6")
                    continue
                if ur1b!= cd:
                    userscore +=ur1b
                    print(f"User scored {ur1b} run, Total runs ={userscore} ")
            
                if cd == ur1b:
                    userscore +=0 
                    print(f"you are out and your score is {userscore} ")
            
                    t=userscore+1
                    print(f"Comp Turn to Bat and his target is {t} and ")
                    cscore=0
                    while True:
                        ur1bo=int(input("Enter 1-6  "))
                        cb=random.randint(1,6)
                
                        if ur1bo>6 or ur1bo ==' ':
                            print("Enter number only in 1-6")
                            continue
                        if ur1bo!= cb:
                            cscore +=cb
                            print(f"Comp scored {cb} run, Total runs ={cscore} ")
                        if cscore>t:
                            print("Comp Won and User Lose")
                        if cb == ur1bo:
                            print(f"Comp is Out and he scored {cscore}  ")
                        
                            if cscore<t:
                                print("User Won and Comp Lose")
                            elif cscore == userscore:
                                print("Match is drawn ,please rerun the programm")
           
#Program Finished  