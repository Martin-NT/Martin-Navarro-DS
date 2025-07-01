from manejador_descuentos import ManejadorDescuentos

class DescuentoTemporada(ManejadorDescuentos):
    def aplicar_descuento(self,precio):
        if self.es_temporada:
            descuento = precio * 0.1
            precio -= descuento
            print(f"Descuento temporado: Descuento de {descuento}% aplicado.")
        elif self.siguiente_manejador:
            self.siguiente_manejador.aplicar_descuento(precio)
        else:
            print(f"Descuento temporado: No se puede aplicar el descuento de {precio}%.")
        return precio

    def es_temporada(self):
        return True