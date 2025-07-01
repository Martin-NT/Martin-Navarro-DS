from reporte import Report
from exportar_pdf import PDFExporter

if __name__ == "__main__":
    reporte = Report()
    contenido = reporte.generate()

    exportador = PDFExporter()
    exportador.export(contenido)
