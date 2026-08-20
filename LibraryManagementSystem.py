#Library Management System

import csv
import os
import json

jsonfile = "book.json"
csvfile = "book.csv"

class Book:  
        def __init__(self, bookid: str, booktitle: str, bookauthor: str, status="available"):
            self.bookid = bookid.upper()
            self.booktitle = booktitle.title()
            self.bookauthor = bookauthor.title()
            self.status = status

        def forjson(self):  
            return {
                "bookid": self.bookid,
                "booktitle": self.booktitle,
                "bookauthor": self.bookauthor,
                "status": self.status
                }

        def display(self):  # to output everything in a string for users
            if self.status == "available":
                bookstatus = "available"
            else:
                bookstatus = "borrowed"
            return self.bookid + " | " + self.booktitle + " | " + self.bookauthor + " | " + bookstatus


def loadbooks():  # function to load books from json or csv
    books = []
    if os.path.exists(jsonfile) and os.path.getsize(jsonfile) > 0:
        try:
            datafile = open(jsonfile, 'r', encoding="utf-8")  # open json first for reading
            data = json.load(datafile)  # reading the file
            for n in data:
                books.append(Book(    # append our book object to a list
                    n.get("bookid", ""),
                    n.get("booktitle", ""),  # .get helps to get value from the dictionary
                    n.get("bookauthor", ""),
                    n.get("status", "available")
                    ))
            datafile.close()
            return books

        except IOError:
            print("json file not found")

    if os.path.exists(csvfile) and os.path.getsize(csvfile) > 0:  # checking for csv if json did not work
        try:
            datafile = open(csvfile, 'r', encoding="utf-8")
            read = csv.DictReader(datafile)  # reading csv file
            for y in read:
                books.append(Book(
                    y.get("bookid", ""),
                    y.get("booktitle", ""),
                    y.get("bookauthor", ""),
                    y.get("status", "available")
                    ))
            datafile.close()
            return books
        except IOError:
            print("csv not found")
    print("there is no any old files")
    return books


def savingbooks(books):  # writing to the file
    try:
        file = open(jsonfile, 'w', encoding="utf-8")  # writing to json
        datasaved = []  # to store all books in a list
        for b in books:
              datasaved.append(b.forjson())
        json.dump(datasaved, file, indent=4)  # .dump writes the data list to a file, indent makes it readable
        file.close()
    except IOError:
        print("Error saving the file")

    try:
        file = open(csvfile, 'w', newline="", encoding="utf-8")
        writer = csv.writer(file)  # writing to the csv file
        writer.writerow(["bookid", "booktitle", "bookauthor", "status"])
        for b in books:
            writer.writerow([b.bookid, b.booktitle, b.bookauthor, b.status])
        file.close()
    except IOError:
        print("not saved csv")


def forinputvalue(question, minimum):  # for correct input value validation
        while True:
                textvalue = input(question).strip()
                if len(textvalue) < minimum:
                        print(" input must be at least " + str(minimum))
                else:
                        return textvalue


def addingbooks(books):  # this function to add new books
    print(" Add book: ")
    while True:
        bookid = forinputvalue("Enter Book ID (format: B001): ", 3).upper()
        # enforce a clear format: letter "B" followed by digits only, e.g. B001, B023
        # this prevents easy-to-miss typos like "0008" (zero) vs "B008" (letter B)
        if not (bookid.startswith("B") and bookid[1:].isdigit()):
            print(" invalid format, ID must be like B001 (letter B + numbers)")
            continue
        duplicate = False
        for item in books:
            if item.bookid == bookid:
                print(" book id already there")
                duplicate = True
                break
        if duplicate:
            continue
        break
    booktitle = forinputvalue("Title: ", 2)
    bookauthor = forinputvalue("Author: ", 2)
    while True:
          status = input("enter status: ")
          if status in ("", "available", "a"):
             status = "available"
             break
          elif status in ("borrowed", "b"):
              status = "borrowed"
              break
          else:
              print("enter available or borrowed")
    books.append(Book(bookid, booktitle, bookauthor, status))


def viewbooks(books):  # to show all books
         print("Books")
         if not books:
                 print("No books in the library")
                 return
         num = 1
         for b in books:
                print(f"{num}. {b.display()}")
                num += 1
         available = 0
         for b in books:
                if b.status == "available":
                        available += 1
         borrowed = len(books) - available
         length = str(len(books))
         print(" ")
         print("Total books: " + length + " Available: " + str(available) + " Borrowed: " + str(borrowed))


def bookupdate(books):  # book updating
         print(" Update Books")
         viewbooks(books)
         if not books:
                 return
         while True:
                try:
                        number = int(input(" Input book number: "))
                        if not 1 <= number <= len(books):
                                print("error, try again")
                                continue
                        break

                except ValueError:
                        print("Invalid, enter again")

         b = books[number - 1]
         print(f"{number}. {b.display()}")
         newtitle = input("New title (" + b.booktitle + ") (press Enter to keep): ").strip()
         if newtitle != "":
                b.booktitle = newtitle.title()
         newauthor = input("New author (" + b.bookauthor + ") (press Enter to keep): ").strip()
         if newauthor != "":
                b.bookauthor = newauthor.title()
         newstatus = input("New status (" + b.status + ") (a = available, b = borrowed, press Enter to keep): ").strip()
         if newstatus == "a" or newstatus == "available":
                b.status = "available"
         elif newstatus == "b" or newstatus == "borrowed":
                b.status = "borrowed"


def deletingbooks(books):  # deleting a book from library system
        print(" Delete Book")
        viewbooks(books)
        if not books:
                return
        try:
                number = int(input("enter book num to delete: "))
                if not 1 <= number <= len(books):
                        print("error")
                        return
        except ValueError:
                print("Invalid number, enter again")
                return
        b = books[number - 1]
        confirming = input("Delete '" + b.booktitle + "'? (y/n): ").strip().lower()
        if confirming == "y":
                books.pop(number - 1)
        else:
                print("not deleted")


def statistics(books):
        print("Library statistics")
        totalbooks = len(books)
        if totalbooks == 0:
                print("No books in Library")
                return
        availablebooks = 0
        for b in books:
                if b.status == "available":
                        availablebooks += 1
        borrowed = totalbooks - availablebooks
        if totalbooks > 0:
                percentage = (availablebooks * 100) / totalbooks

        print("All books : " + str(totalbooks))
        print("Available : " + str(availablebooks))
        print("Borrowed : " + str(borrowed))
        print("Available %: " + str(round(percentage, 1)) + "%")


def sorting(books):
        print("   Sorting Books   ")
        if not books:
                print(" there is no book")
                return
        print("1. BookID")
        print("2. BookTitle")
        print("3. BookAuthor")
        choose = input("choose input:  ").strip()
        if choose == "1":
                bookssorted = sorted(books, key=lambda b: b.bookid)
                labeld = "BookID"
        elif choose == "2":
                bookssorted = sorted(books, key=lambda b: b.booktitle.lower())
                labeld = "BookTitle"
        elif choose == "3":
                bookssorted = sorted(books, key=lambda b: b.bookauthor.lower())
                labeld = "BookAuthor"
        else:
                print("Invalid choice")
                return
        print(" Sorted by " + labeld + ":")
        for i, b in enumerate(bookssorted, start=1):  # FIX: was books_sorted, now bookssorted
            print(f"{i}. {b.display()}")


def searching(books):
        print("   Search Books   ")
        if not books:
                print("there is no book")
                return
        searchword = input(" Input book id, title or author: ").strip().lower()
        if searchword == "":  # FIX: was " " (a space), now "" (empty string)
                print("cannot be empty")
                return
        found = []
        for b in books:
                if searchword == b.bookid.lower() or searchword == b.bookauthor.lower() or searchword in b.booktitle.lower():
                        found.append(b)
        if not found:
                print("no books found")
                return
        print("Found " + str(len(found)) + " books: ")
        number = 1
        for b in found:
                print(f"{number}. {b.display()}")
                number += 1


def main():
        print("   Welcome to Library    ")
        books = loadbooks()
        while True:
                print("     Menu")
                print("1. Add a book")
                print("2. View all")
                print("3. Update")
                print("4. Delete")
                print("5. Statistics")
                print("6. Sort")
                print("7. Search")
                print("8. Exit and save")

                choice = input(" enter your choice: ")
                if choice == "1":
                        addingbooks(books)
                elif choice == "2":
                        viewbooks(books)
                elif choice == "3":
                        bookupdate(books)
                elif choice == "4":
                        deletingbooks(books)
                elif choice == "5":
                        statistics(books)
                elif choice == "6":
                        sorting(books)
                elif choice == "7":
                        searching(books)
                elif choice == "8":
                        savingbooks(books)
                        break
                else:
                        print(" choice is not valid")
                input("press Enter to continue")


if __name__ == "__main__":
        main()























