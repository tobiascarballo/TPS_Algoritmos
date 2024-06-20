#ejer6
#Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar las funciones necesarias 
#para poder realizar las siguientes actividades:

from lista import search, remove, show_list

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
  }
]


#A) eliminar el nodo que contiene la información de Linterna Verde
remove(super_heroes, "nombre", "Linterna Verde")
print("A) El nodo que contiene la informacion de Linterna Verde ha sido eliminado")

#B) mostrar el año de aparición de Wolverine
wolverine_index = search(super_heroes, "nombre", "Wolverine")
print("B) Año de aparición de Wolverine:", super_heroes[wolverine_index]["año_aparicion"])

#C) cambiar la casa de Dr. Strange a Marvel
dr_strange_index = search(super_heroes, "nombre", "Doctor Strange")
if dr_strange_index is not None:
    super_heroes[dr_strange_index]["casa_comic"] = "Marvel Comics"
print("C) La casa de Dr. Strange ha sido cambiada a Marvel")

#D) mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
print("D) Superhéroes con 'traje' o 'armadura' en su biografía:")
for heroe in super_heroes:
    if "traje" in heroe["biografia"].lower() or "armadura" in heroe["biografia"].lower():
        print(heroe["nombre"])

#E) mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
print("E) Superhéroes con fecha de aparición anterior a 1963:")
for heroe in super_heroes:
    if heroe["año_aparicion"] < 1963:
        print(heroe["nombre"], "-", heroe["casa_comic"])

#F) mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
capitana_marvel_index = search(super_heroes, "nombre", "Capitana Marvel")
mujer_maravilla_index = search(super_heroes, "nombre", "Mujer Maravilla")
print("F)")
print("Casa de Capitana Marvel:", super_heroes[capitana_marvel_index]["casa_comic"])
print("Casa de Mujer Maravilla:", super_heroes[mujer_maravilla_index]["casa_comic"])

#G) mostrar toda la información de Flash y Star-Lord
flash_index = search(super_heroes, "nombre", "Flash")
star_lord_index = search(super_heroes, "nombre", "Star-Lord")
print("G)")
print("Información de Flash:", super_heroes[flash_index])
print("Información de Star-Lord:", super_heroes[star_lord_index])

#H) listar los superhéroes que comienzan con la letra B, M y S
print("H) Superhéroes que comienzan con B, M y S:")
for heroe in super_heroes:
    if heroe["nombre"].startswith(("B", "M", "S")):
        print(heroe["nombre"])

#I) determinar cuántos superhéroes hay de cada casa de comic
marvel_count = sum(1 for heroe in super_heroes if heroe["casa_comic"] == "Marvel Comics")
dc_count = sum(1 for heroe in super_heroes if heroe["casa_comic"] == "DC Comics")
print("I)")
print("Número de superhéroes de Marvel Comics:", marvel_count)
print("Número de superhéroes de DC Comics:", dc_count)

#mostrar la lista actualizada de superhéroes
show_list("Lista de Superhéroes Actualizada", super_heroes)