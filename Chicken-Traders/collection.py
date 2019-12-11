class Collection:
    def __init__(self):
        self.category = ["Animal", "Food", "Medicine", "Misc", "Resource", "Technology", "Tool", "Weapon"]
        self.progress = [0, 0, 0, 0, 0, 0, 0, 0]
        self.max = [4, 10, 4, 8, 9, 9, 4, 7]
        self.item_set = set([])
        self.complete = [False, False, False, False, False, False, False, False]

    def check_item_in_set(self, item):
        return item.name in self.item_set

    def add_and_update(self, item):
        index = self.category.index(item.category)
        self.item_set.add(item.name)
        self.progress[index] += 1





    