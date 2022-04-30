# string = """Aika
# Maika
# Zaika"""
# print(string)
# """Comments"""
# full_name = input(('Enter name: ')).split()
# print(full_name)
# first_name = full_name[0]
# last_name = full_name[1] # or full_name[-1]

# string = "Aika kub"
# print(string.istitle())
# string = 'Today is Thursday'
# print(string.startswith('Today')) #True
# print(string.endswith('Thursday')) #True

# my_list = ['Today', 'is', 'Thursday']
# my_list2 = ['C', 'a', 't']
# print(' '.join(my_list))
# print(''.join(my_list2))

# string ='watermelon'
# print(string.count('e'))

#STRING FORMAT 1st way
# f_name = input("Enter first name: ")
# l_name = input("Enter last name: ")
# whole_name = "Welcome, %s %s "% (f_name, l_name)
# print("Welcome, %s %s "% (f_name, l_name))
# print(whole_name)
# #STRING FORMAT 2nd way
# whole_name = 'Welcome, {} {}'.format(f_name, l_name)
# print(whole_name)
# whole_name = 'Welcome, {1} {0}'.format(f_name, l_name)
# print(whole_name)
# whole_name = 'Welcome, {0} {0}'.format(f_name, l_name)
# print(whole_name)
# #STRING FORMAT 3rd way
# whole_name = f'Welcome, {f_name} {l_name}'
# print(whole_name)
# whole_name = f'Welcome, {l_name}, {f_name}'

# whole_name = f'Welcome, {l_name + f_name}'
# print("Check ", whole_name)

string = 'Aika'
list_ = [char for char in string]
print(list_)
list_ = ''.join(list_)
print(list_)
