def roman_to_decimal(roman_numeral):
    # Diccionario para mapear los valores de los símbolos romanos
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def recursive_conversion(roman, total, prev_value):
        if not roman:
            return total
        current_value = roman_values[roman[0]]
        if current_value > prev_value:
            # Restamos el valor anterior (porque es un número romano como IV o IX)
            total += current_value - 2 * prev_value
        else:
            total += current_value
        return recursive_conversion(roman[1:], total, current_value)

    return recursive_conversion(roman_numeral, 0, 0)

# Ejemplo de uso
numero_romano = "XXIV"
numero_decimal = roman_to_decimal(numero_romano)
print(f"El número romano {numero_romano} es igual a {numero_decimal}.")
