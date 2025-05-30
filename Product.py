class Product():
    #constructor
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.price = 0.00

    def display(self):
        print("===========Welcome to Sebong Cafe!===============")
        print("Product Nmae:", self.name, "\nPrice: ", self.price, "\nQuantity: ", self.quantity)

    #getter and setter method
    def get_price(self, sum):
        self.price += sum

    def set_price(self, sum):
        self.price += sum
        
    def get_quantity(self, sum):
        self.quantity += sum

    def set_quantity(self, sum):
        self.quantity += sum

    def sell(self, sum):
        if sum <= self.quantity:
            self.quantity -= sum
        
    def cost(self, sum):
        self.price == sum*self.price

product = Product("Tiramisu", 10)
product.get_price(95)
product.set_price(25)
product.get_quantity(11)
product.set_price(20)
product.sell(9)
product.cost(1)
product.display()
