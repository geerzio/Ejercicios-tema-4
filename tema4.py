# Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
#Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
#Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, 
#el bloque de código que tendrá el bucle deberá:
#Incrementar el valor de la variable en uno cada vez que se ejecute.
#Mostrarlo por pantalla cada vez que se ejecute.
#Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.

# Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que
#la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y 
#deberá mostrarse por pantalla.
#Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año.
#Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola 
#informando de la estación en la que está. 
#También habrá que poner un default para cuando el valor de la variable no sea una estación.

"""
numero = int(input("Ingrese un numero: "))

if numero == 0:
    print("El numero es 0 ")
elif numero < 0:
    print(f"El numero ingresado {numero} es negativo ")
else:
    print(f"El numero ingresado {numero} es positivo ")
"""
"""
cant = 0

while cant <3:
    cant +=1
    print(cant)
    #if cant == 3:
    #    break
"""    
""" # DO WHILE 
cant = 0    
while True:
    cant +=1
    if cant == 3:   
        break
print(cant)
"""  
"""
for numeroFor in range(0,4,+1):
    print(numeroFor)   
"""  
 
#Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año.
#Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola 
#informando de la estación en la que está. 
#También habrá que poner un default para cuando el valor de la variable no sea una estación.   

#x = input("Ingrese la estacion del año: ")


while True:
    x = input("Ingrese la estacion del año: ")
    if x == "verano":
        print("La estacion es:",x)
        break
    elif x == "otoño":
        print("La estacion es:",x)
        break
    elif x == "invierno":
        print("La estacion es:",x)
        break
    elif x == "primavera":
        print("La estacion es:",x)
        break     
    else:
        print("Solo debe ingresar strings ")  
                             
        