class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 Days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has either not availabe or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.book.append(bookName)
        print("Thanks for returning this book ! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow :")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return :")
        return self.book
        

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "C++", "Python OOPS"])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''
        ======Welcome to Centra Library====== 
        Please Choose an option:
        1. List all the books
        2. Request a book 
        3. Add/Return a book 
        4. Exit the library
        '''

        print(welcomeMsg)
        a = int(input("Enter a choice :"))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.requestBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
    