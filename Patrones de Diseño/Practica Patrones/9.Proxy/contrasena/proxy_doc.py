from doc_secreto import DocumentoSecreto

class ProxyDocumentoSecreto:
    def __init__(self, contraseña):
        self.documento = DocumentoSecreto()
        self.contraseña = contraseña
        self.intentos_fallidos = 0
        self.bloqueado = False

    def _verificar_acceso(self):
        if self.bloqueado:
            print("Acceso denegado: el sistema está bloqueado debido a múltiples intentos fallidos.")
            return False

        ingreso = input("Ingrese la contraseña: ")
        if ingreso == self.contraseña:
            self.intentos_fallidos = 0
            return True
        else:
            self.intentos_fallidos += 1
            print("Contraseña incorrecta.")
            if self.intentos_fallidos >= 3:
                self.bloqueado = True
                print("Acceso bloqueado después de 3 intentos fallidos.")
            return False

    def leer(self):
        if self._verificar_acceso():
            self.documento.leer()

    def escribir(self, nuevo_contenido):
        if self._verificar_acceso():
            self.documento.escribir(nuevo_contenido)

    def cambiar_contraseña(self, contraseña_actual, nueva_contraseña):
        if contraseña_actual == self.contraseña:
            self.contraseña = nueva_contraseña
            self.intentos_fallidos = 0
            self.bloqueado = False
            print("Contraseña actualizada con éxito.")
        else:
            print("Error: Contraseña actual incorrecta.")
