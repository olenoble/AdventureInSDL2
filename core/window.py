# TODO:  have the renderer parameters passed with the config
from sdl2 import *


class Window:
    def __init__(self, title, width, height, scale):
        SDL_Init(SDL_INIT_VIDEO)

        self.window = SDL_CreateWindow(str.encode(title),
                                       SDL_WINDOWPOS_UNDEFINED,
                                       SDL_WINDOWPOS_UNDEFINED,
                                       width * scale,
                                       height * scale,
                                       0)

        self.renderer = SDL_CreateRenderer(self.window, -1, SDL_RENDERER_ACCELERATED)
        SDL_RenderSetScale(self.renderer, scale, scale)

    # def draw(self, image, x, y):
    #     SDL_RenderCopy(self.renderer, image, None, SDL_Rect(int(x), int(y), 16, 16))

    def destroy(self):
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)
