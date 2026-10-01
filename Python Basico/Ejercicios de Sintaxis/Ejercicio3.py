import random


secret_number = random.randint(1,10)

print("Adivina el número secreto entre 1 y 10.")


while True:
    number = int(input("Ingrese un número: "))

    if number== secret_number:
        print (f"¡Felicidades! El número {number} es el número secreto.")
        break
    else:
        print("Incorrecto. Inténtelo de nuevo.")
