#Las subclases deben poder reemplazar a su clase base sin alterar el comportamiento esperado del programa.
#En otras palabras, si una clase B hereda de A, deberíamos poder usar B en lugar de A sin que el código falle.

#👀 Problema: Cuadrado hereda de Rectángulo
#En este caso, Cuadrado hereda de Rectángulo, pero no mantiene el comportamiento esperado de un rectángulo. 
#El área de un cuadrado no debe depender de su base y altura independientemente, sino que ambos son iguales, lo que altera la lógica.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):  # Cuadrado hereda de Rectángulo, pero rompe su comportamiento
    def __init__(self, lado):
        super().__init__(lado, lado)  # Usa base y altura iguales, pero cambia la lógica de la clase base

    def area(self):
        # Aquí estamos alterando el comportamiento original, porque la clase base debería calcular área usando base y altura independientes
        return self.base * self.base  # Aunque esto es correcto para un cuadrado, altera la lógica de Rectángulo

# 🔥 Prueba
def print_area(figura: Rectangulo):  # Espera un Rectángulo
    print(f"Área del rectángulo: {figura.area()}")

# Prueba con un rectángulo normal
rect = Rectangulo(4, 5)
print_area(rect)  # ✅ Área del rectángulo: 20

# Prueba con un cuadrado
cuadrado = Cuadrado(4)  # Ahora Cuadrado debería funcionar bien, pero al heredar de Rectángulo, cambia su lógica
print_area(cuadrado)  # 🚨 Área del rectángulo: 16, lo cual es incorrecto ya que se esperaba un comportamiento de rectángulo


#🚨 ¿Por qué este código viola LSP?
#🔴 Cuadrado cambia el comportamiento de Rectangulo porque fuerza a la base y la altura a ser iguales.
#🔴 Si usamos Cuadrado donde se espera un Rectangulo, el código falla porque el cálculo del área no es el esperado.
#🔴 Solución: Cuadrado y Rectangulo no deberían tener relación de herencia.

#✅ Solución (Cómo corregirlo y evitar la violación de LSP)
# La mejor solución es que Rectángulo y Cuadrado no deberían estar en una relación de herencia. 
# En su lugar, deberían implementar una interfaz común (como Forma), de modo que no dependan de la misma base, pero sí de un contrato común para calcular el área.

#🎯 Conclusión
#El mal uso de LSP ocurre cuando la subclase cambia la lógica de la clase base, lo que puede causar comportamientos 
# inesperados al sustituir la clase base por la subclase.
#Evitar que Cuadrado herede de Rectángulo y crear una interfaz común como Forma es una forma de asegurar que 
# el comportamiento de cada clase se mantenga consistente y predecible.