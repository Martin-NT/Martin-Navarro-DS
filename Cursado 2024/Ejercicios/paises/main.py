from ciudad import Ciudad
from continente import Continente
from pais import Pais
from provincia import Provincia


america = Continente("América del Sur")

# Crear países
argentina = Pais("Argentina")
chile = Pais("Chile")
# Crear provincias
mendoza = Provincia("Mendoza")
buenos_aires = Provincia("Buenos Aires", capital=True)

# Agregar países a América
america.agregar_pais(argentina)
america.agregar_pais(chile)

# Agregar provincias a Argentina
argentina.agregar_provincia(mendoza)
argentina.agregar_provincia(buenos_aires)
# Agregar ciudades a provincias
mendoza.agregar_ciudad(Ciudad("San Rafael", 200000))
mendoza.agregar_ciudad(Ciudad("Godoy Cruz", 190000))
buenos_aires.agregar_ciudad(Ciudad("Mar del Plata", 600000))
# Definir fronteras
argentina.agregar_frontera(chile)
mendoza.agregar_frontera(chile)
# Mostrar datos
print(america)
print(argentina)
print(mendoza)
print(buenos_aires)