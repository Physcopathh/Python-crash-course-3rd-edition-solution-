age = int(input('What\'s your age sir... '))

if age < 3:
    print('For you ticket is free')
elif 3 <= age <= 12:
    print(f'{10}$ is your ticket price')
else:
    print(f'{15}$ is your ticket price')
    