#the variable is used for calling the function
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5)) 

#function inside another function
def plus_one(num):
    def add_one(number):
        return number+1
    result = add_one(num)
    return result
print(plus_one(4))


#functions can be passed as arguments to a function
def plus_one(number):
    return number+1
def function_call(function):
    number_to_add = 5
    return function(number_to_add)
print(function_call(plus_one))

#function can generate another function:
def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi
hello = hello_function
print(hello())

#python lets the inner function to access its local namespace
#it is called enclosion

def print_message(message):
    def message_sender():
        print(message)
    message_sender()
print_message('apple')



#creating a decorator that changes all letter to cap
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

#using our decorator
def say_hi():
    return 'hi'
decorate = uppercase_decorator(say_hi)
print(decorate())
#we can use more than one decorator for a function. 


#creating a decorator that makes a list from a sentence and then apply
#uppercase_decorator and slpit_string to the say_hi function

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        




# razbor

##########################
def decor(func):
    def inner():
        print('decor start...')
        func()
        print('decor end...')
    return inner

def say():
    print('say')

var = decor(say) #var now holds the function
print(var) 
var() #calling the var as a function
# Output:
#<function decor.<locals>.inner at 0x1027cea60>
# decor start...
# say
# decor end...
#########################


#########################
def decor(func):
    def inner(*args, **kwargs):
        print('first')
        func(*args, **kwargs)
        print('third')
    return inner 

@decor
def say(argument_):
    print(argument_)
say('second')
# output:
# first
# second
# third

##########################



##########################
def decorator(func):
    print('Decorator function')
    def wrapper():
        print('Wrapper function')
        func()
        print('Wrapper function end')
        return func
    return wrapper


@decorator
def function_to_decorate():
    print('The function to be decorated')

function_to_decorate()
#Output:
# Decorator function
# Wrapper function
# The function to be decorated
# Wrapper function end

##############################
# def check_password(func):
#     def wrapper():
#         return func().strip()
#     return wrapper

# @check_password
# def get_password():
#     password = input('Enter password: ')
#     return password

# print(get_password())

# @check_password
# def get_email():
#     email = input('Input email: ')
#     return email
# print(get_email())

################################

###############################
# def check_password(func):
#     def wrapper(parameter):
#         return func(parameter).strip()
#     return wrapper

# @check_password
# def get_password(password):
#     return password

# password = input('Enter password: ')
# print(get_password(password))

# @check_password
# def get_email():
#     email = input('Input email: ')
#     return email
# print(get_email())

################################

def bread(func):
    def wrapper(filler):
        print('top bread')
        func(filler)
        print('bottom bread')
    return wrapper

def ingridients(func):
    def wrapper(filler):
        print('tomato')
        func(filler)
        print('cucumber')
    return wrapper

@bread
@ingridients
def get_sandwich(filler):
    print(filler)

get_sandwich('ketchup')
#Output:
# top bread
# tomato
# ketchup
# cucumber
# bottom bread

##########################

##########################
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Wrapper:{args}')
        print(f'Wrapper:{kwargs}')
        func(*args, **kwargs)
    return wrapper

@decorator
def func_without_params():
    print('Func without parameters')
@decorator
def func_with_params(name, last_name):
    print('Func with parameters')
    print(name, last_name)

func_without_params()
func_with_params('aika', last_name='kub')
##############################

##############################
def benchmark(iters:int)->int:
    def actual_decorator(func):
        import time
        def wrapper(*args, **kwargs):
            total=0
            for i in range(iters):
                start = time.time()
                func_call = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print(f'Average complete time:{total/iters}')
            return func_call
        return wrapper

    return actual_decorator

@benchmark(iters=10)
def get_webpage(url):
    import requests
    webpage = requests.get(url)
    # return webpage.text

print(get_webpage(url='http://yandex.ru'))

