from bookmanager import BookManager
import pdb

if __name__ == '__main__':
    book_manager = BookManager
    pdb.set_trace()

    # add_book(title, author, genre, year_published)
    # update_book(book_id, title=None, author=None, genre=None, year_published=None)
    # delete_book(book_id)
    # display_books()

    book_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925)
    book_manager.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
    book_manager.add_book("1984", "George Orwell", "Science Fiction", 1949)

    book_manager.update_book(2, title="New Title", year_published=2021)

    book_manager.delete_book(1)

    book_manager.display_books()
