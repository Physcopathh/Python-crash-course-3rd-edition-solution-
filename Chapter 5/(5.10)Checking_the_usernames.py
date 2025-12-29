current_users = ['Shaheer','Timi','Z','Mewish','Fazle Shahil']
new_users = ['Aisha','Laiba','  timi','Torch','Mewish']

for new in new_users:
    if new.lower().strip() in [user.lower().strip() for user in current_users]:
        print(f'"{new.replace(' ','_')}" is already in use, PLEASE ENTER DIFFERENT NAME\n')
    else:
        print(f'"{new}" Avaiable You Can Use It!\n')
        