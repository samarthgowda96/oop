class Book:
    def __init__(self, title, price, Author=None):
        self.title = title
        self.price = price

        self.author=Author
        self.chapters = []

    def addchapter(self, Chapter):
        self.chapters.append(Chapter)
    def getbookpagescount(self):
        res=0
        for i in self.chapters:
            res+= i.pages
        return res

class Author:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages

auth= Author("Leo","Bernard")

b1 = Book("Love, War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getbookpagescount())

auth1= Author("Sammy","Gowda")

b2 = Book("Beileve", 69.0, auth1)
b2.addchapter(Chapter("Chapter 1", 100))
b2.addchapter(Chapter("Chapter 2", 100))
b2.addchapter(Chapter("Chapter 3", 100))

print(b2.author)
print(b2.title)
print(b2.getbookpagescount())
