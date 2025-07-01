from equilatero_factory import TrianguloEquilateroFactory
from escaleno_factory import TrianguloEscalenoFactory
from isosceles_factory import TrianguloIsoscelesFactory

def main():
    equilatero = TrianguloEquilateroFactory()
    escaleno = TrianguloEscalenoFactory()
    isosceles = TrianguloIsoscelesFactory()

    print(equilatero.crear_triangulo(3,3,3).get_description())
    print(equilatero.crear_triangulo(3,3,3).get_superficie())
    print(escaleno.crear_triangulo(3,4,5).get_description())
    print(escaleno.crear_triangulo(3,4,5).get_superficie())
    print(isosceles.crear_triangulo(4,4,5).get_description())
    print(isosceles.crear_triangulo(4,4,5).get_superficie())

if __name__ == "__main__":    
    main()