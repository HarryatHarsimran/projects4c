# project -2
def codeforbook(booklist):
    for i in range(len(booklist)):
        a=booklist[i]
        bookdict[a] = i+1
def avalbook(bookdict):
    print("Books present in the library are : ")
    for x,y in bookdict.items():
         print(f'Name of the book ={x} \tCode= {y} ',end='\n')
def issuebook(booklist,stubookdict):
    name=input("Enter your name")    
    book=input("Enter the name of the book you want to borrow ")
    if book in booklist :
        stubookdict[name] = book
        print(f" You got this book")
        booklist.remove(book)
    else :
        print("Sorry either we don't have this book with us or this book is issued to someonelse")
def returnbook(booklist,stubookdict):
    name=input("Enter your name")
    if name in stubookdict.keys():
        book=input("Enter the code of the book you want to return ")
        booklist.append(book)
        del stubookdict[name]
        print("Thank you for returning this book")
    else:
        print("Please enter your name correctly or there is no pending return")
    
    

if __name__ == "__main__" :
    booklist=['clang', 'datastructures', 'algoithms', 'comp', 'awareness', 'oops', 'code', 'web', 'c++', 'pythn']
    bookdict={}
    codeforbook(booklist)
    stubookdict={}
    while True :
        print('''========= Welcome to Online LIbrary=========
                 1. To see available books
                 2. to issue a book
                 3. To return a book 
                 4. to search a book by its code
                 5. To see the books which arent ther epresent
                 6. to donate a book
                 7. exit library 
                 ***********************************************''')
        ch = int(input("ENter choice "))
        if ch == 1:
            avalbook(bookdict)
        elif ch ==2 :
            issuebook(booklist,stubookdict)
        elif ch ==3 :
            returnbook(booklist,stubookdict)
        elif ch ==4:
            code = int(input("ENter the code (1-10) of the book you want to search "))
            for x,y in bookdict.items():
                if code == y in bookdict.values():
                    print(f"Name of the book is : {x}")
                op= input("If you want to borrow it press b or if you want to check our other options then leave it blank ")
                if op == 'b' or 'B':
                    issuebook(booklist,stubookdict)
                else:
                    continue
        elif ch ==5:
            if len(stubookdict) == 0:
                print("ALL BOOKS ARE AVAiLABLE")
            else:
                for i in stubookdict.values():
                    print(i,end='\n')
        elif ch == 6:
            book=input("Enter the name of the book you want to donate ")
            booklist.append(book)
            print("Thnak you for donating the book:", book)
        elif ch ==7:
            break
        else:
            print("Please reenter choice ")        
