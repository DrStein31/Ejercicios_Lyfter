import json

def get_skills_pokemon():
    skills = []
    number_skills = 1

    while number_skills <= 4:
        skill = input(f"Indica la skill número {number_skills} de tu pokemon: ")
        skills.append(skill)
        number_skills += 1

    return skills


def get_stats_pokemon():
    stats_pokemon = {}
    hp = int(input("Escribe el porcentaje de vida que tiene: "))
    attack = int(input("Escribe el porcentaje de ataque que tiene: "))
    defense = int(input("Escribe el porcentaje de defensa que tiene: "))
    sp_attack = int(input("Escribe el porcentaje de ataque especial que tiene: "))
    sp_defense = int(input("Escribe el porcentaje de defensa especial que tiene: "))
    speed = int(input("Escribe el porcentaje de velocidad que tiene: "))


    stats_pokemon["hp"] = hp
    stats_pokemon["attack"] = attack
    stats_pokemon["defense"] = defense
    stats_pokemon["sp_attack"] = sp_attack
    stats_pokemon["sp_defense"] = sp_defense
    stats_pokemon["speed"] = speed

    return stats_pokemon

def get_new_pokemon():
    new_pokemon = {}

    name_of_pokemon = input("Escribe el nombre del pokemon: ")
    type_of_pokemon = input("Escribe el tipo del pokemon: ")
    level_pokemon = int(input("indica el nivel del pokemon: "))
    weight_of_pokemon = float(input("indica el peso del pokemon: "))
    is_shiny = True if input("¿Tu pokemon es shiny? Responde con si/no").lower() == "si" else False
    if input("¿Tu pokemon tiene un objeto? Responde con si/no").lower() == "si":
        held_item = input("Indica cual objeto tiene: ")
    else:
        held_item = None
    skills = get_skills_pokemon()
    stats = get_stats_pokemon()

    new_pokemon["name"] = name_of_pokemon
    new_pokemon["type"] = type_of_pokemon
    new_pokemon["level"] = level_pokemon
    new_pokemon["weight_kg"] = weight_of_pokemon
    new_pokemon["is_shiny"] = is_shiny
    new_pokemon["held_item"] = held_item
    new_pokemon["skills"] = skills
    new_pokemon["stats"] = stats

    return new_pokemon


def main():
    file_pokemon= input("Escribe el nombre del archivo que quieres usar: ")
    
    new_pokemon = get_new_pokemon()
    with open(file_pokemon, "r", encoding="utf-8") as file:
        data = json.load(file)
        data.append(new_pokemon)

    with open(file_pokemon, "w", encoding="utf-8") as file:
        json.dump(data, file, indent = 4)

if __name__ == "__main__":
    main()