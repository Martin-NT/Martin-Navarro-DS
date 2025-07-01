from artista import Artista
from escultura import Escultura
from museo import Museo
from pintura import Pintura


artista1 = Artista("Pablo Picasso", "1881-10-25", "1973-04-08", "España", "Cubismo")

# Crear objetos de arte
pintura1 = Pintura(1, "Guernica", "Descripción del Guernica", artista1, 1937, "Óleo", "Lienzo", "Cubismo", "España", "Europea", "Renacimiento")
escultura1 = Escultura(2, "El Pensador", "Escultura famosa", artista1, 1902, "Bronce", 1.8, 500, "Realismo", "España", "Europea", "Renacimiento")
# Crear museo
museo = Museo("Museo Nacional del Arte")
museo.agregar_objeto(pintura1)
museo.agregar_objeto(escultura1)
# Mostrar datos
print(museo)
print(pintura1)
print(escultura1)