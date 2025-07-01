from cereal import Cereal
from cooperativa import Cooperativa
from lote import Lote


lote1 = Lote("Lote 1", ["Nitrógeno", "Fósforo", "Potasio"])
lote2 = Lote("Lote 2", ["Calcio", "Magnesio", "Azufre", "Potasio"])

maiz = Cereal("Maíz", "Cosecha Gruesa", ["Nitrógeno", "Fósforo", "Potasio"])
trigo = Cereal("Trigo", "Cosecha Fina", ["Nitrógeno", "Fósforo"])
alfalfa = Cereal("Alfalfa", "Pastura", ["Nitrógeno", "Calcio", "Potasio"])

cooperativa = Cooperativa()
cooperativa.agregar_lote(lote1)
cooperativa.agregar_lote(lote2)
cooperativa.agregar_cereal(maiz)
cooperativa.agregar_cereal(trigo)
cooperativa.agregar_cereal(alfalfa)

lote1.agregar_siembra("Pastura")

print("Sugerencias para Lote 1:")
for cereal in cooperativa.sugerir_cereales(lote1):
    print(cereal)
print("\nSugerencias para Lote 2:")
for cereal in cooperativa.sugerir_cereales(lote2):
    print(cereal)