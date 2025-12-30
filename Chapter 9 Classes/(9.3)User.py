class User:
    def __init__(self,firstname,lastname,**otherinfo):
        self.firstname = firstname
        self.lastname = lastname
        self.completename = firstname +' '+ lastname
        self.otherinfo = otherinfo

    def describe_user(self):
        print(f'The user name is {self.completename}, firstname = {self.firstname}, and lastname = {self.lastname}')
        for key,value in self.otherinfo.items():
            print(key,'=',value,end=',\n')\
            
    def greet_user(self):
        print(f'Hola {self.completename}')

asmar = User('Asmar','Ali',cast='channa',lives='Hyderabad')
kamran = User('Kamran','Syed',visited='Dubai',lives='Karachi')
vivo = User('Mobile','Phone',version='oreo andiord',ram='6gb',rom=128,core='octa-core',price=8000)
asmar.describe_user()
asmar.greet_user()
kamran.describe_user()
kamran.greet_user()
vivo.describe_user()
vivo.greet_user()