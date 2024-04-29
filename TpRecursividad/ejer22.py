def usar_la_fuerza(mochila, objetos, pasos=0):
    """
    Resuelve el problema de la mochila Jedi utilizando recursividad.

    Args:
        mochila (list): Vector que representa la mochila.
        objetos (list): Lista de objetos en la mochila.
        pasos (int): Número de pasos (objetos sacados) hasta ahora.

    Returns:
        int: Número de pasos necesarios para encontrar un sable de luz (o -1 si no se encuentra).
    """
    if not mochila:
        # La mochila está vacía, no se encontró un sable de luz
        return -1
    objeto_actual = mochila.pop(0)
    pasos += 1
    if objeto_actual == "sable de luz":
        # Se encontró un sable de luz
        return pasos
    else:
        # Continuar buscando en la mochila
        return usar_la_fuerza(mochila, objetos, pasos)

# Ejemplo de uso
mochila_jedi = ["comida", "agua", "ropa", "sable de luz", "mapa"]
objetos_encontrados = usar_la_fuerza(mochila_jedi.copy(), mochila_jedi)
if objetos_encontrados != -1:
    print(f"Se encontró un sable de luz en {objetos_encontrados} pasos.")
else:
    print("No se encontró un sable de luz en la mochila.")
