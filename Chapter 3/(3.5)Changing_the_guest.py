peoples = ['Asmar','Fazle Shahil','Kamran_gemini']
print(f'Hello {peoples[0]} you are invited to dinner')
print(f'Hello {peoples[1]} you are invited to dinner')
print(f'Hello {peoples[2]} you are invited to dinner')
print(f"\tSorry {peoples[2]} can't make it")
peoples.pop(2)
peoples.append('Shehla')
print(f'\n\t\tHello {peoples[2]} you are invited to dinner, A special invite to you!')