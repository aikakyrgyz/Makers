try: 
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    result = num1/num2
except ValueError:
    print('You entered a character')
except ZeroDivisionError:
    print('You cannot divide by zero')
else:
    print(num1/num2)
finally:
    print('End')


#2
dict_ = dict.fromkeys(('num1', 'num2', 'num3'), 0)
dict_ = {key: len(key) for key, value in dict_.items()}
dict_.update({'except': 'error'})
print(dict_)
#{'num1': 4, 'num2': 4, 'num3': 4, 'except': 'error'}

while True:
    try:E
        key = input('Enter a word: ')
        if(key == 'exit'):
            break
        dict_[key]+=2
        #{'num1': 6, 'num2': 4, 'num3': 4, 'except': 'error'}
    except KeyError:
        print('There is no such key')
    except TypeError:
        print('You cannot concatenate str with int')
    # except (KeyError, TypeError):
    #     print('There is no such key or You cannot concatenate str with int' )
    else:
        print(dict_[key])
    finally:
        print(dict_)

list_ = [i for i in range(0, 11)]
try:
    index = int(input(': '))
    list_[index] = 'Input'
except ValueError:
    print('You entered a string')
except IndexError:
    print("Index is out of range")
else:
    print(list_[index], 'There was no exception')
finally:
    print(list_)

try:
    print(not_defined)
except NameError:
    print('not_defined is not defined')

number = int(input("Enter a number between 1 and 70"))
if number not in range(1, 71):
    raise Exception('You entered a number out of range 1-70')
print('Thanks')


