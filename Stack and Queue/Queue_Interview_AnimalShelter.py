class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enQueue(self, animal, type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def deQueueCat(self):
        if not len(self.cats):
            return None
        else:
            return self.cats.pop(0)

    def deQueueDog(self):
        if not len(self.dogs):
            return None
        else:
            return self.dogs.pop(0)


# AS = AnimalShelter()
# AS.enQueue("Cat1", "Cat")
# AS.enQueue("Cat2", "Cat")
# AS.enQueue("Dog1", "Dog")
# AS.enQueue("Dog2", "Dog")
# print(AS.deQueueCat())
# print(AS.deQueueDog())
