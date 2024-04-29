class BookManager:
    def __init__(self):
        # Initialize an empty dictionary to store books, their quantities, and prices
        self.books = {}

    def add_book(self, title, quantity, price):
        # Add a book to the inventory or increase its quantity if already present
        if title in self.books:
            self.books[title]["quantity"] += quantity
        else:
            self.books[title] = {"quantity": quantity, "price": price}
            print(f"Added {quantity} copies of '{title}' to the inventory.")

    def display_books(self):
        # Display all books in the inventory
        print("Current Inventory:")
        for title, info in self.books.items():
            print(f"{title}: {info['quantity']} copies, Price: {info['price']}")

    def check_availability(self, title):
        # Check the availability of a specific book
        if title in self.books:
            print(f"'{title}' is available in {self.books[title]['quantity']} copies.")
        else:
            print(f"'{title}' is not available in the inventory.")

    def update_price(self, title, new_price):
        # Update the price of a specific book
        if title in self.books:
            self.books[title]['price'] = new_price
            print(f"Price of '{title}' updated to {new_price}.")
        else:
            print(f"'{title}' is not available in the inventory.")

# Sample usage
book_manager = BookManager()

while True:
    action = input("Enter action (add, display, stock, price, exit): ").lower()
    
    if action == "exit":
        break
    
    if action == "add":
        title = input("Enter title of the book: ")
        quantity = int(input("Enter quantity to add: "))
        price = float(input("Enter price of the book: "))
        book_manager.add_book(title, quantity, price)
    
    elif action == "display":
        book_manager.display_books()
    
    elif action == "stock":
        title = input("Enter title of the book to check stock: ")
        book_manager.check_availability(title)
    
    elif action == "price":
        title = input("Enter title of the book to update price: ")
        new_price = float(input("Enter new price: "))
        book_manager.update_price(title, new_price)
