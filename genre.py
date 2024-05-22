class Genre:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def __str__(self):
        return f"Genre: {self.name} Description: {self.description}"    
    



        