# Test of a script for jupyter notebook build in Python, input and first game.
game = 1
while game == 1:
    print("Welcome to the guessing game!")
    print("Chose one (1) for start or zero (0) for exit!")
    inicio = input("Chose 1 or 0 = ")
    if inicio == '1' :
        print("\nIn this game exist 5 hidden words, try to guess at least one!!!")
        dato = input("Enter a word to try: ")
        lista = ['hi', 'word', 'pig', 'happy', 'dragons']

        if lista.count(dato.lower()) > 0 :
            print("\n-> YOU WIN! :) (√) The word exist: ", dato)
            print("\n#-----------------------------------#\n")
        else:
            print("\n-> YOU LOSE! :( (X) The word don't exist : ", dato)
            print("\n#-----------------------------------#\n")

    elif inicio == '0' :
        game == 0
        print("\n...Leaving the game... See you soon!!!")
        break

    else:
        print("\n¡ WARNING ! -- Please, put value between 0 and 1")
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
