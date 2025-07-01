from abc import ABC, abstractmethod

# 🔹 Interfaz (abstracción) para cualquier tipo de notificación
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# ✅ Implementación concreta de Email
class EmailService(Notificador):
    def enviar(self, mensaje):
        print(f"📧 Enviando email: {mensaje}")

# ✅ Implementación concreta de SMS
class SMSService(Notificador):
    def enviar(self, mensaje):
        print(f"💬 Enviando SMS: {mensaje}")

# ✅ Implementación concreta de WhatsApp
class WhatsAppService(Notificador):
    def enviar(self, mensaje):
        print(f"📱 Enviando WhatsApp: {mensaje}")

# ✅ La clase de alto nivel ahora depende de la abstracción, NO de una implementación concreta
class GestorNotificaciones:
    def __init__(self, servicio: Notificador):  # Inyectamos una abstracción
        self.servicio = servicio

    def notificar(self, mensaje):
        self.servicio.enviar(mensaje)  # Se puede cambiar la implementación sin modificar esta clase

# 🔥 Prueba con distintas implementaciones
email_notificador = GestorNotificaciones(EmailService())
sms_notificador = GestorNotificaciones(SMSService())
whatsapp_notificador = GestorNotificaciones(WhatsAppService())

email_notificador.notificar("¡Hola, usuario por Email!")  # 📧 Enviando email: ¡Hola, usuario por Email!
sms_notificador.notificar("¡Hola, usuario por SMS!")      # 💬 Enviando SMS: ¡Hola, usuario por SMS!
whatsapp_notificador.notificar("¡Hola, usuario por WhatsApp!")  # 📱 Enviando WhatsApp: ¡Hola, usuario por WhatsApp!

#🎯 ¿Por qué ahora cumple con DIP?
# ✅ GestorNotificaciones ya no depende de EmailService, sino de una abstracción (Notificador).
# ✅ Podemos agregar nuevas formas de notificación (SMS, WhatsApp) sin cambiar GestorNotificaciones.
# ✅ Ahora el código es más flexible, reutilizable y fácil de mantener.

#🚀 Resumen del principio DIP
# ❌ Mal diseño: La clase de alto nivel (GestorNotificaciones) depende directamente de una implementación concreta (EmailService).
# ✅ Buen diseño: La clase de alto nivel depende de una abstracción (Notificador), lo que permite cambiar implementaciones sin modificar el código principal.

