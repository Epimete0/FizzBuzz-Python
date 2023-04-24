#Escribir un programa que muestre en pantalla los números del 1 al 100, 
# sustituyendo los múltiplos de 3 por la palabra “fizz”, los múltiplos de 5 por “buzz” y los múltiplos de ambos, 
# es decir, los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”.

i = 0 #Iniciar variable numerica

while not  i == 100:  #Iniciar bucle while
    i += 1

    if (i % 3 == 0 and i % 5 == 0): # Puede ser reemplazado por (i % 15 == 0)
        print("FizzBuzz")

    elif (i % 3 == 0 ): # Primera condicion multiplo de 3
        print("Fizz")
    
    elif (i % 5 == 0):
        print("Buzz") # Segunda condicion multiplo de 5 

    else:             # Caso que no cumpla con las condiciones anteriores
        print(i)
