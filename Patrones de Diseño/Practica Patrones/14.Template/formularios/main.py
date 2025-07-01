from formulario_contacto import FormularioContacto
from formulario_reg import FormularioReg

def main():
    formulario_contacto = FormularioContacto()
    formulario_reg = FormularioReg()

    print("🧩 TEMPLATE METHOD: Formulario\n")

    print("===> Formulario de Contacto")
    formulario_contacto.crear_formulario()

    print("\n===> Formulario de Registro")
    formulario_reg.crear_formulario()

if __name__ == "__main__":
    main()
 