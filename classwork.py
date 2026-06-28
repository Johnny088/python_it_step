class Human:
    def __init__(self, name: str, age: int):  # init - метод-конструктор
        self.name = name
        self.age = age
        self.money = 100

    def __str__(self):
        return f'Human {self.name}'

    def __int__(self):
        return self.age

    def __len__(self):
        return len(self.name)

    def __add__(self, other):  # self + other
        if type(other) is not Human:
            raise ValueError('Додавати можна тільки людину до людини!')

        return self.age + other.age

    def __gt__(self, other):  # self > other
        return int(self) > int(other)

    def say_hi(self):
        print(f'Hello, my name is {self.name}! I`m {self.age} y.o.')

    def birthday(self, years: int):
        self.age += years
        print(f'{self.name} виповнилося {self.age} років!')