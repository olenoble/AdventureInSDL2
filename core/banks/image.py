from sdl2 import *
from sdl2 import sdlimage


class ImageBank:

    def __init__(self):
        self._imgbank = {}

    def get(self, name):
        return self._imgbank[name]

    def loadAll(self, imglist, params=None):
        for key, img in imglist.items():
            imgdict = img if isinstance(img, dict) else {'src': img, 'params': {}}
            self.load(key, imgdict, renderer=params.get('renderer', None))

    def load(self, key, img, renderer=None):
        # Load surface
        surf = sdlimage.IMG_Load(str.encode(img['src']))

        # is there a background color ?
        if img.get('background'):
            SDL_SetColorKey(surf, SDL_TRUE, SDL_MapRGB(surf.contents.format, *img.get('background')))
        texture = SDL_CreateTextureFromSurface(renderer, surf)
        self._imgbank[key] = texture
