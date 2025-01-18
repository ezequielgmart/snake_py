import random

class Character:
    
    def __init__(self):
        
        self.color = (000,200,000)
        
        # self.position = [random.randint(0, 790), random.randint(0, 350)]
        
        self.position_x = 300
        self.position_y = 300
        
        self.size = (20,20)
        
        self.speed = 5
        
        self.alive = True
        
        # Para almacenar la direccion del personaje
        self.current_direction = None
        
        
        # Para almacenar la direccion del personaje
        self.last_direction = None
        
        self.body_parts = [] # List to keep track of body parts
 
    def move_to_left(self):
        
        self.update_body_parts()
        self.position_x -= self.speed
        
    def move_to_right(self):
        self.update_body_parts()
        self.position_x += self.speed
        
    def move_to_up(self):
        self.update_body_parts()
        self.position_y -= self.speed
        
    def move_to_down(self):
        self.update_body_parts()
        self.position_y += self.speed
        
    def print_current_position(self):
        print(f"Snake position -> x: {self.position_x} y: {self.position_y}")    
    
    
    def border_crash(self):
        print("Llego al borde")
        self.print_current_position()
        self.alive = False
        
    def update_body_parts(self): 
        if self.body_parts: # Move each body part to the position of the previous one 
            prev_x, prev_y = self.position_x, self.position_y 
            for part in self.body_parts: 
                current_x, current_y = part.position_x, part.position_y 
                part.position_x, part.position_y = prev_x, prev_y 
                prev_x, prev_y = current_x, current_y    
        
class SnakeBodyPart:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.size = (20, 20)  # Same size as the snake
        self.color = (0, 200, 0)  # Slightly different green color
