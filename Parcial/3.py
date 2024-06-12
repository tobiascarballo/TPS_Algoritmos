from lista import search, show_list
from Jedi import jedis

#Función para obtener el nombre y la especie de un Jedi
def get_name_and_species(jedi):
    return jedi['name'], jedi['species']

#Función para obtener toda la información de un Jedi por nombre
def get_jedi_info_by_name(name):
    for jedi in jedis:
        if jedi['name'] == name:
            return jedi
    return None

#Función para obtener los padawan de un maestro
def get_padawans(master_name):
    padawans = []
    for jedi in jedis:
        if jedi['master'] == master_name:
            padawans.append(jedi)
    return padawans

#Función para filtrar Jedi por especie
def filter_jedi_by_species(species):
    return [jedi for jedi in jedis if jedi['species'] == species]

#Función para filtrar Jedi cuyos nombres comiencen con una letra dada
def filter_jedi_by_name_starting_with(letter):
    return [jedi for jedi in jedis if jedi['name'].startswith(letter)]

#Función para obtener Jedi con más de un color de sable de luz
def get_jedi_with_multiple_lightsaber_colors():
    return [jedi for jedi in jedis if jedi['lightsaber_color'] and '/' in jedi['lightsaber_color']]

#Función para filtrar Jedi por colores de sable de luz
def filter_jedi_by_lightsaber_color(color1, color2):
    return [jedi for jedi in jedis if jedi['lightsaber_color'] == color1 or jedi['lightsaber_color'] == color2]

#Función para obtener los nombres de los padawans de un maestro
def get_padawan_names(jedis, master_name):
    padawans = get_padawans(master_name)
    return [padawan['name'] for padawan in padawans if padawan['rank'] == 'Padawan']

#Función para obtener todos los Jedi con rango de Grand Master
def get_grand_masters():
    return [jedi for jedi in jedis if jedi['rank'] == 'Grand Master']

#a)Listado ordenado por nombre y por especie
jedis_sorted_by_name_and_species = sorted(jedis, key=lambda x: (x['name'], x['species']))
show_list("A) Jedis ordenados por nombre y especie:", jedis_sorted_by_name_and_species)

#b)Mostrar toda la información de Ahsoka Tano y Kit Fisto
ahsoka_info = get_jedi_info_by_name("Ahsoka Tano")
kit_fisto_info = get_jedi_info_by_name("Kit Fisto")
show_list("B) Información de Ahsoka Tano:", [ahsoka_info])
show_list("B) Información de Kit Fisto:", [kit_fisto_info])

#c)Mostrar todos los padawan de Yoda y Luke Skywalker
yoda_padawans = get_padawan_names(jedis, "Yoda")
luke_padawans = get_padawan_names(jedis, "Luke Skywalker")
show_list("C) Padawans de Yoda:", yoda_padawans)
show_list("C) Padawans de Luke Skywalker:", luke_padawans)

#d)Mostrar los Jedi de especie humana y twi'lek
human_jedis = filter_jedi_by_species("Human")
twilek_jedis = filter_jedi_by_species("Twi'lek")
show_list("D) Jedi de especie humana:", human_jedis)
show_list("D) Jedi de especie Twi'lek:", twilek_jedis)

#e)Listar todos los Jedi que comienzan con A
jedis_starting_with_A = filter_jedi_by_name_starting_with("A")
show_list("E) Jedi cuyos nombres comienzan con A:", jedis_starting_with_A)

#f)Mostrar los Jedi que usaron sable de luz de más de un color
jedis_with_multiple_colors = get_jedi_with_multiple_lightsaber_colors()
show_list("F) Jedi que usaron sable de luz de más de un color:", jedis_with_multiple_colors)

#g)Indicar los Jedi que utilizaron sable de luz amarillo o violeta
yellow_or_violet_jedis = filter_jedi_by_lightsaber_color("Yellow", "Violet")
show_list("G) Jedi que utilizaron sable de luz amarillo o violeta:", yellow_or_violet_jedis)

#h)Indicar los nombres de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron
qui_gon_padawans = get_padawan_names(jedis, "Qui-Gon Jinn")
mace_windu_padawans = get_padawan_names(jedis, "Mace Windu")
show_list("H) Padawans de Qui-Gon Jinn:", qui_gon_padawans)
show_list("H) Padawans de Mace Windu:", mace_windu_padawans)

#i)Mostrar todos los Jedi que tengan el ranking de Grand Master
grand_masters = get_grand_masters()
show_list("I) Jedi con rango de Grand Master:", grand_masters)
