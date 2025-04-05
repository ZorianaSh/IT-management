class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = False  

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []  

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} позичив(ла) книгу: {book}")
        else:
            print(f"Книга '{book.title}' вже позичена!")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} повернув(ла) книгу: {book}")
        else:
            print(f"{self.name} не позичав(ла) книгу '{book.title}'.")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки.")

    def list_books(self):
        if not self.books:
            print("Бібліотека порожня!")
        else:
            print(f"Книги в бібліотеці {self.name}:")
            for book in self.books:
                status = "Позичена" if book.is_borrowed else "Доступна"
                print(f"{book} - {status}")

#Початок роботи 
library = Library("Центральна бібліотека")

# Створення книг
book1 = Book("1984", "Джордж Орвелл", "Антиутопія")
book2 = Book("Собачье серце", "Михайло Булгаков", "Сатира")
book3 = Book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", "Фентезі")

# Додавання книг у бібліотеку
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Створення користувача
user = User("Іван", 123)

# Виведення книг
library.list_books()

# Користувач позичає книгу
user.borrow_book(book1)
user.borrow_book(book2)

# Виведення книг після позичання
library.list_books()

# Користувач повертає книгу
user.return_book(book1)

# Виведення книг після повернення
library.list_books()
