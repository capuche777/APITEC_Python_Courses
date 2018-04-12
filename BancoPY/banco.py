option = input("Bienvenido a PyCoin\n Escoja una de las siguientes opciones para acceder\n\n1 - Apertura de Cuenta\n2 - Deposito a Cuenta\n3 - Retiro de Cuenta\n4 - Convertir Saldo a Dolares/Quetzales\n\n0 - Salir\n")

def Main_Menu(option):
    if option == "1":
        Cuenta_Apertura()
    elif option == "2":
        Cuenta_Deposito()
    elif option == "3":
        Cuenta_Retiro()
    elif option == "4":
        Cuenta_Exchange()
    elif option == "0":
        print("Gracias por visitar PyCoin\n\nEsperamos que vuelva")
    else:
        print("Por favor seleccione una opción")
        option = print("Bienvenido a PyCoin\n Escoja una de las siguientes opciones para acceder\n\n1 - Apertura de Cuenta\n2 - Deposito a Cuenta\n3 - Retiro de Cuenta\n4 - Convertir Saldo a Dolares/Quetzales\n\n0 - Salir")
        Main_Menu(option)