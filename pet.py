class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # To Do
        def eat(self):
        # Reduce hunger by 3 points, but not below 0
        self.hunger = max(0, self.hunger - 3)
        # Increase happiness by 1, but not above 10
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        # To Do
        #Increase energy by 5, but not exceeding 10
        self.energy = min(10, self.energy + 5)

    def play(self):
        #ToDo
        #Reducing energy by 2, but not below 0
        self.energy = max(0, self.energy - 2)
        #Increasing happiness by 2, but not exceeding 10
        self.happiness = min (10, self.happines + 2)
        #increasing hunger by 1 but not exceeding 10
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        #ToDo
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        #ToDo
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for t in self.tricks:
                print(f"- {t}")
        else:
             print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        #ToDo
         #Print the current state of the pet.
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print(f"  Tricks learned: {len(self.tricks)}")

