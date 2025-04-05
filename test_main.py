from main import Library, Book, User
import unittest

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.library = Library("Тестова бібліотека")
        self.book1 = Book("1984", "Джордж Орвелл", "Антиутопія")
        self.book2 = Book("Собачье серце", "Михайло Булгаков", "Сатира")
        self.user = User("Олег", 101)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_borrow_book(self):
        self.user.borrow_book(self.book1)
        self.assertTrue(self.book1.is_borrowed)
        self.assertIn(self.book1, self.user.borrowed_books)

    def test_return_book(self):
        self.user.borrow_book(self.book1)
        self.user.return_book(self.book1)
        self.assertFalse(self.book1.is_borrowed)
        self.assertNotIn(self.book1, self.user.borrowed_books)

    def test_borrow_already_borrowed_book(self):
        self.user.borrow_book(self.book1)
        another_user = User("Марія", 102)
        another_user.borrow_book(self.book1) 
        self.assertTrue(self.book1.is_borrowed)

    def test_return_book_not_borrowed(self):
        self.user.return_book(self.book2)  
        self.assertFalse(self.book2.is_borrowed)

if __name__ == '__main__':
    unittest.main()
