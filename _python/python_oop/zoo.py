class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    #creating 1 method to add animals instead of 1 for each type
    def add_animal(self, type, name):
        self.animals.append(Animal(type, name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

#creating an Animal class to create animal objects
class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    #printing animal type and name
    def display_info(self):
        print(f"{self.type}, {self.name}")

zoo1 = Zoo("John's Zoo")
zoo1.add_animal("Lion","Nala")
zoo1.add_animal("Lion","Simba")
zoo1.add_animal("Tiger","Rajah")
zoo1.add_animal("Tiger","Shere Khan")
zoo1.print_all_info()
