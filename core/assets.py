import ctypes

from sdl2 import *
from sdl2 import sdlimage


class AssetsManager:
    def __init__(self, get_data=False, images=None, renderer=None):
        self._images = images if images else {}
        if get_data:
            self.load_images(self._images, renderer=renderer)

    def load_image(self, name, src, renderer):
        surf = sdlimage.IMG_Load(str.encode(src))
        # SDL_SetColorKey(surf, SDL_TRUE, SDL_MapRGB(surf.contents.format, 128, 128, 255))
        # SDL_SetColorKey(surf, SDL_TRUE, SDL_MapRGB(surf.contents.format, 255, 255, 255))
        SDL_SetColorKey(surf, SDL_TRUE, SDL_MapRGB(surf.contents.format, 170, 170, 170))
        texture = SDL_CreateTextureFromSurface(renderer, surf)
        self._images[name] = texture

    def load_images(self, images, renderer=None):
        for name, src in images.items():
            self.load_image(name, src, renderer)

    def get_image(self, name):
        return self._images[name]

    def get_image_size(self, name):
        width = ctypes.c_int()
        height = ctypes.c_int()
        SDL_QueryTexture(self._images[name], None, None, width, height)
        return min(16, width.value), min(16, height.value)

    def destroy(self):
        for image in self._images.values():
            SDL_DestroyTexture(image)
