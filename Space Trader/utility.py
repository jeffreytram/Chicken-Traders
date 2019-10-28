"""Module with utility functions for the game"""
import random


def fuel_calc(fuel_cost_constant, distance, pilot):
    """Returns the fuel cost for the distance"""
    return fuel_cost_constant * distance * (1 - (pilot / 75))


def bprice_calc(player, region):
    for item in region.market:
        tech_factor = 1 - ((region.tech_level.value - item.debut) / 14)
        item.b_price = int(tech_factor * item.base_price * (1 - player.merchant / 75))


def sprice_calc(player, region):
    for item in region.market:
        tech_factor = 1 - ((region.tech_level.value - item.debut) / 14)
        item.s_price = int(
            0.7 * (tech_factor * item.base_price * (1 + player.merchant / 75))
        )
    if len(player.ship.cargo) != 0 or player.ship.cargo_size > 0:
        for item in player.ship.cargo:
            tech_factor = 1 - ((region.tech_level.value - item.debut) / 14)
            item.s_price = int(
                0.7 * tech_factor * item.base_price * (1 + player.merchant / 75)
            )

#Encounter methods.

#Lowers ship fuel level as all options end up with the fuel being spent
def travel_check(game, region):
    distance = game.player.curr_region.distance(new_region)
    fuel_cost = game.fuel_cost_constant * distance * (1 - (game.player.pilot/75))
    fuel_amount = game.player.ship.fuel_level
    if fuel_amount >= fuel_cost:
        game.player.ship.fuel_level = int(fuel_amount - fuel_cost)
        return True
    else:
        return False

def police_check(diff_modifier):
    check_int = random.randint(0, int(100 / diff_modifier))
    if check_int <= 10:
        return True
    else:
        return False

def bandit_check(diff_modifier):
    check_int = random.randint(0, int(100 / diff_modifier))
    if check_int <= 10:
        return True
    else:
        return False

def trader_check():
    rand_int = random.randint(0, 100)
    if rand_int <= 20:
        return True
    else:
        return False

def flee(player):
    pass

def fight(player):
    pass

def rob_trader(player):
    pass
