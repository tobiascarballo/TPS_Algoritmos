def romano_decimal(romano):
    valor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valor[romano]
    if valor[romano[0]] < valor[romano[1]]:
        return -valor[romano[0]] + romano_decimal(romano[1:])
    else:
        return valor[romano[0]] + romano_decimal(romano[1:])
    
#ejemplo
num_romano = "X"
print("el numero romano", num_romano, "es igual a:", romano_decimal(num_romano), "en decimal.")

#otro ejemplo
num_romano1 = "CVII"
print("el numero romano", num_romano1, "es igual a:", romano_decimal(num_romano1), "en decimal.")