import random

greeting = ('hello', 'good morning', 'good day', 'good afternoon', 'hey', "what's up")



class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Store:
    def __init__(self, item: Item = None):
        self.products: list[Item] = []
        if item is not None:
            self.products.append(item)

    def addItem(self, item: Item):
        self.products.append(item)

    def logAllItems(self):
        if not self.products:
            print('The store is empty')
            return
        for i in self.products:
            print(f'name: {i.name} price: {i.price}')

    def __contains__(self, other):
        for i in self.products:
            if i.name == other.name and i.price == other.price:
                return True
        return False


testStore = Store()

print('-----------------An empty store-----------------')

testStore.logAllItems()

print('-----------------Showing all the products-----------------')

testStore.addItem(Item('test1',3_000_000))

testStore.addItem(Item('test2',30_00))

testStore.addItem(Item('test3',3000_00))

testStore.logAllItems()

print('----------------- existing item -----------------')

print((Item('test3',3000_00) in testStore))

print('-----------------item is not in the list -----------------')

print((Item('test4',3000_00) in testStore))

#task2

class Car:
    def __init__(self, name: str, places: int):
        self.name = name,
        self.places = places
        self.passengers: list[Human] = []

    def addPassenger(self, person: Human):

        if len(self.passengers) < self.places:
            person.sayHi()
            self.passengers.append(person)
        else:
            print ('Driver: The car is overcrowded you can use your legs...')

    def showAllPassengers(self):
        if len(self.passengers) < 1:
            print('the car is empty')
        else:
            for i in self.passengers:
                print(f'name: {i.name} {i.age} years old:')

    def __len__(self):
        return len(self.passengers)



class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def sayHi(self):
        print(f'{self.name}: {random.choice(greeting)}')

person1 = Human('Jonny', 25)
person2 = Human('Stacy', 25)
person3 = Human('Jeniffer', 25)
person4 = Human('Bob', 25)
person5 = Human('Bruce', 25)


car1 = Car('Honda', 3)

print('length of an empty car: ', len(car1))

car1.addPassenger(person1)
car1.addPassenger(person2)
car1.addPassenger(person3)
car1.addPassenger(person4)
car1.addPassenger(person5)

print('length of the crowded car: ', len(car1))








