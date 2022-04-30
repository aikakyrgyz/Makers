list1 = []
list2 = list()
print(type(list1))
print(type(list2))
# <class 'list'>
# <class 'list'>

list1 = [1,2,3,4]
list2 = list([1, 2, 3, 4]) #another way of defining a list

list3 = list(list1) # creating a duplicate of a lsit

list1 = [7, 7, 7]
list2 = [7] * 3
print(list1)
print(list2)
# [7, 7, 7]
# [7, 7, 7]

#range(end)
list1 = list(range(10))
print(list1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#range(start, end)
list1 = list(range(1,9))
print(list1)
# [1, 2, 3, 4, 5, 6, 7, 8]

#range(start, end, step)
list1 = list(range(0, 11, 2)) #every two steps, every even number
print(list1)
# [0, 2, 4, 6, 8, 10]

# range from the end 
list1 = list(range(10, 0, -1))
print(list1)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#for
for i in range(0,11):
    print(str(i)+'^2: ', i**2, ' ')
# 0^2:  0  
# 1^2:  1  
# 2^2:  4  
# 3^2:  9  
# 4^2:  16  
# 5^2:  25  
# 6^2:  36  
# 7^2:  49  
# 8^2:  64  
# 9^2:  81  
# 10^2:  100 

#list methods
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # True

list1 = [1, 2, 3, 10]
list2 = [1, 2, 3]
print(list1 > list2) # True
list1 = [1, 2, 3, 10]
list2 = [1, 2, 3, 5]
print(list1 > list2) #True
# when we use the < > sign, every element of list1 is compared with the corresponding elements in list2. 
# The list that has the elements that is first compared as greater
#will be the greater list

list1 = ['Aika', 2020, 'sleepy', [1, 2, 3]]
list1[-1] = [ 3, 2, 1]
list1[-2] = 'motivated'
print(list1)
#['Aika', 2020, 'motivated', [3, 2, 1]]

list1  = ['tomato', 'potato']
for fruit in list1:
    print(fruit)

word = 'Aika'
for letter in word:
    print(letter)
# A
# i
# k
# a

exam = int(input('Enter the number of exams: '))
list_scores = list()
for exam in range(exam):
    score = input('Enter the score for the '+ str(exam+1) +' ' +  'exam')
    list_scores.append(score)
print(list_scores)


fruit = ['apple', 'melon']
vegetables = ['carrot', 'cucumber', 'cabbage']
fruit.extend(vegetables) 
print(fruit)
#['apple', 'melon', 'carrot', 'cucumber', 'cabbage']

fruit = ['apple', 'melon']
vegetables = ['carrot', 'cucumber', 'cabbage']
print(fruit + vegetables)
#['apple', 'melon', 'carrot', 'cucumber', 'cabbage']

# .insert(index, element)
fruit = ['apple', 'melon']
fruit.insert(1, 'cherry')
fruit.insert(0, 'watermelon')
print(fruit)
['apple', 'cherry', 'melon']

fruit = ['apple', 'melon']
fruit.remove('apple')
print(fruit) #['melon']

print(id(fruit)) #4470056832
fruit.clear()      #the object will still exist just without any data inside
print(id(fruit)) #4470056832 

#del fruit #completely deleted the object 
#print(id(fruit)) #NameError: name 'fruit' is not defined

#sort

list1 = ['A', 'D', 'E', 'C']
list1.sort()
print(list1) #['A', 'C', 'D', 'E']

list1 = ['seven', 'cat', 'interesting']
list1.sort(key = len)
print(list1)
# ['cat', 'seven', 'interesting']

#sort
nums.sort(reverse= True)
nums = [1, 2, 3]

list1 = ['A', 'B', 'C', 'D']
list1.reverse()
print(list1)
#['D', 'C', 'B', 'A']

list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D']
list1 = list2
print(id(list1)) #4552817664
print(id(list2)) #4552817664
list1.pop()
print(list1)
print(list2)
# ['A', 'B', 'C']
# ['A', 'B', 'C']

list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D']
list1 = list2.copy()
print(id(list1)) #4552817664
print(id(list2)) #4552817432
list1.pop()
print(list1)
print(list2)
# ['A', 'B', 'C']
# ['A', 'B', 'C', 'D']

list1 = [1, 2, 3]
print(len(list1))

list_of_lists = [['Aika', 21], ['Altynai', 16], ['Azim', 26]]
print(list_of_lists)
print(list_of_lists[0])
print(list_of_lists[0][0])
print(list_of_lists[0][0][0])

for inner_list in list_of_lists:
    for element in inner_list:
        print(element, end = ', ')
    print('\n')

print(1 in list1)




list1 = [1, 2, 3]
deleted = list1.pop(0)
print(deleted) 

a = [1, 2, 3, 2, 2, 'Aika']
for i in range(len(a)):
    if a[i] ==2:
        a[i] =0
    print(a)


#zipping
nums = [1, 2, 3]
words = ['one', 'two', 'three']
new = zip (nums, words)
print(list(new))


