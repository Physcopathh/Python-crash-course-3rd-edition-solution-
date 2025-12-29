users = ['admin','shaheer','z','timi','mishi']
for user in users:
    if user == 'admin':
        print(f'Hello {user.title()},Would you like to see the dashboard?\n')
    else:
        print(f'Hello {user.title()}, Thank You for logging in, into our website.com')