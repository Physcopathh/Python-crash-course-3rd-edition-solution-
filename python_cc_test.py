# Write code here---okay
def unique_elements(user_lists):
    '''Extracting unqiue elements from list'''
    print('Cleaning your list...:')
    cleaned_list = []
    for x in user_lists:
        if x not in cleaned_list:
            cleaned_list.append(x)
    print(f'Here is your clean version:...\n\t{cleaned_list}')


that_list = [1,2,3,3,3,3,4,5]
unique_elements(that_list)


#adding some extra code
def make_list():
    '''Funcation to make it, tell it, it will make it for you'''
    written_list = []
    while True:
        try:
            x = int(input('How your is your list: '))
            break
        except:
            print('Please enter interger and try-again')
            continue

    while len(written_list) < x:
        user_item = input(f'Enter no.{len(written_list)+1} item of your list: ')
        written_list.append(user_item)
    return written_list

unique_elements(make_list())