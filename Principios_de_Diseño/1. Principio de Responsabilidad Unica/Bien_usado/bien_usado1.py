#Ahora cada clase tiene una sola responsabilidad: Report genera datos y PDFExporter maneja la exportación.

class Report:
    def generate(self):
        return "Este es el contenido del reporte."

class PDFExporter:
    def export(self, report: Report):
        print(f"Exportando a PDF: {report.generate()}")

# Prueba
report = Report()
exporter = PDFExporter()
exporter.export(report)
