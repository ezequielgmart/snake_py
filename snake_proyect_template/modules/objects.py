from modules.game import GameModule

class ObjectsModule(GameModule):
    
    def __init__(self, id, name, width,height, sprites, x, y):
        
        super().__init__()
        
        self.id = id
        self.name = name
        self.width = width
        self.height = height
        self.sprites = sprites
        self.x = x
        self.y = y
        