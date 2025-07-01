from servicios.email_service import EmailService
from servicios.sms_service import SMSService
from servicios.whatsapp_service import WhatsAppService
from gestor_notificaciones import GestorNotificaciones

if __name__ == "__main__":
    email = GestorNotificaciones(EmailService())
    sms = GestorNotificaciones(SMSService())
    whatsapp = GestorNotificaciones(WhatsAppService())

    email.notificar("¡Hola, usuario por Email!")
    sms.notificar("¡Hola, usuario por SMS!")
    whatsapp.notificar("¡Hola, usuario por WhatsApp!")
