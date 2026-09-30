my_list = []

for i in range(10):
    number = int(input(f"Ingrese el elemento {i + 1}: "))
    my_list.append(number)

highest = my_list[0]

for number in my_list:
    if number > highest:
        highest = number

print (my_list)
print ("El valor más alto es: ", highest)