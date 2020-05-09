class Transaction:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def print_line(self):
        print(self.title + " " + str(self.amount) + " " + self.category)