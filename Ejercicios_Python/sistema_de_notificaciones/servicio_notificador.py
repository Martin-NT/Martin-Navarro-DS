from notificacion import Notificacion

class ServicioNotificador:
    def notificar(self, mensaje, destinatario, canal: Notificacion):
        canal.enviar(mensaje, destinatario)
