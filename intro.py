task1 = '''Дано рядок. Порахуй частоту кожної літери, а потім — скільки
літер мають однакову частоту. Результатом дайте словники.
ввід: "aabbccc" '''

print(f'\033[33m{task1}\033[36m')

dict = {'a':2, 'b':2, 'c':3}

print(f'{dict} \033[32m')

newDict = {}

for value in dict.values():
    if value in newDict:
        newDict[value] +=1
    else:
        newDict[value] = 1

print(newDict)

task2 = '''Є список чисел. Перевір, чи числа в ньому утворюють зигзаг —
тобто
a1 < a2 > a3 < a4 > a5 ... або навпаки:
a1 > a2 < a3 > a4 < a5 ...
[1, 3, 2, 4, 3] → так
[1, 2, 3, 4] → ні
[5, 1, 6, 2, 7] → так'''

print(f'\033[33m{task2}\033[32m')

test1 = [1,3,2,4,3]
test2 = [1,2,3,4]
test3 = [5,1,6,2,7]



def check_zigzag (list):
    if len(list) < 2:
        return True


    starts_up = all(
        (list[i] < list[i + 1]
         if i % 2 == 0
         else list[i] > list[i + 1])
        for i in range(len(list) - 1)
    )

    starts_down = all(
        (list[i] > list[i + 1]
         if i % 2 == 0
         else list[i] < list[i + 1])
        for i in range(len(list) - 1)
    )

    return starts_up or starts_down

print(f'if {test1} is a zigzag: {check_zigzag(test1)}')
print(f'if {test2} is a zigzag: {check_zigzag(test2)}')
print(f'if {test3} is a zigzag: {check_zigzag(test3)}\033[33m')

task3 = '''Є два користувачі й множини їхніх знайомих. Потрібно знайти тих,
з ким знайомий лише один з них, але не обидва.
user1 = {"Alice", "Bob", "Charlie"}
user2 = {"Bob", "Diana", "Eve"}
→ {"Alice", "Charlie", "Diana", "Eve"}'''

print(task3)

user1 = {"Alice", "Bob", "Charlie"}
user2 = {"Bob", "Diana", "Eve"}

print(type(user1))

def get_unique_names(list1, list2):
    set1 = list1.difference(list2)
    set2 = list2.difference(list1)
    set1.update(set2)
    return set1

set = get_unique_names(user1,user2)

print(set)