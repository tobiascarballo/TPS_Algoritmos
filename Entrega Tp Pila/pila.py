class Stack:

    def __init__(self):
        self.__elements = [] #inicializa la clase

    def push(self, element):
        self.__elements.append(element) #agregar elemento a la lista

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop() #quito elements del final chequenaod antes, sino muestro NONe
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1] #saca el elemento de arriba
        else:
            return None

    def size(self):
        return len(self.__elements) #cantidad de elementos
