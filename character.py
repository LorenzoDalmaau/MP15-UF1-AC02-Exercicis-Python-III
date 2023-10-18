class Character:
    def __init__(self,_name,_created,_gender,_skin_color,_hair,_color,_height,_eye_color,_mass,_homeworld,_birth_year):
        self.name = _name
        self.created = _created
        self.gender = _gender
        self.skin_color = _skin_color
        self.hair = _hair
        self.color = _color
        self.height = _height
        self.eye_color = _eye_color
        self.mass = _mass
        self.homeworld = _homeworld
        self.birth_year = _birth_year

    # This function prints the character's information.
    def printCharacter(self):
        print("\n")
        print("Name: ", self.name)
        print("Created:", self.created)
        print("Gender:", self.gender)
        print("Skin color:", self.skin_color)
        print("Hair:", self.hair)
        print("Color:", self.color)
        print("Height: ", self.height)
        print("Eye color: ", self.eye_color)
        print("Mass: ", self.mass)
        print("Homeworld: ", self.homeworld)
        print("Birth year: ", self.birth_year)
        print("\n")

        

    