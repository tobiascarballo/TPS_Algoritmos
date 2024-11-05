#1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente: 
#a) los índices de cada uno de los árboles deben ser nombre, número y tipo; 
#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–; 
#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico; 
#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre; 
#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
#f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 


from arbol_avl import BinaryTree

# se crean los 3 arboles
name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = BinaryTree()

# datos de pokemons
pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["agua"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["roca", "dragón"]},
]

# a) cargar los datos en los arboles por nombre, numero, tipo
for pokemon in pokemons:
    # arbol por nombre
    name_tree.insert_node(pokemon["nombre"], pokemon)
    
    # arbol por numero
    number_tree.insert_node(pokemon["numero"], pokemon)
    
    # arbol por tipo
    for tipo in pokemon["tipo"]:
        if not type_tree.search(tipo):
            type_tree.insert_node(tipo, {"pokemons": []})
        node = type_tree.search(tipo)
        node.other_value["pokemons"].append(pokemon)

# b) busqueda por numero y nombre por proximidad
print("\nb) Busqueda por numero")
node = number_tree.search(1)
if node:
    print(f"Pokemon numero {node.value}:")
    print(f"Nombre: {node.other_value['nombre']}")
    print(f"Tipo(s): {', '.join(node.other_value['tipo'])}")

print("\nb) busqueda por proximidad de nombre (Bul)")
name_tree.proximity_search("Bul")

# c) mostrar Pokemon por tipos especificos
tipos_buscar = ["agua", "fuego", "planta", "eléctrico"]
print("\nc) pokemon por tipos")
for tipo in tipos_buscar:
    node = type_tree.search(tipo)
    if node:
        print(f"\npokemons de tipo {tipo}:")
        for pokemon in node.other_value["pokemons"]:
            print(f"- {pokemon['nombre']}")

# d) listado ordenado por numero y nombre, y listado por nivel
print("\nd) listado ordenado por numero")
number_tree.inorden()

print("\nd) listado ordenado por nombre")
name_tree.inorden()

print("\nd) listado por nivel")
name_tree.by_level()

# e) mostrar datos de Pokemon especificos
print("\ne) datos de Pokemon especificos")
pokemones_buscar = ["Jolteon", "Lycanroc", "Tyrantrum"]
for nombre in pokemones_buscar:
    node = name_tree.search(nombre)
    if node:
        print(f"\nPokemon: {node.value}")
        print(f"Numero: {node.other_value['numero']}")
        print(f"Tipo(s): {', '.join(node.other_value['tipo'])}")

# f) contar Pokemon de tipo electrico y acero
print("\nf) conteo de Pokemon por tipo")
for tipo in ["eléctrico", "acero"]:
    node = type_tree.search(tipo)
    if node:
        cantidad = len(node.other_value["pokemons"])
        print(f"pokemon de tipo {tipo}: {cantidad}")
    else:
        print(f"pokemon de tipo {tipo}: 0")