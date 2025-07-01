# main.py
from computadora_builder import ComputadoraBuilder
from director import Director

def main():
    # Crear un ConcreteBuilder
    builder = ComputadoraBuilder()
    
    # Crear un Director y pasarle el builder
    director = Director(builder)
    
    # Construir la computadora utilizando el Director
    computadora = director.construir_computadora()
    
    # Mostrar la configuración de la computadora construida
    computadora.mostrar_configuracion()

if __name__ == "__main__":
    main()
