import pygame
import sys
import os 

from modules.character.module import Character,SnakeBodyPart, NPC
from modules.objects.module import Food
from modules.config import settings

class Game():
    
    def __init__(self):
        
        super().__init__()
        
        # Inicializar pygame
        pygame.init()
            
        # configuraciones de pygame     
        self.display_width = settings.DISPLAY['width']
        self.display_height = settings.DISPLAY['heigth']
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        # entorno del videojuego
        self.list_of_characters = []
        
        self.snake = Character()
        
        self.npc = NPC(settings.COLORS['RED'])
        
        self.list_of_characters.append(self.snake)
        self.list_of_characters.append(self.npc)
        
        self.list_of_objects = []
        self.there_is_food = False
        self.counter = 0
        

    def run(self):
        
        while self.snake.alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_LEFT: 
                        direction = "LEFT"
                        self.snake.change_direction(direction)
                            
                    elif event.key == pygame.K_RIGHT: 
                        direction = "RIGHT"
                        self.snake.change_direction(direction)
                        
                    elif event.key == pygame.K_UP: 
                        direction = "UP"
                        self.snake.change_direction(direction)
                        
                    elif event.key == pygame.K_DOWN: 
                        direction = "DOWN"
                        self.snake.change_direction(direction)
                            
                    elif event.type == pygame.KEYUP: 
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN): 
                            
                            self.snake.change_direction(None)
           
                    elif event.key == pygame.K_SPACE:
                        self.snake.alive = False
                        print("Exit pressed")
                
            # Mover el personaje en la dirección actual 
            self.snake.move_character_towards_direction()
            

            
            # observar que ambos no choquen los border
            for character in self.list_of_characters:
                if self.display_border_coalition(character):
                    character.alive = False
                    print("Choco con border! ")
                    exit()
                

            
            # Spawn food if there is none
            if not self.there_is_food:   
                 
                food = self.spawn_food()
                self.there_is_food = True
                self.list_of_objects.append(food)
                
   
            # Check if the character eats the food
            for character in self.list_of_characters:
                
                if character.eat(food):
                    
                    self.list_of_objects.remove(food)
                    
                    food = self.spawn_food()
                    self.there_is_food = True
                    self.list_of_objects.append(food)
            
            self.npc.auto_move(food)
            
            # self.greedy_move(food, self.snake)
            
            # # Check for collision with itself 
            # if self.detect_self_collision(): 
            #     print("Self-collision detected!") 
            #     self.snake.alive = False
                
            # Actualizar pantalla
            self.update_display(self.list_of_characters,self.list_of_objects)

            # Controlar la velocidad de fotogramas
            self.clock.tick(settings.FRAMERATE)

            
    def draw_character(self, character):
        # Draw the main character
        self.display.fill(character.color, (character.position_x, character.position_y, *character.size))
        
        # Draw the body parts
        for part in character.body_parts:
            self.display.fill(part.color, (part.position_x, part.position_y, *part.size))


    def draw_object(self, object):
        self.display.fill(object.color, (object.position_x, object.position_y, *object.size))
        
        
    def spawn_food(self):
        secure_area = [self.display_width,self.display_height]
        print(secure_area)
        food = Food(secure_area[0],secure_area[1])
        return food

    def update_display(self, list_of_characters, list_of_objects):
        # Rellenar la pantalla con un color
        self.display.fill(settings.COLORS['BLACK'])

        for character in list_of_characters:
            self.draw_character(character)
        
        for object in list_of_objects:
            self.draw_object(object)    
        
        # Actualizar la pantalla
        pygame.display.flip()


    # detects collision with the borders of the display
    def display_border_coalition(self, character):    
        
        if character.position_y >= self.display_height or character.position_y < 0:
            return True
        elif character.position_x >= self.display_width or character.position_x < 0:    
            return True
        else:
            return False

    def detect_self_collision(self): 
        # Check for collision between the head and the body parts 
        head_rect = pygame.Rect(self.snake.position_x, self.snake.position_y, *self.snake.size) 
        
        for part in self.snake.body_parts: 
            part_rect = pygame.Rect(part.position_x, part.position_y, *part.size) 
            
            if head_rect.colliderect(part_rect): 
                return True 
            
        return False 