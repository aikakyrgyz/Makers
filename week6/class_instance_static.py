''' 
instance method - self
class method - @classmethod, cls
static method - @staticmethod
'''
# class Makers:
#     language_choices = 'Python', 'JavaScript'
#     def __init__(self, name):
#         self.name =name
#     def method1(self):
#         return f'Hello {self.name}'
#     def method2(self):
#         return f'Welcome, chose your language? {self.language_choices}'
#     def method3(self, choice):
#         return f'Great! You chose {choice}'

# student1 = Makers('Aika')
# print(student1.method1())
# print(student1.method2())
# print(student1.method3(choice = 'Python'))class Makers:
class Makers:
    language_choices = 'Python', 'JavaScript' #variable of the class
    def __init__(self, name):
        self.name =name
    def instance_method(self):
        return f'Hello {self.name}'
    @classmethod
    def method2(cls):
        return f'Welcome, choose your language? {cls.language_choices}'
    @staticmethod
    def method3(choice):
        return f'Great! You chose {choice}'

student1 = Makers('Aika')
print(student1.instance_method())
print(student1.method2())
print(student1.method3(choice = 'Python'))


#use of class method
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_info(self):
        return f'{self.name}, {self.email}'
    @classmethod
    def add_data(cls, user_info:list): #creates object
        name, email = user_info
        return cls(name, email) #same as User(name, email) ->init
list_of_users =[['Aika', 'aika@gmail.com'], ['apple', 'apple@gmail.com']]
for info in list_of_users:
    user = User.add_data(info)
    print(user.get_info())
# user1 = User(name = "aika", email = 'aikamusiconly@gmail.com')
# print(user1.get_info())

class Lottery:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def generate_number():
        import random
        number = random.sample(list('123456789'), k=5)
        number = ''.join(number)
        return number
    def get_number(self):
        number = self.generate_number()
        self.number = number
        return f'Dear {self.name}! Your lucky number is {self.number}'
participant = Lottery('Alive')
print(participant.get_number())

class Pizza:
    def __init__(self, ingriedients:list):
        self.ingridients = ingriedients
    def __repr__(self):
        return f'Pizza with {self.ingridients}'
    @staticmethod
    def circle_area(radius):
        from math import pi 
        return round(pi*(radius**2))
    def area(self, radius):
        self.radius = radius
        return f'The area of your {self} is: {self.circle_area(radius)}'
    @classmethod
    def margarita(cls):
        return cls(['tomatoes', 'mozarella', 'basil'])
    @classmethod
    def pepperoni(cls):
        return cls(['pepperoni', 'cheese'])
pizza1 = Pizza.margarita()
print(pizza1.area(4))
pizza2 = Pizza.pepperoni()
print(pizza2)
print(pizza2.area(1))

