from abc import ABC, abstractmethod

class CreadorFormulario(ABC):
    def crear_formulario(self):
        print("\n🧾 Creando formulario...")
        self.agregar_campos()
        if self.validar_datos():
            self.enviar_formulario()
        else:
            print("❌ Error: los datos no son válidos.")

    @abstractmethod
    def agregar_campos(self):
        pass

    @abstractmethod
    def validar_datos(self):
        pass

    @abstractmethod
    def enviar_formulario(self):
        pass
