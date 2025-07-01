from basico import ManejadorBasico
from tecnico import ManejadorTecnico
from avanzado import ManejadorAvanzado

def main():
    manejador_basico = ManejadorBasico()
    manejador_tecnico = ManejadorTecnico()
    manejador_avanzado = ManejadorAvanzado()

    manejador_basico.set_siguiente(manejador_tecnico)
    manejador_tecnico.set_siguiente(manejador_avanzado)

    # Realizar pruebas de manejo de solicitudes
    niveles = [1, 2, 3, 4, 5]
    for nivel in niveles:
        print(f"\nSolicitud de nivel de complejidad {nivel}:")
        manejador_basico.manejar_solicitud(nivel)

if __name__ == "__main__":
    main()  