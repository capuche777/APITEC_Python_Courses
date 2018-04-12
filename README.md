Utilizando lo aprendido hasta este punto (condicionales, ciclos y funciones),
escriba un programa de consola que maneje las transacciones bancarias de un usuario con ls siguientes funcionalidades:

## Aperturar una cuenta, pidiéndole al usuario la siguiente información:
- Nombre
- Apellido
- DPI
- PIN
- Modeda (Q o $)
- Tipo (clásica, ahorro, preferente)
- Monto de apertura (100, 200, 500, 1000) || ($15,   $25   $75  $125)

## Poder depositar y retirar montos variables definidos por el usuario, 
utilizando el DPI y el PIN para verificar la transacción.
- Se puede depositar cualquier monto en cualquier tipo de cuenta
- En la cuenta clásica sólo se puede retirar Q2,000 ($250) en total, y Q500 ($75) a la vez
- En la cuenta ahorro sólo se puede retirar Q2,000 ($250) en total, y Q1000 ($125) a la vez
- En la cuenta preferente se puede retirar cualquier monto

## Convertir la el monto de la cuenta de una moneda a otra a Q8/$, utilizando el DPI y el PIN para verificar la conversión.

## Cerrar la cuenta, la cual hace que el usuario ya no pueda hacer transacciones, utilizando el DPI y el PIN para verificar el cierre.