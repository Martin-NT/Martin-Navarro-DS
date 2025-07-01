from abc import ABC, abstractmethod

# Handler
class ManejadorSoporte(ABC):
    def __init__(self):
        self.siguiente = None

    def establecer_siguiente(self, manejador):
        self.siguiente = manejador
        return manejador

    @abstractmethod
    def manejar(self, problema):
        pass

# ConcreteHandlers
class SoporteBasico(ManejadorSoporte):
    def manejar(self, problema):
        if problema == "contraseña":
            print("Soporte Básico resolvió el problema de contraseña.")
        elif self.siguiente:
            self.siguiente.manejar(problema)

class SoporteTecnico(ManejadorSoporte):
    def manejar(self, problema):
        if problema == "error sistema":
            print("Soporte Técnico resolvió el problema de sistema.")
        elif self.siguiente:
            self.siguiente.manejar(problema)

class SoporteEspecializado(ManejadorSoporte):
    def manejar(self, problema):
        if problema == "fallo servidor":
            print("Soporte Especializado resolvió el problema del servidor.")
        elif self.siguiente == None:
            print("Problema no resuelto.")

if __name__ == "__main__":
    # Crear manejadores
    basico = SoporteBasico()
    tecnico = SoporteTecnico()
    especializado = SoporteEspecializado()

    # Armar la cadena
    basico.establecer_siguiente(tecnico).establecer_siguiente(especializado)

    # Solicitudes
    basico.manejar("contraseña")
    basico.manejar("error sistema")
    basico.manejar("fallo servidor")
    basico.manejar("problema desconocido")
