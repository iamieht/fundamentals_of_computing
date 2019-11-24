class Tile(object):
    def __init__(self, num):
        self.number = num

    def get_number(self):
        return self.number


my_tile = Tile(3)
your_tile = Tile(4)