import json
import os

# ---------------------------
# Load the library from a file
# ---------------------------
def load_library(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)  # Load existing library
    return []  # Return empty library if file doesn't exist

# ---------------------------
# Save the library to a file
# ---------------------------
def save_library(filename, library):
    with open(filename, 'w') as file:
        json.dump(library, file, indent=4)  # Save library in readable JSON format

# ---------------------------
# Add a new book
# ---------------------------
def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print(f"✅ '{title}' has been added to your library.\n")

# ---------------------------
# Remove a book by title
# ---------------------------
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"🗑️ '{title}' has been removed from your library.\n")
            return
    print(f"⚠️ Book titled '{title}' not found.\n")

# ---------------------------
# Search for a book by title or author
# ---------------------------
def search_books(library):
    keyword = input("Enter a title or author to search for: ").strip().lower()
    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print_book(book)
            found = True
    if not found:
        print("🔍 No matching books found.\n")

# ---------------------------
# Display all books
# ---------------------------
def display_books(library):
    if not library:
        print("📚 Your library is empty.\n")
        return
    for book in library:
        print_book(book)

# ---------------------------
# Print a book's details
# ---------------------------
def print_book(book):
    print(f"📖 Title: {book['title']}")
    print(f"✍️ Author: {book['author']}")
    print(f"📅 Year: {book['year']}")
    print(f"🏷️ Genre: {book['genre']}")
    print(f"✅ Read: {'Yes' if book['read'] else 'No'}\n")

# ---------------------------
# Display statistics
# ---------------------------
def display_statistics(library):
    total = len(library)
    read = sum(1 for book in library if book['read'])
    percentage = (read / total * 100) if total > 0 else 0
    print(f"📊 Total books: {total}")
    print(f"📚 Books read: {read}")
    print(f"📈 Percentage read: {percentage:.2f}%\n")

# ---------------------------
# Main program loop
# ---------------------------
def main():
    FILENAME = "library.json"
    library = load_library(FILENAME)

    while True:
        print("====== Personal Library Manager ======")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(FILENAME, library)
            print("📁 Library saved. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select a number from 1 to 6.\n")

# ---------------------------
# Run the program
# ---------------------------
if __name__ == "__main__":
    main()