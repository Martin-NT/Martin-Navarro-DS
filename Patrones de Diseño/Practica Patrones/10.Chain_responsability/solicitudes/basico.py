from manejador_soporte import ManejadorSoporte

class ManejadorBasico(ManejadorSoporte):
    def manejar_solicitud(self,complejidad):
        if complejidad <= 2:
            print(f"Manejador basico: Procesando solicitud de complejidad {complejidad}...")
        elif self.siguiente_manejador:
            self.siguiente_manejador.manejar_solicitud(complejidad)
        else:
            print(f"Manejador basico: No se puede manejar la solicitud de complejidad {complejidad}.")