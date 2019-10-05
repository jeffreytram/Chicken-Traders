from Game import Game

skillPoints = [4, 4, 4, 4]
game = Game("Hard")
game.startGame("Ricardo", skillPoints, 100)
for reg in game.universe.regionList:
    print(reg.name)
    print(reg.coordinates.x_position)
    print(reg.coordinates.y_position)
    print(reg.tech_level)

print(game.player.name)
print(game.player.pilot)
print(game.player.fighter)
print(game.player.merchant)
print(game.player.engineer)
print(game.player.credit)
print(game.player.currRegion.name)
print(game.player.currRegion.coordinates.x_position)
print(game.player.currRegion.coordinates.y_position)
print(game.player.currRegion.tech_level)
