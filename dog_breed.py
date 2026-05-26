class dog:

    species = "canine"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

dog1 = dog("Labrador Retriever", "white")
dog2 = dog("German Shepherd", "brown")

print(f"Dog number 1 is a {dog1.breed}. He is {dog1.color}.")
print(f"Dog number 2 is a {dog2.breed}. He is {dog2.color}.")