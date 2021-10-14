class CoffeeShop:
    specialty = 'espresso'
    
    def __init__(self, coffee_price):
        self.coffee_price = coffee_price
    
    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')
    
    # static method    
    @staticmethod
    def check_weather(arg):
        print(arg, 'Its sunny')
    # class method
    @classmethod
    def change_specialty(self, specialty):
        self.specialty = specialty
        print(f'Specialty changed to {specialty}')

CoffeeShop.check_weather(12)
coffee_shop = CoffeeShop('5')
coffee_shop.change_specialty('biriyani')
print(coffee_shop.specialty)