sandwich_orders = ['Kabab sandwich', 'Cheeze Sandwich', 'Yellow sandwich']
finished_sandwich_orders = []
while sandwich_orders != []:
    finished_sandwich = sandwich_orders.pop()
    print(f'Made your {finished_sandwich}')
    finished_sandwich_orders.append(finished_sandwich)

for sandwich in finished_sandwich_orders:
    print('\n', sandwich, 'is made')