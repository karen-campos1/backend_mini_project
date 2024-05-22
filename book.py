# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books
from genre import Genre


class Book(Genre):
    def __init__(self, title, author, isbn, publication_date, genre):
        super().__init__(genre.name, genre.description)
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre = genre
        self.__is_available = True
        
    def get_title(self):
        return self.__title
        
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publication_date(self):
        return self.__publication_date
    
    def get_genre(self):
        return self.__genre
    
    def is_available(self):
        return self.__is_available
    
    def get_genre(self):
        return self.__genre
    
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
        else:
            raise ValueError("Book is already borrowed.")
        
    def return_book(self, book):
        if not self.__is_available:
            self.__is_available = True
        else:
            raise ValueError("Book is already available.")
        
    def __str__(self):
        availability = "Available" if self.__is_available else "Borrowed"
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, " \
               f"Publication Date: {self.__publication_date}, Genre: {self.__genre.get_name()}, Status: {availability}"
