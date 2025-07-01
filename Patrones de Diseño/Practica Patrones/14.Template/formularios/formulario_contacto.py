from creador_formulario import CreadorFormulario

class FormularioContacto(CreadorFormulario):
    def agregar_campos(self):
        print("📝 Agregando campos: Nombre, Email, Mensaje.")

    def validar_datos(self):
        print("🔍 Validando datos del formulario de contacto...")
        return True

    def enviar_formulario(self):
        print("📨 Enviando formulario de contacto.")
