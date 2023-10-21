from src.Items.Armas.arma import Arma


class Arco(Arma):

    def __init__(self,costo,peso,dano,velocidad,recarga)-> None:
        super.__init__(costo,peso,dano)

        self.velocidad = velocidad
        self.recarga = recarga
    def atacar(self):
        print(f"El arco ataco con {self.dano} de dano")


