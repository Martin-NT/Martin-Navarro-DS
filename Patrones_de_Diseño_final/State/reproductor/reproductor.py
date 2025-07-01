from estados.estado_detenido import EstadoDetenido
from estados.estado_pausado import EstadoPausado
from estados.estado_reproduciendo import EstadoReproduciendo

class Reproductor:
    def __init__(self):
        # Estados posibles
        self.estado_reproduciendo = EstadoReproduciendo()
        self.estado_pausado = EstadoPausado()
        self.estado_detenido = EstadoDetenido()

        # Estado inicial
        self.estado_actual = self.estado_detenido

    def cambiar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado

    def reproducir(self):
        self.estado_actual.reproducir(self)

    def pausar(self):
        self.estado_actual.pausar(self)

    def detener(self):
        self.estado_actual.detener(self)
        
    def avanzar_cancion(self):
        self.estado_actual.avanzar_cancion(self)

    def retroceder_cancion(self):
        self.estado_actual.retroceder_cancion(self)