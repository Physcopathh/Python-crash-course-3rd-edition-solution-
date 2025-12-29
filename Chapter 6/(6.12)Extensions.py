fav_places = {
    'Asmar':{'Dubai','karachi','pakwan center'},
    'Shaheer':{'Pakwan center','game'},
    'Laiba':{'monga'},
    'Shawal':{'hello'},
    'this':'that',
}

for key,value in fav_places.items():
    print(key.title(),'Fav places are:')
    # adding if and else statement
    if type(value) == set and len(value) > 1:
        for key in value:
            print(key)
        print('\n')
    elif type(value) == set and len(value) == 1:
        a = ''
        for v in value:
            a+=v          #looping and adding the value to a variable a then printing it eventually!
        print(a,'\n')
    else:
        print(value,'\n')

