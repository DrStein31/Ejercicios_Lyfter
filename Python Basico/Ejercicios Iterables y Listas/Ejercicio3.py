my_list = []

count = int(input("¿Cuántos elementos tendrá la lista? "))

for i in range(count):
    number = int(input(f"Ingrese el elemento {i + 1}: "))
    my_list.append(number)

print("Lista original:", my_list)

temp = my_list[0]
my_list[0] = my_list[len(my_list) - 1]
my_list[len(my_list) - 1] = temp

print("Lista modificada:", my_list)