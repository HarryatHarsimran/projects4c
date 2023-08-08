import random
def number():
    n= random.randint(1,10)
    return n
def alp():
    ap=random.randint(65,90)
    c=random.randint(1,2)
    al=chr(ap)
    if c==1 :
        al=al.upper()
    else:
        al=al.lower()
    return al
def show(a):
    for p in a:
        print(p,end= "")   
def algo():
    li=[]
    for i in range(5):
        if i%2 == 0:
            io=number()
            li.append(io)
        else:
            oi=alp()
            li.append(oi)
    show(li)
num=1  
while num<11:
    print(" \n Captcha:" ,end=">")
    algo()
    num+=1
    


