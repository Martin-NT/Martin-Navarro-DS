from circulo import Circulo
from cuadrado import Cuadrado
from lado import Lado
from puntos import Punto
from triangulo import Triangulo


p1 = Punto(0, 0)
p2 = Punto(1, 0)
p3 = Punto(0, 1)

lado1 = Lado(p1, p2)
lado2 = Lado(p2, p3)
lado3 = Lado(p3, p1)

triangulo = Triangulo()
triangulo.agregar_lado(lado1)
triangulo.agregar_lado(lado2)
triangulo.agregar_lado(lado3)
triangulo.dibujar()

cuadrado = Cuadrado()
cuadrado.dibujar()

circulo = Circulo()
circulo.dibujar()

print(triangulo)
print(triangulo.lados)
