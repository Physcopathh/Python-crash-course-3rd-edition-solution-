def make_car(manifatular, model, **info_car):
    info_car['Manifactural'] = manifatular
    info_car['model'] = model
    return info_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#Boys commitment I am doing it