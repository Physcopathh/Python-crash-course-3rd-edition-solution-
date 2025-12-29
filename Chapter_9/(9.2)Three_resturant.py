class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def desrible_resturant(self):
        print(f'The name of this resturant is {self.resturant_name} with cuisine type of {self.cuisine_type}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is now open')


resturant = Resturant('Al-Fajr','Launge')
my_resturant = Resturant('Junaid-Burger','Classical')
their_resturant = Resturant('Humarah-Resturant','Humarah-type')
resturant.desrible_resturant()
my_resturant.desrible_resturant()
their_resturant.desrible_resturant()