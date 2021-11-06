import json
import csv
import itertools


def book_reader():
    with open('books.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            yield row


new_books_list = []
for book in book_reader():
    new_books_list.append({'title': book[0],
                           'author': book[1],
                           'pages': int(book[3]),
                           'genre': book[2]})


with open("users.json", "r") as f:
    users = json.loads(f.read())

users_list = users
new_users_list = []
for user in users_list:
    new_users_list.append({'name': user["name"],
                           'gender': user["gender"],
                           'address': user["address"],
                           'age': user["age"],
                           'books': []})


iterable = itertools.cycle(range(len(new_users_list)))

for book in new_books_list:
    item = next(iterable)
    new_users_list[item]['books'].append(book)


with open("reference.json", "w") as f:
    s = json.dumps(new_users_list, indent=4)
    f.write(s)

