from modules.objects import ObjectsGame

class GameObjectsCustomized(ObjectsGame):
    
    # Método constructor que recibe un diccionario de configuración
    def __init__(self, config):  
        
        # Llama al constructor de la clase base (pygame.sprite.Sprite)
        super().__init__(config)  