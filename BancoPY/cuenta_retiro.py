# El siguiente diccionario fue agregado solo para pruebas
cuenta = {
    'nombre': "Antonio",
    'apellido': "Perez",
    'dpi': "1234567891234",
    'pin': "1234",
    'tipo': "Dolares",
    'moneda': "Q",
    'monto_saldo': "1000",
    'monto_retirado': "0"
}

def Cuenta_Retiro():
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    if monto_retiro > int(cuenta['monto_saldo']):
        print("Sus fondos son insuficientes para realizar la transacción")
        Cuenta_Retiro()
    else:
        cuenta['monto_saldo'] = int(cuenta['monto_saldo']) - monto_retiro
        cuenta['monto_retirado'] = int(cuenta['monto_retirado']) + monto_retiro
        print('Su nuevo saldo es: ' + str(cuenta['moneda']) + str(cuenta['monto_saldo']))

Cuenta_Retiro()