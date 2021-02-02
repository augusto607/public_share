#Seccion 4: Introduccion a python
print("Hello World")

print("# ---------------------------------------- #\n")
#Operaciones matematicas basicas
suma = 5 + 3
resta = 5 - 3
multiplicar = 5 * 3
dividir = 5/3

print('Suma = ', suma,'\n', 'Resta = ', resta,'\n', 'Multiplicacion = ', multiplicar,'\n', 'Division = ', dividir,'\n')

print("# ---------------------------------------- #\n")

#Identacion en python:
    #Se trata de los margenes que utiliza python para poder funcionar correctamente, es decir, todo debe estar correctamente 
    #identado para que funcione, ejemplo:
if (5 > 3):
    print("Cinco es el numero mayor")
else:
    print("Cinco es el numero menor")

print("# ---------------------------------------- #\n")
 
#Definir multiples variables pero con un mismo valor
var1 = var2 = var3 = "Valor Inicial"
print(var1, var2, var3)