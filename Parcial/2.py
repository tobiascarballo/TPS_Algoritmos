from pila import Stack
from dino import dinosaurios

pila_dinosaurios = Stack()
for dino in dinosaurios:
    pila_dinosaurios.push(dino)

#a)
especies = set()
for dino in dinosaurios:
    especies.add(dino["especie"])
print("A) La cantidad de especies son:", len(especies))

#b)
descubridores = set()
for dino in dinosaurios:
    descubridores.add(dino["descubridor"])
print("B) La cantidad de descubridores distintos son:", len(descubridores))

#c)
print("C) Los dinosaurios que empiezan con T son:")
pila_aux = Stack()
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    if dino["nombre"].startswith("T"):
        print(dino["nombre"])
    pila_aux.push(dino)

while pila_aux.size() > 0:
    pila_dinosaurios.push(pila_aux.pop())

#d)
print("D) Los dinosaurios que pesan menos de 275 kg son:")
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    peso_kg = int(dino["peso"].split()[0])
    if peso_kg < 275:
        print(dino["nombre"])
    pila_aux.push(dino)

while pila_aux.size() > 0:
    pila_dinosaurios.push(pila_aux.pop())

#e)
pila_aqs = Stack()
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    if dino["nombre"][0] in ['A', 'Q', 'S']:
        pila_aqs.push(dino)
    else:
        pila_aux.push(dino)

print("E) Los dinosaurios que comienzan con A, Q, S son:")
while pila_aqs.size() > 0:
    dino = pila_aqs.pop()
    print(dino["nombre"])
    pila_aux.push(dino)

while pila_aux.size() > 0:
    pila_dinosaurios.push(pila_aux.pop())