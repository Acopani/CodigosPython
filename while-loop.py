numero = int(input("Digita un número del 1 al 10: "))
# Validamos que el número esté en el rango
if 1 <= numero <= 10:
    #Inicia desde 1
    contador = 1
    #Hace la multiplicacion hasta llegar a 10
    while contador<= 10:
    #Imprime la tabala de multiplicar 
        print(f"{numero} x {contador} = {numero * contador}")
    #Cada bucle hace la suma de 1
        contador += 1
else:
    print("El número no está entre el 1 y el 10.")
print("--------------------------------------------------------------------------")


print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))