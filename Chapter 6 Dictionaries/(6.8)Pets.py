animal_a = {
    'Pet':'cat',
    'owneer':'noone'
}

animal_b = {
    'Pet':'cell',
    'owner':'battery',
    'age':'12'
}

animal_c = {
    'Pet':'elephant',
    'owner':'not me'
}

animal_d = {
    'Pet':'dog',
    'owner':'dadi'
}

pets = [animal_a, animal_b, animal_c, animal_d]
for pet in pets:
    for key,value in pet.items():
        print(key.title(),':',value.title())
    print('\n')