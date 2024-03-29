from sdl2 import *


class Display:
    def __init__(self, title, width, height, scale, asset_manager=None):
        self.window = SDL_CreateWindow(str.encode(title),
                                       SDL_WINDOWPOS_UNDEFINED,
                                       SDL_WINDOWPOS_UNDEFINED,
                                       width * scale,
                                       height * scale,
                                       0)
        self.renderer = SDL_CreateRenderer(self.window, -1, SDL_RENDERER_ACCELERATED)
        self.asset_manager = asset_manager
        SDL_RenderSetScale(self.renderer, scale, scale)

    def draw(self, image, x, y):
        SDL_RenderCopy(self.renderer, self.asset_manager.get_image(image), None, SDL_Rect(int(x), int(y), 16, 16))

    # def draw_sprite(self, image, x, y):
    #     SDL_RenderCopy(self.renderer, self.asset_manager.get_image(image),
    #                    SDL_Rect(0, 0, 34, 95), SDL_Rect(int(x), int(y), 16, 16))

    def draw_sprite(self, image, x, y, pos, flip):
        # SDL_RenderCopy(self.renderer, self.asset_manager.get_image(image),
        #                SDL_Rect(int(pos * 32), 0, 32, 32), SDL_Rect(int(x), int(y), 16, 16))
        # SDL_RenderCopyEx(self.renderer, self.asset_manager.get_image(image), 
        #                  SDL_Rect(int(pos * 32), 0, 32, 32), SDL_Rect(int(x), int(y), 16, 16), 0, None, flip)
        SDL_RenderCopyEx(self.renderer, self.asset_manager.get_image(image), 
                         SDL_Rect(int(pos * 64), 0, 64, 64), SDL_Rect(int(x), int(y), 32, 32), 0, None, flip)


    def destroy(self):
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)
