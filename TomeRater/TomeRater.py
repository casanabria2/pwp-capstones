class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books_read}".format(name = self.name, email = self.email, books_read = len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        print("User's email has been updated from " + self.email + " to " + address)
        self.email = address

    def read_book(self, book, rating = 'None'):
        self.books[book] = rating

    def get_average_rating(self):
        sum_books = 0
        count_books = 0
        for book in self.books:
            if self.books[book] != 'None':
                sum_books += self.books[book]
                count_books += 1
        return sum_books / count_books


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        print("Book {title} has had its ISBN updated from {isbn_orig} to {isbn_new}".format(title = self.title, isbn_orig = self.isbn, isbn_new = isbn))
        self.isbn = isbn

    def add_rating(self, rating):
        if rating == 'None':
            self.ratings.append(rating)
        else:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def get_average_rating(self):
        sum_ratings = 0
        count_ratings = 0
        for rating in self.ratings:
            if rating != 'None':
                sum_ratings += rating
                count_ratings += 1
        return sum_ratings / count_ratings

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        if self.exists_isbn(isbn):
            print("ISBN already exists!")
        else:
            return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        if self.exists_isbn(isbn):
            print("ISBN already exists!")
        else:
            return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        if self.exists_isbn(isbn):
            print("ISBN already exists!")
        else:
            return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = 'None'):
        try:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            try:
                self.books[book] += 1
            except KeyError:
                self.books[book] = 1
        except KeyError:
            print("No user with email {email}!".format(email = email))

    def add_user(self, name, email, user_books = []):
        if '@' in email and ('.com' in email or '.edu' in email or '.org' in email):
            if email not in self.users:
                self.users[email] = User(name, email)
                for book in user_books:
                    self.add_book_to_user(book, email)
            else:
                print("User {email} already exists!".format(email = email))
        else:
            print("Invalid email address")

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(self.users[user])

    def get_most_read_book(self):
        max_read = 0
        for book in self.books:
            if self.books[book] > max_read:
                max_read = self.books[book]
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        max_avg_rating = 0
        for book in self.books:
            avg_rating = book.get_average_rating()
            if avg_rating > max_avg_rating:
                max_avg_rating = avg_rating
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        max_avg_rating = 0
        for user in self.users:
            avg_rating = self.users[user].get_average_rating()
            if avg_rating > max_avg_rating:
                max_avg_rating = avg_rating
                most_positive_user = user
        return most_positive_user

    def exists_isbn(self, isbn):
        exists_isbn = False
        for book in self.books:
            if book.isbn == isbn:
                exists_isbn = True
                break;
        return exists_isbn