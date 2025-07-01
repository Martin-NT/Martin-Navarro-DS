from controlador_impresoras import ControladorImpresoras

def main():
    controlador = ControladorImpresoras()

    # Agregar impresoras
    controlador.agregar_impresora("HP LaserJet 1010")
    controlador.agregar_impresora("Canon PIXMA MG2500")
    controlador.agregar_impresora("Epson EcoTank L3110")

    # Listar impresoras
    controlador.listar_impresoras()

    # Imprimir un documento
    print("\nEstado antes de imprimir en 'HP LaserJet 1010':")
    controlador.verificar_estado("HP LaserJet 1010")

    controlador.imprimir("HP LaserJet 1010", "ReporteAnual.pdf")

    print("\nEstado después de imprimir en 'HP LaserJet 1010':")
    controlador.verificar_estado("HP LaserJet 1010")

    # Verificar estado de otra impresora
    controlador.verificar_estado("Canon PIXMA MG2500")

    # Intentar imprimir en una impresora (que debería estar disponible)
    print("\nIntentando imprimir en 'HP LaserJet 1010' nuevamente:")
    controlador.imprimir("HP LaserJet 1010", "DocumentoUrgente.docx")

    print("\nEstado después de segunda impresión en 'HP LaserJet 1010':")
    controlador.verificar_estado("HP LaserJet 1010")

    # Verificar estado de una impresora no registrada (aquí da error porque no existe)
    print("\nVerificando estado de impresora no registrada:")
    controlador.verificar_estado("HP LaserJet 1012")

if __name__ == "__main__":
    main()
