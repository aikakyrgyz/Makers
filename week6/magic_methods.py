# #1.dir()
class X:
    pass
obj = X()
print(dir(obj))
#'__class__', '__delattr__', '__dict__', '__dir__', 
# '__doc__', '__eq__', '__format__', 
print(dir(6))
print(dir('String'))
def func():
    pass
print(dir(func))

#2. __init__
# __new__
# __str__
#__repr__

#__init__
class User:
    def __init__(self, **kwargs):
        print('Object is initializing')
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']
        print('Object has been initialized')
user = User(name = 'Linus', lastname = 'Torvalds' )
#__new__
class Human(object):
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        instance = object.__new__(cls)
        instance.heart = '4 chambers' #all of the object created from this class will have the heart attribute
        print('Object created')
        return instance
    def __init__(self, name, lastname):
        print('Object is initializing')
        self.name = name
        self.lastname = lastname

human1 = Human(name='Linus', lastname = 'Torvalds')
print(human1.heart)
human2  = Human('Aika', 'K')
print(human2.heart)

#Singleton = is when we can create only one object from a class

class Sun:
    instance = None
    def __new__(cls):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance
sun1 = Sun()
sun2 = Sun()
sun3 = Sun()
print(sun1 is sun2) #sun1 and sun2 are the same object
# all 3 suns are the same objects

#__str__
class Human:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def get_full_name(self):
        return f'{self.name} {self.lastname}'
    def __str__(self): 
        return self.get_full_name()
human1 = Human('Aika', 'Kub')
print(human1) 


#__repr__ - similiar to __str__.When there is no __str__ method, __repr__ takes ahold
class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name} str method'
    def __repr__(self):
        return f'{self.name} repr method'
human1 = Human('Aika')
print(human1) 
# >>> human = Human('Aika')
# >>> print(human)
# Aika str method
# >>> human
# Aika repr method
'''
__add__(self, other) -> +
__sub__(self, other)-> -
__mul__(self, other) -> *
__truediv__(self, other) -> /
__mod__(self, other) -> %
'''
class MyInt(int):
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        print('custom add')
        return self.value + other
    def __sub__(self, other):
        print("Custom sub")
        return self.value - other
    def __mul__(self, other):
        print('Custom mul')
        return self.value * other
    def __rtruediv__(self, other):
        return other/self.value
a = MyInt(10)
print(a+5)
print(a-5)
print(a*3)
print(10-a) #use __rsub__
print(a-11) #use __sub__
print(20/a) 
#Reflected arithmetic operators
# other - value (flipped)
'''
def __radd__(self, other):
    return other +self.value
def __rsub__(self, other):
    return other -self.value
def __rtruediv__(self, other):
    return other/self.value
'''

#Sostavnoe prisvainvanie
'''
a =1
a+=7

def __iadd__(self, other):
    return self.value + other
a = 1
a+=7
print(a) #returns 8

'''
#magid methods of comparison
'''
__eq__ - ==
__ne__ - !=
__gt__ - >
__lt__ - <
__le__ - <=
__ge__ - >=
'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age  == other.age
    def __ne__(self, other):
        return self.age!=other.age
    def __gt__(self, other):
        return len(self.name) >len(other.name)
    def __lt__(self, other):
        return len(self.name)<len(other.name)


human1 = Human('aika', 21)
human2 = Human('altyna', 16)
print(human1 ==human2) #false #ages not the same
print(human1!=human2) # true, ages are different
print(human1 >human2) #false, aika is shorter than altyna
print(human1<human2)

#3. __getattr__, __setattr__, __delattr__
class MyClass:
    def __init__(self):
        self.name = 'Aika'
        print(self.__dict__)#{'name': 'Aika'}
    def __getattr__(self, item):
        print('__getattr__')
        return self.__dict__.get(item, 'no such attribute')
    def __getattribute__(self, item):
        print('__getattribute__')
        return super().__getattribute__(item)
    def __setattr__(self, item, value):
        print(f'Setting attribute {item} = {value}')
        self.__dict__[item] = value 
    def __delattr__(self, item):
        print('Deleteing ', item)
        self.__dict__.pop(item, 0)      
obj = MyClass()
# print(obj.age)#no such attribute
# print(obj.name)
# obj.name = 'newname'
obj.age = 2
del obj.name
print(MyClass.__dict__)
# __getattr__ and __getattribute__ difference
#__getattr__ works only when the attribute does not exist
#__getattribute__ works any time


'''
__len__ -> len()
__getitem __(self, key) - > self.key
__setitem__(self, key, value) ->self.key = value
__delitem__(self, key) ->del self[key]
__contains__(self, item) -> item in self or item not in self- > true or false
'''
class MyClass(dict):
    def __getitem__(self, key):
        print('custom getitem')
        return super().__getitem__(key)
    def __setitem__(self, key, value):
        value +=1
        super().__setitem__(key, value)

dict_ = MyClass(a=1, b=2)
print(dict_)
dict_['a'] = 1 #setting item
print(dict_['a'])

class MyList(list):
    def __init__(self, iterable):
        self.list = iterable
    def __contains__(self, item):
        if item in self.list:
            return True
        else:
            return False
a = MyList([1, 2, 3, 4, 5])
print(3 in a) #True
print(99 in a) #False

class MyClass:
    def __del__(self):
        print('Object is deleted')
obj = MyClass()
del obj

from os.path import join 
class FileObject: 
    def __init__(self, filepath='~', filename='sample.txt'): 
 # открыть файл filename в filepath в режиме чтения и записи
        self.file = open(join(filepath, filename), 'r+') 
    def __del__(self): 
        self.file.close() 
        del self.file
obj = FileObject()
print(obj.file)
#delets the attribute
#__delattr__ is triggered