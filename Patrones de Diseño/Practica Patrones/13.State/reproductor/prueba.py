from reproductor import Reproductor

def main():
    reproductor = Reproductor()
    
    reproductor.reproducir()
    reproductor.avanzar_cancion()
    
    reproductor.pausar()
    reproductor.retroceder_cancion()
    
    reproductor.reproducir()
    reproductor.detener()
    reproductor.detener()

if __name__ == "__main__":
    main()