# iterator2.py
from collections.abc import Iterator, Iterable


class Book:

    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name


class BookShelf(Iterable):

    def __init__(self):
        self.__books = []
    
    def append_book(self, book: Book):
        self.__books.append(book)
    
    def get_book_at(self, index):
        return self.__books[index] # IndexError
    
    def __iter__(self): # ループ文の際にIteratorとして回してくれる
        print('Iteratorを作成しました')
        return BookShelfIterator(self)

    def get_iterator(self):
        return BookShelfIterator(self)

    def get_reverse_iterator(self):
        return BookShelfIterator(self, reverse=True)

class BookShelfIterator(Iterator):

    def __init__(self, book_shelf: BookShelf, reverse=False):
        self.__book_shelf = book_shelf
        self.__index = -1 if reverse else 0
        self.__reverse = reverse
    
    def __next__(self):
        try:
            print(f'try: {self.__index}')
            book = self.__book_shelf.get_book_at(self.__index)
            self.__index += -1 if self.__reverse else 1
        except IndexError:
            raise StopIteration() # Iterator.nextが終了することを伝える信号
        return book

book_shelf = BookShelf()
book_shelf.append_book(Book('Dragon Ball 1'))
book_shelf.append_book(Book('Dragon Ball 2'))
book_shelf.append_book(Book('Dragon Ball 3'))
book_shelf.append_book(Book('Dragon Ball 4'))
book_shelf.append_book(Book('Dragon Ball 5'))

for book in book_shelf:
    print(book.get_name())
print('-' * 100)
book_iterator = book_shelf.get_iterator()
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())
print(next(book_iterator).get_name())


reverse_iterator = book_shelf.get_reverse_iterator()
print('*'*100)
for book in reverse_iterator:
    print(book.get_name())