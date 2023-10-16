class Character:
    def __init__(self,name,created,gender,skin_color,hair,color,height,eye_color,mass,homeworld,birth_year):
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair = hair
        self.color = color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year

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
        print("--------------------------------------------")
        

    