from objetodearte import ObjetoDeArte


class Escultura(ObjetoDeArte):
    def __init__(self, id_objeto, titulo, descripcion, artista, anio_creacion, pais, cultura, epoca, material, altura, peso, estilo):
        super().__init__(id_objeto, titulo, descripcion, artista, anio_creacion, pais, cultura, epoca)
        self.material = material
        self.altura = altura
        self.peso = peso
        self.estilo = estilo

    def __repr__(self):
        return super().__repr__() + f", Escultura(Material={self.material}, Altura={self.altura}, Peso={self.peso}, Estilo={self.estilo})"
