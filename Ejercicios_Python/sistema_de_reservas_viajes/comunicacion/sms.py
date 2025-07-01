from interfaces.notificador import Notificador

class Sms(Notificador):
    def notificar(self, mensaje, destinatario):
        print(f"--> Enviando SMS a {destinatario}")
        print(f"--> Mensaje: {mensaje}")