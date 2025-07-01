from notificacion import Notificacion

class EmailNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        print(f"[Email] Enviando a {destinatario}, mensaje: {mensaje}")
