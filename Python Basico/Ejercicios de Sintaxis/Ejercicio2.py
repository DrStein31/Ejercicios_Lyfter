print ("----Experimentando con sumas----")

name = input("Escriba su nombre: ")
last_name = input("Escriba su apellido: ")
age = int(input("Escriba su edad: "))

if age >= 0 and age <= 2:
    category = "Bebé"
elif age <= 11:
    category = "Niño"
elif age <= 14:
    category = "Preadolescente"
elif age <= 17:
    category = "Adolescente"
elif age <= 25:
    category = "Adulto joven"
elif age <= 64:
    category = "Adulto"
else:
    category = "Adulto mayor"

print("\nNombre:", name, last_name)
print("Edad:", age)
print("Categoría:", category)