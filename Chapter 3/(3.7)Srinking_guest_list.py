peoples = ['Asmar','Fazle Shahil','Kamran_gemini']
print(f'Hello {peoples[0]} you are invited to dinner')
print(f'Hello {peoples[1]} you are invited to dinner')
print(f'Hello {peoples[2]} you are invited to dinner')
print(f"\n\tSorry {peoples[2]} can't make it")
peoples.pop(2)
peoples.append('Shehla')
print(f'\n\tHello {peoples[2]} you are invited to dinner, A special invite to you!')
print(f"\n Hello '{peoples[0]}, {peoples[1]}, {peoples[2]}', we have found ourself bigger table!")
peoples.insert(0,'Shaheer')
peoples.insert(2,'Laiba')
peoples.append('Talha')

print(f'\nHELLO OUR GUESTS YOU ARE INVITED TO OUR NEW DINNER TABLE MY DEAR {peoples[0]}')
print(f'HELLO OUR GUESTS YOU ARE INVITED TO OUR NEW DINNER TABLE MY DEAR {peoples[1]}')
print(f'HELLO OUR GUESTS YOU ARE INVITED TO OUR NEW DINNER TABLE MY DEAR {peoples[2]}')
print(f'HELLO OUR GUESTS YOU ARE INVITED TO OUR NEW DINNER TABLE MY DEAR {peoples[3]}')
print(f'HELLO OUR GUESTS YOU ARE INVITED TO OUR NEW DINNER TABLE MY DEAR {peoples[4]}')
print(f'HELLO OUR GUESTS YOU ARE INVITED TO OUR NEW DINNER TABLE MY DEAR {peoples[5]}')

print('\n\n\t"You Can Only Invite Two Guests Only"')

print(f'\n"Sorry my dear {peoples.pop()} I can\'t invite you to dinner my bad"')
print(f'"Sorry my dear {peoples.pop()} I can\'t invite you to dinner my bad"')
print(f'"Sorry my dear {peoples.pop()} I can\'t invite you to dinner my bad"')
print(f'"Sorry my dear {peoples.pop()} I can\'t invite you to dinner my bad"')

print(f'\n{peoples[0]} and {peoples[1]} are still invited to dinner')

del peoples[0:]

print(peoples)