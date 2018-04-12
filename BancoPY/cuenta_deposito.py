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

#funcion principal para depositos en Quetzales y Dolares
def Cuenta_Deposito():
    monto = int(input('Digite la cantidad a depositar\n'))
    if monto <= 0:
        print('El monto debe ser a partir de ' + cuenta['moneda'] + '1.00')
    else:
        nuevo = int(cuenta['monto_saldo']) + monto
        cuenta["monto_saldo"] = str(nuevo)
        print('El deposito se ha realizado con éxito,\nSu nuevo saldo es ' + str(cuenta['moneda']) + str(cuenta['monto_saldo']))

Cuenta_Deposito()