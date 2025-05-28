from Pet import Cow, PolarBear, Chimpanzee, Lion

if __name__ == "__main__":
    cow = Cow("Liya", 8, "Animal")
    cow.display()
    cow.sound()

polarBear = PolarBear("Bob", 5, "Animal")
polarBear.display()
polarBear.sound()

chimpanzee = Chimpanzee("Micky", 4, "Animal")
chimpanzee.display()
chimpanzee.sound()

lion = Lion("Sher", 10, "Animal")
lion.display()
lion.sound()