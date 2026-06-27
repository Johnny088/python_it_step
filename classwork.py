print("hello")

print('10' + '10')

integer = 10_000_000

for number in range(1, 10_000):
    print(number)

    text = 'testing'

# for index in range(len(text)):   #not a good way
#     print(text[index])

for char in text:       #best practice
    print(char)

for index,char in enumerate(text):
    print(f"index: {index} ... char: {char}")


test_search = (['python', 'c++', 'c#', 'java', 'rubi'])

test_word = input('type the word: ').lower()

isFound = False

for index, word in enumerate(test_search):
    if word == test_word:
        print(word)
        print (f"word: '{word}' was found in the list")
        isFound = True
        break

if not isFound:
    print("word wasn't found")