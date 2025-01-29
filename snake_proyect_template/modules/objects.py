import pygame

class ObjectsGame(pygame.sprite.Sprite):
    
    # Método constructor que recibe un diccionario de configuración
    def __init__(self, config):
        super().__init__()
        self.image = pygame.image.load(config['sprites'])
        self.rect = self.image.get_rect()
        
        # Establece la posición inicial del sprite usando la configuración
        self.rect.topleft = (config["position"]["x"], config["position"]["y"])
    
    # Método para actualizar la posición del sprite
    def update(self):  
        
        pass
        
