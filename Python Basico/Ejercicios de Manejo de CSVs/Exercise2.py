import csv

def get_number_of_games():
    while True:
        try:
            number_of_games = int(input("Ingrese la cantidad de videojuegos que desea agregar: "))
            if number_of_games <= 0:
                print("Cantidad no válida. Por favor, ingresa una cantidad mayor a 0.")
                continue
            break
        except ValueError:
            print("Cantidad no válida. Por favor, ingresa un número entero")
    return number_of_games


def data_games():
    games = []
    for _ in range(get_number_of_games()):
        game = {}
        name = input("Ingrese el nombre del videojuego: ")
        genre = input(f"Indica el género de {name}: ")
        developer = input(f"Indica el nombre del desarrollador de {name}: ")
        esrb_rating = input(f"Indica la clasificación ESRB de {name}: ")

        game["name"] = name
        game["genre"] = genre
        game["developer"] = developer
        game["esrb_rating"] = esrb_rating
        games.append(game)
    return games

def save_new_csv(output_file, data):

    with open(output_file, "w", encoding="utf-8", newline="") as file:

        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)


def main():

    data = data_games()
    output_file = input("Ingrese el nombre del nuevo archivo: ")
    save_new_csv(output_file, data)

if __name__ == "__main__":
    main()