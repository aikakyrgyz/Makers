class Grandpa:
    def talant(self):
        print('I am good at dancing')
class Grandma:
    def talant(self):
        print('I am good at singing')
class Father:
    # def talant(self):
        # print("I am good at writing")
    last_name = 'White'
class Mother(Grandpa, Grandma):
    last_name = 'Brown'
class Child(Father, Mother):
    pass
child = Child()
print(child.last_name)
child.talant()
print(Child.mro())

#first: looks for the first class in the paranthesis, 
#if that class has parents then looks in them, and only then 
#jumps to the second class in the paranthesis
#Here:->

class Grandpa:
    pass
class Grandma:
    pass
class Mother(Grandpa, Grandma):
    pass
class Father:
    pass
class Child(Mother, Father):
    pass

print(Child.mro())
# <class '__main__.Child'>, 
# <class '__main__.Mother'>, 
# <class '__main__.Grandpa'>,
#  <class '__main__.Grandma'>, 
#  <class '__main__.Father'>, 
#  <class 'object'>

#inheritance and parameters:
class A:
    def __init__(self, param):
        print(f'A class parameter: {param}')

class B:
    def __init__(self, param):
        print(f'B class parameter: {param}')

class C(A, B):
    pass

c = C(param = 'apple') #A class parameter apple
print(C.mro()) #[<class '__main__.C'>,
                # <class '__main__.A'>, 
                # <class '__main__.B'>,
                #  <class 'object'>]

# # parameters must match passed must match with the first occurance of the fun
# class A:
#     def __init__(self, param, param2):
#         print(f'A class parameter: {param}')
#     def get(self):
#         print('AAAAA')
# class B:
#     def __init__(self, param):
#         print(f'B class parameter: {param}')
#     def get(self):
#         print('B')
# class C(A, B):
#     def get(self):
#         print('C')

# c = C(param = 'apple')#__init__() missing 1 required positional argument: 'param2'
# print(C.mro())
# ######################

class A:
    def __init__(self, param, param2):
        print(f'A class parameter: {param}')
    def get(self):
        print('AAAAA')
class B:
    def __init__(self, param):
        print(f'B class parameter: {param}')
    def get(self):
        print('B')
class C(A, B):
    def get(self):
        print('C')

c = C(param = 'apple', param2 = 'cherry')#__init__() missing 1 required positional argument: 'param2'
print(C.mro())
c.get() #C

#Diamond Problem
class A:
    def f(self):
        print('A')
class B(A):
    # def f(self):
    #     print('B')
    pass
class C(A):
    def f(self):
        print("C")
class D(B, C):
    # def f(self):
    #     print('D')
    pass

d = D()
d.f() #D

######
class A:
    def f(self):
        print('A')
class B(A):
    def f(self):
        super().f()
        print('B')
class C(A):
    def f(self):
        super().f()
        print('C')
class D(B, C):
    pass

d = D()
d.f()
#A
#C
#B

#Mixins:

class Insect:
    pass
class Bird:
    def __init__(self):
        print("Bird")
class FlyMixin:
    def fly(self):
        print('I can fly')
class Hawk(Bird, FlyMixin):
    pass
class Eagle(Bird, FlyMixin):
    pass
class Butterfly(Insect, FlyMixin):
    pass
class Pinguin(Bird):
    pass
hawk = Hawk()
hawk.fly()
eagle = Eagle()
eagle.fly()
butterfly= Butterfly()
butterfly.fly()
pinguin = Pinguin()

#classes of different parent classes can inherit Mixin
class Gadgets:
    pass
class Vehicle:
    pass
class RadioMixin:
    pass
class Car(Vehicle, RadioMixin):
    pass
class Phone(Gadgets, RadioMixin):
    pass
######
class A: 
    def hello(self): 
        print('hello world') 
class B: 
    def hello(self): 
        print('HELLO WORLD') 
class C(A, B): 
    pass 

obj = C() 
obj.hello()  #hello world

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
class LimitSizeButton(Button, LimitSizeMixin): pass 
b = LimitSizeButton(10, 20, 200, 100)
#lecture
# class IceCream():
#     def __init__(self, flavor):
#         self.flavor = flavor
#     def melt(self):
#         print('Melting')

# class Cake():
#     def __init__(self, level:int):
#         self.level = level
#     def add_extra_level(self):
#         self.level +=1

# class Developer:
#     projects = []
#     def __init__(self, language):
#         self.language = language
#         self.projects_count =0
#     def add_project(self, project):
#         self.projects_count+=1
#         self.projects_count+=1
#         print(f'New project {project} added')
# class Mentor(Teacher, Developer):
#     def __init__(self, langauge):
#         Developer.__init__(self, language)
#         self.group_count = 0

# nur = Menton('Python')
# print(nur.projects_count)
# print(nur.group_count)

class GmailMixin():
    def gmail_validate(self, email:str):
        if email.endswith('@gmail.com'):
            self.email = email
            print('Account created')
        else:
            print("Add @gmail.com extension")

class Gmail(GmailMixin):
    def __init__(self, email):
        super().gmail_validate(email)
