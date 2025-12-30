peoples = {
    'Yousra':{2,4,5},
    'Taimoor':{2,4,5},
    'Asmar':{7},
    'Laiba':{5},
    'Fazle Shahil':{10,20}
    }

for people, numbers in peoples.items():
    if len(numbers) > 1:
        print(people.title(),'fav numbers are:')
        for number in numbers:
            print(number)
    else:
        print(people.title(),'fav number is',numbers)
