import time
from reproductorDVD import ReproductorDVD
from sistema_sonido import SistemaSonido
from television import Television

class FacadeCine:
    def __init__(self):
        self.television = Television()
        self.reproductorDVD = ReproductorDVD()
        self.sistemaSonido = SistemaSonido()
        self.tiempo_inicio = None

    def iniciar_pelicula(self, volumen=10):
        print("\n🎬 Preparando todo para ver la película...\n")
        time.sleep(1)

        self.television.encender()
        time.sleep(1)

        self.reproductorDVD.encender()
        time.sleep(1)

        self.sistemaSonido.encender()
        time.sleep(1)

        self.sistemaSonido.volumen(volumen)
        time.sleep(1)

        print("▶️  Iniciando la reproducción...\n")
        self.reproductorDVD.reproducir()
        self.tiempo_inicio = time.time()

    def finalizar_pelicula(self):
        print("\n🛑 Finalizando la sesión de cine...\n")
        time.sleep(1)

        self.reproductorDVD.detener()
        time.sleep(1)

        self.reproductorDVD.apagar()
        time.sleep(1)

        self.sistemaSonido.apagar()
        time.sleep(1)

        self.television.apagar()
        time.sleep(1)

        if self.tiempo_inicio:
            duracion = time.time() - self.tiempo_inicio
            print(f"\n📽️  Tiempo total de reproducción: {duracion:.2f} segundos")
        
        print("👋 Cine finalizado. ¡Gracias por usar el sistema!\n")
