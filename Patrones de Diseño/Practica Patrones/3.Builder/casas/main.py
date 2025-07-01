from casa_builder import CasaBuilder

def main():
    builder = CasaBuilder()
    builder.set_habitaciones(10)
    builder.set_baños(2)
    builder.set_piscina(True)
    builder.set_jardin(True)

    casa = builder.build()
    casa.resumen()

if __name__ == "__main__":    
    main()