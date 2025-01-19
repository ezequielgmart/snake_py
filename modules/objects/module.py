import random

from modules.config import settings 

class GameObject:
    
    def __init__(self, display_max_width, display_max_height):
        
        self.color = settings.COLORS['BLUE']
        
        self.position_x = random.randint(0, display_max_width) 
        
        self.position_y = random.randint(0, display_max_height)
        
        self.size = (20,20)
        
        self.speed = [random.choice([-1, 1]), random.choice([-1, 1])]
        
        self.alive = True

    
    def print_current_position(self):
        print(f"Object position -> x: {self.position_x} y: {self.position_y}")    
        
        
    
class Food(GameObject):   
     
    def __init__(self,display_max_width, display_max_height):
        super().__init__(display_max_width, display_max_height)