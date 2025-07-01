from cliente import Cliente
from empresa import Empresa
from lider import Lider
from producto import Producto
from representante import Representante
from venta import Venta


empresa = Empresa("Cosmética Natural")

# Crear productos
crema = Producto("Crema Facial", 100)
shampoo = Producto("Shampoo Orgánico", 50)
empresa.agregar_producto(crema)
empresa.agregar_producto(shampoo)

# Crear clientes
cliente1 = Cliente("Juan Pérez", "Calle Falsa 123", "123456789", "2023-01-15")
cliente2 = Cliente("María García", "Avenida Siempre Viva", "987654321", "2023-02-01")

# Crear líder y vendedores
lider = Lider("Pedro González", "Boulevard Central", "741258963", "1980-10-10", "20123456789", "2010-05-01", "2015-07-20")
vendedor1 = Representante("Ana López", "Calle Verde 456", "852369741", "1992-07-15", "30123456789", "2020-08-10")
lider.agregar_vendedor(vendedor1)

# Registrar clientes
lider.agregar_cliente(cliente1)
vendedor1.agregar_cliente(cliente2)

# Registrar ventas
venta1 = Venta("2023-11-10", crema, 100, cliente1)
venta2 = Venta("2023-11-15", shampoo, 50, cliente2)
lider.registrar_venta(venta1)
vendedor1.registrar_venta(venta2)

# Agregar representantes a la empresa
empresa.agregar_representante(lider)
empresa.agregar_representante(vendedor1)

# Calcular comisiones
porcentaje_comision = 10  
print(f"Comisión Líder: {lider.calcular_comision(porcentaje_comision)}")
print(f"Comisión Vendedor: {vendedor1.calcular_comision(porcentaje_comision)}")

# Mostrar datos
print(empresa)
print(lider)
print(vendedor1)