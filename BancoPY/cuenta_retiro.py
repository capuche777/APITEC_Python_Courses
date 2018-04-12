# El siguiente diccionario fue agregado solo para pruebas
cuenta = {
    'nombre': "Antonio",
    'apellido': "Perez",
    'dpi': "1234567891234",
    'pin': "1234",
    'tipo': "Cuenta Preferente",
    'moneda': "$",
    'monto_saldo': 1000,
    'monto_retirado': 0
}

def Cuenta_Retiro():
    moneda = cuenta['moneda']
    retirado = cuenta['monto_retirado']
    tipo = cuenta['tipo']

# Este if, else determina el tipo de cuenta para agregar una llave limite para poder realizar los retiros
    if tipo == "Cuenta Clasica" and moneda == "Q" or tipo == "Cuenta Ahorro" and moneda == "Q":
        cuenta['limite'] = 2000
        if tipo == "Cuenta Clasica":
            cuenta['retiro_max'] = 500
        else:
            cuenta['retiro_max'] = 2000
    elif tipo == "Cuenta Clasica" and moneda == "$" or tipo == "Cuenta Ahorro" and moneda == "$":
        cuenta['limite'] = 250
        if tipo == "Cuenta Clasica":
            cuenta['retiro_max'] = 75
        else:
            cuenta['retiro_max'] = 125

# Almacena el limite establecido para ser utilizado en la operacion siguiente
    limite = cuenta['limite']
    maximo = cuenta['retiro_max']

if retirado < limite:
    Retirar()

"""def Retirar():
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    if monto_retiro > int(cuenta['monto_saldo']):
        print("Sus fondos son insuficientes para realizar la transacción")
        Cuenta_Retiro()
    elif monto_retiro <= 0:
        print("Solo se permiten retiros mayores a " + cuenta['moneda'] + "1.00")
        Cuenta_Retiro()
    else:
        cuenta['monto_saldo'] = cuenta['monto_saldo'] - monto_retiro
        cuenta['monto_retirado'] = cuenta['monto_retirado'] + monto_retiro
        print('Su nuevo saldo es: ' + cuenta['moneda'] + str(cuenta['monto_saldo']))

"""
Cuenta_Retiro()