# un archivo donde editar de manera personalizada las clases que vendran predefinidas 

# ejemplo, para el juego de snake quiero personalizar que cuando se mueva tenga una direccion

# importo la clase playerModule

from modules.players import PlayerModule

class PlayerCustomized(PlayerModule):
    
    def __init__(self, config):
        super().__init__(config)