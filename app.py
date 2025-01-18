import pygame
import sys

from modules.character.module import Character,SnakeBodyPart
from modules.objects.module import GameObject, Food

class Game:
    def __init__(self):
        super().__init__()
        # Inicializar pygame
        pygame.init()

        self.display_width = 900
        self.display_height = 600

        # Configurar la pantalla
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Mi Primer Juego')

        # Inicializar el reloj para controlar la velocidad de fotogramas 
        self.clock = pygame.time.Clock()

        # Lista de personajes
        self.list_of_characters = []

        self.snake = Character()
        self.list_of_characters.append(self.snake)
        
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
                        # left
                        self.snake.current_direction = 1
                    elif event.key == pygame.K_RIGHT: 
                        # Rigth
                        self.snake.current_direction = 2
                    elif event.key == pygame.K_UP: 
                        # Up
                        self.snake.current_direction = 3
                    elif event.key == pygame.K_DOWN: 
                        # Down
                        self.snake.current_direction = 4
                    elif event.type == pygame.KEYUP: 
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN): 
                            self.snake.current_direction = None
           
                    elif event.key == pygame.K_SPACE:
                        self.snake.alive = False
                        print("Exit pressed")
                
            # Mover el personaje en la dirección actual 
            if self.snake.current_direction == 1: 
                self.snake.move_to_left()
            elif self.snake.current_direction == 2: 
                self.snake.move_to_right()
            elif self.snake.current_direction == 3: 
                self.snake.move_to_up()
            elif self.snake.current_direction == 4: 
                self.snake.move_to_down()
            
            self.display_border_coalition()
            
            # Check for collision with itself 
            if self.detect_self_collision(): 
                print("Self-collision detected!") 
                self.snake.alive = False
            
            # Spawn food if there is none
            if not self.there_is_food:        
                food = self.spawn_food()
                self.there_is_food = True
                self.list_of_objects.append(food)
   
            # Check if the character eats the food
            self.eat(food)
            
            # Actualizar pantalla
            self.update_display(self.list_of_characters,self.list_of_objects)

            # Controlar la velocidad de fotogramas
            self.clock.tick(60)


    def draw_character(self, character):
        # Draw the main character
        self.display.fill(character.color, (character.position_x, character.position_y, *character.size))
        
        # Draw the body parts
        for part in character.body_parts:
            self.display.fill(part.color, (part.position_x, part.position_y, *part.size))


    def draw_object(self, object):
        self.display.fill(object.color, (object.position_x, object.position_y, *object.size))
        
    def spawn_food(self):
        food = Food(self.display_width,self.display_height)
        return food

    def update_display(self, list_of_characters, list_of_objects):
        # Rellenar la pantalla con un color
        self.display.fill((0, 0, 0))

        for character in list_of_characters:
            self.draw_character(character)
        
        for object in list_of_objects:
            self.draw_object(object)    
        
        # Actualizar la pantalla
        pygame.display.flip()

    def display_border_coalition(self):    
        
        if self.snake.position_y >= self.display_height or self.snake.position_y < 0:
            self.snake.border_crash()
            
        if self.snake.position_x >= self.display_width or self.snake.position_x < 0:    
            self.snake.border_crash()

    def eat(self, food): 
        # Check if the character collides with the food 
        character_has_eat = self.character_collision_with_food(food) 
        
        if character_has_eat: 
            # Remove the food and reset the flag 
            self.list_of_objects.remove(food) 
            self.there_is_food = False 
            
            # Add new body part to the snake at the current position of the last body part 
            if self.snake.body_parts: 
                last_part = self.snake.body_parts[-1] 
            else: last_part = self.snake 
            # Add new body part one step behind the last part to prevent immediate self-collision 
            if self.snake.current_direction == 1: 
                # moving left 
                new_x = last_part.position_x + 20 
                new_y = last_part.position_y 
            elif self.snake.current_direction == 2: 
                # moving right 
                new_x = last_part.position_x - 20 
                new_y = last_part.position_y 
                
            elif self.snake.current_direction == 3: 
                # moving up 
                new_x = last_part.position_x 
                new_y = last_part.position_y + 20 
            elif self.snake.current_direction == 4: 
                # moving down 
                new_x = last_part.position_x 
                new_y = last_part.position_y - 20 
                new_body_part = SnakeBodyPart(new_x, new_y) 
                self.snake.body_parts.append(new_body_part)                
            
    def character_collision_with_food(self, food): 
        character_rect = pygame.Rect(self.snake.position_x, self.snake.position_y, *self.snake.size) 
        food_rect = pygame.Rect(food.position_x, food.position_y, *food.size) 
        return character_rect.colliderect(food_rect)
    
    def detect_self_collision(self): 
        # Check for collision between the head and the body parts 
        head_rect = pygame.Rect(self.snake.position_x, self.snake.position_y, *self.snake.size) 
        
        for part in self.snake.body_parts: 
            part_rect = pygame.Rect(part.position_x, part.position_y, *part.size) 
            
            if head_rect.colliderect(part_rect): 
                return True 
            
        return False 