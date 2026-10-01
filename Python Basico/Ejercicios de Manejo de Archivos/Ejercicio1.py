def read_songs(file_songs):
    with open(file_songs, "r") as input_file:
        songs = input_file.readlines()
        songs.sort()
        return songs


def write_songs(output_file, songs): 
    with open(output_file, "w", encoding="utf-8") as sorted_file:
        for song in songs:
            sorted_file.write(song)


def main():
    
    input_file = input("Escribe el archivo que quieres ordenar: ")
    output_file = input("Escribe el nombre del nuevo archivo: ")
    songs = read_songs(input_file)
    write_songs(output_file, songs)

if __name__ == "__main__":
    main()