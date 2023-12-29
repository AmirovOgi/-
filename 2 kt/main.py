import csv
import json

def load_books_and_users(books_file, users_file):
    with open(books_file, newline='') as csvfile:
        books = list(csv.DictReader(csvfile))

    with open(users_file) as jsonfile:
        users = json.load(jsonfile)

    return users, books

def format_book_info(book):
    return {
        "title": book['Title'],
        "author": book['Author'],
        "pages": book['Pages'],
        "genre": book['Genre']
    }

def format_user_info(user, books):
    return {
        "name": user['name'],
        "gender": user['gender'],
        "address": user['address'],
        "age": user['age'],
        "books": [format_book_info(book) for book in books]
    }

def organize_users_and_books(users, books):
    count_users = len(users)
    books_per_user, remainder = divmod(len(books), count_users)

    users_with_books = []
    for i in range(count_users):
        user = users[i]
        user_books = books[i * books_per_user:(i + 1) * books_per_user]

        if i < remainder:
            user_books.append(books[count_users * books_per_user + i])

        users_with_books.append(format_user_info(user, user_books))

    return users_with_books

if __name__ == "__main__":
    users, books = load_books_and_users("books.csv", "users.json")
    result_data = organize_users_and_books(users, books)
