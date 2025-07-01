from interface.notificador import Notificador

class SMSService(Notificador):
    def enviar(self, mensaje):
        print(f"💬 Enviando SMS: {mensaje}")
