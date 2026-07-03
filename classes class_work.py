class Human:
    def __init__(self, name, age): #self is like this in c#
        self.name = name
        self.age = age
    def show(self):
        print(f'name: {self.name}, age: {self.age}')
    def method(self):
        print('function is working')
    def __len__(self):
        return len(self.name)
    def __int__(self):
        return self.age



person1 = Human('Johnny', 25)

person1.show()

person1.name = 'Bob'

person1.show()

age = int(person1)

print(age)

print(len(person1))

person1.method()