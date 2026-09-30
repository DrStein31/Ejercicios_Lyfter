print ("----Experimentando con sumas----")


# string + string
print("Hola " + " Mundo")

# string + int
print("Edad: " + 20)
# TypeError: can only concatenate str (not "int") to str

# int + string
print(20 + " años")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# list + list
print([1, 2] + [3, 4])
# Resultado: [1, 2, 3, 4]

# string + list
print("Hola" + [1, 2])
# TypeError: can only concatenate str (not "list") to str

# float + int
print(3.5 + 2)
# Resultado: 5.5

# bool + bool
print(True + True)
# Resultado: 2

print(True + False)
# Resultado: 1

print(False + False)
# Resultado: 0