from interface.notificador import Notificador

class EmailService(Notificador):
    def enviar(self, mensaje):
        print(f"📧 Enviando email: {mensaje}")
