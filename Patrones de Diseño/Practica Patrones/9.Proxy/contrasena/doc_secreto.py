class DocumentoSecreto:
    def __init__(self, contenido="Este es un documento secreto."):
        self.contenido = contenido

    def leer(self):
        print(f"Leyendo el contenido del documento: {self.contenido}")

    def escribir(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        print("Contenido del documento actualizado.")
