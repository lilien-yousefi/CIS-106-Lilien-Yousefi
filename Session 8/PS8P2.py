# comment - Lilien Yousefi

# car class:
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def get_discount_price(self):
        return self.sticker_price * 0.90

# derived sport class:
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.include_wheels = False
        self.include_engine = False
        self.include_interior = False


    def SportWheels(self, include):
        self.include_wheels = include.upper() == 'Y'

    def SportEngine(self, include):
        self.include_engine = include.upper() == 'Y'

    def SportInterior(self, include):
        self.include_interior = include.upper() == 'Y'


    def price_with_options(self):
        price = self.get_discount_price()
        if self.include_wheels:
            price += 1000.00
        if self.include_engine:
            price += 3000.00
        if self.include_interior:
            price += 2000.00
        return price

def main():
    print("Enter Car Information:")
    make = input("Make: ")
    model = input("Model: ")
    sticker_price = float(input("Sticker Price: $"))

    car = Sport(make, model, sticker_price)

    wheels = input("Include Sport Wheels? (Y/N): ")
    engine = input("Include Sport Engine? (Y/N): ")
    interior = input("Include Sport Interior? (Y/N): ")

    car.SportWheels(wheels)
    car.SportEngine(engine)
    car.SportInterior(interior)


    print("Make:", car.make)
    print("Model:", car.model)
    print("Sticker Price: $", format(car.sticker_price, ".2f"))
    print("Discount Price (90%): $", format(car.get_discount_price(), ".2f"))
    print("Final Price with Options: $", format(car.price_with_options(), ".2f"))

if __name__ == "__main__":
    main()
