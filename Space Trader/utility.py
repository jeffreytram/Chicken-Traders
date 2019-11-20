"""Module with utility functions for the game"""
import random
import math
from item import Item


def fuel_calc(fuel_cost_constant, distance, pilot):
    """Returns the fuel cost for the distance"""
    return fuel_cost_constant * distance * (1 - (pilot / 75))


def repair_cost(repair, engineer):
    return int((repair * 7) * (1 - (engineer / 30)))


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


# Encounter methods.

# Lowers ship fuel level as all options end up with the fuel being spent
def travel_check(game, region):
    distance = game.player.curr_region.distance(region)
    fuel_cost = game.fuel_cost_constant * distance * (1 - (game.player.pilot / 75))
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


def encounter_check(diff_modifier, player):
    check_int = random.randint(0, 200)
    # total encounter chance =  15% * diff
    if check_int <= 10 * diff_modifier:
        return gen_trader()
    elif check_int <= 20 * diff_modifier:
        return gen_bandit()
    elif check_int <= 30 * diff_modifier and len(player.ship.cargo) > 0:
        return gen_police(player)
    else:
        return None


# creates a police dict
def gen_police(player):
    return {"name": "Police", "item": police_item(player)}


# returns a random item the player has
def police_item(player):
    return player.ship.cargo[random.randint(0, len(player.ship.cargo) - 1)]


# removes the item from the player
def forfeit_police(player, police):
    player.ship.cargo.remove(police["item"])


def flee_police(player, police):
    if skill_check(player.pilot):
        # successful flee attempt
        player.karma -= 2
        return True
    else:
        # fail flee attempt
        # forfeit item, lose 15 health, lose 70 credits
        forfeit_police(player, police)
        player.ship.health_level -= 15
        player.credit -= 70
        player.karma -= 1
        return False


def fight_police(player, police):
    if skill_check(player.fighter):
        # successful fight attempt
        player.karma -= 2
        return True
    else:
        # fail fight attempt
        # forefeit item
        forfeit_police(player, police)
        player.karma -= 1
        return False


# creates a bandit dict
def gen_bandit():
    return {"name": "Bandit", "demand": random.randint(75, 150)}


def pay_bandit(player, bandit):
    # Try to pay bandit's demand
    if player.credit >= bandit["demand"]:
        # successful payment
        player.credit -= bandit["demand"]
        return 1
    elif len(player.ship.cargo) > 0:
        # give up all inventory.
        player.ship.cargo.clear()
        return 2
    else:
        # Get damaged
        player.ship.health_level -= 15
        return 3


def fight_bandit(player, bandit):
    if skill_check(player.fighter):
        # successful fight attempt
        # take the bandits credits
        player.credit += int(bandit["demand"] * (5 / 4))
        player.karma += 2
        return True
    else:
        # fail fight attempt
        # lose all credits and get damaged
        player.credit = 0
        player.ship.health_level -= 20
        return False


def flee_bandit(player):
    if skill_check(player.pilot):
        # successful flee atempt
        player.karma += 1
        return True
    else:
        # fail flee attempt
        # lose all credits and get damaged
        player.credit = 0
        player.ship.health_level -= 20
        return False


# create a trader dict
def gen_trader():
    return {"name": "Trader", "item": trader_item()}


# returns a random item
def trader_item():
    item = random.choice(Item.__subclasses__())(random.randint(3, 6))
    # item = rand_element(Item.__subclasses__())(random.randint(3, 6))
    item.b_price = int(0.7 * item.base_price)
    item.s_price = int(0.6 * item.base_price)
    return item


def rob_trader(player, trader):
    if skill_check(player.fighter):
        # successful robbery
        for cargo in player.ship.cargo:
            if cargo.name == trader["item"].name:
                cargo.amount += 1
                trader["item"].amount -= 1
                player.karma -= 2
                return 1
        player.ship.cargo.append(trader["item"])
        player.karma -= 2
        return True
    else:
        # failed robbery attempt
        # player's ship loses 10 health
        player.ship.health_level -= 10
        player.karma -= 1
        return False


def negotiate_trader(player, trader):
    if skill_check(player.merchant):
        # successful negotiation attempt
        if player.karma > 0:
            # half off
            trader["item"].b_price = int(trader["item"].b_price * (1 / 2))
        elif player.karma < 0:
            # 12.5% off
            trader["item"].b_price = int(trader["item"].b_price * (7 / 8))
        else:
            # item's price 33% off
            trader["item"].b_price = int(trader["item"].b_price * (2 / 3))
        return True
    else:
        # failed negotation attempt
        # increase item's price by 150% if bad or neutral karma
        if player.karma <= 0:
            trader["item"].b_price = int(trader["item"].b_price * (3 / 2))
        return False

    # Ignore does nothing
    # Just use previous buy method for buying items.


def skill_check(skill):
    check_int = random.randint(0, 100)
    # success chance - 15% to 60%
    threshold = math.sqrt(skill) * 15
    return check_int <= threshold
    # if check_int <= threshold:
    #     return True
    # else:
    #     return False


def damage(player, npc):
    h_damage = npc.fighterLevel * 100
    if player.ship.health_level >= h_damage:
        player.ship.health_level -= h_damage
    else:
        player.ship.health_level = 0

