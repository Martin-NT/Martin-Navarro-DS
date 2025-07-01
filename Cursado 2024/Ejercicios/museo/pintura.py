from objetodearte import ObjetoDeArte


class Pintura(ObjetoDeArte):
    def __init__(self, id_objeto, titulo, descripcion, artista, anio_creacion, pais, cultura, epoca, tipo, soporte, estilo):
        super().__init__(id_objeto, titulo, descripcion, artista, anio_creacion, pais, cultura, epoca)
        self.tipo = tipo
        self.soporte = soporte
        self.estilo = estilo
        

    def __repr__(self):
        return super().__repr__() + f", Pintura(Tipo={self.tipo}, Soporte={self.soporte}, Estilo={self.estilo})"
