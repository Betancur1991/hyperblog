x= int(input("Ingresa un numero entre 2 y 2000 "))

if x < 2 or x>2000:
    print("Ingresa otro número, que se encuentre dentro del rango")
    if x%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

    contador=0
    for i in range(2,x):
        evalua=x%i
        if evalua==0:
            contador+=1

    if contador != 0:
        print("No es un numero primo")
    elif contador==0:
        print("El numero ingresado es un numero primo")

    print("Los divisores de este numero son:")

    for i in range(1,x+1):
        if x%i==0:
            print(i)
