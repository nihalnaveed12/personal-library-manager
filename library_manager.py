import json
import os


LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read = input("Have you read it? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            found = True
            print("❌ Book removed successfully.")
            break
    if not found:
        print("⚠️ Book not found.")

def search_books(library):
    keyword = input("Enter title/author/genre to search: ").strip().lower()
    results = [book for book in library if keyword in book["title"].lower() or
               keyword in book["author"].lower() or keyword in book["genre"].lower()]
    
    if results:
        print(f"\n🔍 Found {len(results)} result(s):")
        for book in results:
            display_book(book)
    else:
        print("❌ No matching books found.")

def view_books(library):
    if not library:
        print("📚 Your library is empty.")
        return
    print("\n📘 All Books in Library:")
    for idx, book in enumerate(library, 1):
        print(f"\nBook {idx}:")
        display_book(book)

def display_book(book):
    read_status = "Read" if book["read"] else "Unread"
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    print(f"Genre: {book['genre']}")
    print(f"Status: {read_status}")

def show_stats(library):
    total = len(library)
    read = sum(1 for book in library if book["read"])
    unread = total - read
    print("\n📊 Library Statistics:")
    print(f"Total Books: {total}")
    print(f"Read: {read}")
    print(f"Unread: {unread}")

def menu():
    library = load_library()

    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. View All Books")
        print("5. Show Statistics")
        print("6. Save Library")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            view_books(library)
        elif choice == "5":
            show_stats(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved successfully.")
        elif choice == "7":
            save_library(library)
            print("👋 Exiting and saving library. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
