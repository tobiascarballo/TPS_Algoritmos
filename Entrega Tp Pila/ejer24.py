#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de 
#películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Stack

class personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

#creamos una pila con los personajes del MCU, (contiene nombre y cant de peliculas de la saga en l que participo)
mcu_stack = Stack()
mcu_stack.push(personaje("Iron Man", 10))
mcu_stack.push(personaje("Thor", 9))
mcu_stack.push(personaje("Captain America", 11))
mcu_stack.push(personaje("Black Widow", 8))
mcu_stack.push(personaje("Hulk", 6))
mcu_stack.push(personaje("Hawkeye", 5))
mcu_stack.push(personaje("Rocket Raccoon", 4))
mcu_stack.push(personaje("Groot", 3))
mcu_stack.push(personaje("Doctor Strange", 3))
mcu_stack.push(personaje("Spider-Man", 3))

def encontrar_posicion(pila, nombre_personaje):
    pila_aux = Stack()
    posicion = 1
    encontrado = False

    while pila.size() > 0 and not encontrado:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje.nombre == nombre_personaje:
            encontrado = True
        else:
            posicion += 1

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return posicion if encontrado else -1

def personajes_mas_de_cinco_peliculas(pila):
    pila_aux = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje.peliculas > 5:
            personajes.append((personaje.nombre, personaje.peliculas))

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return personajes

def peliculas_viuda_negra(pila):
    pila_aux = Stack()
    peliculas = 0

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje.nombre == "Black Widow":
            peliculas = personaje.peliculas

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return peliculas

def personajes_con_letras(pila, letras):
    pila_aux = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje.nombre[0] in letras:
            personajes.append(personaje.nombre)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return personajes

#a) posición de Rocket Raccoon y Groot
posicion_rocket = encontrar_posicion(mcu_stack, "Rocket Raccoon")
posicion_groot = encontrar_posicion(mcu_stack, "Groot")
print(f"Rocket Raccoon está en la posición: {posicion_rocket}")
print(f"Groot está en la posición: {posicion_groot}")

#b) personajes que estuvieron en más de 5 películas
personajes_mas_5_pelis = personajes_mas_de_cinco_peliculas(mcu_stack)
print("Personajes con más de 5 películas:")
for nombre, peliculas in personajes_mas_5_pelis:
    print(f"{nombre} participó en {peliculas} películas")

#c) películas en las que participó Black Widow
peliculas_black_widow = peliculas_viuda_negra(mcu_stack)
print(f"Black Widow participó en {peliculas_black_widow} películas")

#d) nombres de personajes que empiezan con C, D y G
personajes_cdg = personajes_con_letras(mcu_stack, {'C', 'D', 'G'})
print("Nombres de personajes que empiezan con C, D o G:")
for nombre in personajes_cdg:
    print(nombre)