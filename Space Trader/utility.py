import random
from item import *
"""Module with utility functions for the game"""

def fuel_calc(fuel_cost_constant, distance, pilot):
	"""Returns the fuel cost for the distance"""
	return fuel_cost_constant * distance * (1 - (pilot/75))

def bprice_calc(merchant, item):
	return int((1 + random.randint(0, 20)/100) * item.base_price * (1 - merchant/75))

def sprice_calc(merchant, item):
	return int((1 - random.randint(10, 20)/100) * item.base_price * (1 + merchant/75))