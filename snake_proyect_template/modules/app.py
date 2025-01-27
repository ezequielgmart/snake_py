"""
Este archivo es para: ejecutar el juego

Dependencias: 

game.py
players.py

Requerido en: todos los archivos de módulos
"""

# Librerías de Python
import pygame  # Importa la biblioteca Pygame
import sys  # Importa la biblioteca sys para manejar la salida del programa

# Dependencias
from modules.game import GameModule  # Importa la clase GameModule desde el módulo game
from modules.levels import LevelModule  # Importa la clase LevelModule desde el módulo levels

class GameApp(GameModule):  # Define la clase GameApp que hereda de GameModule
    
    def __init__(self):
        
        super().__init__()  # Llama al constructor de la clase base (GameModule)
        

        self.game_config = self.config_file['game_settings']  # Carga la configuración del juego desde el archivo de configuración
        
        # Configurar la pantalla
        self.screen = pygame.display.set_mode((self.game_config['screen_width'], 
                                               self.game_config['screen_height']))  # Configura la pantalla con el ancho y alto especificados
        
        pygame.display.set_caption(self.game_config['name'])  # Establece el título de la ventana del juego

        # Colores
        self.white = (255, 255, 255)  # Define el color blanco en formato RGB

        # Carga la configuración de los niveles desde el archivo JSON
        self.levels_config = self.get_levels_config()  
        
        # Carga la configuración de los jugadores desde el archivo JSON
        self.players_config = self.get_players_config()
        
        # Obtiene el ID del nivel inicial
        self.start_level_id = self.levels_config["start_level"]  
        
        # Inicializa current_level_no con el ID del nivel inicial
        self.current_level_no = self.start_level_id  
        
        # Crea un diccionario de niveles
        self.levels = {config["room_id"]: LevelModule(config, self.players_config) for config in self.levels_config["instances"]}  
        
        # Establece el nivel actual
        self.current_level = self.levels[self.current_level_no]  
        
        # Crea un objeto Clock para controlar el tiempo del juego
        self.clock = pygame.time.Clock()  
     
    def run(self): 
        clock = pygame.time.Clock()  # Crea un objeto Clock para controlar el tiempo del juego

        while True:  # Bucle principal del juego
            for event in pygame.event.get():  # Itera sobre los eventos de Pygame
                if event.type == pygame.QUIT:  # Si se cierra la ventana del juego
                    pygame.quit()  # Cierra Pygame
                    sys.exit()  # Sale del programa
                elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                    if self.current_level_no == 0:  # Si el nivel actual es el nivel inicial
                        self.current_level_no = 1  # Cambia al siguiente nivel
                        self.current_level = self.levels[self.current_level_no]  # Establece el nuevo nivel actual
                    
            self.current_level.update()  # Actualiza el estado del nivel actual

            if self.current_level.game_over:
                self.current_level_no = 2  # Cambia al siguiente nivel
                self.current_level = self.levels[self.current_level_no]  # Establece el nuevo nivel actual
                
            self.screen.fill(self.white)  # Llena la pantalla con el color blanco
            self.current_level.draw(self.screen)  # Dibuja el nivel actual en la pantalla

            pygame.display.flip()  # Actualiza la pantalla
            clock.tick(60)  # Controla la velocidad del juego a 60 fotogramas por segundo
            
            if self.current_level_no == 0:  # Si el nivel actual es el nivel inicial
                pass  # No hace nada
