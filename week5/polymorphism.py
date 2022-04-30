a = 6
b =9
print(a+b)
##############################
c = '6'
d = '9'
print(c+d)
##############################
f = [1, 2, 3, 4, 5]
e = [6, 7, 8, 9, 10]
print(f+e)
##############################
'''dir'''
'''__add__'''
a = 'aika'
b = 7
c = [True, 'water']
d = {'name':'Aika'}
e = (1, 2, 3, 4, 5)
f = {False, 'water', 77}
print(f'String methods: {dir(a)}')
print(f'Int methods:{dir(b)}')
print(f'List methods:{dir(c)}')
print(f'Dict methods:{dir(d)}')
print(f'Tuple methods:{dir(e)}')
print(f'Set methods:{dir(c)}')
##############################
'''pop() ->list, dict, set'''
list_ = [1, 2, 3, 4, 5]
dict_ = dict(a=1, b=2, c=3)
set_ = {True, 'aika', 88, 99}

list_.pop(1)
dict_.pop('b')
set_.pop()

print(list_)
print(dict_)
print(set_)

#########################################################

#polymorphism in classes
class Car:
    def __init__(self, name):
        self.name = name
    def go(self, destination):
        print(f'{self.name} is goign by car to {destination}')
class Ship:
    def __init__(self, name):
        self.name = name
    def go(self, destination):
        print(f'{self.name} is goign by ship to {destination}')

class Airplane:
    def __init__(self, name):
        self.name = name
    def go(self, destination):
        print(f'{self.name} is flying to {destination}')
'''continued on polymorphism2.py'''
#########################################################

class infoMixin:
    def info(self):
        my_class = self.__class__.__name__
        print(f'I am a {my_class}, named {self.name}, age {self.age}')

class Cat(infoMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Meow")
class Dog(infoMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Guf")    
class Duck(infoMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Quack")  


cat = Duck('Tom', 7)
cat.info()
'''continued on polymorphism2.py '''
###########################################

class T1:
    def __init__(self, iterable):
        self.list = iterable
    def total(self):
        return sum(self.list)

class T2:
    def __init__(self, iterable):
        self.list = iterable
    def total(self):
        return len(self.list)

t1 = T1([1, 2, 3, 4, 5])
t2 = T2([1, 2, 3, 4, 5])
print(t1.total())
print(t2.total())

#####################################################
class GraphicalEntity: 
    def __init__(self, pos_x, pos_y, size_x, size_y): 
        self.pos_x = pos_x 
        self.pos_y = pos_y 
        self.size_x = size_x 
        self.size_y = size_y 
class Button(GraphicalEntity): 
    def __init__(self, pos_x, pos_y, size_x, size_y): 
        super().__init__(pos_x, pos_y, size_x, size_y) 
        self.status = False 
    def toggle(self): 
        self.status = not self.status 
class LimitSizeMixin: 
    def __init__(self, pos_x, pos_y, size): 
        size_x = min(size_x, 500) 
        size_y = min(size_y, 400) 
        super().__init__(pos_x, pos_y, size_x, size_y) 
class LimitSizeButton(Button, LimitSizeMixin): 
    pass 


b = LimitSizeButton(10, 20, 200, 100)
print(b.pos_x)
print(b.pos_y)
print(b.size_x)
print(b.size_y)
#####################################
class AbstractionMixin:
    def go(self):
        return 'Go'
class Car(AbstractionMixin):
    def go(self):
        # print('Go by car')
        super().go() # returned value is rewritten by the following return
        return 'car'
class Ship(AbstractionMixin):
    def go(self):
        print('Go by ship')

a = AbstractionMixin()
a.go()
car = Car()
ship = Ship()
print(car.go())

################################################
class MyInt(int):
    def __init__(self, num1):
        self.num1 = num1
    def __add__(self,num2):
        print("It is addition")
        return self.num1 +num2
        
class MyString(str):
    def __init__(self, str1):
        self.str1 = str1
    def __add__(self, str2):
        print("It is concatenation")
        return self.str1 +str2

int_ = MyInt(5)
print(int_+5)
print(int_.__add__(5))


str_ = MyString('app')
print(str_.__add__('store'))
print(str_.__add__('7'))
