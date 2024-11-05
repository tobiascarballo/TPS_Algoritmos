class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element) #agregar elemento a la lista

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop() #quito elementos del final chequeando antes, sino muestro NONE
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1] #muestro el elemento sin borrarlo como en el "pop"
        else:
            return None

    def size(self):
        return len(self.__elements)