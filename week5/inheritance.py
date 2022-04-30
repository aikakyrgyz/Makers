class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) 
#same as
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(self, fname, lname) 
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#practice
####################
class Parent:
    pass
class Child(Parent):
    pass
####################
class A:
    pass
class B(A):
    pass
class C(B):
    pass
c = C()
print(isinstance(c, A)) #True
#####################
class Polygon:
    sides = 'many'
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def get_perimeter(self):
        if self.args:
            return sum(self.args)
        elif self.kwargs:
            return sum(self.kwargs.values())
class Rectangle(Polygon):
    sides = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    def get_perimeter(self):
        return (self.a+self.b)*2    
class Triangle(Polygon):
    sides = 3
    def __init__(self,a, b, c):
        self.a = a
        self.b = b 
        self.c = c
    def get_perimeter(self):
        return (self.a+self.b+self.c)
class Square(Rectangle):
    def __init__(self, a):
        self.a =a
    def get_perimeter(self):
        return self.a*4
#parent object
polygon = Polygon(8, 9, 3)
print(polygon.get_perimeter())
print(polygon.sides)
#child object
rectangle = Rectangle(7, 6)
print(rectangle.sides)
print(rectangle.get_perimeter())
#child object
triangle = Triangle(1, 1, 1)
print(triangle.sides)
print(triangle.get_perimeter())
#child object
square = Square(5)
print(square.sides) #accesses the sides in the Rectangle class
print(square.get_perimeter())
##################################

#int, tuple, dict, list, bool, str, set, frozenset
#redefine one of the dict items

class MyDict(dict):
    def get(self, key, default = 'No key'):
        print("This method has been changed")
        return dict.get(self, key, default)
dict1 = dict(a=3, b=5, c=8)
print(dict1.get('d')) #Output:none

dict2 = MyDict(a=3, b=5, c=7)
print(dict2.get('d')) #Output:This method has been changed
                      #       No key

###################################
class Person():
    def __init__(self, name, lastname, idnumber):
        self.name = name
        self.lastname = lastname
        self.idnumber = idnumber
    def get_info(self):
        print(f'{self.name} {self.lastname}, id: {self.idnumber}')

class Employee(Person):
    def __init__(self, name, lastname, idnumber, position, salary):
        super().__init__(name, lastname, idnumber)# do NOT use self when using super()
        self.position = position
        self.salary = salary
    def get_info(self):
        super().get_info()# do NOT use self when using super()
        print(f'Position: {self.position}, salary: {self.salary}')



#child object
employee = Employee('Aika', 'Kub', '1630632', 'programmer', '10000')
employee.get_info()
#####################################
class Art:
    students_count = 100

class Music(Art):
    students_count = 50
    def __init__(self):
        Music.students_count +=1
        Art.students_count+=1 #cannot do super().students_count

class Acting(Art):
    students_count = 30
    def __init__(self):
        Acting.students_count +=1
        Art.students_count+=1


student1 = Music()
student2 = Acting()
student3 = Acting()
print(student1.students_count)
print(student2.students_count)
print(student3.students_count)

#########################################
class Animal:
    def sound(self):
        raise NotImplementedError
class Cat(Animal):
    def sound(self):
        print('Meow')
class Dog(Animal):
    def sound(self):
        print('Uf')

animal = Animal()
animal.sound() # NotImplementedError
dog = Dog()
dog.sound() #Uf

########################################
class A:
    def __init__(self,name):
        print('A')
        self.name = name
class B(A):
    def __init__(self, name):
        print('B')
        A.__init__(self,name)

a = A('Aika')
print(a.name)
b = B('AikaBBBBB')
print(b.name)
print(a.name)
##########################################
class Person: 
    def __init__(self, name, age): 
        self.__name = name # устанавливаем имя 
        self.__age = age # устанавливаем возраст 
    @property 
    def age(self): 
 	    return self.__age 
    @age.setter 
    def age(self, age): 
        if age in range(1, 100): 
 	        self.__age = age 
        else: 
 	        print("Недопустимый возраст") 
    @property 
    def name(self): 
 	    return self.__name 
    def display_info(self): 
 	    print("Имя:", self.__name, "\tВозраст:", self.__age) 
class Employee(Person): 
    def details(self, company): 
 # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут 
 	    print(self.name, "работает в компании", company) 

tom = Employee("Tom", 23) 
tom.details("Google") 
tom.age = 33 
tom.display_info() 

# Output:
# Tom работает в компании Google
# Имя: Tom        Возраст: 33


