from interface.notificador import Notificador

class WhatsAppService(Notificador):
    def enviar(self, mensaje):
        print(f"📱 Enviando WhatsApp: {mensaje}")
