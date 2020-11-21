# TODO: 2. More abstraction
#           a. drawing logic should not be in game / player
#           b. physics logic must be out of player
#           c. player object is unrelated to collider
#       3. add target to pick up

from core.game import Game

if __name__ == '__main__':
    game = Game('Game', 320, 240, 2)
    game.run()
