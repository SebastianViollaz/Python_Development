from src.Items.item import Item 
from src.jugador import Jugador
class Potenciador(Item):

    def __init__(self,cos,peso,cantidad,estadistica) -> None:
        super().__init__(cos,peso)
        posibles_estadisitcas = ["Vida","Dano"]
        self.estadistica = posibles_estadisitcas[estadistica]
        self.cantidad = cantidad

    def usar(self,personaje : Jugador):
        personaje.Estadisticas[self.estadistica] += self.cantidad
        

        