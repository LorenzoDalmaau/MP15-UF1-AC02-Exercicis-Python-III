from character import Character

# Clase que hereda de Character.
class CharacterFilms(Character):
    def __init__(self,name,created,gender,skin_color,hair,color,height,eye_color,mass,homeworld,birth_year):
        super().__init__(name, created, gender, skin_color, hair, color, height, eye_color, mass, homeworld, birth_year)
        self.num_of_films 
        self.first_films
        self.alive_at_the_end


    # Metodos
    def get_num_of_films(self):
        return self.num_of_films
    
    def get_first_films(self):
        return self.first_films
    
    def get_alive_at_the_end(self):
        return self.alive_at_the_end