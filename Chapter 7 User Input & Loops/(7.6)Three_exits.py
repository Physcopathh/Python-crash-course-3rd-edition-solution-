#FROM 7.4 pizza topping
prompt = 'Tell me what topping you like'
prompt += '\n enter\'quit\' to stop: '
topping = str(input(prompt))

while True:
    if topping.strip() == 'quit':
        break   
    else:
        print(f'\nadding {topping} to your pizza\n')
        topping = str(input(prompt))

x = True
while x:
    if topping.strip() == 'quit':
        x = False
    print(f'\nadding {topping} to your pizza\n')
    topping = str(input(prompt))

while True:
    if topping.strip() == 'quit':
        break
    print(f'\nadding {topping} to your pizza\n')
    topping = str(input(prompt))



#From movie ticket.py 7.5
while True:
    age = input('What\'s your age sir... ')

    if age == 'quit':
        break
    elif int(age) < 3:
        print('For you ticket is free')
    elif 3 <= int(age) <= 12:
        print(f'{10}$ is your ticket price')
    else:
        print(f'{15}$ is your ticket price')
 
x = True
while x:
    age = input('What\'s your age sir... ')

    if age == 'quit':
        x = False
    elif int(age) < 3:
        print('For you ticket is free')
    elif 3 <= int(age) <= 12:
        print(f'{10}$ is your ticket price')
    else:
        print(f'{15}$ is your ticket price')
    
while True:
    age = input('What\'s your age sir... ')

    if age == 'quit':
        break

    if age < '3':
        print('For you ticket is free')
    elif 3 <= age <= '12':
        print(f'{10}$ is your ticket price')
    else:
        print(f'{15}$ is your ticket price')
    