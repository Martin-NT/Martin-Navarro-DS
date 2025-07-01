from manejador_descuentos import ManejadorDescuentos

class DescuentoPorVolumen(ManejadorDescuentos):
    def aplicar_descuento(self,precio):
        if self.es_por_volumen:
            descuento = precio * 0.05
            precio -= descuento
            print(f"Descuento por volumen: Descuento de {descuento}% aplicado.")
        elif self.siguiente_manejador:
            self.siguiente_manejador.aplicar_descuento(precio)
        else:
            print(f"Descuento por volumen: No se puede aplicar el descuento de {precio}%.")
        return precio

    def es_por_volumen(self):
        return True