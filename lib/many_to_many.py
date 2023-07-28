class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # contracts(self): This method should return a list of related contracts.
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    # books(self): This method should return a list of related books using the Contract class as an intermediary.
    def books(self):
        contracts = self.contracts()
        return [contract.book for contract in contracts ]
    
    # This method should create 
    # and return a new Contract object between the author and the specified book with the specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(author=self, book=book, date=date, royalties=royalties)
    
    #  return the total amount of royalties that the author has earned from all of their contracts.
    def total_royalties(self):
        contracts = self.contracts()
        return sum(contract.royalties for contract in contracts) 


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    #  Book class has method contracts() that returns a list of its contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    #  Book class has method authors() that returns a list of its authors
    def authors(self):
        contracts = self.contracts()
        return [contract.author for contract in contracts]



# Create a Contract class that has the following properties: 
# author (Author object), book (Book object), date (string), and royalties (int).
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author should be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The book should be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # A class method contracts_by_date(cls, date): 
    # This method should return all contracts that have the same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls):
        contracts = [contract for contract in cls.all]
        return sorted(contracts, key=lambda contract: contract.date)


 
author1 = Author("Khang")
book1 = Book("JavaScript")
contract1 = Contract(author1, book1, "2023-07-28", 15)
contract2 = Contract(author1, book1, "2023-07-29", 10)

author2 = Author("Ngoc")
book2 = Book("Python")
contract1 = Contract(author2, book2, "2022-02-02", 20)
contract2 = Contract(author2, book2, "2022-01-01", 25)


author2_contracts = author2.contracts()
for contract in author2_contracts:
    print(contract.date)     
    print(contract.royalties)