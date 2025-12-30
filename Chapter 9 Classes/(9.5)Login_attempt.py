class User:
    def __init__(self,firstname,lastname,login_attempt=0,**otherinfo):
        self.firstname = firstname
        self.lastname = lastname
        self.completename = firstname +' '+ lastname
        self.login_attempt = login_attempt
        self.otherinfo = otherinfo

    def describe_user(self):
        print(f'The user name is {self.completename}, firstname = {self.firstname}, and lastname = {self.lastname}')
        for key,value in self.otherinfo.items():
            print(key,'=',value,end=',\n')\
            
    def greet_user(self):
        print(f'Hola {self.completename}')

    def increment_user_attempt(self):
        self.login_attempt += 1
    
    def reset_login_attempt(self):
        self.login_attempt = 0

vivo = User('Mobile','Phone',version='oreo andiord',ram='6gb',rom=128,core='octa-core',price=8000)
print(vivo.login_attempt)
vivo.increment_user_attempt()
vivo.increment_user_attempt()
vivo.increment_user_attempt()
vivo.increment_user_attempt()
print(vivo.login_attempt)
vivo.reset_login_attempt()
print(vivo.login_attempt)