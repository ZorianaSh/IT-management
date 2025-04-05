class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        # Прибрано ініціалізацію is_borrowed
        # self.is_borrowed = False  ← Помилка: відсутня ініціалізація статусу позиченості.

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow_book(self, book):
        # Помилка: книга не позичається
        if not book.is_borrowed:
            # book.is_borrowed = True  ← закоментовано, книга не позичається
            self.borrowed_books.append(book)
        else:
            print(f"Книга '{book.title}' вже позичена!")

    def return_book(self, book):
        # Помилка: книга не повертається
        if book in self.borrowed_books:
            # book.is_borrowed = False  ← закоментовано, книга не повертається
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} не позичав(ла) книгу '{book.title}'.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        # Помилка: книга не додається
        # self.books.append(book)  ← закоментовано, книга не додається
        print(f"Книга '{book.title}' не була додана до бібліотеки.")

    def list_books(self):
        for book in self.books:
            status = "Доступна" if not book.is_borrowed else "Позичена"
            print(f"{book.title} by {book.author} ({book.genre}) - {status}")
