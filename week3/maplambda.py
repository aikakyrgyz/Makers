#map() 

#map(function, iterable)

def myfunction(word):
    return len(word)
list_ =['aika', 'orange']
x = map(myfunction, ('aika', 'apple'))
print(list(x)) # [4,5] #converting map to list


# without using map
number_str = ['1', '2', '3']
number_int =[]
for i in number_str:
    number_int.append(int(i))
print(number_int)
#1, 2, 3]

#using a map

number_str = ['1', '2', '3']
number_int = list(map(int, number_str)) #need to convert for readability
print(number_int)
# 1, 2, 3]


#lambda ()
#syntax: lambda arguments: expression

x = lambda a, b: a*b
print(x(5,6))
#30

x = lambda a: a+10
print(x(5))
#15

#lambda()
numbers = [1,2,3,4,5]
double_numbers = list(map(lambda x: x*2, numbers))
print(double_numbers)
#[2, 4, 6, 8, 10]

#filter
#syntaxL filter(function, iterable)

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)




#practice

#map()

def capital(word: str) -> str: #annotation, we want our function to accept only strings
    return word.title()

list_names = ['aika', 'sam']
capital_names = list(map(capital, list_names))
print(capital_names)
#['Aika', 'Sam']

#map()

def dollars_to_soms(dollars: int) ->int:
    return(f'{dollars} is {round(dollars*84.8)} soms')

to_convert = [100, 1000, 60000]
converted = list(map(dollars_to_soms, to_convert))
print(converted)
#['100 is 8480 soms', '1000 is 84800 soms', '60000 is 5088000 soms']

#lambda()

print((lambda x:x**2)(9)) #81

square = lambda x:x**2
print(square(9)) #81

print((lambda x, y, z: x+y+z) (1, 1, 1)) #3


list1 = [1,2, 3]
list2 = [4, 5, 6]

new_list = list(map(lambda x, y: x+y, list1, list2)) 
print(new_list) #[5, 7, 9]

#- 1.loop
num_list = [1, 2, 3, 4, 5]
num_list2 = []
for i in num_list:
    num_list2.append(i*2)
print(num_list2) #[2, 4, 6, 8, 10]
#-

#- 2. map and lambda

num_list = [1, 2, 3, 4, 5]
num_list2 = list(map(lambda x:x*2, num_list))
print(num_list2) #[2, 4, 6, 8, 10]
#-

#- 3. list comprehension
num_list = [1, 2, 3, 4, 5]
num_list2 = [x*2 for x in num_list]
print(num_list2) #[2, 4, 6, 8, 10]


#-filter 

fruits = ['mango', 'apple', 'melon', 'apple', 'strawberry']
filtered_fruits = list(filter(lambda fruit: fruit.startswith('m'), fruits)) #if fruit.startswith('m') returns TRUE then it is added into the filtere_fruits list, otherwise it is skipped)
print(filtered_fruits) #['mango', 'melon']

#-

#-filter 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers) #[2, 4, 6, 8]

#-

#-filter
dict_ = [{'name': 'Aika', 'age':21}, {'name':'Altynai', 'age':16}]
dict_new = list(filter(lambda x: x['name'] == 'Aika', dict_))
print(dict_new) 
#[{'name': 'Aika', 'age': 21}]
#-

#-filter
people = [{'name': 'Aika', 'age':21}, {'name':'Altynai', 'age':16}, {'name':'Aika', 'age':1}]
dict_new = list(filter(lambda x: x['name'] == 'Aika', people))
print(dict_new) # [{'name': 'Aika', 'age': 21}, {'name': 'Aika', 'age': 1}]
#-


#-filter

users = [{'name':'Aika', 'comments': ['I like it', 'I have missed you']}, {'name':'Altynai', 'comments':['TikTok is my life']},{'name': 'cha_3943', 'comments':[]}]
active_users = list(filter(lambda x: x.get('comments', None), users)) #if active, the list is not empty, -> true
inactive_users = list(filter(lambda x: not x.get('comments', None), users)) 
print(f'Active users {active_users}') #Active users: {'name': 'Aika', 'comments': ['I like it', 'I have missed you']}, {'name': 'Altynai', 'comments': ['TikTok is my life']}]
print(f'Inactive users {inactive_users}') #Inactive users [{'name': 'cha_3943', 'comments': []}]

#-


#-filter used with map
names = ['Tom', 'Tim', 'Bob', 'Alexander', 'Fillipino']
greeting = list(map(lambda x: f'Greetings, {x}!', filter(lambda x: len(x)<4,names)))
print(greeting)
#['Greetings, Tom', 'Greetings, Tim', 'Greetings, Bob']
#-

#reduce() ->value
import functools
numbers = [1, 2, 3, 4, 5]
sum_ = functools.reduce(lambda x, y: x+y, numbers) 
print(sum_)
#1. x = 1 , y = 2, x+y = 3 -> x =3
#2. x = 3, y =3, x+y = 6 -> x = 6
#3. x = 6, y = 4, x+y = 10 -> x = 10
#4. x =10, y = 5, x+y = 15 -> 15
#-

#-reduce
numbers = [1, 77, 64, -76, 100]
max_ = functools.reduce(lambda x, y: x if x>y else y, numbers)
print(max_) #100
#-
#reduce
numbers = [1, 77, 64, -76, 100]
multiplied = functools.reduce(lambda x, y: x*y, numbers)
print(multiplied) #-37452800


#-zip()
lista = [1, 2, 3, 4, 5]
listb = ['a', 'b', 'c', 'd']
zipped_list = list(zip(lista, listb))
print(zipped_list) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
listc = [-1, -2, -3, -4, -5]
zipped_list = list(zip(lista, listc, listb)) #[(1, -1, 'a'), (2, -2, 'b'), (3, -3, 'c'), (4, -4, 'd')]
print(zipped_list)
#-

#-zip() ends on the shortest iterable object

list_a = [1, 2]
list_b = ['a', 'b', 'c', 'd', 'e']
print(list(zip(list_a, list_b))) #[(1, 'a'), (2, 'b')]
#so ends at 2 even though list_b has more elements 
#-

#-zip can make a dictionary

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
print(dict(zip(list_a, list_b))) #{1: 'a', 2: 'b', 3: 'c'}

list_b = ['a']
print(dict(zip(list_a, list_b))) #{1:'a'}

#-

# -unzipping

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
zipped = zip(list_a, list_b)
unzipped = zip(*zipped)
print(list(unzipped)) #[(1, 2, 3), ('a', 'b', 'c')]
#-

#-unzipping and separating each tuple
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
zipped = zip(list_a, list_b)
tuple_a, tuple_b = list(zip(*zipped))
print(tuple_a) #(1, 2, 3)
print(tuple_b) #('a', 'b', 'c')
#-



#enumerate(object) or enumerate(object, start = 5) #by default start is 0
seasons = ['spring', 'winter', 'fall', 'summer']
enumerated_seasons = list(enumerate(seasons)) # we can do list, tuple, dict, or set
print(enumerated_seasons) #[(0, 'spring'), (1, 'winter'), (2, 'fall'), (3, 'summer')]
#enumerate(object, start =2)
#-

#abs()
num = -19
print(abs(num))#19

# all - Return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True.
list_ = [0, 0, 0, 0]
print(all(list_)) #False

list_ = [1, 1, 1, 0]
print(all(list_)) # False

list_ = [1, 3, 4, 'aika'] 
print(all(list_)) #True


# any - returns True if at least one elemnt in iterable is True:
list_ = [0, 0, 0, 1]
print(any(list_)) #True