class Author:
    def __init__(self, name, age):
        # Initializing name and age attributes
        self.name = name
        self.age = age
    
    # Method for displaying the title
    def title(self):
        print("Let Me Love You")

class Book(Author):
    def title(self):
        print("Java Basics")

class Song(Author):
    def title(self):
        print("Hug Me")

# Creating instances of Book and Song
book1 = Author("Michelle More", 40)
book2 = Book("James Nestor", 20)
music = Song("Lauren Hills", 24)

# Looping through instance to display information
for x in (book1, book2, music):
    print(x.name, x.age)
    x.title()