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