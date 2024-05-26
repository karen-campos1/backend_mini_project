from book import Book
from user import User
from genre import Genre
from author import Author


class Library:
    
    def __init__(self):
        self.books = []
        self.borrowed_books = []
        self.users = []
        self.genres = []
        self.authors = []
        
# first menu: book operations menu    
# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books
    def add_book(self):
        title = input("Enter book title: ").title()
        author = input("Enter book author: ").title()
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter the publication date (EX: yyyy-mm-dd): ")
        genre_name = input("Enter book's genre: ")
        genre_description = input("Enter the genre's description: ")
        genre = Genre(genre_name, genre_description)
        new_book = Book(title, author, isbn, publication_date, genre)
        self.books.append(new_book)
        print(f"Book: {title} by {author} was added successfully!")
     
        
    def checkout_book(self):
        library_id = input("Enter your library member ID number: ").upper()
        user = self.find_user(library_id)
        if user is None:
            print("User Not Found.\nYou are being routed to create a library user account..")
            return

        isbn = input("Enter the ISBN of the book to check out: ")
        book_found = False
        for book in self.books:
            if book.get_isbn() == isbn:
                book_found = True
                if book.is_available():
                    try:
                        user.borrow_book(book)
                        book.borrow_book()
                        print(f"Book '{book.get_title()}' checked out to {user.get_name()}")
                    except ValueError as e:
                        print(f"An error occurred: {e}")
                else:
                    print("That book is unavailable or not found.")
                break
        if not book_found:
            print("Book not found.")

  
    def return_book(self):
        library_id = input("Enter your library member ID number: ")   
        user = self.find_user(library_id)
        if user is None:
            print("User Not Found.")
            return
        
        isbn = input("Enter the ISBN of the book to return: ")
        for book in self.books:
            if book.get_isbn() == isbn and not book.is_available():
                try:
                    user.return_book(book)
                    book.return_book()
                    print(f"Book '{book.title}' returned successfully by {user.name}.")
                except ValueError as e:
                    print(f"An error occurred: {e}")
                    return
        print("Book not found or not borrowed.")
        
        
    def search_books(self):
        search = input("Enter the ISBN or title of the book: ").title()
        for book in self.books:
            if book.get_isbn() == search or book.get_title().title() == search:
                print(book)
                return
            print("Book not found.")                
    
    def display_all_books(self):
        if not self.books:
            print("No books available.")
        else:    
            for book in self.books:
                print(book)     
            
# 2nd menu:                
# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users   
     
    def add_user(self):
        name = input("Enter the user's name: ")
        library_id = "ID" + str(len(self.users) + 1).zfill(5)
        new_user = User(name, library_id)
        self.users.append(new_user)
        print("You've successfully created a new user!")
        print(f"Please save your Library ID number for your records. Your Library ID #: {library_id} ")
        return new_user
    
    def find_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None
    
    
    def view_user_details(self):
        library_id = input("Enter the user's library ID: ")
        user = self.find_user(library_id)
        if user:
            print(user)
        else:
            print("User not found.")
            
    def display_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)
            
#Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors

    def add_author(self):
        name = input("Enter the author's name: ")
        biography = input("Enter some information about the author (optional): ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"You successfully added {name} to authors.")
        return new_author
    
    def view_author_details(self):
        author_name = input("Enter the author's name: ")
        for author in self.authors:
            if author.name() == author_name:
                print(f"Name: {author.name()}")
                print(f"Biography: {author.biography()}")
                return
        else:
            print("Author not found.")    
            
    def display_all_authors(self):         
        if not self.authors:
            print("Author not found.")
        for book in self.authors:
            print(self.authors)
  
            
# Genre Operations:
# 1. Add a new genre
# 2. View genre details
# 3. Display all genres

    def add_genre(self):
        genre_name = input("Enter the genre name: ")
        description = input("Enter a description for the genre entered (optional): ")
        new_genre = Genre(genre_name, description)
        self.genres.append(new_genre)  # Correctly appending to self.genres
        print(f"You successfully added {genre_name} to the list of genres.")
        return new_genre
    
    def view_genre_details(self):
        genre_name = input("Enter the genre name: ")
        genre = self.find_genre(genre_name)
        if genre:
            print(genre)
        else:
            print("Genre not found.")
            
    def display_all_genres(self):         
        if not self.authors:
            print("Genre not found.")
        for genre in self.genres:
            print(self.genres)