from notificacion import Notificacion

class SMSNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        print(f"[SMS] Enviando a {destinatario}, mensaje: {mensaje}")
