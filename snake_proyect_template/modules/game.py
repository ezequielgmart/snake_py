"""

This file is for: todas las otras clases heredaran de esta. 

dependencies: 

N/A

Required on: all module files

"""

import json 

class GameModule:

    
    def __init__(self):
        # Guardar todas las configuraciones que esten en los archivos json 
        self.levels_file = './/settings//levels.json'
        self.rooms_file = './/settings//rooms.json'
        self.objects_file = './/settings//objects.json'
        self.players_file = './/settings//players.json'
        
        # Ajustes del juego por defecto y otros datos
        self.config_file = self.get_data_from_json_file('.//settings//game.json')

    # 
    def get_objects_config(self):
        data = self.get_data_from_json_file(self.objects_file)
        return data
    
    def get_players_config(self):
        data = self.get_data_from_json_file(self.players_file)
        return data
    
    def get_levels_config(self):
        data = self.get_data_from_json_file(self.rooms_file)
        return data
            
    def get_data_from_json_file(self,dir):    
        
        with open(dir, 'r') as file:
            data = json.load(file)
            
        return data    