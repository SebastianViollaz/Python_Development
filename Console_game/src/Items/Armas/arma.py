from src.Items.item import Item

class Arma(Item):

    def __init__(self,costo,peso,dano)-> None:
        super().__init__(costo,peso)
        self.dano = dano

