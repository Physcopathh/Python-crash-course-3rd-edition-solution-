class Resturant:
    def __init__(self,resturant_name,cuisine_type,number_served=0):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def desrible_resturant(self):
        print(f'The name of this resturant is {self.resturant_name} with cuisine type of {self.cuisine_type}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is now open')

    def cus_served(self):
        if self.number_served == 0:
            print(f'{self.resturant_name} hasn\'t served anyone!')
        else:
            print(f'{self.resturant_name} have served {self.number_served} customer')

    def set_num_served(self,amount):
        self.number_served += amount
        print(f'a day of business the numbers served were {self.number_served}')

resturant = Resturant('Al-Fajr','Launge',20)
resturant.cus_served()
resturant.set_num_served(19)
resturant.cus_served()

resturant = Resturant('Al-Fajr','Launge')
resturant.cus_served()