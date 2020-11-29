# TODO: 2. More abstraction
#           a. drawing logic should not be in game / player
#           b. physics logic must be out of player
#           c. player object is unrelated to collider

from core.game import Game

if __name__ == '__main__':
    game = Game('Game', 320, 240, 3)
    t, i = game.run()

    print('Average FPS = %.3f' % (i / t))

    print('Done')
