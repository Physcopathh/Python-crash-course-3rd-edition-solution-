person_a = {
            'firstname':'Rawal',
            'lastname':'Initiz',
            'city':'Hyderabad',
            'age':17
            }

person_b = {
            'firstname':'Shaheer',
            'lastname':'Hussain',
            'city':'Karachi',
            'age':18
}

person_c = {
            'firstname':'Yousra',
            'lastname':'Kashkali',
            'city':'Hyderabad',
            'age':19
}

peoples = [person_a, person_b, person_c]
for people in peoples:
    for key,value in people.items():
        print(key.title(),':',value)
    print('\n')