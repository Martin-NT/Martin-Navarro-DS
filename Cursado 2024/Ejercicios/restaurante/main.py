from ciudad import Ciudad
from persona import Persona
from plato import Plato
from restaurante import Restaurante


ciudad = Ciudad("Ciudad Gourmet")

# Crear restaurantes
restaurante1 = Restaurante("El Sabor")
restaurante2 = Restaurante("La Comida Rápida")
# Crear platos
pizza = Plato("Pizza")
pasta = Plato("Pasta")
hamburguesa = Plato("Hamburguesa")
# Agregar platos al menú de los restaurantes
restaurante1.agregar_plato(pizza)
restaurante1.agregar_plato(pasta)
restaurante2.agregar_plato(hamburguesa)
# Agregar restaurantes a la ciudad
ciudad.agregar_restaurante(restaurante1)
ciudad.agregar_restaurante(restaurante2)
# Crear personas
persona1 = Persona("Juan")
persona2 = Persona("María")
# Agregar platos favoritos
persona1.agregar_plato_favorito(restaurante1, pizza)
persona1.agregar_plato_favorito(restaurante1, pasta)
persona2.agregar_plato_favorito(restaurante2, hamburguesa)
# Mostrar datos
print(ciudad)
print(restaurante1)
print(restaurante2)
print(persona1)
print(persona2)