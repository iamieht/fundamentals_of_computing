class Tile(object):
    def __init__(self, num, exposed):
        self.number = num
        self.exposed = exposed

    def get_number(self):
        return self.number
    
    def is_exposed(self):
        return self.exposed
    
    def expose_tile(self):
        self.exposed = True
    
    def hide_tile(self):
        self.exposed = False

    def __str__(self):
        return "Number is " + str(self.number) + ", " + "exposed is " + str(self.exposed) 

    


my_tile = Tile(3, True)
your_tile = Tile(4, False)