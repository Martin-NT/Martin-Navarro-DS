# Memento 
class Memento:
    def __init__(self, texto):
        self._estado = texto  # estado interno

    def get_estado(self):
        return self._estado

#  Originador 
class EditorTexto:
    def __init__(self):
        self._contenido = ""

    def set_estado(self, texto):
        self._contenido += texto

    def mostrar(self):
        print(f"Contenido actual: {self._contenido}")

    def guardar(self):
        return Memento(self._contenido)

    def restaurar(self, memento):
        self._contenido = memento.get_estado()

# Cuidador 
class Historial:
    def __init__(self):
        self._mementos = []

    def guardar_estado(self, memento):
        self._mementos.append(memento)

    def deshacer(self):
        if self._mementos:
            return self._mementos.pop()
        return None

# Cliente 
def cliente():
    editor = EditorTexto()
    historial = Historial()

    editor.set_estado("Hola")
    historial.guardar_estado(editor.guardar())

    editor.set_estado(" mundo")
    historial.guardar_estado(editor.guardar())

    editor.set_estado(" cruel")
    editor.mostrar()  # Hola mundo cruel

    print("Deshaciendo último cambio...")
    estado_anterior = historial.deshacer()
    if estado_anterior:
        editor.restaurar(estado_anterior)
    editor.mostrar()  # Hola mundo

# Ejecutar 
if __name__ == "__main__":
    cliente()
