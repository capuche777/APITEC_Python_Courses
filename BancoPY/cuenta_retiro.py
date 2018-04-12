# El siguiente diccionario fue agregado solo para pruebas
cuenta = {
    'nombre': "Antonio",
    'apellido': "Perez",
    'dpi': "1234567891234",
    'pin': "1234",
    'tipo': "Cuenta Clasica",
    'moneda': "$",
    'monto_saldo': "1000",
    'monto_retirado': 300
}

def Cuenta_Retiro():
    moneda = cuenta['moneda']
    retirado = cuenta['monto_retirado']
    tipo = cuenta['tipo']
    if moneda == "$":
        if tipo == "Cuenta Clasica" and retirado <= 250:
            Retirar()
    else:
        if tipo == "Cuenta Clasica" and retirado <= 2000:
            Retirar()

def Retirar():
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    if monto_retiro > int(cuenta['monto_saldo']):
        print("Sus fondos son insuficientes para realizar la transacción")
        Cuenta_Retiro()
    elif monto_retiro <= 0:
        print("Solo se permiten retiros mayores a " + cuenta['moneda'] + "1.00")
        Cuenta_Retiro()
    else:
        cuenta['monto_saldo'] = int(cuenta['monto_saldo']) - monto_retiro
        cuenta['monto_retirado'] = int(cuenta['monto_retirado']) + monto_retiro
        print('Su nuevo saldo es: ' + cuenta['moneda'] + cuenta['monto_saldo'])

Cuenta_Retiro()