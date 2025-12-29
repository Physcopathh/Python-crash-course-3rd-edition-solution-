sandwich_orders = ['Pastrami sandwich', 'Kabab sandwich', 'Pastrami sandwich', 'Cheeze Sandwich', 'Yellow sandwich', 'Pastrami sandwich']

print('deli has ran out of pastrami!')
while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')
print(sandwich_orders)

finished_sandwich_orders = []
while sandwich_orders != []:
    finished_sandwich = sandwich_orders.pop()
    print(f'Made your {finished_sandwich}')
    finished_sandwich_orders.append(finished_sandwich)

for sandwich in finished_sandwich_orders:
    print('\n', sandwich, 'is made')