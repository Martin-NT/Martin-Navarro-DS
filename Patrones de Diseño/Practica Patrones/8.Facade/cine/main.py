from facade_cine import FacadeCine

def main():
    print("🎉 Bienvenido al sistema de Cine en Casa 🎉")
    input("🎞️  Presiona Enter cuando para iniciar la película...")
    cine = FacadeCine()
    cine.iniciar_pelicula(volumen=15)
    input("🎞️  Presiona Enter cuando termine la película...")
    cine.finalizar_pelicula()

if __name__ == "__main__":
    main()
