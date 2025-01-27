import pygame  # Importa la biblioteca Pygame
from modules.players import PlayerModule  # Importa la clase PlayerModule desde el módulo players

# Clase Nivel
class LevelModule:
    def __init__(self, config, players_config):  
        # Método constructor que recibe la configuración del nivel y la configuración de los jugadores
        
        self.config = config  # Guarda la configuración del nivel
        self.background = pygame.image.load(config["background"])  # Carga la imagen de fondo del nivel
        self.players = pygame.sprite.Group()  # Crea un grupo de sprites para los jugadores
        self.objects = pygame.sprite.Group()  # Crea un grupo de sprites para los objetos
        self.load_level(players_config)  # Llama al método load_level para cargar los jugadores y objetos del nivel
        
        self.game_over = False 


    # Método para cargar los jugadores y objetos del nivel
    def load_level(self, players_config):  
        if "players" in self.config and self.config["players"]:  # Verifica si hay jugadores en la configuración del nivel
            player_id = self.config["players"]["player_id"]  # Obtiene el ID del jugador desde la configuración del nivel
            player_config = next(player for player in players_config if player["player_id"] == player_id)  # Busca la configuración del jugador correspondiente en la lista de configuraciones de jugadores
            player = PlayerModule(player_config)  # Crea una instancia de PlayerModule con la configuración del jugador
            self.players.add(player)  # Añade el jugador al grupo de sprites de jugadores

        for obj in self.config["objects"]:  # Itera sobre los objetos en la configuración del nivel
            # Aquí puedes agregar la lógica para crear otros objetos del nivel
            pass

    # Método para actualizar el estado del nivel        
    def update(self):  
        player_statuses = [player.update() for player in self.players]  # Obtén los estados de todos los jugadores        
        if any(status == False for status in player_statuses):
                self.game_over = True
                print("Game Over")
        

    # Método para dibujar el nivel en la pantalla
    def draw(self, screen):  
        screen.blit(self.background, (0, 0))  # Dibuja la imagen de fondo en la pantalla
        self.players.draw(screen)  # Dibuja todos los jugadores en el grupo de sprites en la pantalla
