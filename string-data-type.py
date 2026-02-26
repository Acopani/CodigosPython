#Crea una varibale myStrig y dentro de ella guardamos un comentario
myString = "This is a string."
#Imprimimos el valor de la variable myString
print(myString)

#Imprimimos el tipo de dato de la variable myString
print(type(myString))
#Imprimimos el valor de la variable myString, un texto y finalmente el tipo de dato
print(myString + " is of the data type " + str(type(myString)))

#Crea la varibale firstString y denbtro de ella guarda el valor de WATER
firstString = "water"

#Crea la varibale secondString y dentro de ella guarda el valor de FALL
secondString = "fall"

#Crea la varibale thirdString y denbtro de ella guarda el valor concatenado de las 2 variables
thirdString = firstString + secondString
#Imprime la variable thirdString
print(thirdString)

#Crea la variable name y usando la funcion input almacenamos el valor escrito por el usuario en la consola
name = input("What is your name? ")
#Imprime la variable name
print(name)

#Crea la variable color y usando la funcion input almacenamos el valor escrito por el usuario en la consola
color = input("What is your favorite color?  ")
#Crea la variable animal y usando la funcion input almacenamos el valor escrito por el usuario en la consola
animal = input("What is your favorite animal?  ")
#Imprime el comentario YOU LIKE A y la variable name color y animal
#Los corchetes imprime la secuencia de las variable como las usamos
print("{}, you like a {} {}!".format(name,color,animal))
print("{}, you like a {} {}!".format(animal,color,name))