from abc import ABC, abstractmethod

# Interfaz Mediator
class Mediator(ABC):
    @abstractmethod
    def notificar(self, remitente, evento: str):
        pass

# Clase base para los componentes (colegas)
class ComponenteBase:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    def setMediator(self, mediator: Mediator):
        self._mediator = mediator

class ComponenteA(ComponenteBase):
    def hacer_algo_a(self):
        print("ComponenteA hace algo A.")
        if self._mediator:
            self._mediator.notificar(self, "A")

    def accion_extra_a(self):
        print("ComponenteA realiza acción extra sin notificar.")

class ComponenteB(ComponenteBase):
    def hacer_algo_b(self):
        print("ComponenteB hace algo B.")
        if self._mediator:
            self._mediator.notificar(self, "B")

    def accion_extra_b(self):
        print("ComponenteB realiza acción extra sin notificar.")


# Implementación concreta del Mediator
class MediadorConcreto(Mediator):
    def __init__(self, comp_a: ComponenteA, comp_b: ComponenteB):
        self._comp_a = comp_a
        self._comp_b = comp_b
        self._comp_a.setMediator(self)
        self._comp_b.setMediator(self)

    def notificar(self, remitente, evento: str):
        if evento == "A":
            print("Mediator: manejando evento A → realizando acción en B sin notificar de nuevo")
            self._comp_b.accion_extra_b()
        elif evento == "B":
            print("Mediator: manejando evento B → realizando acción en A sin notificar de nuevo")
            self._comp_a.accion_extra_a()



# Ejemplo de uso
if __name__ == "__main__":
    comp_a = ComponenteA()
    comp_b = ComponenteB()
    mediator = MediadorConcreto(comp_a, comp_b)

    print("Cliente activa A:")
    comp_a.hacer_algo_a()

    print("\nCliente activa B:")
    comp_b.hacer_algo_b()
