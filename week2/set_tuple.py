import antigravity #will generate a comics

# empty_set = set()
# empty_dict = {}

# a = {'Aika', 7, 9, True, False}
# b = set('Aika')
# print(b) 
# #{'k', 'i', 'A', 'a'} or {'a', 'i', 'k', 'A'} or {'k', 'a', 'i', 'A'}
# # the letter are unordered since set is unordered data type
# c = set(range(1, 10, 2))
# print(c) #{1, 3, 5, 7, 9}

# d = {'Aika', 'Maika', 6, True, [1,2,3]} 
# #typeError: unhashable type: 'list' 
# sets cannot contain lists and set, they can only contain unchangable data types (int, bool, str, float)

#Пустой кортеж работает как синглтон, 
# т.е. в памяти запущенного Python скрипта 
# всегда находится  только один пустой кортеж. 
# Все пустые кортежи просто ссылаются на один и тот же объект, 
# это  возможно благодаря тому, что кортежи неизменяемы.
a = {1, 2, 3, 4, 5}
b = {2, 5, 1, 4, 3}
print(a==b) #True

set1 = {'Aika', 'Altynai'}
set1.add('Azim')
print(set1) #{'Altynai', 'Aika', 'Azim'}

set1 = {'Aika', 'Altynai'}
set2 = {'Azim'}
set1.update({'Azim'}) #or set1.update(set2)

print(set1) #{'Altynai', 'Aika', 'Azim'}


fruit = {'apple', 'cherry', 'melon'}
fruit.remove('apple') #{'cherry', 'melon'}
fruit.discard('apple') #{'cherry', 'melon'}

# fruit.remove('nothing')# KeyError: 'nothing'
# fruit.discard('nothing') # no error :)

fruit = {'apple', 'cherry', 'melon'}
fruit.pop() #deletes a random element
print(fruit) 

fruit = {'apple', 'cherry', 'melon'}
fruit.clear()
print(fruit) #return an empty set, set()

fruit = {'apple', 'cherry', 'melon'}
fruit2 = fruit.copy()
print(fruit2)

#intersection()
ingridients = {'egg', 'apple', 'sugar', 'cherry', 'cucumber'}
vegetables = {'cucumber'}
fruit = {'apple', 'cherry', 'melon', 'cucumber'}
intersection_set = ingridients.intersection(fruit)
print(intersection_set) #{'cherry', 'apple'}
# can also use & sign 
print(ingridients & fruit)#{'cherry', 'apple'}
print(ingridients & fruit & vegetables)

#union()
ingridients = {'egg', 'apple', 'sugar', 'cherry', 'cucumber'}
vegetables = {'cucumber'}
fruit = {'apple', 'cherry', 'melon', 'cucumber'}
union_set = ingridients.union(fruit)
print(union_set)
print(ingridients | fruit | vegetables)

#difference()
ingridients = {'egg', 'apple', 'sugar', 'cherry', 'cucumber'}
fruit = {'apple', 'cherry', 'melon', 'cucumber'}
difference_set_ingridients = ingridients.difference(fruit) # will return elemts that are unique fro ingridients
print(difference_set_ingridients) #{'egg', 'sugar'} - these are the elements that are contained only in ingridients set
#also we can use - 
print(ingridients - fruit) #{'egg', 'sugar'}

#symmetric_difference
ingridients = {'egg', 'apple', 'sugar', 'cherry', 'cucumber'}
fruit = {'apple', 'cherry', 'melon', 'cucumber'}
print(ingridients.symmetric_difference(fruit)) #{'melon', 'sugar', 'egg'}

#isdisjoint
num1 = {1,2, 3, 4, 5}
num2 = {7, 8, 9}
print(num1.isdisjoint(num2)) #true

#isdisjoint
num1 = {1,2, 3, 4, 5}
num2 = {7, 8, 9, 5}
print(num1.isdisjoint(num2)) #false
#issubset, issuperset
num1 = {1, 2, 3}
num2 = {2, 3}
print(num1.issuperset(num1)) #true
print(num1>=num2)
print(num2.issubset(num1)) #true
print(num2<=num1)

#intersection_update
num1 = {1, 2, 3}
num2 = {2}
num1.intersection_update(num2)
print(num1) #{2}

#difference_update
num1 = {1, 2, 3}
num2 = {2}
num1.difference_update(num2)
print(num1) #num1 = {1, 3}

#symmetric_difference_update
num1 = {1, 2, 3}
num2 = {2, 5, 7}
num1.symmetric_difference_update(num2)
print(num1) #{1, 3, 5, 7} 

my_fset = frozenset()

#declaring tuples
my_tuple = tuple()
my_tuple = ()
my_tuple = 'Aika', 3, True
my_tuple = ('Aika',) #must put a coma if there is only one element in the tuple
my_tuple = tuple('Aika')

#tuple -slices
my_tuple = (1, 2, 3, 'Aika')
print(my_tuple[0:])

#count()
my_tuple = (1, 2, 3, 'Aika')
print(my_tuple.count(1)) #3

#index
my_tuple = (1, 2, 3)
print(my_tuple.index(1)) #5
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))

#accessing elements of tuple with index
my_tuple = (1, 2, 3, ['Aika', 1])
my_tuple[-1][0] = 'Maika'
print(my_tuple) #(1, 2, 3, ['Maika', 1])


#empty tuple

a = ()
b = ()
print(a is b) #true

#empty set 
a = []
b = []
print(a is b) #false

#for in tuple
my_tuple = ('Aika', 'Azim')
for name in my_tuple:
    print(name)
#for in set
my_set = {'Aika', 'Azim'}
for name in my_set:
    print(name*3)

#while loop
names = {'Aika', 'Azim'} #note, it is a set
while names:
    print(names)
    names.pop()
print('End')

#while loop
while True:
    word = input('Enter a word: ')
    if word.lower() == 'exit':
        break
    elif not word:
        print('Type something')
        continue
    else:
        print(word[::-1])


#creating a tuple from list
my_list = [1, 2, 3]
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

my_tuple = 'Aika', 3
print(type(my_tuple))
print(my_tuple)

#adding tuples
my_tuple = ('Aika', 'Azim')
my_tuple2 = (21, 26)
new_tuple= my_tuple + my_tuple2
print(new_tuple)
print(my_tuple[1])

#assign each tuple value to a variable
user = ("Aybek", 22, False) 
name, age, isMarried = user 
print(name) # Aybek 
print(age) # 22 
print(isMarried) # False


countries = ( 
 ("Germany", 80.2, (("Berlin",3.326), ("Hamburg", 1.718))), 
 ("France", 66, (("Paris", 2.2),("Marsel", 1.6))) 
) 
for country in countries: 
    countryName, countryPopulation, cities = country 
    print("\nCountry: {} population: {}".format(countryName, countryPopulation)) 
for city in cities: 
    cityName, cityPopulation = city 
    print("City: {} population: {}".format(cityName, cityPopulation)) 
