#task1

import random

class Sniper:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def shoot(self, sniper):
        sniper.health -=20

sniper1 = Sniper(name = 'Ben')
sniper2 = Sniper(name = 'Tom')

choices = (sniper1, sniper2)
while True:
    shooter = random.choice(choices)
    if shooter == sniper1:
        shot = sniper2
    else:
        shot = sniper1
    shooter.shoot(shot)
    print(f'Shooter {shooter.name} is shooting, {shot.name} has {shot.health} health points')
    
    if sniper1.health ==0:
        print(f'{sniper1.name} is dead. {sniper2.name} won')
        break
    elif sniper2.health ==0:
        print(f'{sniper2.name} is dead.{sniper1.name} won')
        break
    else:
        continue

#task2

class Hogwarts:
    dict_ = {'courage':'Gryffindor', 
              'intelligence': 'Ravenclaw',
              'justice':"Huflepuff",
              'ambition':'Slytherin'}
    def __init__(self, courage, intelligence, justice, ambition):
        self.courage = courage
        self.intelligence = intelligence
        self.justice = justice
        self.ambition = ambition
        self.qualities = locals()
    def sorting_hat(self):
        dictionary = {value:key for key, value in self.qualities.items() if type(value) ==int}
        max_point = max(dictionary.keys())
        max_quality = dictionary[max_point]
        self.faculty = Hogwarts.dict_[max_quality]
        print("You are admitted to", self.faculty)
        

student1 = Hogwarts(courage=5, intelligence =10, justice =4, ambition=0)
student1.sorting_hat()
student2 = Hogwarts(courage =10, intelligence = 4, justice = 3, ambition = 0)
student2.sorting_hat()
            



#practice

class A:
    pass

a = A()#object of class == exemplyar
print(isinstance(a, A)) #True

print(type(a)) #<class '__main__.A'>

class Car:
    car_count = 0
    def __init__(self):
        Car.car_count +=1 #refering to the class, not the object!

car1 = Car()
car2 = Car()
car3 = Car()
print(Car.car_count)


class Bag: 
    brand = 'gucchi'
    def buy_bag(self, brand): 
        self.brand = brand 


bag1 = Bag() 
bag2 = Bag() 
bag1.buy_bag('CHANEL') 
print(bag1.brand)  #CHANEL
print(bag2.brand) #gucchi/

class Lipstick: 
    color = 'red'
    def set_color(self, color): 
        self.color = color 
Lipstick().set_color('pink') 
print(Lipstick().color) 
#output: red
