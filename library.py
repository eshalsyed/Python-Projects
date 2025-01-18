# Personal Library 
import requests

library = []
print("-------LIBRARY-------")

def add():
    add = input("Enter book name: ")
    genre = input("Enter book genre: ")
    author = input("Enter author: ")
    store = {"title": add, "genre": genre, "author": author, "status": "unread"}
    library.append(store)
    print("Book successfully added!!")

def view():
    if not library:
        print("Library is empty")
    else:
        print("Here is your library:\n")
        for i, book in enumerate(library, start=1):
            print(f"{i}. Title: {book['title']}, Genre: {book['genre']}, Author: {book['author']}, Status: {book['status']}\n")

def read():
    if not library:
        print("Library is empty")
        return
    try:
        op = int(input("Enter the number of book you wish to mark as read: ")) - 1
        if 0 <= op < len(library):
            library[op]["status"] = "read"
            print(f"\n {library[op]['title']} has been marked as read! ")
            
        else:
            print("Invalid option. Please try again. ")
    except ValueError:
        print("Invalid option. Please try again. ")

def delete():
    if not library:
        print("Library is empty")
        return
    view()
    try: 
        d_op = int(input("Enter the number of the book you wish to delete: ")) - 1
        if 0 <= d_op < len(library):
            removed_book = library.pop(d_op)
            print(f"{removed_book['title']} has been removed from the library.")
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    

def find():
    gen = input("Enter a genre to get recommendations: ")
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{gen}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\nRecommended books:\n")
        for item in data.get("items", []):
            title = item["volumeInfo"].get("title", "Unknown")
            author = ", ".join(item["volumeInfo"].get("authors", ["Unknown"]))
            print(f"{title} by {author}")
    else:
        print("Failed to get recommended books")



def main():
    while True:

        print("1. Add book to library")
        print("2. View library")
        print("3. Mark book as read")
        print("4. Delete book from library")
        print("5. Find recommended books")
        print("6. Exit")
        choice = input("Enter option(1-6): ")

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            read()
        elif choice == "4":
            delete()
        elif choice == "5":
            find()
        elif choice == "6":
            sure = input("Are you sure you want to exit? ( yes or no)").strip().lower()
            if sure == "yes":
                print("Good Bye!!")
                break
        else:
            print("Invalid option.")
main()
