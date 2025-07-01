from animal import Animal
from area import Area
from comunidad import ComunidadAutonoma
from parque import ParqueNacional
from vegetal import Vegetal
from personal import Celador, Guarda, Investigador
from entrada import Entrada
from excursion import Excursion

# Crear una comunidad autónoma
andalucia = ComunidadAutonoma("Andalucía", "Consejería de Medio Ambiente")

# Crear un parque nacional
parque = ParqueNacional("Doñana", "1969-10-28")
andalucia.agregar_parque(parque)

# Crear áreas en el parque
area1 = Area("Marismas", 500)
area2 = Area("Dunas", 300)
parque.agregar_area(area1)
parque.agregar_area(area2)

# Crear especies
encina = Vegetal("Quercus ilex", "Encina", 2000, True, "Primavera")
lince = Animal("Lynx pardinus", "Lince Ibérico", 50, "Invierno", "Carnívoro")
conejo = Animal("Oryctolagus cuniculus", "Conejo", 500, None, "Herbívoro")

# Asociar especies a áreas
area1.agregar_especie(encina)
area1.agregar_especie(lince)

# Agregar alimentos al lince
lince.agregar_alimento(conejo)

# Crear personal y asignar roles
celador1 = Celador("12345678A", "Juan Pérez", "Calle Real 1", "123456789", 2000.0, "SS123456")
guarda1 = Guarda("87654321B", "Ana Martínez", "Avenida del Parque 5", "987654321", 2500.0, "SS987654", "Jeep", "AB-123-CD")
investigador1 = Investigador("11223344C", "Carlos López", "Calle Ciencia 10", "1122334455", 3000.0, "SS112233", "Biología")

# Asignar personal al parque y a las áreas
parque.agregar_personal(celador1)
parque.agregar_personal(guarda1)
parque.agregar_personal(investigador1)

guarda1.asignar_area(area1)
guarda1.asignar_area(area2)

# Crear y asignar entrada
entrada1 = Entrada(1)
parque.agregar_entrada(entrada1)
celador1.asignar_entrada(entrada1)

# Asignar especies investigadas al investigador
investigador1.agregar_especie_investigada(lince)
investigador1.agregar_especie_investigada(encina)

# Crear excursión y agregar visitantes
excursion1 = Excursion("EXC001", "2024-12-01", "10:00")
parque.agregar_excursion(excursion1)

# Mostrar datos
print(andalucia)
print(parque)
print(area1)
print(encina)
print(lince)
print(celador1)
print(guarda1)
print(investigador1)
print(entrada1)
print(excursion1)
