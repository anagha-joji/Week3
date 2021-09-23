from random import randrange

class Pet:
    boredom_decrement = 3
    boredom_max = 10
    boredom_threshold = 3
    hunger_decrement = 2
    hunger_max = 10
    hunger_threshold = 3
    sounds = ['"Hi"']

    def __init__(self,name,animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom -= 1
        self.hunger -= 1

    def mood(self):
        if self.hunger > self.hunger_threshold and self.boredom > self.boredom_threshold:
            return "happy"
        elif self.hunger < self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def _str_(self):
        return "\nI am " + self.name + "." + "\nI feel " + self.mood() + "."

    def teach(self, word):
        self.sounds.append(word)
        self.clock_tick()

    def talk(self ):
        print("I am a " + self.animal_type + "," + "named " + self.name + "." + "I feel " + self.mood() + " now.\n")
        print(self.sounds[randrange(len(self.sounds))])
        self.clock_tick()

    def feed(self):
        print("**yummy** .\nThank you!")
        meal = randrange(self.hunger, self.hunger_max)
        self.hunger += meal

        if self.hunger < 0:
            self.hunger = 0
            print("I am still hungry!")
        elif self.hunger > self.hunger_max:
            self.hunger = self.hunger_max
            print("I am full!")
        self.clock_tick()

    def play(self):
        print("Woohoo!")
        fun = randrange(self.boredom, self.boredom_max)
        self.boredom += fun
        if self.boredom < 0:
            self.boredom = 0
            print("I am bored ")
        elif self.boredom > self.boredom_max:
            self.boredom = self.boredom_max
            print("I am happy! ")
        self.clock_tick()

def main():
    pet_name = input("Provide a name for your pet: ")
    pet_type = input("What type of animal is your pet? ")

    my_pet = Pet(pet_name, pet_type)
    input("Hello! I am " + my_pet.name + "\nPress enter to start. ")

    choice = None
    while choice != 0:
        print("1 - Feed your pet \n2 - Talk to your pet \n3 - Teach your pet a new word \n4 - Play time \n0 - Quit")
        choice = input("Enter your Choice: ")

        if choice == "0":
            print("Good bye")
            break
        elif choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word = input("What do you want to teach? ")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else:
            print("Please enter a valid option ")

main()







