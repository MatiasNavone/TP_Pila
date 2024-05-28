#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que

#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
#bos episodios.




pila_v = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa"]
pila_vii = ["Han Solo", "Leia Organa", "Rey", "Finn", "Kylo Ren"]

personajes_comun = []

pila_vii_lista = list(pila_vii)

while pila_v:
    personaje = pila_v.pop()  
    if personaje in pila_vii_lista:
        personajes_comun.append(personaje)  


print("Personajes en comun:", personajes_comun)

