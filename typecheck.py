class Book:
    BOOK_TYPES=('HARDCOVER','PAPERBACK','EBOOK')

    __booklist=None

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES
    @staticmethod
    def getbooklist():
        if Book.__booklist==None:
            Book.__booklist=[]
        return Book.__booklist

    def __init__(self,title,booktype):
        self.title= title
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype=booktype


class Newspaper:
    def __init__(self,name):

        self.name= name
print('Book types: ', Book.getbooktypes())

b1=Book("dog", "HARDCOVER")
b2= Book('cat','EBOOK')
n1= Newspaper('toi')
n2= Newspaper('ton')

print(type(b1))
print(type(n1))

print(type(b1)==type(b2))
print(type(b1)==type(n1))

print(isinstance(b2,Book))
print(isinstance(b2,Newspaper))

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)