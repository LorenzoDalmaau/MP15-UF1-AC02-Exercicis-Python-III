from character import Character

# Clase que hereda de Character.
class CharacterFilms(Character):
    def __init__(self,name,created,gender,skin_color,hair,color,height,eye_color,mass,homeworld,birth_year, num_of_films, first_film, alive_at_the_end):
        super().__init__(name, created, gender, skin_color, hair, color, height, eye_color, mass, homeworld, birth_year)
        self.num_of_films = num_of_films
        self.first_film = first_film
        self.alive_at_the_end = alive_at_the_end

    def get_num_of_films(self):
        return self.num_of_films

    def get_first_film(self):
        return self.first_film

    def get_alive_at_the_end(self):
        return self.alive_at_the_end
    

    def printInfo(self):
        super().printCharacter()
        print("Number of films: ", self.get_num_of_films())
        print("First film: ", self.get_first_film())
        print("Alice at the end: ", self.get_alive_at_the_end())
        print("\n")
        print("--------------------------------------------")