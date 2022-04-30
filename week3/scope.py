def func():
    print(locals())
func()
#{}- returns an empty dictionary, since right now there are no parameters to a function (local variables)

def func(name):
    age = 21
    print('my name is:', name)
    print(locals()) #{'name': 'Aika', 'age': 21}
func('Aika') #my name is:aika
print(globals()) 

name = 'Raychel'
def get_name():
    name = 'John'
    age = 21
    print('THe namespace of get_name:', locals()) #The namespace of get_name: {'name': 'John', 'age': 21}
print('The outside namespace: ', locals()) #The outside namespace:  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.}
print(globals()) #same as calling locals() in global namespace
get_name()


fruit =  'mango'
def func_1():
    name = 'func_1'
    def func_2():
        #name = 'func_2'
        print(name)
        print(locals())
    func_2()
    print('func_1:', locals())

func_1()