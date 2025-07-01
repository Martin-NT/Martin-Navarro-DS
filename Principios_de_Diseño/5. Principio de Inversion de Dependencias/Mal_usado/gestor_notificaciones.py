from email_service import EmailService

class GestorNotificaciones:
    def __init__(self):
        self.servicio_email = EmailService()  # ❌ Dependencia directa a una implementación concreta

    def notificar(self, mensaje):
        self.servicio_email.enviar_email(mensaje)  # Solo funciona con EmailService
