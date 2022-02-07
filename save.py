import shelve
import parameters as p


class Save:

    def __init__(self):
        self.file = shelve.open('data')

    def save(self):
        self.file['dino_y'] = p.dino_y

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 0

    def __del__(self):
        self.file.close()
