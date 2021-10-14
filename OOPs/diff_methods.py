class Book:
    publisher = 'VGS'
    def __init__(self, name, price, pages):
        self.name = name
        self.price = price
        self.pages = pages

    @classmethod
    def book_publisher(cls):
        return cls.publisher

    @staticmethod
    def wish():
        print('Good luck for your exams')

book1 = Book('Telugu', 120, 500)
print(book1.name)
print(Book.book_publisher())
Book.wish()