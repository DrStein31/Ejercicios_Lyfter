number1 = int(input("Escribe el primer número: "))
number2 = int(input("Escribe el segundo número: "))
number3 = int(input("Escribe el tercer número: "))

if number1 > number2 and number1 > number3:
    print (f"El número {number1} es el mayor")
elif number2 > number3:
    print (f"El número {number2} es el mayor")
else:
    print (f"El número {number3} es el mayor")

