def operations(current_number):    
    try:
        option = int(input("Ingresa la opción que necesitas: "))
    except ValueError:
        print ("Opción inválida. Debe de ser un número del 1 al 5")
        return current_number

    match option:
        case 1:
            try:
                second_number = float(input("Ingresa el número a sumar: "))
                return current_number + second_number
            except ValueError:
                print ("Número inválido. Por favor, ingrese un número válido para realizar la operación.")
                return current_number
        case 2:
            try:
                second_number = float(input("Ingresa el número a restar: "))
                return current_number - second_number
            except ValueError:
                print ("Número inválido. Por favor, ingrese un número válido para realizar la operación.")
                return current_number
        case 3:
            try:
                second_number = float(input("Ingresa el número a multiplicar: "))
                return current_number * second_number
            except ValueError:
                print ("Número inválido. Por favor, ingrese un número válido para realizar la operación.")
                return current_number
        case 4:
            try:
                second_number = float(input("Ingresa el número a dividir: "))
                return current_number / second_number
            except ValueError:
                print ("Número inválido. Por favor, ingrese un número válido para realizar la operación.")
                return current_number
            except ZeroDivisionError:
                print ("No se puede dividir por 0. Debes escribir un nuevo número.")
                return current_number
        case 5:
            return 0
    #Este case funciona como un try and except, pero es específicamente para un match. No hace falta un try and except
        case _:
            print("Opción inválida. Debe ser un número del 1 al 5")
            return current_number

def calculator():
    while True:
        try:
            current_number = float(input("Ingresa el número actual: "))
            break
        except ValueError:
            print("Número inválido. Por favor, ingresa un número válido.")
    
    while True:
        print ("""
===== CALCULADORA =====

    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Borrar resultado
""")
        current_number = operations(current_number)
        print (f"Resultado: {current_number}")

calculator()

