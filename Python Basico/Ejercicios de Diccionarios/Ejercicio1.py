info_hotel = {}
info_room = {}

info_hotel["name"] = input("Indica el nombre del hotel: ")
info_hotel["hotel_stars"] = int(input("Indica el número de estrellas: "))
info_hotel["rooms"] = []

for index in range(3):
    info_room = {}
    info_room["number"] = int(input("Indica el número de la habitación: "))
    info_room["floor"] = int(input("Indica el número de piso: "))
    info_room["price_per_night"] = float(input("Indica el número de precio por noche: "))
    info_hotel["rooms"].append(info_room)
    

print (info_hotel)