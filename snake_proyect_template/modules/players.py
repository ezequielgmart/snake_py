# Clase Jugador

import pygame  # Importa la biblioteca Pygame


# Define la clase PlayerModule que hereda de pygame.sprite.Sprite
class PlayerModule(pygame.sprite.Sprite):  
    
    # Método constructor que recibe un diccionario de configuración
    def __init__(self, config):  
        
        # Llama al constructor de la clase base (pygame.sprite.Sprite)
        super().__init__()  
        
        # Crea una superficie del sprite
        self.image = pygame.image.load(config['sprites'])
        
        # Obtiene el rectángulo que delimita la superficie del sprite
        self.rect = self.image.get_rect()  
        
        # Establece la posición inicial del sprite usando la configuración
        self.rect.topleft = (config["position"]["x"], config["position"]["y"])  
        
        # Establece la velocidad del sprite, con un valor predeterminado de 5 si no se especifica en la configuración
        self.speed = config.get("speed", 5)  
        
        self.direction = config["direction"]
        
        self.live = config["live"]

    # Método para actualizar la posición del sprite
    def update(self):  
        
        keys = pygame.key.get_pressed()  # Obtiene el estado de todas las teclas del teclado
        
        if keys[pygame.K_LEFT]:  # Si la tecla izquierda está presionada
            self.move_left()
        if keys[pygame.K_RIGHT]:  # Si la tecla derecha está presionada
            self.move_right()
            
        if keys[pygame.K_UP]:  # Si la tecla arriba está presionada
            self.move_up()
            
        if keys[pygame.K_DOWN]:  # Si la tecla abajo está presionada
            
            self.move_down()
        
        # Condicion de victoria
        if self.live <= 0:
            return False
        
        return True
    
    def move_left(self):
        self.rect.x -= self.speed  # Mueve el sprite a la izquierda
    
    
    def move_right(self):
        self.rect.x += self.speed  # Mueve el sprite a la derecha
    
    
    def move_up(self):
        self.rect.y -= self.speed  # Mueve el sprite hacia arriba
    
    
    def move_down(self):
        self.rect.y += self.speed  # Mueve el sprite hacia abajo