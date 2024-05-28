#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;

#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.


class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

class Personaje:
    def __init__(self, name, countMovies):
        self.name = name
        self.countMovies = countMovies

personajes = [
    Personaje("Spider-Man", 4),
    Personaje("Iron Man", 8),
    Personaje("Capitan America", 7),
    Personaje("Black Widow", 7),
    Personaje("Rocket Raccoon", 5),
    Personaje("Groot", 3),
    Personaje("DeadPool", 1),
]

chars = ["C", "D", "G"]

pilaPersonajes = Pila()

for personaje in personajes:
    pilaPersonajes.apilar(personaje)

pos = 1
Mas_de_5_sagas = []
caracteristicas = []

while not pilaPersonajes.esta_vacia():
    personaje = pilaPersonajes.desapilar()
    if personaje.name == "Groot" or personaje.name == "Rocket Raccoon":
        print(f"La posición de {personaje.name} es: {pos}")
    if personaje.countMovies > 5:
        Mas_de_5_sagas.append(personaje)
    if personaje.name == "Black Widow":
        print(f"Black Widow participó en {personaje.countMovies} películas")
    if personaje.name[0] in chars:
        caracteristicas.append(personaje)
    pos += 1

print("Los personajes que participaron en más de 5 sagas son los siguientes:")
for personaje in Mas_de_5_sagas:
    print(f"{personaje.name} trabajó en {personaje.countMovies} películas")

print("Los personajes que empiezan con las letras C, D o G son:")
for personaje in caracteristicas:
    print(personaje.name)