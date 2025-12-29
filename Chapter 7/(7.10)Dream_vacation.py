x = {}
while True:
    user= input('what is your name' )
    vacation = input('Place, you going as dream place: ')
    x[user] = vacation

    yes_no = input('wanna do more poll?. ')
    if 'no' == yes_no:
        for a, b in x.items():
            print(f'\n{a} dream place is {b}')
        break