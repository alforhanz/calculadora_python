numero1= int(input("Introduzca el primer valor: "))
numero2= int(input("Introduzca el segundo valor: "))

eleccion = 0

while eleccion !=6:
    print(""" 
      Indique la operacion que decea realizar
      
      1) Sumar
      2) Restar
      3) Multiplicar 
      4) Dividir
      5) Reset
      6) Salir
      """)
    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("El resultado de la suma es: ", numero1 + numero2)
    elif eleccion == 2:
        print(" ")
        print("El resultado de la resta es: ", numero1 - numero2)
    elif eleccion == 3:
        print(" ")
        print("El resultado de la multiplicacion es: ", numero1 * numero2)
    elif eleccion == 4:
        print(" ")
        print("El resultado de la divicion es: ", numero1 / numero2)
    elif eleccion == 5:
        numero1= int(input("Introduzca el primer valor: "))
        numero2= int(input("Introduzca el segundo valor: "))
    elif eleccion == 6:
        print(" ")
        print("Gracias por usar nuestro programa")
