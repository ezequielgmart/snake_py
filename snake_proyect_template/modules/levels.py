# Importa la biblioteca Pygame
import pygame  
import sys

# from modules.players import PlayerModule  # Importa la clase PlayerModule desde el módulo players
from customs_libs.players import PlayerCustomized
from customs_libs.custom_objs import ObjectsGameCustomized
 
 
# Clase Nivel
class LevelModule:
    def __init__(self, config):  
        # Método constructor que recibe la configuración del nivel y la configuración de los jugadores
        
        self.config = config  # Guarda la configuración del nivel
        self.background = pygame.image.load(config["background"])  # Carga la imagen de fondo del nivel
        self.players = pygame.sprite.Group()  # Crea un grupo de sprites para los jugadores
        self.objects = pygame.sprite.Group()  # Crea un grupo de sprites para los objetos
        
        # Añade un atributo booleano para rastrear si los jugadores y objetos han sido creados
        self.players_loaded = False
        self.objects_loaded = False
        
        self.game_over = False 


    # este metodo recibira las instacias de objetos y jugadores para crear el nivel de acorde a la configuracion de nivel del levels.json 
    def load_level(self, players_config, objects_config): 
        """
            OJO AL DATO MINITRO
            
            Que ta haciendo esto? 
            
            es una condicional negativa, si cuando cargue los jugadores hay un error, quiero que me rompa la ejecucion y tire un error
            
            igual para los objetos del juego
        """
        if not self.load_players_in_level(players_config):
            sys.exit()
            raise "An error has occurred loading players"
        elif not self.load_objects_in_level(objects_config):
            sys.exit()
            raise "An error has occurred loading objets"
        else:    
            print("running")
        
        
    def load_players_in_level(self, players_config):
        if not self.players_loaded and len(self.config['players']) > 0:  # Verifica si hay jugadores en la configuración del nivel
        
            for player_data in self.config['players']:  # Itera sobre cada jugador en la configuración del nivel
                player_id = player_data["player_id"]
                """
                    # Busca en la lista `players_config` un diccionario que contenga un jugador con el `player_id` igual a `player_id`.
                    # Utiliza una expresión generadora para iterar a través de la lista `players_config` y encuentra el primer jugador que coincida.
                    # Si se encuentra un jugador con el `player_id` correspondiente, se devuelve ese diccionario de configuración del jugador.
                    # Si no se encuentra ningún jugador con ese `player_id`, devuelve `None`.
                """
                player_config = next((player for player in players_config if player["player_id"] == player_id), None)
                
                if player_config:
                    # Crea una instancia de PlayerCustomized con la configuración del jugador
                    objPlayer = PlayerCustomized(player_config)  
                    
                    # Añade el jugador al grupo de sprites de jugadores 
                    self.players.add(objPlayer)
                    
            # Marca que los jugadores ya han sido cargados
            self.players_loaded = True         
            
        return True    
    
    
        
    def load_objects_in_level(self, objects_config):
        if not self.objects_loaded and len(self.config['objects']) > 0:  # Verifica si hay jugadores en la configuración del nivel
        
            for object_data in self.config['objects']:  # Itera sobre cada jugador en la configuración del nivel
                game_object_id = object_data["object_id"]
                """
                    # Busca en la lista `object_config` un diccionario que contenga un jugador con el `player_id` igual a `player_id`.
                    # Utiliza una expresión generadora para iterar a través de la lista `object_config` y encuentra el primer jugador que coincida.
                    # Si se encuentra un jugador con el `player_id` correspondiente, se devuelve ese diccionario de configuración del jugador.
                    # Si no se encuentra ningún jugador con ese `player_id`, devuelve `None`.
                """
                object_config = next((game_object for game_object in objects_config if game_object["object_id"] == game_object_id), None)
                
                if object_config:
                    # Crea una instancia de objectCustomized con la configuración del jugador
                    obj_game_object = ObjectsGameCustomized(object_config)  
                    
                    # Añade el jugador al grupo de sprites de jugadores 
                    self.objects.add(obj_game_object)
                    
            # Marca que los jugadores ya han sido cargados
            self.objects_loaded = True         
            
        return True    
            
    # Método para actualizar el estado del nivel        
    def update(self, players_config, objects_config):  
        self.load_level(players_config, objects_config)
        player_statuses = [player.update() for player in self.players]  # Obtén los estados de todos los jugadores        
        if any(status == False for status in player_statuses):
            self.game_over = True
            print("Game Over")
        

    # Método para dibujar el nivel en la pantalla
    def draw(self, screen):  
        screen.blit(self.background, (0, 0))  # Dibuja la imagen de fondo en la pantalla
        self.players.draw(screen)  # Dibuja todos los jugadores en el grupo de sprites en la pantalla
        self.objects.draw(screen)  # Dibuja todos los objetos en el grupo de sprites en la pantalla
