class DogInfo:
    increase_weight = 1.01
    num_of_dogs = 0
    def __init__(self, name, breed, age, fur_colour, weight): #The things in brackets are arguements
        self.name = name #These are instance variables
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour
        self.weight = weight
        self.human_age = age * 7

        DogInfo.num_of_dogs += 1

    def identity(self):
        return '{} is a {}'.format( self.name, self.breed)
    def feed_dog(self):
        self.weight = float(self.weight * self.increase_weight) #Use float so that the 1.01 does not get round down to 1.00
    @classmethod
    def setincrease_weight(cls, amount):
        cls.increase_weight = amount

animal1 = DogInfo("Billy", "Labrador", 3, "Black", 90) #The things in brackets are instances
animal2 = DogInfo("Robert", "Pug", 5, "Brown", 45)
animal3 = DogInfo("Dummy", "Golden Retriever", 7, "Blonde", 90)
animal4 = DogInfo("Axel", "German Shepard", 1, "Black", 95)
animal5 = DogInfo("Sausage", "Weiner Dog", 8, "White", 60)

DogInfo.setincrease_weight(1.02)

print(DogInfo.num_of_dogs)
print(animal1.increase_weight)
print(animal1.identity())
print(animal2.identity())
print(animal1.weight)
animal1.feed_dog()
print(animal1.weight)

'''print (animal1.name, animal1.breed, animal1.age, animal1.fur_colour, animal1.weight)
print (animal2.name, animal2.breed, animal2.age, animal2.fur_colour, animal2.weight)
print (animal3.name, animal3.breed, animal3.age, animal3.fur_colour)
print (animal4.name, animal4.breed, animal4.age, animal4.fur_colour)
print (animal5.name, animal5.breed, animal5.age, animal5.fur_colour)'''


        
