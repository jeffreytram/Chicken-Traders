"""Module with utility functions for the game"""


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

def damage(player, npc):
    damage = npc.fighterLevel * 100
    if (player.ship.health_level >= damage):
        player.ship.health_level = player.ship.health_level - damage
    else:
        player.ship.health_level = 0
