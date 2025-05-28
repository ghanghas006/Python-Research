from Cat import Cat, DomesticCat, WildCat

if __name__ == "__main__":
    cat1 = Cat("Luna", 5, True)
    cat1.display()
    cat1.sound()

cat1.isHappy = False
cat1.display()

domesticCat = DomesticCat("Roshi", "Dino", 2, False)
domesticCat.display()
domesticCat.sound()

wildCat = WildCat("Tiger", 10)
wildCat.display()
wildCat.sound()
