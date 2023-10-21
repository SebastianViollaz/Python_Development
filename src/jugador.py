class Jugador():
    def __init__(self,nombre : str,vida : int,dano:int):
        self.x = 0
        self.y = 0
        self.iamge = None
        self.nombre = nombre
        self.Estadisticas = {"Vida": vida,
                             "Dano" : dano}

    def dibujar(self,gameDisplay):
        gameDisplay.blit(self.img, (self.x,self.y))

    def mover(self,x,y):
        self.x +=x
        self.y -=y

    def perdervida(self,cant):
        self.Estadisticas['Vida'] -= cant
      
    def atacar(self, enemigo):
        """esta funcion ataca a un enemigo, donde el tipo dato de este tiene que ser Jugador"""
        print(f"{self.nombre} ataca a {enemigo.nombre}")
        enemigo.perdervida(self.Estadisticas["Dano"])
    
    def describir(self):
        print(f"Nombre = {self.nombre}", end=" / ")
        print(f"Vida = {self.Estadisticas['Vida']}",end=" / ")
        print(f"Dano = {self.Estadisticas['Dano']}")
    
    def curar(self):
        self.Estadisticas['Vida'] += 4