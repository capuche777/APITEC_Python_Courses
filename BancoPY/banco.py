cuenta = {
    'nombre': "",
    'apellido': "",
    'dpi': "",
    'pin': "",
    'tipo': "",
    'moneda': "",
    'monto_apertura': ""
}

#Funcion encargada de solicitar datos de usuario:
def Cuenta_Apertura():
    cuenta['nombre'] = input('Ingrese nombre de usuario: ')
    cuenta['apellido'] = input('Ingrese apellido de usuario: ')
    cuenta['dpi'] = input('Ingrese el DPI del usuario: ')
    cuenta['pin'] = input('Ingrese un numero de PIN (4 Digitos): ')
    # Se ha creado una serie de if, elif para determinar el ingreso del usuario, si prefiere ingresar numericamente el tipo de cuenta o por medio de strings
    cuenta['tipo'] = input('Que tipo de cuenta desea aperturar: \n1 - Cuenta Clasica\n2 - Cuenta Ahorro\n3 - Cuenta Preferente\n')
    if cuenta['tipo'] == "1" or cuenta['tipo'] == "cuenta clasica" or cuenta['tipo'] == "Cuenta Clasica":
        cuenta['tipo'] == "Cuenta Clasica"
    elif cuenta['tipo'] == "2" or cuenta['tipo'] == "cuenta ahorro" or cuenta['tipo'] == "Cuenta Ahorro":
        cuenta['tipo'] = "Cuenta Ahorro"
    else:
        cuenta['tipo'] == "Cuenta Preferente"
    cuenta['moneda'] = input('Ingrese Tipo de moneda: \n1 - Quetzales\n2 - Dolares\n')
    if cuenta['moneda'] == "1" or  cuenta['moneda'] == "Quetzales" or cuenta['moneda'] == "quetzales":
        cuenta['moneda'] = "Quetzales"
    else:
        cuenta['moneda'] = "Dolares"
    print("La cuenta se ha aperturado con éxito, los datos son:\nNombre Completo: " + cuenta['nombre'] + " " + cuenta['apellido'] + "\nNumero de DPI: " + cuenta['dpi'] + "\nTipo de cuenta: " + cuenta['tipo'] + "\nMoneda: " + cuenta['moneda'] + "\nPIN: " + cuenta['pin'])

Cuenta_Apertura()