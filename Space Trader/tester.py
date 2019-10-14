from game import Game

skill_points = [4, 4, 4, 4]
game = Game("Hard")
game.start_game("Raymond", skill_points, 200)
for reg in game.universe.region_list:
    print(reg.name)
    print(reg.coordinates.x_position)
    print(reg.coordinates.y_position)
    print(reg.tech_level)

print()
print()
game2 = Game("Easy")
game2.start_game("Ricardo", skill_points, 100)
for reg in game2.universe.region_list:
    print(reg.name)
    print(reg.coordinates.x_position)
    print(reg.coordinates.y_position)
    print(reg.tech_level)
print()
print()
for reg in game.universe.region_list:
    print(reg.name)
    print(reg.coordinates.x_position)
    print(reg.coordinates.y_position)
    print(reg.tech_level)


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
