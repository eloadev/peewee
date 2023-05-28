from peewee import *
from book import Book


class BookManager:
    @staticmethod
    def create(title, author, genre, year_published):
        book = Book(title=title, author=author, genre=genre, year_published=year_published)
        book.save()
        print("Book added successfully.")

    @staticmethod
    def update(book_id, title=None, author=None, genre=None, year_published=None):
        try:
            book = Book.get(Book.id == book_id)
        except Book.DoesNotExist:
            print("Book not found.")
            return

        if title:
            book.title = title
        if author:
            book.author = author
        if genre:
            book.genre = genre
        if year_published:
            book.year_published = year_published

        book.save()
        print("Book updated successfully.")

    @staticmethod
    def delete(book_id):
        try:
            book = Book.get(Book.id == book_id)
        except Book.DoesNotExist:
            print("Book not found.")
            return

        book.delete_instance()
        print("Book deleted successfully.")

    @staticmethod
    def all():
        books = Book.select()
        if books:
            for book in books:
                print(book)
        else:
            print("No books found.")
