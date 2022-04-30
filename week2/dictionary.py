# dict_ = {}
# dict_ = dict()

# #1st way to create a dictionary
# dict_ = {'name': 'Aika', 'last name': 'Kub', 'age': 21}
# print (dict_) #{'name': 'Aika', 'last name': 'Kub', 'age': 21}

# #2nd way to create a dictionary
# dict_ = dict(name='Aika', last_name='Kub', age=21)
# print(dict_)
# #3rd way to create a dictionary
# list_ = [['name', 'Aika'], ['last name', 'Kub'], ['age', 21]] 
# tuple_ = (('name', 'Aika'), ('last name', 'Kub'), ('age', 21))
# #each list must contain two elements only
# dict_ = dict(list_)
# dict_1 = dict(tuple_)
# print(dict_)
# print(dict_1)
# #we can combine:
# list_ = [['name', 'Aika'], ['last name', 'Kub'], ['age', 21]]
# tuple_ = (('name', 'Aika'), ('last name', 'Kub'), ('age', 21))
# dict_ = dict(list_, name='Aika', last_name='Kub', age=21)
# print(dict_)

# #accessing elements 
# dict_ = dict(name='Aika', last_name='Kub', age=21)
# print(dict_['name'])
# #changing the value of a key
# dict_['name'] = 'Altyn'
# print(dict_) #{'name': 'Altyn', 'last_name': 'Kub', 'age': 21}
# dict_['year'] = 1999
# print(dict_ )

# #get the value
# print(dict_.get('age')) #21
# #difference between using .get() and [index]
# print(dict_.get('date', 'there is not key date')) # will not return error, it will return None
# #print(dict_['date']) #gives a key error

# #clear()
# dict_.clear()
# print(dict_) #{} clear the dictionary

# #copy
# dict_ = {'name': 'Aika', 'age': 21}
# dict_2 = dict_ #now both dict_ and dict_2 have the same  address
#                 # so changing the dict_ will also affect dict_2
# #so that it does not happen, use .copy()

# dict_ = {'name': 'Aika', 'age': 21}
# dict_2 = dict_.copy()
# dict_2['year'] = 1999 # we are changing dict_2

# print(dict_)
# print(dict_2)


# #pop()
# dict_ = {'name': 'Aika', 'age': 21}
# dict_.pop('name')
# print(dict_)

# print(dict_.pop('year', 'no such key in dict'))
# print(dict_)



# #popitem()
# dict_ = {'name': 'Aika', 'age': 21}
# dict_.popitem()
# print(dict_)
# #deletes the last element, in older versions it deletes the random element'

# #setdefault(key, default)
# dict_ = dict(a=1, b=2, c=3)
# print(dict_.setdefault('b')) #just like get()
#                             #returns the value of a key
# print(dict_.setdefault('d', 4))
# print(dict_)
#                         #since there is no value 'd' it will create a new one
# dict_.setdefault('a', 100)
# print(dict_)    
#                     #since 'a' already exists, the value of a will stay the same


# #update()
# dict_ = dict(a=1, b=2, c=3)
# dict_2 = {'name': 'Aika', 'age': 21}
# dict_.update(dict_2)
# print(dict_)
# #if there are the same keys then:
# dict_ = dict(a =1, b = 2, c = 3)
# dict_2 = dict(a = 100, b= 101, d = 4)
# dict_.update(dict_2)
# print(dict_) #{'a': 100, 'b': 101, 'c': 3, 'd': 4}
#             #so the values of the dublicate keys will be 
#             #rewritten with the values of dict_2


# #fromkeys(seq, value= None)
# numbers = [1, 2, 3, 4, 5]
# new_dict = dict.fromkeys(numbers,'a')
# print(new_dict)
# new_dict = dict.fromkeys(numbers)
# print(new_dict)

# #items(), keys(), values()

# dict_ = {'name': 'Aika', 'age': 21}
# print(dict_.items()) #dict_items([('name', 'Aika'), ('age', 21)])
# print(dict_.keys()) #dict_keys(['name', 'age'])
# print(dict_.values())#dict_values(['Aika', 21])

# #loops with dictionaries

# contacts = {'Aika':'0702570213', 'Kolya':'0702570213', 'Azim': '0704999000'}
# for info in contacts:
#     print(info) #by default prints only the keys
#     #Aika
#     #Kolya
#     #Azim

# contacts = {'Aika':'0702570213', 'Kolya':'0702570213', 'Azim': '0704999000'}
# for name, tel in contacts.items():
#     print(name, tel)
# # Aika 0702570213
# # Kolya 0702570213
# # Azim 0704999000


# #nested dictionaries

# nested_dict = {'Kubanychbekovy': {
#     'Azim':1994,
#     'Aika':1999,
#     'Altynai': 2004,
#     }
# }

# print(nested_dict['Kubanychbekovy'])
# #{'Azim': 1994, 'Aika': 1999, 'Altynai': 2004}
# print(nested_dict['Kubanychbekovy']['Altynai'])
# #2004

# #hints in python

# #howdoi while loop in pythnon

# dict_ = {}
# dict_.update({'a':2})
# print(dict_)
# dict_['b'] = 2
# print(dict_)
# dict_.setdefault('c', 6)
# print(dict_)






#1st way to create a dictionary
dict_ = {'name': 'Aika', 'last name': 'Kub', 'age': 21}
print (dict_) #{'name': 'Aika', 'last name': 'Kub', 'age': 21}

#2nd way to create a dictionary
dict_ = dict(name = 'Aika', last_name='Kub', age=21)
print(dict_)

#3rd way to create a dictionary
list_ = [['name', 'Aika'], ['last name', 'Kub'], ['age', 21]] 
tuple_ = (('name', 'Aika'), ('last name', 'Kub'), ('age', 21))
#each list must contain two elements only
dict_ = dict(list_)
dict_1 = dict(tuple_)
print(dict_)
print(dict_1)
#we can combine:
list_ = [('name', 'Aika'), ('last name', 'Kub'), ('age', 21)]
tuple_ = (('name', 'Aika'), ('last name', 'Kub'), ('age', 21))

dict_ = dict(list_, name='Aika', last_name='Kub', age=21)
print(dict_)



for  value in dict_.values():
    list_ = ['bread1', 'bread2', 'bread3']
    dict_ = {}
print(dict_.fromkeys(list_, 20))

