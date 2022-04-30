#Google notes


#List comprehension
fruits = ['apple', 'banana', 'cherry']
fruits_new = [x for x in fruits if 'a' in x] #the list will contain all string with 'a'
print(fruits_new) #['apple', 'banana']

#2
fruits = ['apple', 'banana', 'cherry']
fruits_new = [x for x in fruits if x!='apple'] #all fruits except apple
print(fruits_new) #['banana', 'cherry']

#3
fruits = ['apple', 'banana', 'cherry']
fruits_new = [x for x in fruits] #kinda copies only 
print(fruits_new)#['apple', 'banana', 'cherry']

#4
list_ = [x for x in range(10)]
print(list_) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#5
list_ = [x for x in range(10) if x<5] #contains all the numbers less than 5
print(list_) #[0, 1, 2, 3, 4]

#6
fruits = ['apple', 'banana', 'cherry']
fruits_new = [x.upper() for x in fruits]
print(fruits_new) #['APPLE', 'BANANA', 'CHERRY']

#7, with else statement
fruits = ['apple', 'banana', 'cherry']
fruits_new = [x if x!='banana' else 'orange' for x in fruits] #if x is 'banana' return 'no bananan
print(fruits_new) #['apple', 'orange', 'cherry']

#8
name = ['Aika', 'Azim', 'Altynai', 'Kubanychbekov']
name_new = [x for x in name if len(x)<6]
print(name_new)
#9

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = [f'Odd number {x}' if x%2!=0 else f'even number {x}' for x in a]
#['Odd number 1', 'even number 2', 'Odd number 3', 
# 'even number 4', 'Odd number 5', 'even number 6', 
# 'Odd number 7', 'even number 8', 'Odd number 9', 
# 'even number 10']
print(even_num)

#10
names_ = ['Aika', 'Azim', 'Altynai']
invite_ = ['You are invited: ' + name for name in names_]
print(invite_)

#11
nums_ = [-12, -11, -10, -9,-8, -4, -2, 2, 4, 8, 9, 10, 11, 12]
nums_ = [num for num in nums_ if num%2 == 0 and num>0] #can be or too
print(nums_) #[2, 4, 8, 10, 12]
#12
num_ = ['2020', '2020year', '2021', '2020y']
num_1 = [num for num in num_ if num.isdigit()]
print(num_1) #['2020', '2021']
#13
names_ = ['Aika', 'Azim', 'Altynai']
lengths = [len(name) for name in names_]
print(lengths) #[4, 4, 7]

#14
nums_ = [-12, -11, -10, -9,-8, -4, -2, 2, 4, 8, 9, 10, 11, 12]
nums_new = [num if num<0 else num**2 for num in nums_]
print(nums_new) #[-12, -11, -10, -9, -8, -4, -2, 4, 16, 64, 81, 100, 121, 144]
#15
nums_ = [-12, -11, -10, -9,-8, -4, -2, 2, 4, 8, 9, 10, 11, 12]
nums_new = [num if num<0 else num**2 for num in nums_ if num%2 ==0] #if the number is even only
print(nums_new) #[-12, -10, -8, -4, -2, 4, 16, 64, 100, 144]
#16
fruits = ['apple', 'banana', 'mango2312', 'watermelon', 'Apple1', 'GOOGLE']
filtered_fruits = [
    fruit + ' is a fruit'
    if fruit.islower()
    else fruit + ' is not a fruit '
    for fruit in fruits
    if fruit.isalpha()]
print(filtered_fruits) 

#the last if, is the first if in regular loop


# if fruit.isalpha():
    # if fruit.islower():
    #     fruit+ 'is a fruit'
    # else:
    #     fruit + 'is not a fruit'
#['apple is a fruit', 'banana is a fruit', 'watermelon is a fruit', 'GOOGLE is not a fruit ']

#Google notes
#dictionary comrephension



#1
sq_dict = dict()
for num in range (0, 11):
    sq_dict[num] = num*num
print(sq_dict)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#now with dict comprehension
sq_dict = {num:num*num for num in range(0, 11)}
print(sq_dict)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#2, using data from old dictionary
old_price = {'milk': 1, 'coffee': 5}
new_price = {key:value*2 for key, value in old_price.items()}
print(new_price) #{'milk': 2, 'coffee': 10}

#3, if conditional dictionary
nums = {1:1, 2:2, 3:3, 6:6, 99:99, 100:100, 55:55, 88:88}
even_nums = {key: 'Even' for key, value in nums.items() if value%2 ==0}
print(even_nums)
#{2: 'Even', 6: 'Even', 100: 'Even', 88: 'Even'}

# muliple if statements:
nums = {1:1, 2:2, 3:3, 6:6, 99:99, 100:100, 55:55, 88:88}
nums_ = {key:value for key, value in nums.items() if key<100 if value%2 ==0}
print(nums_) 
#{2: 2, 6: 6, 88: 88}
#nums_ includes only elements whose key<100 and value is even

#4, if-else conditional comprehension
nums = {1:1, 2:2, 3:3, 6:6, 99:99, 100:100, 55:55, 88:88}
even_nums = {key: ('Even' if value%2 ==0 else 'Odd') for key, value in nums.items()}
print(even_nums)
#{1: 'Odd', 2: 'Even', 3: 'Odd', 6: 'Even', 99: 'Odd', 100: 'Even', 55: 'Odd', 88: 'Even'}

#5, nester dictionary comprehension
dict_ = dict()
for i in range(0, 11):
    dict_[i] = {x:i*x for x in range(0, 10)}
    print(dict_[i])

#6
dict_ = dict(a = 1, b =2, c = 3)
dict_new = {value:key for key, value in dict_.items()}
print(dict_new)
#{1: 'a', 2: 'b', 3: 'c'}

#7
dict_ = dict(a = 1, b =2, c = 3)
dict_new = {key.upper(): value*0 for key, value in dict_.items()}
print(dict_new)
#{'A': 0, 'B': 0, 'C': 0}

#8
nested_dict = {'Aika': {'study':8, 'sleep': 8}, 'Altynai': {'study':6,'sleep':10}}
dict_new = {key: {inner_key: inner_value - 1 for inner_key, inner_value in value.items()} for key, value in nested_dict.items()}
print(dict_new) 
#{'Aika': {'study': 7, 'sleep': 7}, 'Altynai': {'study': 5, 'sleep': 9}}

#9
list_ = [1, 1, 2, 2, 3, 3]
set_ = {num for num in list_}
print(set_) #{1, 2, 3}

aika = dict(name = 'Aika', age =21)
azim = dict(name = 'Azim', age =26)
altynai = dict(name = 'Altynai', age = 16)
users = [aika, azim, altynai]
ages = [user.get('age', None) for user in users]
print(ages) #[21, 26, 16]

older =0
younger = 0
count = 0
for age in ages:
    if age>=18:
        older+=1
    else:
        younger+=1
    count+=1

older = older * (100/count)
younger = younger * (100/count)
print(f'{older}% of users are older than 18')
print(f'{younger}% of users are younger than 18')
#66.66666666666667% of users are older than 18
#33.333333333333336% of users are younger than 18

#end of comprehension 
matrix = [
    [0, 1, 2, 3],
    [1, 1, 2, 3],
    [2, 1, 2, 3],
    [3, 1, 2, 3]
]
table_from_matrix = [n for row in matrix for n in row]
print(table_from_matrix) #[0, 1, 2, 3, 1, 1, 2, 3, 2, 1, 2, 3, 3, 1, 2, 3]

# for loop
matrix_rep =[]
for row in matrix:
    for n in row:
        matrix_rep.append(n)
print(matrix_rep) ##[0, 1, 2, 3, 1, 1, 2, 3, 2, 1, 2, 3, 3, 1, 2, 3]

# Date and time
from datetime import datetime
start = datetime.now()
list_ = []
# for i in range(100000):
#     list_.append(i)
list_ = [i for i in range(100000)]
print(datetime.now() - start) 
#for loop: #0:00:00.048397
#comprehension: #0:00:00.009347

str_list = ['1', '2']
for i in range(0, len(str_list)):
    str_list[i] = int(str_list[i])
print(str_list)


nums = ['a', 'b', 'c', 'd']
print(list(enumerate(nums))) #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
set_comp= {num:index for num, index in enumerate(nums)}
print(set_comp) #{0: 'a', 1: 'b', 2: 'c', 3: 'd'}


#generator
num = [1, 2, 3]
dict_gen = dict((num, num**2) for num in num) #creating a dict
print(dict_gen) #{1: 1, 2: 4, 3: 9}

print(next(dict(dict_gen)))




word = 'aika'
word_list = list(word) #['a', 'i', 'k', 'a']
print(word_list)
print(''.join((letter) for letter in word_list))


