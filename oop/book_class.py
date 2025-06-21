class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        if hasattr(self, 'title'):
            print(f"Deleting {self.title}")
        else:
            print("Deleting an unknown book object.")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

if __name__ == "__main__":
    print("--- Testing Book class directly ---")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(book1)
    print(repr(book1))
    del book1
    print("--- End of direct testing ---")
