import random
import utility
class Item:
	def __init__(self, amount):
		self.amount = amount

#Make more items
class Computer(Item):
	"""Framework for computer"""
	name = "Computer"
	category = "Rescources"
	debut_cap = [6, 8]
	size = 1
	base_price = 300
	description = "It's a Computer!"
	def __init__(self, amount):
		super().__init__(amount)


class Strange_Talisman(Item):
	"""Framework for starngeTalisman"""
	name = "Strange Talisman"
	category = "Misc"
	debut_cap = [1, 1]
	size = 1
	base_price = 5
	description = "A strange talisman from a wandering civilization. It feels warm."
	def __init__(self, amount):
		super().__init__(amount)

class Banana(Item):
	"""Framework for starngeTalisman"""
	name = "Banana"
	category = "Misc"
	debut_cap = [1, 8];
	size = 1
	base_price = 5
	description = "AHHHH. I am banana! Lots of potassium!!!!!"
	def __init__(self, amount):
		super().__init__(amount)

class Apple(Item):
	"""Framework for starngeTalisman"""
	name = "Apple"
	category = "Food"
	debut_cap = [1, 8]
	size = 1
	base_price = 5
	description = "yes. apples."
	def __init__(self, amount):
		super().__init__(amount)

class Gun(Item):
	"""Framework for starngeTalisman"""
	name = "Gun"
	category = "Weapon"
	debut_cap = [1, 8]
	size = 1
	base_price = 5
	description = "This is gun. BOOM! BOOM!"
	def __init__(self, amount):
		super().__init__(amount)

class Bigger_Gun(Item):
	"""Framework for starngeTalisman"""
	name = "Bigger Gun"
	category = "Weapon"
	debut_cap = [1, 8]
	size = 1
	base_price = 5
	description = "now with bigger \"BOOM! BOOM!\"'s"
	def __init__(self, amount):
		super().__init__(amount)

class Fart_In_A_Jar(Item):
	"""Framework for starngeTalisman"""
	name = "Fart in a jar"
	category = "Weapon"
	debut_cap = [1, 8]
	size = 1
	base_price = 5
	description = "mmmm.... fresh air"
	def __init__(self, amount):
		super().__init__(amount)

class Friendship(Item):
	"""Framework for starngeTalisman"""
	name = "Friendship"
	category = "Misc"
	debut_cap = [1, 8]
	size = 1
	base_price = 5
	description = "eeeeeeeeeeeeee friendship"
	def __init__(self, amount):
		super().__init__(amount)

class Russia(Item):
	"""Framework for starngeTalisman"""
	name = "Russia"
	category = "Country"
	debut_cap = [1, 8]
	size = 1
	base_price = 5
	description = "remember to share young comrade"
	def __init__(self, amount):
		super().__init__(amount)