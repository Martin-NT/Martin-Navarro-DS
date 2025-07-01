# Las clases deben estar abiertas a la extensión, pero cerradas a la modificación.

# Si cada vez que agregamos un método de pago modificamos PaymentProcessor, romperemos el código existente.

class PaymentProcessor:
    def process_payment(self, payment_type):
        if payment_type == "credit_card":
            print("Pagando con tarjeta de crédito")
        elif payment_type == "mercado_pago":
            print("Pagando con Mercado Pago")

processor = PaymentProcessor()
processor.process_payment("credit_card")
