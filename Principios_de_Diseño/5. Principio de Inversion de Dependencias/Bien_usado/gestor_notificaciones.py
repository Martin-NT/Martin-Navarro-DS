from interface.notificador import Notificador

class GestorNotificaciones:
    def __init__(self, servicio: Notificador):  # ✅ Depende de una abstracción
        self.servicio = servicio

    def notificar(self, mensaje):
        self.servicio.enviar(mensaje)
