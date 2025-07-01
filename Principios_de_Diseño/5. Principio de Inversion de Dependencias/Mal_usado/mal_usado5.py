#"Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones."

#Esto significa que, en lugar de que las clases de alto nivel dependan directamente de implementaciones concretas, 
# deben depender de abstracciones (interfaces o clases base).

# ❌ Violación de DIP: la clase de alto nivel depende de una implementación concreta

class EmailService:
    def enviar_email(self, mensaje):
        print(f"📧 Enviando email: {mensaje}")

class GestorNotificaciones:
    def __init__(self):
        self.servicio_email = EmailService()  # ❌ Dependencia directa (mala práctica)

    def notificar(self, mensaje):
        self.servicio_email.enviar_email(mensaje)  # ❌ Acoplado solo a email

# 🔥 Prueba
gestor = GestorNotificaciones()
gestor.notificar("¡Hola, usuario!")  # 📧 Enviando email: ¡Hola, usuario!

#🚨 ¿Por qué esto es un problema?
# 🔴 GestorNotificaciones solo funciona con EmailService. Si queremos usar SMS o WhatsApp, tendríamos que modificar esta clase cada vez.
# 🔴 Al estar fuertemente acoplado a EmailService, no podemos cambiar la implementación fácilmente.

#✅ Solución: Aplicar DIP con una abstracción (Buen diseño)
#En lugar de depender directamente de EmailService, la clase GestorNotificaciones dependerá de una interfaz (Notificador) 
# que define el comportamiento común.