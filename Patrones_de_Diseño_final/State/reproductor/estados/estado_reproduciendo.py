from estado_reproductor import EstadoReproductor

class EstadoReproduciendo(EstadoReproductor):
    def reproducir(self, reproductor):
        print("\n▶️  Ya se está reproduciendo.")

    def pausar(self, reproductor):
        print("\n⏸️  Pausando reproducción.")
        reproductor.cambiar_estado(reproductor.estado_pausado)

    def detener(self, reproductor):
        print("\n⏹️  Deteniendo reproducción.")
        reproductor.cambiar_estado(reproductor.estado_detenido)
        
    def avanzar_cancion(self, reproductor):
        print("\n⏭️  Avanzando canción...")
        print("\n🎵 Reproduciendo siguiente canción")

    def retroceder_cancion(self, reproductor):
        print("\n⏮️  Retrocediendo canción...")
        print("\n🎵 Reproduciendo canción anterior")
