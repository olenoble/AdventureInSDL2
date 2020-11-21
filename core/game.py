import time

from sdl2 import *

from .assets import AssetsManager
from .display import Display
from .keyboard import Keyboard

from core.level import Level
from core.player import Player


class Game:
    GRID_SIZE = 16
    ASSETS = {'bg': './assets/background.png',
              'player': './assets/player.png',
              'wall': './assets/wall.png'
              }

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

    def get_assets(self):
        self.assets_manager.load_images(self.ASSETS, renderer=self.display.renderer)

    def update(self, delta_time):
        self.player.update(delta_time)
        self.draw()

    def draw(self):
        for bg_x in range(int(self.width / self.GRID_SIZE)):
            for bg_y in range(int(self.height / self.GRID_SIZE)):
                self.display.draw('bg', bg_x * self.GRID_SIZE, bg_y * self.GRID_SIZE)
        self.draw_asset(self.level)
        self.draw_asset(self.player)

    def run(self):
        event = SDL_Event()
        last_time = time.time()
        running = True

        while running:
            time_now = time.time()
            delta_time = time_now - last_time
            last_time = time_now

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

    def draw_asset(self, drawable):
        drawable.draw(self.display)

    def destroy(self):
        self.assets_manager.destroy()
        self.display.destroy()
        SDL_Quit()
