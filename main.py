import json
from character import Character

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

    

def __main__():
    print("Selecciona una Exercici:")
    print("1. Exercici 1")
    print("2. Exercici 2")
    print("3. Exercici 3")
    
    choice = input("Ingresa el número de la Exercici deseada: ")
    
    match choice:
        case "1":
            print("Lista de Personajes.")
            # Función que muestre por pantalla los caracteres de Star Wars.
            json_data:list = read_json()
            
            for character in json_data:
                character.printCharacter()
            
        case "2":
            print("Has seleccionado Estadístiques.")
            
        case "3":
            print("Has seleccionado Canvia el format de dades.")
        case _:
            print("Exercici no válida. Por favor, selecciona una Exercici válida.")


__main__()
