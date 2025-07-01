from estado_reproductor import EstadoReproductor

class EstadoPausado(EstadoReproductor):
    def reproducir(self, reproductor):
        print("\n▶️  Reanudando reproducción.")
        reproductor.cambiar_estado(reproductor.estado_reproduciendo)

    def pausar(self, reproductor):
        print("\n⚠️  Ya está pausado.")

    def detener(self, reproductor):
        print("\n⏹️  Deteniendo reproducción desde pausa.")
        reproductor.cambiar_estado(reproductor.estado_detenido)
