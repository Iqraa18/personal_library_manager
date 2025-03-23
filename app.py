import json

# Load Library from File
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save Library to File
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Add a Book
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
    save_library(library)
    print("✅ Book added successfully!")

# Remove a Book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search for a Book
def search_book(library):
    search_by = input("Search by (1: Title, 2: Author): ")
    query = input("Enter search term: ").strip().lower()
    
    results = [book for book in library if query in book[search_by == "2" and "author" or "title"].lower()]
    
    if results:
        print("📚 Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("❌ No matching books found.")

# Display All Books
def display_books(library):
    if not library:
        print("📚 Your library is empty.")
        return
    print("📖 Your Library:")
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display Statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"📊 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.2f}%")

# Main Menu
def main():
    library = load_library()
    
    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("📁 Library saved to file. Goodbye!")
            save_library(library)
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
