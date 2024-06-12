import random

def listar_a_la_inversa(lista):
    if len(lista) <= 1:
        return lista
    else:
        return listar_a_la_inversa(lista[1:]) + [lista[0]]

longitud = random.randint(1, 10)
lista_aleatoria = [random.randint(1, 100) for i in range(longitud)]

print(f"La lista original es: {lista_aleatoria}")
print(f"La lista invertida es: {listar_a_la_inversa(lista_aleatoria)}")