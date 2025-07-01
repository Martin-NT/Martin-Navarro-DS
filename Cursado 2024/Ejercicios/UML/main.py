from cooperativa import Cooperativa
from lote import Lote
from cereal import GranosGruesos,GranosFinos,Pasturas
from mineral import Mineral

def main():
    mineral1 = Mineral("Cobre","Primario")
    mineral2 = Mineral("Plata","Secundario")
    mineral3 = Mineral("Potasio","Secundario")

    maiz = GranosGruesos("Maiz",[mineral1,mineral2])
    trigo = GranosFinos("Trigo",[mineral2])
    alfalfa = Pasturas("Alfalfa",[mineral1,mineral3])

    lote1 = Lote(1,"Especial",[mineral1,mineral2,mineral3])

    cooperativa = Cooperativa("Cooperativa de Cereales")
    cooperativa.agregar_lote(lote1)

    sugerencia = cooperativa.sugerir_cereal(lote1,[maiz,trigo,alfalfa])
    if sugerencia:
        print(f"Se recomienda el cereal {sugerencia.nombre} para el lote {lote1.id}.")
    else:
        print("No se puede sugerir ningún cereal.")

if __name__ == "__main__":
    main()  