from notificacion import Notificacion

class WhatsappNotificacion(Notificacion):
    def enviar(self, mensaje, destinatario):
        print(f"[WhatsApp] Enviando a {destinatario}, mensaje: {mensaje}")
