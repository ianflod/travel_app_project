class City:

    def __init__(self, name, country, completed = False, id = None):
        self.name = name
        self.country = country
        self.completed = completed
        self.id = id

    def mark_completed(self):
        self.completed = True

        
