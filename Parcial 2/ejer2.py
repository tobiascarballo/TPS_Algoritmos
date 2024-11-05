#2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas: 
#a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
#c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
#d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

from grafo import Graph

# Crear el grafo no dirigido
grafo = Graph(dirigido=False)

# d) cargar los personajes del punto d en el grafo
personajes = [
    'Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 
    'C-3PO', 'Leia', 'Rey', 'Kylo Ren', 
    'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8'
]

for personaje in personajes:
    grafo.insert_vertice(personaje)

# a) agregar las aristas con la cantidad de episodios compartidos
grafo.insert_arista('Luke Skywalker', 'Darth Vader', 2)
grafo.insert_arista('Luke Skywalker', 'Leia', 5)
grafo.insert_arista('Leia', 'Han Solo', 3)
grafo.insert_arista('Han Solo', 'Chewbacca', 4)
grafo.insert_arista('Yoda', 'Luke Skywalker', 1)
grafo.insert_arista('R2-D2', 'C-3PO', 6)
grafo.insert_arista('Rey', 'BB-8', 3)
grafo.insert_arista('Kylo Ren', 'Rey', 2)
grafo.insert_arista('Yoda', 'Leia', 1)

# b) arbol de expansión minima y determinar si contiene a Yoda
arbol_expansion_minimo = grafo.kruskal('Luke Skywalker')
yoda_incluido = any('Yoda' in arbol for arbol in arbol_expansion_minimo)

# c) determinar número máximo de episodios compartidos y quienes son los que lo comparten
max_episodios = 0
max_pareja = ('', '')
for nodo in grafo.elements:
    for arista in nodo['aristas']:
        if arista['peso'] > max_episodios:
            max_episodios = arista['peso']
            max_pareja = (nodo['value'], arista['value'])

# print de los resultados
print("b) Árbol de expansión mínimo:", arbol_expansion_minimo)
print("b) En el árbol de expansión mínimo esta Yoda?:", "Sí" if yoda_incluido else "No")
print("c) Máximo de episodios compartidos:", max_episodios)
print("c) Personajes que comparten el máximo de episodios:", max_pareja)