def second_function():
    print("Este es el mensaje de la segunda función")


def first_function():
    print ("Este es el mensaje de la primera función")
    second_function()


first_function()