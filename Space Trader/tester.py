from game import Game

skill_points = [4, 4, 4, 4]
game = Game("hard")
print(game.diff)
print(game.fuel_cost_constant)
print()
print()
game.start_game("Raymond", skill_points, 200)
for reg in game.universe.region_list:
    print(reg.name)
    print(reg.coordinates.x_position)
    print(reg.coordinates.y_position)
    print(reg.tech_level.name)
    print(reg.tech_level.value)
    print()

    for stuff in reg.market:
        print(stuff.name)
        print(stuff.amount)
    print()
    print()
print()
print()

game.player.ship.fuel_level = 0
print(game.player.purchase_fuel(20))
print(game.player.ship.fuel_level)


# game = universe_create()
# travel_test(game)

# items = []
# for cls in Item.__subclasses__():
#     print("[" + str(cls.debut_cap[0]) + ", " + str(cls.debut_cap[1]) + "]")
#     print()
#     klass = cls(10)
#     items.append([klass, random.randint(10, 20)])
# print(items[0])
# print(items[1])
# print()
# print(items[0][0].amount)


# print()
# print()
# game2 = Game("Easy")
# game2.start_game("Ricardo", skill_points, 100)
# for reg in game2.universe.region_list:
#    print(reg.name)
#    print(reg.coordinates.x_position)
#    print(reg.coordinates.y_position)
#    print(reg.tech_level)
# print()
# print()
# for reg in game.universe.region_list:
#    print(reg.name)
#    print(reg.coordinates.x_position)
#    print(reg.coordinates.y_position)
#    print(reg.tech_level)

# print(game.player.name)
# print(game.player.pilot)
# print(game.player.fighter)
# print(game.player.merchant)
# print(game.player.engineer)
# print(game.player.credit)
# print(game.player.curr_region.name)
# print(game.player.curr_region.coordinates.x_position)
# print(game.player.curr_region.coordinates.y_position)
# print(game.player.curr_region.tech_level)
