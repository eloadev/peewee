from bookmanager import BookManager
import pdb

if __name__ == '__main__':
    book_manager = BookManager
    pdb.set_trace()

    # create(title, author, genre, year_published)
    # update(book_id, title=None, author=None, genre=None, year_published=None)
    # delete(book_id)
    # all()

    book_manager.create("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925)
    book_manager.create("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
    book_manager.create("1984", "George Orwell", "Science Fiction", 1949)

    book_manager.update(2, title="New Title", year_published=2021)

    book_manager.delete(1)

    book_manager.all()
