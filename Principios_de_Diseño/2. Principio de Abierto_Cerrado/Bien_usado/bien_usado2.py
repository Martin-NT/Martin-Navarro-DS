from abc import ABC, abstractmethod
# Podemos agregar nuevos métodos de pago sin modificar PaymentProcessor, cumpliendo OCP. 

class PaymentMethod(ABC):
    @abstractmethod # Usa @abstractmethod para obligar a las subclases a implementar pay().
    def pay(self): 
        pass #NO tiene implementación del método pay(), solo define que todas las subclases deben tenerlo.
    
#Clases Concretas
# ✅ Cada clase representa un método de pago diferente.
# ✅ Todas heredan de PaymentMethod y definen su propia implementación de pay().

class CreditCardPayment(PaymentMethod):
    def pay(self):
        print("Pagando con tarjeta de crédito")

class MPPayment(PaymentMethod):
    def pay(self):
        print("Pagando con Mercado Pago")

class BitcoinPayment(PaymentMethod):  # ¡Nuevo método sin modificar PaymentProcessor!
    def pay(self):
        print("Pagando con Bitcoin")
        
class PaymentProcessor:
    def process_payment(self, payment: PaymentMethod):
        payment.pay()

# Uso
processor = PaymentProcessor()
processor.process_payment(CreditCardPayment())  
processor.process_payment(MPPayment())  
processor.process_payment(BitcoinPayment())

# 🎯 ¿Por qué este diseño cumple con OCP?
# ✅ Abierto a la extensión: Si agregamos más métodos de pago, solo creamos una nueva clase sin modificar PaymentProcessor.
# ✅ Cerrado a la modificación: PaymentProcessor no cambia al agregar nuevos pagos, evitando errores en código existente.