cities = {
    'Hyderabad':{'Fav thing':'new-Yock','famous for':'my city'},
    'Karachi':{'Fav thing':'biryani','famous for':'biryani','you like':'biryani','???':'biryani!'},
    'Islamabad':{'Fav thing':'you dont know'}
}

for city, info in cities.items():
    print(city,':')
    for key, value in info.items():
        print(key,":",value)
    print('\n')