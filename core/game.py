# A few things I don't like
# TODO: 1. player and other object should not have a renderer or collision object attached to them
#       2. collision detection is performed independently

import time
from sdl2 import *
# import ctypes
from .assets import AssetsManager
from .display import Display
from .keyboard import Keyboard

from core.level import Level
from core.player import Player
from core.background import BackGround


class Game:
    GRID_SIZE = 16
    ASSETS = {'bg': './assets/background.png',
              # 'player': './assets/player.png',
              'player': './assets/vegeta2.png',
              'wall': './assets/wall.png'
              }

    display_refs = ['background', 'level', 'player']

    def __init__(self, title, width, height, scale):
        SDL_Init(SDL_INIT_VIDEO)

        self.width = width
        self.height = height

        self.assets_manager = AssetsManager()
        self.display = Display(title, width, height, scale, asset_manager=self.assets_manager)
        self.keyboard = Keyboard()

        self.get_assets()

        self.level = Level('wall', self.GRID_SIZE)
        self.player = Player(self, 'player', 140, 65)
        self.background = BackGround('bg', self.GRID_SIZE, self.height, self.width)

        self.current_time = 0

    def get_assets(self):
        self.assets_manager.load_images(self.ASSETS, renderer=self.display.renderer)

    @staticmethod
    def init_time():
        """ the reason I put this (and the next) into a method is that I can use something else than actual time """
        return time.time()

    def timing(self):
        time_now = time.time()
        delta_time = time_now - self.current_time
        self.current_time = time_now
        return delta_time

    def update(self, delta_time):
        self.player.update(delta_time)
        self.draw()

    def run(self):
        # x = SDL_AddEventWatch
        # y = SDL_SetEventFilter
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

            self.update(delta_time)
            SDL_RenderPresent(self.display.renderer)

        self.destroy()

    def draw(self):
        for obj in self.display_refs:
            self.draw_asset(getattr(self, obj))

    def draw_asset(self, drawable):
        drawable.draw(self.display)

    def destroy(self):
        self.assets_manager.destroy()
        self.display.destroy()
        SDL_Quit()
