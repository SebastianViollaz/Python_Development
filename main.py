from src.jugador import Jugador
from src.Items.Potenciadores.potenciador import Potenciador
import random
import os

def MostrarJugadores():
    """Muestra la lista de jugadores con su posicion en la lista"""
    i = 0
    print(("---------------").center(ancho_consola))
    for jugador in jugadores_activos:
        print(f"{i} : {jugador.nombre}")
        jugador.describir()
        i+=1
    print(("---------------").center(ancho_consola))
    
def MostrarPotenciadores():
    i = 0
    print(("----------").center(ancho_consola))
    for potencidor in lista_potenciadores:
        print(f"{i} : {potencidor.estadistica}")
        i+=1
    print(("----------").center(ancho_consola))

#SetUPGeneral
ancho_consola = 80 #Para centrar Prints

#Creacion de la LISTA_JUGADORES
cantidad_jugadores = int(input("Cantidad de jugadores?"))
jugadores_activos : list[Jugador] = []
for i in range(0,cantidad_jugadores):
    nombre = input(f"Ingrese el nombre del jugador{i + 1}")
    vida = random.randint(0,150)
    dano = random.randrange(0,30)
    jugadores_activos.append(Jugador(nombre,vida,dano))


#Lista de potenciadores comunes (Podria exisitr en cada jugador por separado)
lista_potenciadores = []
lista_potenciadores.append(Potenciador(10,0,100,0))
lista_potenciadores.append(Potenciador(10,0,100,1))

os.system('cls' if os.name == 'nt' else 'clear')

TURNO_JUGADOR = 0
print(("---ESTADISTICAS INICIALES---").center(ancho_consola))
while True:

    JUGADOR = jugadores_activos[TURNO_JUGADOR]
    MostrarJugadores()
    print("------------------------")
    print(f"Turno de: {JUGADOR.nombre}")
    print("------------------------")
    
    #Menu de selccion de opciones
    print("\n1:Atacar\n2:Curar\n3:Usar Potenciadores")
    opcion = input("Ingrese su opcion: ")
    
    #Menu de opciones
    if opcion == "1": #Ataque
        objetivo = int(input("A qun quiere atacar? : "))
        os.system('cls' if os.name == 'nt' else 'clear')

        if objetivo != TURNO_JUGADOR:
            JUGADOR.atacar(jugadores_activos[objetivo])
        else:
            print("Sos vos mismo perdes el turno")
    elif opcion == "2": #Curacion
        JUGADOR.curar()
    elif opcion == "3": #Uso de potenciadores
        if len(lista_potenciadores) != 0:
            JUGADOR.describir()
            MostrarPotenciadores()
            objetivo = int(input("Que potenciador queres?"))
            os.system('cls' if os.name == 'nt' else 'clear')
            lista_potenciadores[objetivo].usar(JUGADOR)
            lista_potenciadores.pop(objetivo)
        else:
            print("No quedan potenciadores Perdes el turno")


    #Elimino jugadores muertos
    for jugador in jugadores_activos:
        if jugador.Estadisticas["Vida"] <= 0:
            jugadores_activos.remove(jugador) 
    
    #Defino el siguiente turno  
    if TURNO_JUGADOR == len(jugadores_activos)-1:
        TURNO_JUGADOR = 0
    else:
        TURNO_JUGADOR = 1
    os.system('cls' if os.name == 'nt' else 'clear')


