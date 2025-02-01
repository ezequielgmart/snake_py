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
from modules.game_config import GameModule
from modules.levels import LevelModule  # Importa la clase LevelModule desde el módulo levels


class GameApp(GameModule):  # Define la clase GameApp que hereda de config
    
    def __init__(self):
        
            super().__init__()  # Llama al constructor de la clase base (config)
            
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
            
            
            # Carga la configuración de los objectos desde el archivo JSON
            self.objects_config = self.get_objects_config()
            
            # Obtiene el ID del nivel inicial
            self.start_level_id = 0
            
            # Inicializa current_level_no con el ID del nivel inicial
            self.current_level_no = self.start_level_id  
            
            # Crea un diccionario de niveles
            """
            Para cada configuración `config` en `self.levels_config["instances"]`:
                - Usar `config["room_id"]` como clave del diccionario.
                - Crear una instancia de `LevelModule` usando `config`, `self.players_config`, y `self.objects_config` como el valor correspondiente a esa clave.
            Asignar el diccionario resultante a `self.levels`.

            """
            self.levels = {config["level_id"]: LevelModule(config) for config in self.levels_config["instances"]}  
            
            # Establece el nivel actual
            self.current_level = self.levels[self.current_level_no]  
            

            # Crea un objeto Clock para controlar el tiempo del juego
            self.clock = pygame.time.Clock()  
    
    
    # def update_current_level(self):
    #     self.levels[self.current_level_no].load_level(self.current_level_no,self.players_config,self.objects_config)
        
     
    def run(self): 

        # self.levels[self.current_level_no].load_level(self.current_level_no,self.players_config,self.objects_config)
        
        running = True
            
        while running:  # Bucle principal del juego
            for event in pygame.event.get():  # Itera sobre los eventos de Pygame
                if event.type == pygame.QUIT:  # Si se cierra la ventana del juego
                    pygame.quit()  # Cierra Pygame
                    sys.exit()  # Sale del programa
                elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                    if self.current_level_no == 0:  # Si el nivel actual es el nivel inicial
                        self.current_level_no = 1  # Cambia al siguiente nivel
                        self.current_level = self.levels[self.current_level_no]  # Establece el nuevo nivel actual
               
            self.current_level.update(self.players_config,self.objects_config)  # Actualiza el estado del nivel actual

            # Si la condicion de perdida es True en este nivel, entonces:     
            if self.current_level.game_over:
                self.current_level_no = 2  # Cambia al siguiente nivel
                self.current_level = self.levels[self.current_level_no]  # Establece el nuevo nivel actual
                
            self.screen.fill(self.white)  # Llena la pantalla con el color blanco
            self.current_level.draw(self.screen)  # Dibuja el nivel actual en la pantalla

            pygame.display.flip()  # Actualiza la pantalla
            self.clock.tick(60)  # Controla la velocidad del juego a 60 fotogramas por segundo
            
            if self.current_level_no == 0:  # Si el nivel actual es el nivel inicial
                pass  # No hace nada
