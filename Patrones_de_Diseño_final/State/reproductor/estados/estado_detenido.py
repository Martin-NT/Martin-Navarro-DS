from estado_reproductor import EstadoReproductor

class EstadoDetenido(EstadoReproductor):
    def reproducir(self, reproductor):
        print("\n▶️  Iniciando reproducción.")
        reproductor.cambiar_estado(reproductor.estado_reproduciendo)

    def pausar(self, reproductor):
        print("\n⚠️  No se puede pausar. Está detenido.")

    def detener(self, reproductor):
        print("\n⚠️  Ya está detenido.")
        
    def avanzar_cancion(self, reproductor):
        print("\n⚠️  No se puede avanzar. Está detenido.")

    def retroceder_cancion(self, reproductor):
        print("\n⚠️  No se puede retroceder. Está detenido.")
