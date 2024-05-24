# Welcome to the Library Management System!
# Main Menu:
# 1. Book Operations
# 2. User Operations
# 3. Author Operations
# 4. Genre Operations
# 5. Quit

from library import Library

def main():
    library = Library()
    
    print("\nWelcome to the Library Management System!")    
    while True:
        print("""\nMain Menu:\n  Select one of the following options:\n
        1 - Book Menu
        2 - User Menu
        3 - Author Menu
        4 - Genre Menu
        5 - Quit""")
        main_menu_choice = input("Enter your choice: ")
        try: 
            if main_menu_choice == "1":
                print("""\nBook Operations Menu:
        1 - Add a new book
        2 - Borrow a book
        3 - Return a book
        4 - Search for a book
        5 - Display all books
        6 - Exit to main menu """)
                book_menu_choice = input("\nEnter choice: ")
                if book_menu_choice == "1":
                    library.add_book()
                elif book_menu_choice == "2":
                    library.checkout_book()
                elif book_menu_choice == "3":
                    library.return_book()
                elif book_menu_choice == "4":
                    library.search_books()
                elif book_menu_choice == "5":
                    library.display_all_books()
                elif book_menu_choice == "6":
                    break
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")
        try: 
            if main_menu_choice == "2":
                print("""\nUser Operations Menu:
        1 - Add a new user
        2 - View user details
        3 - Display all users
        4 - Exit to main menu""")
                user_menu_choice = input("\nEnter choice: ")
                if user_menu_choice == "1":
                    library.add_user()
                elif user_menu_choice == "2":
                    library.view_user_details()
                elif user_menu_choice == "3":
                    library.display_all_users()
                elif user_menu_choice == "4":
                    return
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")
        try: 
            if main_menu_choice == "3":
                print("""\nAuthor Operations Menu:
        1 - Add a new author
        2 - View author details
        3 - Display all authors
        4 - Exit to main menu""")
                author_menu_choice = input("\nEnter choice: ")
                if author_menu_choice == "1":
                    library.add_author()
                elif author_menu_choice == "2":
                    library.view_author_details()
                elif author_menu_choice == "3":
                    library.display_all_authors()
                elif author_menu_choice == "4":
                    return
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")
        try: 
            if main_menu_choice == "4":
                print("""\nGenre Operations Menu:
        1 - Add a new genre
        2 - View genre details
        3 - Display all genres
        4 - Exit to main menu""")
                genre_menu_choice = input("\nEnter choice: ")
                if genre_menu_choice == "1":
                    library.add_genre()
                elif genre_menu_choice == "2":
                    library.view_genre_details()
                elif genre_menu_choice == "3":
                    library.display_all_genres()
                elif genre_menu_choice == "4":
                    return
                else:
                    print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")  
        if main_menu_choice == "5":
            print("\nExiting the program...")
            break

if __name__ == "__main__":
    main()





# Book Operations:
# ```
# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books
#     ```
# User Operations:
# ```
# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users
#     ```
# Author Operations:
# ```
# Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors
#     ```
# Genre Operations:
# ```
# Genre Operations:
# 1. Add a new genre
# 2. View genre details
# 3. Display all genres
#     ```
