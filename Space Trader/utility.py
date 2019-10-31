"""Module with utility functions for the game"""
import random
from item import Item

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
    distance = game.player.curr_region.distance(region)
    fuel_cost = game.fuel_cost_constant * distance * (1 - (game.player.pilot/75))
    fuel_amount = game.player.ship.fuel_level
    if fuel_amount >= fuel_cost:
        game.player.ship.fuel_level = int(fuel_amount - fuel_cost)
        return True
    else:
        return False

def travel(player, region):
    bprice_calc(player, region)
    sprice_calc(player, region)
    player.curr_region = region


def police_check(diff_modifier, player):
    check_int = random.randint(0, int(100 / diff_modifier))
    if check_int <= 8 and len(player.ship.cargo) > 0:
        return True
    else:
        return False

def gen_police(player):
    return {
    "npc": "Police",
    "item": police_item(player)
    }

#returns index(s) for popping from cargo later
def police_item(player):
    return random.randint(0, len(player.ship.cargo) - 1)

def surrender(player, poli):
    player.ship.cargo.pop(poli["item"])

def flee_poli(player, poli):
    if skill_check(player.pilot):
        return True
    else:
        surrender(player, poli)
        player.ship.health_level -= 15
        player.credit -= 70
        return False

def fight_poli(player, poli):
    if (skill_check(player.fighter)):
        return True
    else:
        surrender(poli["item"])
        return False


def bandit_check(diff_modifier):
    check_int = random.randint(0, int(100 / diff_modifier))
    if check_int <= 8:
        return True
    else:
        return False

def gen_bandit():
    return {
    "npc": "Bandit",
    "demand": random.randint(75, 150)
    }

def pay_bandit(player, bandit):
    if player.credit >= bandit["demand"]:
        player.credit -= bandit["demand"]
    elif len(player.ship.cargo) > 0:
        player.ship.cargo.clear()
    else:
        player.ship.health_level -= 15

def flee_bandit(player):
    if skill_check(player.pilot):
        return True
    else:
        player.credit = 0
        player.ship.health_level -= 20
        return False

def fight_bandit(player, bandit):
    if skill_check(player.fighter):
        player.credit += int(bandit["demand"] * (5 / 4))
        return True
    else:
        player.credit = 0
        player.ship.health_level -= 20
        return False


def trader_check():
    check_int = random.randint(0, 50)
    if rand_int <= 7:
        return True
    else:
        return False

def gen_trader():
    return {
    "npc": "Trader",
    "item": utility.trader_item()
    }

def trader_item():
    return rand_element(Item.__subclasses__())(random.randint(3, 6))

def rob_trader(player, trader):
    if (skill_check(player.fighter)):
        trader["item"].amount = random.rantint(1, trader["item"].amount)
        player.cargo.append(trader["item"])
        return True
    else:
        player.ship.health_level -= 10
        return False

def negotiate(player, trader):
    if (skill_check(player.merchant)):
        trader["item"].b_price = int(trader["item"].b_price * (2 / 3))
        return True
    else:
        trader["item"].b_price = int(trader["item"].b_price * (3 / 2))
        return False

#Ignore does nothing

#Just use previous buy method for buying items.

def skill_check(skill):
    check_int = random.randint(0, (100 - 3 * skill))
    if check_int <= 20:
        return True
    else:
        return False

def rand_element(list):
    return list[random.randint(0, len(list) - 1)]

def damage(player, npc):
    damage = npc.fighterLevel * 100
    if (player.ship.health_level >= damage):
        player.ship.health_level = player.ship.health_level - damage
    else:
        player.ship.health_level = 0
