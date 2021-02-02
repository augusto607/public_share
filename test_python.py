# Test de un script realizado en python - input y primer juego
game = 1
while game == 1:
    print("Bienvenido al juego de adivinanzas")
    print("Elija uno (1) para jugar o cero (0) para salir!")
    inicio = input("Escoja 1 o 0 = ")
    if inicio == '1' :
        print("\nExisten 5 palabras ocultas en este juego, intente adivinar una!!!")
        dato = input("Ingrese una palabra: ")
        lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

        if lista.count(dato) > 0 :
            print("\n-> YOU WIN! :) (√) La palabra existe: ", dato)
            print("\n#-----------------------------------#\n")
        else:
            print("\n-> YOU LOSE! :( (X) La palabra no existe : ", dato)
            print("\n#-----------------------------------#\n")

    elif inicio == '0' :
        game == 0
        print("\n...Saliendo del juego... Hasta pronto!!!")
        break

    else:
        print("\n¡ WARNING ! -- Favor indique un valor entre 0 y 1")
        print("\n#-----------------------------------#\n")
        

print('\n# --------------------------------------- #\n')

#calculadora 
print("Calculadora Python")
primero = input('Ingresa el primer numero = ')
try:
    primero = int(primero)
except:
    primero = 'caracter'
if (primero == 'caracter'):
    print('Solo debes ingresar valores enteros')
    exit()

segundo = input('Ingresa el segundo numero = ')
try:
    segundo = int(segundo)
except:
    segundo = 'caracter'
if (segundo == 'caracter'):
    print('Solo debes ingresar valores enteros')
    exit()

simbolo = input('Indique la operacion a realizar(Suma: + , Resta: - , Multip: * , Division: /) : ')

if (simbolo == '+'):
    print('(+)Suma = ', primero + segundo)
elif (simbolo == '-'):
    print('(-)Resta = ', primero - segundo)
elif (simbolo == '*'): 
    print('(*)Multiplicacion = ', primero * segundo)
elif (simbolo == '/'):
    print('(/)Division = ', primero / segundo)
else:
    print("Por favor indique el simbolo correcto para la operacion(Suma: + , Resta: - , Multip: * , Division: /)")