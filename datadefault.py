# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass,field
import random

def price_function():
    return float(random.randrange(20,40))
@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str ="No Title"
    author: str="No Author"
    pages: int=0
    price: float =field(default_factory=price_function)

b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)