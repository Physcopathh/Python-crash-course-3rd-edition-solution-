class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def desrible_resturant(self):
        print(f'The name of this resturant is {self.resturant_name} with cuisine type of {self.cuisine_type}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is now open')


resturant = Resturant('Al-Fajr','Launge')
resturant.desrible_resturant()
resturant.open_resturant()