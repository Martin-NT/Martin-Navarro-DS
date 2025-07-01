from interfaces.notificador import Notificador

class Email(Notificador):
    def notificar(self, mensaje, destinatario):
        print(f"--> Enviando email a {destinatario}")
        print(f"--> Mensaje: {mensaje}")