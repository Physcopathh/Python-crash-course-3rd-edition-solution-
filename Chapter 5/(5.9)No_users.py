users = []
if users ==  []:
    print('WE NEED TO FIND SOME USERS')
else:
    for user in users:
        if user == 'admin':
            print(f'Hello {user.title()},Would you like to see the dashboard?\n')
        else:
            print(f'Hello {user.title()}, Thank You for logging in, into our website.com')