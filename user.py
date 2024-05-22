# User Operations:
# ```
# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
        
    def get_name(self):
        return self.__name
    
    def get_library_id(self):
        return self.__library_id
    
    
    def borrowed_books(self):
        return self.__borrowed_books
    
    def borrow_book(self,book):
        if book not in self.__borrowed_books:
            self.__borrowed_books.append(book)
        else:
            raise ValueError("Book already borrowed by the user.")
        
    def return_book(self,book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
        else:
            raise ValueError("Book not borrowed by the user.")
        
    def __str__(self):
        borrowed_books_titles = [book.get_title() for book in self.__borrowed_books]
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(borrowed_books_titles)}"