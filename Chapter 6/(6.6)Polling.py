favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
peoples = ['jen','Taimoor','Yousra','Understand krta hai','love you mwhhh!']
for people in peoples:
    if people in favorite_languages.keys():
        print(f'Thanks for taking the poll, {people.title()}\n')
    else:
        print(f'{people.title()}, You should take the poll\n')
