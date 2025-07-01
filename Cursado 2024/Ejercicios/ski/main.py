from equipo import Equipo
from esquiador import Esquiador
from federacion import Federacion
from prueba import Prueba


federacion1 = Federacion("Federación Alpina")
federacion2 = Federacion("Federación Nórdica")

# Crear esquiadores
esquiador1 = Esquiador("12345678A", "Juan", "1990-01-15", 34)
esquiador2 = Esquiador("87654321B", "María", "1995-06-20", 29)

federacion1.agregar_esquiador(esquiador1)
federacion2.agregar_esquiador(esquiador2)

# Crear equipos
equipo1 = Equipo("Equipo A", "Entrenador Carlos")
equipo1.agregar_esquiador(esquiador1)
equipo1.agregar_esquiador(esquiador2)

# Crear pruebas
prueba_individual = Prueba("Slalom", "Individual")
prueba_equipo = Prueba("Relevos", "Equipo")

# Agregar participantes a las pruebas
prueba_individual.agregar_participante(esquiador1, 1)
prueba_individual.agregar_participante(esquiador2, 2)
prueba_equipo.agregar_participante(equipo1, 1)

# Mostrar datos
print(federacion1)
print(federacion2)
print(prueba_individual)
print(prueba_equipo)