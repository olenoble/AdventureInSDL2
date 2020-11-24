from .banks.image import ImageBank
from .banks.audio import AudioBank


class Store:
    def __init__(self):
        self._bank = {'Image': ImageBank(),
                      'Audio': AudioBank(),
                      }

    def loadAll(self, assets, params):
        self._bank['Image'].loadAll(assets.get('Image'), params.get('Image'))
        self._bank['Audio'].loadAll(assets.get('Audio'), params.get('Audio'))

    def get_image(self, name):
        self._bank['Image'].get(name)

    def get_audio(self, name):
        self._bank['Audio'].get(name)

