"""Module with utility functions for the game"""
import random
import math
from item import Item
from transaction import Transaction

category = [
        "Animal",
        "Food",
        "Medicine",
        "Misc",
        "Weapon",
        "Resource",
        "Technology",
        "Tool"
    ]

def fuel_calc(fuel_cost_constant, distance, pilot, cargo_size):
    """Returns the fuel cost for the distance"""
    return int(fuel_cost_constant * distance * (1 - (pilot / 75)) + (cargo_size / 50))


def repair_cost(repair, engineer):
    return int((repair * 7) * (1 - (engineer / 30)))


def bprice_calc(player, region):
    for item in region.market:
        tech_factor = 1 - ((region.tech_level.value - item.debut) / 14)
        price_board_multiplier = region.price_board[category.index(item.category)]
        item.b_price = int(
            tech_factor
            * item.base_price
            * (1 - player.merchant / 70)
            * region.news_multiplier
            * price_board_multiplier
        )
        #print(region.name +": " + item.name + " " + str(tech_factor) + " "+ str(item.base_price) + " " + str(region.news_multiplier) + " " + str(price_board_multiplier))


def sprice_calc(player, region):
    for item in region.market:
        tech_factor = 1 - ((region.tech_level.value - item.debut) / 10)
        price_board_multiplier = region.price_board[category.index(item.category)]
        item.s_price = int(
            0.7
            * tech_factor
            * item.base_price
            * (1 + player.merchant / 70)
            * region.news_multiplier
            * price_board_multiplier
        )
    if len(player.ship.cargo) != 0 or player.ship.cargo_size > 0:
        for item in player.ship.cargo:
            tech_factor = 1 - ((region.tech_level.value - item.debut) / 10)
            price_board_multiplier = region.price_board[category.index(item.category)]
            item.s_price = int(
                0.7
                * tech_factor
                * item.base_price
                * (1 + player.merchant / 70)
                * region.news_multiplier
                * price_board_multiplier
            )


# Encounter methods.

# Lowers ship fuel level as all options end up with the fuel being spent
def travel_check(game, region):
    distance = game.player.curr_region.distance(region)
    fuel_cost = fuel_calc(game.fuel_cost_constant, distance, game.player.pilot, game.player.ship.cargo_size)
    fuel_amount = game.player.ship.fuel_level
    if region == game.player.curr_region:
        return 2
    if fuel_amount >= fuel_cost:
        game.player.ship.fuel_level = fuel_amount - fuel_cost
        return 1
    else:
        return 3

# updates fuel cost from every region to the given region
def update_all_travel_cost(game, curr_region):
    for region in game.universe.region_list:
        distance = curr_region.distance(region)
        region.travel_cost = fuel_calc(game.fuel_cost_constant, distance, game.player.pilot, game.player.ship.cargo_size)

# controller for travel
def travel(game, region):
    bprice_calc(game.player, region)
    sprice_calc(game.player, region)
    game.player.curr_region = region
    game.increment_time()
    if random.randint(1, 5) > 2:
        add_news(game)

# add news
def add_news(game):
    game.news.insert(0, news_event(game.universe.region_list))
    if len(game.news) > 5:
        game.news.pop(-1)


def encounter_check(diff_modifier, player, region_list, time):
    if time >= 9 and time <= 18:
        time_modifier = 1
    else:
        time_modifier = 1.5
    check_int = random.randint(1, 100)
    if check_int <= 10 / time_modifier: # 6% - 10% chance
        return gen_trader()
    elif check_int > 10 and check_int <= 10 + 4 * diff_modifier * time_modifier: # 4% - 12% chance
        return gen_bandit()
    elif check_int > 30 and check_int <= 30 + 4 * diff_modifier * time_modifier and len(player.ship.cargo) > 0: # 4% - 12% chance
        return gen_police(player)
    else:
        return None


def news_event(region_list):
    rng = random.randint(1, 10)
    percent = (
        random.randint(70, 90)
        if random.randint(1, 2) == 1
        else random.randint(110, 130)
    )
    multiplier = percent / 100
    all_items = Item.__subclasses__()
    if rng <= 2:
        # adjust base_price of all items
        for item in all_items:
            item.base_price *= multiplier
        return (
            "The Universe's prices are "
            + ("increasing" if percent > 100 else "decreasing")
            + "! ("
            + str(percent - 100)
            + "%)"
        )
    elif rng <= 5:
        # adjust base_price of category
        rand_category = category[random.randint(0, len(category) - 1)]
        for item in all_items:
            if item.category == rand_category:
                item.base_price *= (1 + multiplier % 1 * 2) if multiplier > 1 else 1 - (1 - multiplier) * 2
        return (
            "The price of "
            + rand_category
            + " items have "
            + ("increased" if percent > 100 else "decreased")
            + "! ("
            + str((percent - 100) * 2)
            + "%)"
        )
    elif rng <= 8:
        # adjust b_price of specific item
        rand_item = all_items[random.randint(0, len(all_items) - 1)]
        rand_item.base_price *= (1 + multiplier % 1 * 3) if multiplier > 1 else 1 - (1 - multiplier) * 3
        return (
            rand_item.name
            + " is becoming "
            + ("trendy" if percent > 100 else "unpopular")
            + "! ("
            + str((percent - 100) * 3)
            + "%)"
        )
    else:
        # adjust base_price of all items in a specific region
        rand_region = region_list[random.randint(0, len(region_list) - 1)]
        rand_region.news_multiplier *= multiplier
        return (
            "Region "
            + rand_region.name
            + "'s prices are "
            + ("increasing" if percent > 100 else "decreasing")
            + "! ("
            + str(percent - 100)
            + "%)"
        )

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
        # forfeit item, lose 15 health, lose 100 credits
        forfeit_police(player, police)
        player.ship.health_level -= 15
        player.credit -= 100
        player.karma -= 1
        player.transaction_history.append(Transaction("Police fee", 100, "fees", "expenses"))
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
        player.transaction_history.append(Transaction("Bandit fee", bandit["demand"], "fees", "expenses"))
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
        winnings = int(bandit["demand"] * (5 / 4))
        player.credit += winnings
        player.karma += 2
        player.transaction_history.append(Transaction("Bandit loot", winnings, "loot", "earnings"))
        return True
    else:
        # fail fight attempt
        # lose 1/3 credits and get damaged
        losings = int(player.credit / 3)
        player.credit = losings
        player.ship.health_level -= 20
        player.transaction_history.append(Transaction("Bandit fee", losings, "fees", "expenses"))
        return False


def flee_bandit(player):
    if skill_check(player.pilot):
        # successful flee atempt
        player.karma += 1
        return True
    else:
        # fail flee attempt
        # lose 1/2 credits and get damaged
        losings = int(player.credit / 2)
        player.credit = losings
        player.ship.health_level -= 20
        player.transaction_history.append(Transaction("Bandit fee", losings, "fees", "expenses"))
        return False


# create a trader dict
def gen_trader():
    return {"name": "Trader", "item": trader_item()}


# returns a random item
def trader_item():
    # reroll item until we get item whose base price >= 30
    item = random.choice(Item.__subclasses__())(random.randint(3, 6))
    while item.base_price < 30:
        item = random.choice(Item.__subclasses__())(random.randint(3, 6))
    # item = rand_element(Item.__subclasses__())(random.randint(3, 6))
    item.b_price = int(0.7 * item.base_price)
    item.s_price = int(0.6 * item.base_price)
    return item


def rob_trader(player, trader):
    if skill_check(player.fighter):
        # successful robbery
        if player.ship.cargo_space < trader["item"].size:
            return 3
        for cargo in player.ship.cargo:
            if cargo.name == trader["item"].name:
                cargo.amount += 1
                trader["item"].amount -= 1
                player.karma -= 2
                return 1
        player.ship.cargo.append(trader["item"])
        player.karma -= 2
        return 1
    else:
        # failed robbery attempt
        # player's ship loses 10 health
        player.ship.health_level -= 10
        player.karma -= 1
        return 2


def negotiate_trader(player, trader):
    if skill_check(player.merchant):
        # successful negotiation attempt
        # item's price 33% off
        trader["item"].b_price = int(trader["item"].b_price * (2 / 3))
        return True
    else:
        # failed negotation attempt
        # increase item's price by 33%
        trader["item"].b_price = int(trader["item"].b_price * (3 / 2))
        return False

    # Ignore does nothing
    # Just use previous buy method for buying items.


def skill_check(skill):
    check_int = random.randint(0, 100)
    # success chance - 15% to 60%
    threshold = math.sqrt(skill) * 15
    return check_int <= threshold

def get_skill_check(skill):
    return math.floor(math.sqrt(skill) * 15)
