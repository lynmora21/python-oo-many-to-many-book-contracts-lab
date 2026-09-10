class Author:
    # Keep track of all authors created.
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return all contracts belonging to this author.
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return all books this author has contracts for.
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Create a new contract connecting this author and book.
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Add together royalties from all of this author's contracts.
        return sum(contract.royalties for contract in self.contracts())


class Book:
    # Keep track of all books created.
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Return all contracts belonging to this book.
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return all authors who have contracts for this book.
        return [contract.author for contract in self.contracts()]


class Contract:
    # Keep track of all contracts created.
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        # Return contracts matching the requested date.
        return [contract for contract in cls.all if contract.date == date]
