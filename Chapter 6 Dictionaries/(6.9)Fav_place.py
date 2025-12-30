fav_places = {
    'Asmar':{'Dubai','karachi','pakwan center'},
    'Shaheer':{'Pakwan center','game'},
    'Laiba':{'monga'},
}

for key,value in fav_places.items():
    print(key.title(),'Fav places are:')
    for key in value:
        print(key)
    print('\n')