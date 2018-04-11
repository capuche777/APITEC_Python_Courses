# El siguiente diccionario fue agregado solo para pruebas
cuenta = {
    'nombre': "Antonio",
    'apellido': "Perez",
    'dpi': "1234567891234",
    'pin': "1234",
    'tipo': "Dolares",
    'moneda': "Quetzales",
    'monto_saldo': "1000"
}

def Cuenta_Retiro():
    monto_retiro = input("Ingrese el monto a retirar: ")
    if int(monto_retiro) > int(cuenta['monto_saldo']):
        print("Sus fondos son insuficientes para realizar la transacción")
        Cuenta_Retiro()
    else:
        cuenta['monto_salldo'] = int(cuenta['monto_retiro']) - int(monto_retiro)

Cuenta_Retiro()