class Transaction:
    def __init__(self, item, price, category, transaction_type):
        self.item = item
        self.price = price
        self.category = category
        self.transaction_type = transaction_type

    def print_line(self):
        print(self.item + " " + str(self.price) + " " + self.category + " " + self.transaction_type)