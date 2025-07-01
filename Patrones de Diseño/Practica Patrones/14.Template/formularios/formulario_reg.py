from creador_formulario import CreadorFormulario

class FormularioReg(CreadorFormulario):
    def agregar_campos(self):
        print("📝 Agregando campos: Usuario, Contraseña, Email.")

    def validar_datos(self):
        print("🔍 Validando datos del formulario de registro...")
        return True

    def enviar_formulario(self):
        print("📨 Enviando formulario de registro.")
