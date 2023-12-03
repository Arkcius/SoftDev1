"""
Make a library
Author: Ryan Robison
"""
import csv

class Book:
    __slots__ = ["title","author","copies"]

    def __init__(self,title:str,author:str,copies:int=1):
        self.title = title
        self.author = author
        self.copies = copies

class Patron:
    __slots__ = ["id","name","has","want"]

    def __init__(self,id="000-0000",name:str="Reader"):
        self.id = id
        self.name = name
        self.has = []
        self.want = []

class CardCatalog:
    __slots__ = ["books_by_title","books_by_author"]
    def __init__(self):
        self.books_by_title = {}
        self.books_by_author = {}

class Library:
    __slots__ = ["on_shelves","patrons","card_catalog"]
    def __init__(self,inventory_filename):
        self.on_shelves = []
        self.patrons = []
        self.card_catalog = CardCatalog ()
        
        with open(inventory_filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_file)

            for record in csv_reader:
                count = int(record[2])
                book = Book(record[0],record[1],count)
                self.on_shelves.append(book)

                books_by_author = self.card_catalog.books_by_author
                if book.author not in books_by_author:
                    books_by_author[book.author] = []
                books_by_author[book.author] += [book]

                books_by_title = self.card_catalog.books_by_title
                if book.title not in books_by_title:
                    books_by_title[book.title] = []
                books_by_title[book.title] += [book]

LIBRARY = Library("data/books.csv")

def find_books_by_author(author):
    found_books = []
    books = LIBRARY.card_catalog.books_by_author
    if author in books:
        found_books = books[author]
    return found_books

def find_books_by_title(title):
    found_books = []
    books = LIBRARY.card_catalog.books_by_title
    if title in books:
        found_books = books[title]
    return found_books

def checkout(book,patron):
    if len(patron.has) <=2:
        if book.copies>0:
            patron.has.append(book)
            book.copies -= 1
        else:
            patron.want.append(book)
    else:
        print("Too many books requested")

def return_book(book,patron):
    patron.has.remove(book)
    book.copies += 1
    for patron in LIBRARY.patrons:
        if book in patron.want:
            patron.want.remove(book)
            patron.has.append(book)
            book.copies -=1
            break


def main():
    patron = Patron(0,"Bruce")
    LIBRARY.patrons.append(patron)
    print(LIBRARY.patrons[0].name)
    print(LIBRARY.on_shelves[10].title,LIBRARY.on_shelves[10].author
    ,LIBRARY.on_shelves[10].copies)

    abook1= find_books_by_title("Beloved")
    abook2= find_books_by_author("Toni Morrison")
    print(abook1[0].title)
    print(abook2[0].title)
    checkout(abook1[0],patron)
    print(patron.has[0].title)
    print(LIBRARY.on_shelves[10].title,LIBRARY.on_shelves[10].author
    ,LIBRARY.on_shelves[10].copies)
    return_book(abook1[0],patron)
    print(LIBRARY.on_shelves[10].title,LIBRARY.on_shelves[10].author
    ,LIBRARY.on_shelves[10].copies)


main()