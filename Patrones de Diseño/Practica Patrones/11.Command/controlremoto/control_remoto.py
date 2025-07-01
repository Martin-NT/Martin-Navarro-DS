class ControlRemoto:
    def __init__(self):
        self.comando_actual = None

    def asignar_comando(self, comando):
        self.comando_actual = comando

    def presionar_boton(self):
        if self.comando_actual:
            self.comando_actual.ejecutar()
        else:
            print("No hay ningún comando ejecutándose")

    def presionar_boton_deshacer(self):
        if self.comando_actual:
            self.comando_actual.deshacer()
        else:
            print("No hay ningún comando deshaciendo")