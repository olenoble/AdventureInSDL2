# A few things I don't like
# TODO: 1. player and other object should not have a renderer or collision object attached to them
#       2. collision detection is performed independently

from sdl2 import *
from .universe import Universe
from .store import Store
from .window import Window
from .keyboard import Keyboard


import time
from core.level import Level
from core.player import Player
from core.background import BackGround


class GameLoop:
    GRID_SIZE = 16
    display_refs = ['background', 'level', 'player']

    def __init__(self, config):
        self.config = config

        # Initialize video
        self.width = config.get('width', 320)       # only used in player...
        self.height = config.get('height', 200)
        self.window = Window(config.get('title', '320'), self.width, self.height, config.get('scale', 1))

        # create keyboard interface
        self.keyboard = Keyboard()

        # create store (will load assets later)
        self.store = Store()
        self.store.loadAll(self.config.get('Assets'), {'Image': {'renderer': self.window.renderer}})

        # # create renderer
        # self.level = Level('wall', self.GRID_SIZE)
        # self.player = Player(self, 'player', 160, 120)
        # self.background = BackGround('bg', self.GRID_SIZE, self.height, self.width)

        self.current_time = 0

    @staticmethod
    def init_time():
        """ the reason I put this (and the next) into a method is that I can use something else than actual time """
        return time.time()

    def timing(self):
        time_now = time.time()
        delta_time = time_now - self.current_time
        self.current_time = time_now
        return delta_time

    # def update(self, delta_time):
    #     self.player.update(delta_time)
    #     self.draw()

    def run(self):
        event = SDL_Event()
        self.current_time = self.init_time()
        running = True

        while running:
            delta_time = self.timing()

            SDL_PollEvent(event)
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                self.keyboard.set_key_down(event.key.keysym.sym, True)
            elif event.type == SDL_KEYUP:
                self.keyboard.set_key_down(event.key.keysym.sym, False)

            # self.update(delta_time)
            SDL_RenderPresent(self.window.renderer)

        self.destroy()

    # def draw(self):
    #     for obj in self.display_refs:
    #         self.draw_asset(getattr(self, obj))
    #
    # def draw_asset(self, drawable):
    #     drawable.draw(self.display)

    def destroy(self):
        # self.assets_manager.destroy()
        self.window.destroy()
        SDL_Quit()
