
from src.Items.Armas.arma import Arma

class Espada(Arma):

    def __init__(self,costo,peso,dano,sangrado,)-> None:
        self.costo = costo
        self.peso = peso
        self.sangrado = sangrado
        self.dano = dano
    
    def atacar(self):
        print(f"La espada  ataco con {self.dano} de dano")
