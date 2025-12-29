#FIRST!!!----------------------------------------------------------------------------------------------------------------
pizza = ['Chicken','Cheeze','Chocolate']
for p in pizza:
    print(f'\nI sometime loves {p} Pizza')

print('\nI love the pizza this much and that much\nI love it that much that this much\nThat much bro\n\nI am lying for the sake of course but "I really love pizza"')

friends_pizza = pizza[:]
pizza.append('Lemon')
friends_pizza.append('Vanilla')

print(f"\nMy pizzas are:")
for i in pizza:
    print(f'{i} Pizza')

print('\nMy friend\'s pizzas are:')
for i in friends_pizza:
    print(f'{i} Pizza')



#SECOND!!!---------------------------------------------------------------------------------------------------------------
'''
animals = ['Cat','Dog','Loin']
for animal in animals:
    print(animal)
'''

#SECOND PART
animals = ['Cat','Dog','Loin']
for animal in animals:
    print(f'{animal} would be a great pet\n')

print('\n\t"These animal walk on 4 leg\'s"')



#THIRD!!!-----------------------------------------------------------------------------------------------------------------
cubes = [value**3 for value in range(1,11)]
print(cubes)

print('\nThe first three numbers are:')
print('\t',cubes[0:3])

print('\nThe middle three numbers are:')
print('\t',cubes[4:7])

print('\nThe last three numbers are:')
print('\t',cubes[-3:])