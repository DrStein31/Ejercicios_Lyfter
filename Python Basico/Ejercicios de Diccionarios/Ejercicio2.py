list_a = ["first_name", "last_name", "role"]
list_b = ["Carlos", "Méndez", "Software Engineer"]
information = {}


for index in range(len(list_a)):
    information[list_a[index]] = list_b[index]

print (information)