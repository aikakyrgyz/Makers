class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        #cannot make the set_password function with @property
        #since this function requires an argument
        #the function must have only one argument - self
    def get_password(self, username):
        if self.username == username:
            return self.__password  
        else:
            return 'there is no account'
    #cannot use setter
    #setter decorator can only accept TWO arguments - self and another parameter
    def set_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
        else:
            return 'old passwords do not match'
    def get_info(self):
        print(f'Username {self.username}, password {self.__password}')

user1 = User(username = 'aikakyrgyz', password = 'Aigerim')
print(user1.username)

#access modifiers:
# public - password, get_info()
#protected - _password, _get_info()
#private - __password, __get_info()

class Divider:
    def __init__(self):
        self.__divide_num = 1
    @property
    def divider(self):
        return self.__divide_num
    @divider.setter
    def divider(self, value):
        self.__divide_num = 2
    def divide(self, value):
        return value/self.__divide_num

obj = Divider()
print(obj.divider) #after using the decorator, no need to use ()
print(obj.divide(7))
obj.divider = 14



# @property - decorator that lets us to access the methods 
#of the class as the variables of the class, wihtout ()
#func_name.setter - setter
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    @property
    def full_name(self):
        return f'{self.name}, {self.last_name}'

person = Person('Aika', 'K')
print(person.full_name)
#can't change the attribute full_name
#person.full_name = 'name last name' #syntax error

class Car:
    def _inject_fuel(self):
        print('Fuel injected')
    def _init_bang(self):
        print('Bang')
    def _send_signal_to_ignition_system(self):
        print('Ignition started')
        self._inject_fuel()
        self._init_bang()

    def _send_signal_to_pc(self):
        print("Start")
        self._send_signal_to_ignition_system()

    def start_engine(self):
        self._send_signal_to_pc()

car = Car()
car.start_engine()
car._init_bang() #we can access protected members

# difference between protected and private

#protected attributes are:
#1. underscore
#2. we can access the protected variables and methods
#3. protected members are inherited by child classes


#private members are NOT inherited by the child class
# class A:
#     def __private_method(self):
#         print('Private function')

# class B(A):
#     pass

# b = B()
# b.__private_method() #AttributeError: 'B' object has no attribute '__private_method'

#pprotected members ARE inherited by the child class
class A:
    def _protected_method(self):
        print('Protected function')

class B(A):
    pass

b = B()
b._protected_method()


