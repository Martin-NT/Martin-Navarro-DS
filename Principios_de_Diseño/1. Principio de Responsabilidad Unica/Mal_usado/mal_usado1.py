# Una clase debe tener una única razón para cambiar.
#Si una clase maneja múltiples responsabilidades, los cambios en una pueden afectar a la otra,
# dificultando el mantenimiento.

# Aquí la clase Report tiene dos responsabilidades: generar el reporte y exportarlo a archivo PDF.

class Report:
    def generate(self):
        return "Este es el contenido del reporte."

    def export_to_pdf(self):
        print("Exportando a PDF...")
