"""
* Create a Library Class
* Display Book
* LendBook (Where owns the book if not present)
* Add Book
* BookCollection = Library(list of book , Library Name)
* Create a main function and run to the infinite
* While loop asking user for their Input 
"""

class Library:
    def __init__(self , list , name):
        self.BookList = list
        self.name = name
        self.BookDict = {}
        
    def DisplayBook(self):
        print("We have following book in our Library" + " "+ self.name)
        for book in  self.BookList:
            print(book)
    def LendBook(self , user , book):
        if book not in self.BookDict.keys():
            self.BookDict.update({book:user})
            print("Lender Book DataBase has been update . you can take the book name")
        else:
            print("Book is already being used by" + self.BookDict[book])
    def AddBook(self,book):
        self.BookList.append(book)
        print("Book Has Being  Added to the BookList")
    def return_Book(self , book):
        self.BookDict.pop(book)
        
if __name__ == '__main__':
    Book_Collection = Library(["C++ Basic" , "Data Struture " , "Full Stack Web Development" , "AWS"] , "BookCollection")
    while True:
        print("Welcome to the " + Book_Collection.name + " " + "library . Enter your choice to the continue")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1' , '2' , '3' , '4']:
            print("Enter the Valid Option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            Book_Collection.DisplayBook()
        elif  user_choice == 2:
            book = input("Enter the name of the Book you want to lend")
            user = input("Enter your name")
            Book_Collection.LendBook(user , book)
        elif user_choice == 3:
            book = input("Enter the name of the Book . You Want to add")
            Book_Collection.AddBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return")
            Book_Collection.return_Book(book)
        else:
            print("Not a Valid Options")
            user_choice2 = ""
            while (user_choice2 != 'c' and user_choice2!='q' ):
                user_choice2 = input()
                if user_choice2 == 'q':
                    exit()
                if user_choice2 == 'c':
                    continue
            
            
