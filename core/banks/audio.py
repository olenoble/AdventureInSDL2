


class AudioBank:

    def __init__(self):
        self._soundbank = {}

    def get(self, name):
        return self._soundbank[name]

    def loadAll(self, namelist, params):
        return None

    def load(self, name, params):
        return None