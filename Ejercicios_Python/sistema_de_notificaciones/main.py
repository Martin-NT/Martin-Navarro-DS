from canales.email import EmailNotificacion
from canales.sms import SMSNotificacion
from canales.whatsapp import WhatsappNotificacion
from servicio_notificador import ServicioNotificador

if __name__ == "__main__":
    servicio = ServicioNotificador()
    
    email = EmailNotificacion()
    sms = SMSNotificacion()
    whatsapp = WhatsappNotificacion()
    
    print("=== Ejecución de notificaciones ===")
    servicio.notificar("Hola!", "maria@mail.com", email)
    servicio.notificar("Hola!", "+54123456789", sms)
    servicio.notificar("Hola!", "Martina Rizzotti", whatsapp)

#MALA PRACTICA si tuviera constructor(__init__) a un canal fijo
"""servicio_email = ServicioNotificador(email)
servicio_sms = ServicioNotificador(sms)
servicio_whatsapp = ServicioNotificador(whatsapp)


servicio_email.notificar("Hola!", "maria@mail.com")
servicio_sms.notificar("Hola!", "+54123456789")
servicio_whatsapp.notificar("Hola!", "Martina Rizzotti")"""
