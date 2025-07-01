from ciudad import Ciudad
from pais import Pais
from provincia import Provincia


argentina = Pais("Argentina")

# Crear provincias
mendoza = Provincia("Mendoza")
buenos_aires = Provincia("Buenos Aires")

# Agregar ciudades a Mendoza
mendoza.agregar_ciudad(Ciudad("Mendoza", 500, 400, 300, 200, 100, 2000))
mendoza.agregar_ciudad(Ciudad("San Rafael", 400, 300, 200, 100, 50, 700))
mendoza.agregar_ciudad(Ciudad("Godoy Cruz", 600, 500, 400, 300, 200, 1800))

# Agregar ciudades a Buenos Aires
buenos_aires.agregar_ciudad(Ciudad("La Plata", 800, 700, 600, 500, 400, 1000))
buenos_aires.agregar_ciudad(Ciudad("Mar del Plata", 500, 500, 500, 500, 500, 2500))

# Agregar provincias al país
argentina.agregar_provincia(mendoza)
argentina.agregar_provincia(buenos_aires)

# Consultas
print("Ciudades en déficit:")
for ciudad in argentina.ciudades_en_deficit():
    print(ciudad)
print("\nProvincias con más de la mitad de ciudades en déficit:")
for provincia in argentina.provincias_afectadas():
    print(provincia)