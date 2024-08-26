# Object Oriented Programming
# Classes - Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# Inheritance - in OOP, when a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods.

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

# Polymorphism - The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()