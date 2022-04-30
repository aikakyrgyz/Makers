# def name_of_function():
#     some_code
#     return variable
# name_of_function()



def no_return_function():
    print('Function is called')

print(no_return_function()) #if the function does not return anything, by default if will return none

def my_function():
    return 1+3

list_ = [1, 2, 3, my_function()] #we can pass the function to the list
print(list_)


def my_function2():
    print("This function calls my_function")
    print(my_function())

print(my_function2())

def welcome(name, last_name):
    return f'Welcome {name} {last_name}'
name = input('Enter your name')
last_name = input("Enter your last name ")
print(welcome(name, last_name))


def make_list(word):
    list_ = list(word)
    return list_
print(make_list('Aika'))

def get_vowels(word):
    list_ = ['a', 'o', 'u', 'i', 'e', 'y']
    list_vowels = [letter for letter in word if letter in list_]
    result = ''.join(list_vowels)
    return result

print(get_vowels(make_list('aika')))

def info(name, age):
    print( f'{name} and {age}')
#positional arguments
info('Aika', 16)
#keyword arguments
info(age = 19, name ='Aika')
#default argument:
def info(name, age = 18):
    print(f'{name} and {age}')

#positional argument must be before keyword argument

# we can rewrite the default argument

def profile(name, age, pic = 'default.jpg'):
    print(f'Your {name}, your age {age} and pic is {pic}')

profile('Aika', 21)
profile('Aika', 21, 'selfie.jpg')


def func(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
func('Aika') #Aika
func('Aika', 'in', 'tuple')  #Aika
                             #('in', 'tuple')
func('Aika', 'in', 'tuple', name = 'Aika', age= 21) 
#Aika
#('in', 'tuple')
#{'name': 'Aika', 'age': 21} 



def func(*tuple_, **dict_):
    print(tuple_)
    print(dict_)

func()
#() 
#{}

func('Aika', 'Altynai')
#('Aika', 'Altynai')

func('tuple', name= 'Aika', age= 21, sister = 'Altynai')
#('tuple',)
#{'name': 'Aika', 'age': 21, 'sister': 'Altynai'}


#dictionary (kwargs)
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

list_ = [1, 2, 3, 4]
 def func(passed_list = list_):



func(list_2)
def func(name, **info):
    profile = {}
    profile['name'] = name
    for key, value in info.items():
        profile[key] = value
    return profile


print(func('spartanov',location='Makers',field='python'))

