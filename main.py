import json
from character import Character
from character_films import CharacterFilms

# This function reads the json file and returns a list of Character objects.
def read_json():
    characters = []

    with open("starwars.json", "r") as json_file:
        data = json.load(json_file)

        for item in data:
            fields = item["fields"]
            character = Character(
                fields["name"],
                fields["created"],
                fields["gender"],
                fields["skin_color"],
                fields["hair_color"],
                fields["hair_color"],
                fields["height"],
                fields["eye_color"],
                fields["mass"],
                fields["homeworld"],
                fields["birth_year"]
            )
            characters.append(character)

    return characters


# This function loads the films of each character.
def load_character_films(characters):
    charactersFilms = []
    for character in characters:
        match character.name:
            case "Luke Skywalker":
                infoLuke = ["4","Star Wars: Episode IV - A New Hope (1977)","ded"]
                luke = CharacterFilms(character.name, character.created, character.gender, character.skin_color, character.hair, character.color, character.height, character.eye_color, character.mass, character.homeworld, character.birth_year, infoLuke[0], infoLuke[1],infoLuke[2])
                charactersFilms.append(luke)
                

            case "Chewbacca":
                infoChewbacca = ["6","Star Wars: Episode IV - A New Hope (1977)","alive"]
                chewbacca = CharacterFilms(character.name, character.created, character.gender, character.skin_color, character.hair, character.color, character.height, character.eye_color, character.mass, character.homeworld, character.birth_year, infoChewbacca[0], infoChewbacca[1],infoChewbacca[2])
                charactersFilms.append(chewbacca)
                
            case "Anakin Skywalker":
                infoAnakin = ["4","Star Wars: Episode VI - Return of the Jedi (1983)","dead"]
                anakin = CharacterFilms(character.name, character.created, character.gender, character.skin_color, character.hair, character.color, character.height, character.eye_color, character.mass, character.homeworld, character.birth_year, infoAnakin[0], infoAnakin[1],infoAnakin[2])
                charactersFilms.append(anakin)
                
            case _:
                charact = CharacterFilms(character.name, character.created, character.gender, character.skin_color, character.hair, character.color, character.height, character.eye_color, character.mass, character.homeworld, character.birth_year, "Null", "Null","Null")
                charactersFilms.append(charact)


    return charactersFilms




# This function exports the data to a json file.
def export_json(charactersFilms):
    # Convert each object in the list to a dictionary
    data = [obj.__dict__ for obj in charactersFilms]
    with open("new_starwars.json", "w") as json_file:
        json.dump(data, json_file, indent=4)



def __main__():
    json_data:list = read_json()
    data_characterFilm:list = []
    while(True):
        print("Selecciona una opcio:")
        print("1. Veure les dades dels personatjes")
        print("2. Carregar noves dades als personatjes")
        print("3. Printar el characters amb les noves dades")
        print("4. Escriure un ficher json amb les noves dades")
    
        choice = input("Ingresa el número de l'opcio desitjada: ")
    
        match choice:
            # This case shows the list of characters.
            case "1":
                print("List of characters:")
            
                for character in json_data:
                    character.printCharacter()
        
            case "2":
                print("\n")
                print("Noves dades carregades als personatges")
                print("\n")

                data_characterFilm = load_character_films(json_data)
            
            case "3":

                if not data_characterFilm:
                    print("\n")
                    print("Primer has de carregar les noves dades (opcio 2)")
                    print("\n")
                else:
                    for character in data_characterFilm:
                        character.printInfo()


            case "4":

                if not data_characterFilm:
                    print("\n")
                    print("Primer has de carregar les noves dades (opcio 2)")
                    print("\n")
                else:
                    print("Export data to json")
                    export_json(data_characterFilm)
                    
                    print("Export data to json")
                    export_json(data_characterFilm)                
            case _:
                print("Exercici no válida. Por favor, selecciona una Exercici válida.")


__main__()
