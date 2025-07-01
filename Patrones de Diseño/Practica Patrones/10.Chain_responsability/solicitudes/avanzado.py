from manejador_soporte import ManejadorSoporte

class ManejadorAvanzado(ManejadorSoporte):
    def manejar_solicitud(self,complejidad):
        if 4 < complejidad <= 6:
            print(f"Manejador avanzado: Procesando solicitud de complejidad {complejidad}...")
        elif self.siguiente_manejador:
            self.siguiente_manejador.manejar_solicitud(complejidad)
        else:
            print(f"Manejador avanzado: No se puede manejar la solicitud de complejidad {complejidad}.")