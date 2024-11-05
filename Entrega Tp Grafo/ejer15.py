#15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

#a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica);
#b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;
#c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#e. determinar si algún país tiene más de una maravilla del mismo tipo;
#f. deberá utilizar un grafo no dirigido.

from grafo import Graph
# f) Se inicializa el grafo como no dirigido
grafo_maravillas = Graph(dirigido=False)

# a) Se define las maravillas y sus datos básicos
maravillas = [
    {"nombre": "Chichen Itza", "pais": ["México"], "tipo": "arquitectónica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectónica"},
    {"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectónica"},
    {"nombre": "Coliseo", "pais": ["Italia"], "tipo": "arquitectónica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectónica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectónica"},
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectónica"},
    {"nombre": "Amazonas", "pais": ["Brasil", "Perú", "Colombia"], "tipo": "natural"},
    {"nombre": "Bahía de Ha Long", "pais": ["Vietnam"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Komodo", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Parque Nacional de las Montañas Azules", "pais": ["Australia"], "tipo": "natural"},
    {"nombre": "Table Mountain", "pais": ["Sudáfrica"], "tipo": "natural"}
]

# Agregamos las maravillas como vértices en el grafo
for maravilla in maravillas:
    grafo_maravillas.insert_vertice(maravilla["nombre"])

# b) Se agregan las aristas con distancias (conexiones entre maravillas de mismo tipo)
# Suponiendo que tenemos una lista de distancias entre maravillas de cada tipo
distancias_arquitectonicas = [
    ("Chichen Itza", "Cristo Redentor", 2000),
    ("Chichen Itza", "Machu Picchu", 4000),
    ("Chichen Itza", "Coliseo", 8000),
    ("Chichen Itza", "Taj Mahal", 15000),
    ("Chichen Itza", "Petra", 13000),
    ("Chichen Itza", "Gran Muralla China", 12000),
    ("Cristo Redentor", "Machu Picchu", 3500),
    ("Cristo Redentor", "Coliseo", 9400),
    ("Cristo Redentor", "Taj Mahal", 13900),
    ("Cristo Redentor", "Petra", 11100),
    ("Cristo Redentor", "Gran Muralla China", 17500),
    ("Machu Picchu", "Coliseo", 10700),
    ("Machu Picchu", "Taj Mahal", 15000),
    ("Machu Picchu", "Petra", 14500),
    ("Machu Picchu", "Gran Muralla China", 16500),
    ("Coliseo", "Taj Mahal", 6700),
    ("Coliseo", "Petra", 2500),
    ("Coliseo", "Gran Muralla China", 8000),
    ("Taj Mahal", "Petra", 4300),
    ("Taj Mahal", "Gran Muralla China", 5000),
    ("Petra", "Gran Muralla China", 4900),
]

distancias_naturales = [
    ("Amazonas", "Bahía de Ha Long", 17000),
    ("Amazonas", "Cataratas del Iguazú", 3200),
    ("Amazonas", "Isla Jeju", 18000),
    ("Amazonas", "Komodo", 19000),
    ("Amazonas", "Parque Nacional de las Montañas Azules", 13000),
    ("Amazonas", "Table Mountain", 14000),
    ("Bahía de Ha Long", "Cataratas del Iguazú", 20000),
    ("Bahía de Ha Long", "Isla Jeju", 2700),
    ("Bahía de Ha Long", "Komodo", 4000),
    ("Bahía de Ha Long", "Parque Nacional de las Montañas Azules", 7600),
    ("Bahía de Ha Long", "Table Mountain", 13000),
    ("Cataratas del Iguazú", "Isla Jeju", 20000),
    ("Cataratas del Iguazú", "Komodo", 19000),
    ("Cataratas del Iguazú", "Parque Nacional de las Montañas Azules", 13500),
    ("Cataratas del Iguazú", "Table Mountain", 16000),
    ("Isla Jeju", "Komodo", 4800),
    ("Isla Jeju", "Parque Nacional de las Montañas Azules", 8600),
    ("Isla Jeju", "Table Mountain", 13400),
    ("Komodo", "Parque Nacional de las Montañas Azules", 5800),
    ("Komodo", "Table Mountain", 10600),
    ("Parque Nacional de las Montañas Azules", "Table Mountain", 11000),
]

# Se agregan las aristas en el grafo
for origen, destino, distancia in distancias_arquitectonicas + distancias_naturales:
    grafo_maravillas.insert_arista(origen, destino, distancia)

# c) Encontrar el árbol de expansión mínima para cada tipo (arquitectonia y natural)
def arbol_minimo_por_tipo(tipo):
    vertices_tipo = [v for v in maravillas if v["tipo"] == tipo]
    return grafo_maravillas.kruskal(vertices_tipo[0]["nombre"])

arbol_minimo_arquitectonico = arbol_minimo_por_tipo("arquitectónica")
arbol_minimo_natural = arbol_minimo_por_tipo("natural")

# d) Verificar países con maravillas de ambos tipos
def paises_con_dos_tipos():
    paises_arquitectonicos = {pais for m in maravillas if m["tipo"] == "arquitectónica" for pais in m["pais"]}
    paises_naturales = {pais for m in maravillas if m["tipo"] == "natural" for pais in m["pais"]}
    return paises_arquitectonicos.intersection(paises_naturales)

paises_con_ambos_tipos = paises_con_dos_tipos()

# e) Verificar si algún país tiene múltiples maravillas del mismo tipo
def paises_con_multiples_maravillas(tipo):
    contador = {}
    for m in maravillas:
        if m["tipo"] == tipo:
            for pais in m["pais"]:
                if pais in contador:
                    contador[pais] += 1
                else:
                    contador[pais] = 1
    return [pais for pais, count in contador.items() if count > 1]

paises_multiples_arquitectonicas = paises_con_multiples_maravillas("arquitectónica")
paises_multiples_naturales = paises_con_multiples_maravillas("natural")

# print de cada resultado
print("c) Árbol de expansión mínima arquitectónico:", arbol_minimo_arquitectonico)
print("")
print("c) Árbol de expansión mínima natural:", arbol_minimo_natural)
print("")
print("e) Países con maravillas de ambos tipos:", paises_con_ambos_tipos)
print("")
print("d) Países con múltiples maravillas arquitectónicas:", paises_multiples_arquitectonicas)
print("")
print("d) Países con múltiples maravillas naturales:", paises_multiples_naturales)