# Author Operations:
# ```
# Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
        
    def name(self):
        return self.__name
    
    def biography(self):
        return self.__biography
    
    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"