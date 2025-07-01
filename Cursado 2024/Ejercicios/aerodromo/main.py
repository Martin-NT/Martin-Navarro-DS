from aerodromo import Aerodromo
from avion import Avion
from hangar import Hangar
from mecanico import Mecanico
from piloto import Piloto
from propietario import Propietario


propietario = Propietario("123456789", "Juan Pérez", "Calle Falsa 123", "123456789")
# Crear aviones
avion1 = Avion("ABC123", "2020-01-15", "Cessna 172", 4, 767)
avion2 = Avion("DEF456", "2018-06-30", "Boeing 747", 660, 400000)

propietario.agregar_avion(avion1)
propietario.agregar_avion(avion2)

# Crear mecánico
mecanico = Mecanico("987654321", "Pedro García", "Avenida Siempre Viva", "987654321", 3000, "Diurno")
mecanico.realizar_servicio(avion1, "2023-11-01", 5, "Mantenimiento General")

# Crear piloto
piloto = Piloto("741258963", "María López", "Boulevard Central", "2613007699", "LIC123", ["Altura máxima 10,000m"])
piloto.agregar_avion_autorizado(avion1)

# Crear hangares
hangar1 = Hangar(1, 5, "Zona Norte")
hangar1.agregar_avion(avion1)
hangar1.agregar_avion(avion2)

# Crear aeródromo
aerodromo = Aerodromo("Aeródromo Central")
aerodromo.agregar_hangar(hangar1)

# Mostrar datos
print(aerodromo)
print(hangar1)
print(avion1)
print(mecanico)
print(piloto)
