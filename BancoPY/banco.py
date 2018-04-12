cuenta = {
    'nombre': "",
    'apellido': "",
    'dpi': "",
    'pin': "",
    'tipo': "",
    'moneda': "",
    'monto_saldo': "",
    'monto_retirado': ""
}

def Main_Menu():
    option = input("Bienvenido a PyCoin\n Escoja una de las siguientes opciones para acceder\n\n1 - Apertura de Cuenta\n2 - Deposito a Cuenta\n3 - Retiro de Cuenta\n4 - Convertir Saldo a Dolares/Quetzales\n\n0 - Salir\n")
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
        print("La opción solicitada no existe\nPor favor seleccione una opción\n\n")
        option = print("Bienvenido a PyCoin\n Escoja una de las siguientes opciones para acceder\n\n1 - Apertura de Cuenta\n2 - Deposito a Cuenta\n3 - Retiro de Cuenta\n4 - Convertir Saldo a Dolares/Quetzales\n\n0 - Salir")
        Main_Menu()

# Funcion que maneja en general la apertura de cuenta
#Funcion encargada de solicitar datos de usuario:
def Cuenta_Apertura():
    cuenta['nombre'] = input('Ingrese nombre de usuario: ')
    cuenta['apellido'] = input('Ingrese apellido de usuario: ')

    dpi = input('Ingrese el DPI del usuario: ')
    Validar_DPI(dpi)

    pin = input('Ingrese un numero de PIN (4 Digitos): ')
    Validar_pin(pin)
    
    # Se ha creado una serie de if, elif para determinar el ingreso del usuario, si prefiere ingresar numericamente el tipo de cuenta o por medio de strings
    tipo = input('Que tipo de cuenta desea aperturar: \n1 - Cuenta Clasica\n2 - Cuenta Ahorro\n3 - Cuenta Preferente\n')
    Clasificar_Cuenta(tipo)
    
    moneda = input('Ingrese Tipo de moneda: \n1 - Quetzales\n2 - Dolares\n')
    Asignar_Moneda(moneda)
    
    print("La cuenta se ha aperturado con éxito, los datos son:\nNombre Completo: " + cuenta['nombre'] + " " + cuenta['apellido'] + "\nNumero de DPI: " + cuenta['dpi'] + "\nTipo de cuenta: " + cuenta['tipo'] + "\nMoneda: " + cuenta['moneda'] + "\nPIN: " + cuenta['pin'] + "\nSaldo de cuenta: " + cuenta['moneda'] + cuenta['monto_saldo'] + "\n\n\n")
    Main_Menu()

# Funcion encargada de validar el DPI del usuario
def Validar_DPI(dpi):
    if len(dpi) != 13:
        print('El DPI debe tener 13 digitos')
        dpi = input('Ingrese el DPI del usuario: ')
        Validar_DPI(dpi)
    else:
        cuenta['dpi'] = dpi

# Funcion para validar el PIN del usuario, este debe tener 4 digitos
def Validar_pin(pin):
    if len(pin) != 4:
        print('El PIN debe tener 4 digitos')
        pin = input('El usuario debe digitar un PIN: ')
        Validar_pin(pin)
    else:
        cuenta['pin'] = pin
    

# Funcion encargada de determinar el tipo de cuenta que el cliente está aperturando
def Clasificar_Cuenta(tipo):
    if tipo == "1" or tipo == "cuenta clasica" or tipo == "Cuenta Clasica":
        cuenta['tipo'] = "Cuenta Clasica"
    elif tipo == "2" or tipo == "cuenta ahorro" or tipo == "Cuenta Ahorro":
        cuenta['tipo'] = "Cuenta Ahorro"
    elif tipo == "3" or tipo == "cuenta preferente" or tipo == "Cuenta Preferente":
        cuenta['tipo'] = "Cuenta Preferente"
    else:
        print('Por favor seleccione una de las cuentas disponibles.')
        tipo = input('Que tipo de cuenta desea aperturar: \n1 - Cuenta Clasica\n2 - Cuenta Ahorro\n3 - Cuenta Preferente\n')
        Clasificar_Cuenta(tipo)

# Funcion encargada de asignar la moneda 
def Asignar_Moneda(moneda):
    if moneda == "1" or  moneda == "Quetzales" or moneda == "quetzales":
        cuenta['moneda'] = "Q"
        monto = input("Ingrese el monto de apertura: \n1 - Q100.00\n2 - Q200.00\n3 - Q500.00\n4 - Q1000.00\n")
        Monto_Apertura_Quetzales(monto)
    elif moneda == "2" or moneda == "Dolares" or moneda == "dolares":
        cuenta['moneda'] = "$"
        monto = input("Ingrese el monto de apertura: \n1 - $15.00\n2 - $25.00\n3 - $75.00\n4 - $125.00\n")
        Monto_Apertura_Dolares(monto)
    else:
        print('Por favor seleccione una de las monedas predeterminadas')
        moneda = input('Ingrese Tipo de moneda: \n1 - Quetzales\n2 - Dolares\n')
        Asignar_Moneda(moneda)

# Funcion encargada de recibir el monto de apertura de la cuenta en Quetzales
def Monto_Apertura_Quetzales(monto):
    if monto == "1" or monto == "100":
        cuenta['monto_saldo'] = "100"
    elif monto == "2" or monto == "200":
        cuenta['monto_saldo'] = "200"
    elif monto == "3" or monto == "500":
        cuenta['monto_saldo'] = "500"
    elif monto == "4" or monto == "1000":
        cuenta['monto_saldo'] = "1000"
    else:
        print('Por favor seleccione uno de los montos autorizados')
        monto = input("Ingrese el monto de apertura: \n1 - 100.00\n2 - 200.00\n3 - 500.00 \n4 - 1000.00\n")
        Monto_Apertura_Quetzales(monto)

# Funcion encargada de recibir el monto de apertura de la cuenta en Dolares
def Monto_Apertura_Dolares(monto):
    if monto == "1" or monto == "15":
        cuenta['monto_saldo'] = "15"
    elif monto == "2" or monto == "25":
        cuenta['monto_saldo'] = "25"
    elif monto == "3" or monto == "75":
        cuenta['monto_saldo'] = "75"
    elif monto == "4" or monto == "125":
        cuenta['monto_saldo'] = "125"
    else:
        print('Por favor seleccione uno de los montos autorizados')
        monto = input("Ingrese el monto de apertura: \n1 - $15.00\n2 - $25.00\n3 - $75.00\n4 - $125.00\n")
        Monto_Apertura_Dolares(monto)

#funcion principal para depositos en Quetzales y Dolares
def Cuenta_Deposito():
    monto = int(input('Digite la cantidad a depositar\n'))
    if monto <= 0:
        print('El monto debe ser a partir de ' + cuenta['moneda'] + '1.00')
    else:
        nuevo = int(cuenta['monto_saldo']) + monto
        cuenta["monto_saldo"] = str(nuevo)
        print('El deposito se ha realizado con éxito,\nSu nuevo saldo es ' + str(cuenta['moneda']) + str(cuenta['monto_saldo']))
        Main_Menu()

Main_Menu()