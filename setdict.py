# Create a Python program that generates a set of unique numbers from a given list of numbers, then performs the following operations:
# Adds new elements to the set
# Removes existing elements from the set
# Performs union, intersection, and difference operations with another set
# Implement a dictionary-based data storage system that stores information about books in a library, including:
# Book title
# Author
# Publication year
# Genre
# Write functions to:
# Add new books to the dictionary
# Remove existing books from the dictionary
# Search for books by title, author, or genre
# Display all books in the dictionary, sorted by title or author
# Test your implementation with sample data and verify that all operations work as expected.
set_numbers = {1, 2, 3, 4, 5,1, 2, 3}  # Initial set of unique numbers
print("Initial set of unique numbers:", set_numbers)
user_input = input("Enter a number to add to the set: ")
set_numbers.add(int(user_input))  # Add new element to the set
print("Set after adding new element:", set_numbers)
user_input = input("Enter a number to remove from the set: ")
set_numbers.discard(int(user_input))  # Remove existing element from the set
print("Set after removing element:", set_numbers)
# Perform union, intersection, and difference operations with another set   
set2 = {4, 5, 6, 7, 8}
print("Second set:", set2)
print("Union of sets:", set_numbers.union(set2))
print("Intersection of sets:", set_numbers.intersection(set2))
print("Difference of sets:", set_numbers.difference(set2))


def add_book(library, title, author, year, genre):
    library[title] = {
        'author': author,
        'year': year,
        'genre': genre
    }
    print(f"Book '{title}' added to the library.")
def remove_book(library, title):
    if title in library:
        del library[title]
        print(f"Book '{title}' removed from the library.")
    else:
        print(f"Book '{title}' not found in the library.")
def search_books(library, search_term, search_type):
    results = []
    for title, info in library.items():
        if search_type == 'title' and search_term.lower() in title.lower():
            results.append((title, info))
        elif search_type == 'author' and search_term.lower() in info['author'].lower():
            results.append((title, info))
        elif search_type == 'genre' and search_term.lower() in info['genre'].lower():
            results.append((title, info))
    return results
def display_books(library, sort_by='title'):
    if sort_by == 'title':
        sorted_books = sorted(library.items(), key=lambda x: x[0])
    elif sort_by == 'author':
        sorted_books = sorted(library.items(), key=lambda x: x[1]['author'])
    else:
        print("Invalid sort option. Sorting by title.")
        sorted_books = sorted(library.items(), key=lambda x: x[0])
    
    for title, info in sorted_books:
        print(f"Title: {title}, Author: {info['author']}, Year: {info['year']}, Genre: {info['genre']}")
# Sample data for testing
library = {}
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
add_book(library, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
add_book(library, "1984", "George Orwell", 1948, "Dystopian Fiction")
print("\nAll books in the library (sorted by title):")
display_books(library, sort_by='title')
print("\nSearching for books by author 'George Orwell':")
search_results = search_books(library, "George Orwell", "author")
for title, info in search_results:
    print(f"Title: {title}, Author: {info['author']}, Year: {info['year']}, Genre: {info['genre']}")
remove_book(library, "1984")
print("\nAll books in the library (sorted by title):")
display_books(library, sort_by='title')