# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author :str
    pages :int
    price :float
    
    def bookinfo(self):
        return f"{self.title} written by {self.author} of {self.pages} costs {self.price}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)


# TODO: comparing two dataclasses - they implement __eq__
print(b1==b3)

# TODO: change some fields
b1.author="sammy"
print(b1.bookinfo())

