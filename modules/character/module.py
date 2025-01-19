import random

import pygame

from modules.config import settings 

class Character:
    
    def __init__(self, color = None):
        
        if color == None:
        
            self.color = settings.COLORS['GREEN']
        
        else:
            
            self.color = color    
        
        self.position_x = settings.INITIAL_POSITION["x"]
        self.position_y = settings.INITIAL_POSITION["y"]
        
        self.size = (settings.SIZE["width"],settings.SIZE["heigth"])
        
        self.speed = settings.SPEED
        
        self.body = []
        
        self.alive = True
        
        # Para almacenar la direccion del personaje
        self.current_direction = None
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
        
    def change_direction(self, direction):
        # Directions
        
        """
        
        1 -> left
        2 -> rigth
        3 -> up
        4 -> down
        
        """
        if self.current_direction == None:
            
            # Si no tiene una direccion asinada se puede cambiar a la nueva direccion que se le sta pasando
            
            self.current_direction = direction
        
        elif self.current_direction == "LEFT" and direction == "RIGHT":
            
            # Si tengo una direccion a la izquierda, y llega direccion a la derecha, no puede cambiar
            self.current_direction  = "LEFT"
        
        elif self.current_direction == "RIGHT" and direction == "LEFT":    
            
            # Si tengo una direccion a la derecha, y llega direccion a la izquierda, no puede cambiar
            self.current_direction  = "RIGHT"
        
        elif self.current_direction == "UP" and direction == "DOWN":    
            
            # Si tengo una direccion a la arriba, y llega direccion a la abajo, no puede cambiar
            self.current_direction  = "UP"
                
        elif self.current_direction == "DOWN" and direction == "UP":    
            
            # Si tengo una direccion a la abajo, y llega direccion a la arriba, no puede cambiar
            self.current_direction  = "DOWN"
        
        else:
            
            self.current_direction = direction
                
        
    def move_character_towards_direction(self):
        # Mover el personaje en la dirección actual 
        if self.current_direction == "LEFT": 
            self.move_to_left()
        elif self.current_direction == "RIGHT": 
            self.move_to_right()
        elif self.current_direction == "UP": 
            self.move_to_up()
        elif self.current_direction == "DOWN": 
            self.move_to_down()
            
    def print_current_position(self):
        print(f"Position -> x: {self.position_x} y: {self.position_y}")    
    
    def update_body_parts(self): 
        if self.body_parts: # Move each body part to the position of the previous one 
            prev_x, prev_y = self.position_x, self.position_y 
            for part in self.body_parts: 
                current_x, current_y = part.position_x, part.position_y 
                part.position_x, part.position_y = prev_x, prev_y 
                prev_x, prev_y = current_x, current_y    
    
    def eat(self, food): 
        
        trigger = self.character_collision_with_food(food)
        # Check if the character collides with the food 
        
        if trigger:
            # Remove the food and reset the flag 
            
            # # Add new body part to the snake at the current position of the last body part 
            # if self.body_parts: 
            #     last_part = self.body_parts[-1] 
            # else: 
            #     last_part = self 
            
            # # Add new body part one step behind the last part to prevent immediate self-collision 
            # if self.current_direction == "LEFT": 
            #     # moving left 
            #     new_x = last_part.position_x + 2 
            #     new_y = last_part.position_y 
            # elif self.current_direction == "RIGHT": 
            #     # moving right 
            #     new_x = last_part.position_x - 2 
            #     new_y = last_part.position_y 
            # elif self.current_direction == "UP": 
            #     # moving up 
            #     new_x = last_part.position_x 
            #     new_y = last_part.position_y + 2 
            # elif self.current_direction == "DOWN": 
            #     # moving down 
            #     new_x = last_part.position_x 
            #     new_y = last_part.position_y - 2 
            # new_body_part = SnakeBodyPart(new_x, new_y) 
            # self.body_parts.append(new_body_part)                

            return True
        
        else:  
              
            return False

    # colission with the food        
    def character_collision_with_food(self, food): 
        character_rect = pygame.Rect(self.position_x, self.position_y, *self.size) 
        food_rect = pygame.Rect(food.position_x, food.position_y, *food.size) 
        return character_rect.colliderect(food_rect)
                    
class SnakeBodyPart:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.size = (20, 20)  # Same size as the snake
        self.color = (0, 200, 0)  # Slightly different green color


class NPC(Character):
    
    def __init__(self, color = None):
        
        super().__init__(color)
        
        self.position_x = 400
        self.position_y = 400
        
    def auto_move(self, food):
        distance = self.search_food(food)
        distance_to_right_border = self.position_x - settings.DISPLAY['width']
        distance_to_bottom_border = self.position_y - settings.DISPLAY['heigth']

        if distance_to_right_border <= -10:
            self.stop_npc()
            self.handle_border_collision(distance_to_right_border, distance_to_bottom_border, distance)
        else:
            self.move_towards_food(distance)

    def handle_border_collision(self, distance_x, distance_y, food_distance):
        if food_distance['x'] < 0 and food_distance['y'] < 0:
            self.change_direction_and_move("RIGHT" if food_distance['x'] < 0 else "LEFT", "Second if")
        elif food_distance['x'] > 1:
            self.change_direction_and_move("LEFT", "Third if")
        elif food_distance['x'] < 0 and food_distance['x'] < -890:
            self.change_direction_and_move("RIGHT", "Fourth if")
        else:
            self.change_direction_and_move("RIGHT", "Fourth if")

        if food_distance["y"] > 19:
            self.change_direction_and_move("UP", "Fifth if")
        elif food_distance["y"] < -19:
            self.change_direction_and_move("DOWN", "Sixth if")
        else:
            self.stop_npc()

    def move_towards_food(self, distance):
        if distance["x"] > 0:
            self.change_direction_and_move("RIGHT", "Move towards food X")
        elif distance["x"] < 0:
            self.change_direction_and_move("LEFT", "Move towards food X")
        elif distance["y"] > 0:
            self.change_direction_and_move("DOWN", "Move towards food Y")
        elif distance["y"] < 0:
            self.change_direction_and_move("UP", "Move towards food Y")

    def change_direction_and_move(self, direction, scenario):
        self.stop_npc()
        npc_status = {
            "direction": direction,
            "scenario": scenario
        }
        print(npc_status)
        self.change_direction(direction)
        self.move_character_towards_direction()

        
    # Algoritmo que medira la distancia a la comida para ir a buscarla   
    def search_food(self, food):    
        
        distance = {
            "x":self.position_x - food.position_x,
            "y":self.position_y - food.position_y
        }
        
        return  distance
    
    def stop_npc(self):
        self.change_direction(None)
        