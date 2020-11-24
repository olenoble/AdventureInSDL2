# TODO: 2. More abstraction
#           a. drawing logic should not be in game / player
#           b. physics logic must be out of player
#           c. player object is unrelated to collider

from core.loop import GameLoop

# Place this in a external json file of sorts
game_config = {'title': 'Scandyum',

               # Wrap this up in a dict with Window key
               'width': 320,
               'height': 240,
               'scale': 3,

               # Now assets
               'Assets': {'Image': {'bg': './assets/background.png',
                                    'player': {'src': './assets/vegeta_new.png', 'background': (170, 170, 170)},
                                    'wall': './assets/wall.png'
                                    }
                          },

               # get player + level+ bckgrd into Universe
               # Player
               'Player': {'class': None,
                          },

               # Level
               'Level': {'class': 'TileSet',
                         },

               # Background
               'Background': {'class': None,
                              },

               }

if __name__ == '__main__':
    game = GameLoop(game_config)
    game.run()
