class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if self.price > 10000:
            self.tax = .15 * 100
        else:
            self.tax = .12 * 100

    def display_all(self):
        print 'Price:' + str(self.price)
        print 'Speed ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.milage) + 'mpg'
        print 'Tax: ' + str(self.tax)
        return self
car_one = Car(20000, 35, 'full', 15)
car_one.display_all()
car_two = Car(2000, 5, 'Not Full', 105)
car_two.display_all()
car_three = Car(2000, 15, 'Kind of full', 19)
car_three.display_all()
car_four = Car(2000, 25, 'Full', 25)
car_four.display_all()
car_five = Car(2000, 45, 'Empty', 22)
car_five.display_all()
car_six = Car(20000000, 35, 'Full', 30)
car_six.display_all()
