from manejador_soporte import ManejadorSoporte

class ManejadorTecnico(ManejadorSoporte):
    def manejar_solicitud(self,complejidad):    
        if 2 < complejidad <= 4:
            print(f"Manejador tecnico: Procesando solicitud de complejidad {complejidad}...")
        elif self.siguiente_manejador:
            self.siguiente_manejador.manejar_solicitud(complejidad)
        else:
            print(f"Manejador tecnico: No se puede manejar la solicitud de complejidad {complejidad}.")