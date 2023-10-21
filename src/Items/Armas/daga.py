
from src.Items.Armas.arma import Arma

class Daga(Arma):

    def __init__(self,costo,peso,dano,critico)-> None:
        self.costo = costo
        self.peso = peso
        self.critico = critico
        self.dano = dano
    
    def atacar(self):
        print(f"La daga ataco con {self.dano} de dano")
