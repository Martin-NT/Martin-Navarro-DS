class ObjetoDeArte:
    def __init__(self, id_objeto, titulo, descripcion, artista, anio_creacion, pais, cultura, epoca):
        self.id_objeto = id_objeto
        self.titulo = titulo
        self.descripcion = descripcion
        self.artista = artista  
        self.anio_creacion = anio_creacion
        self.pais = pais
        self.cultura = cultura
        self.epoca = epoca

    def __repr__(self):
        return f"ObjetoDeArte({self.titulo}, Artista={self.artista.nombre}, Año={self.anio_creacion}, País={self.pais}, Cultura={self.cultura}, Época={self.epoca})"



