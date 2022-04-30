# #printing the contents of a file

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# #The keyword with closes the file once access to it is no longer needed.
# #The only difference between this output and the original file is the extra blank line at the end of the output.

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip()) 

# #if the file is in a folder that is inside the working folder:
# #with open('text_files/filename.txt') as file_object:

# #defining an ABSOLUTE PATH, Using absolute paths, you can read files from any location on your sys- tem.
# #file_path = '/home/ehmatthes/other_files/text_files/filename.txt' 
# #with open(file_path) as file_object:

# # reading line by line

# filename = 'pi_digits.txt'
# with open(filename) as file_object: 
#     for line in file_object:
#         print(line) #has a lot of blank lines


# #reading line by line, eliminating extra black lines
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#     print(line.rstrip())


# # When you use with, the file object returned by open()
# #  is only available inside the with block that contains it. 
# #  If you want to retain access to a file’s 
# #  contents outside the with block, 
# #  you can store the file’s lines in a 
# #  list inside the block and then work with that list.


# # making a list of lines from a file:
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


# # pi_digits.py

# # 3.1415926535
# #   8979323846
# #   2643383279

# # working with the file
# filename = 'pi_30_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)

# # 3.141592653589793238462643383279



# #NOTE: When Python reads from a text file, it interprets all text in the file as a string. 
# # If you read in a number and want to work with that value in a numerical context,
# #  you’ll have to convert it to an integer using the int() function or convert it 
# # to a float using the float() function.

# # working with large files, printing only the first 52 digits:

# filename = 'pi_30_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string[:52] + '...')


# #3.14159265358979323846264338327950288419716939937510...



# filename = 'pi_million_digits.txt'
#    with open(filename) as file_object:
#        lines = file_object.readlines()
#    pi_string = ''
#    for line in lines:
#        pi_string += line.rstrip()

# birthday = input("Enter your birthday, in the form mmddyy: ") 
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")





# #writing to files:

# filename = 'programming.txt'
# with open(filename, 'w') as file_object: #'w' is a write mode
#   file_object.write("I love programming.")

# #read mode ('r')
# #  write mode ('w')
# #  append mode ('a')
# #  read and write to the file ('r+').

# #writing multiple lines:
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")

# #I love programming.
# #I love creating new games.

# filename = 'programming.txt'
# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")
#     file_object.write("I love creating apps that can run in a browser.\n")


# # I love programming.
# # I love creating new games.
# # I also love finding meaning in large datasets.
# # I love creating apps that can run in a browser.

# #Handling the FileNotFoundError Exception

# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)
# #Sorry, the file alice.txt does not exist.


#LECTURE

#printing all of the content of the while
#file1 = open("file_name.txt", 'r')
#print(file1.read())


#------------
# file1 = open("file.txt", 'r')
# print(file1.read())
# #I love you
# # You love me
# # Everything starts
# # From love


# #-------------
# file1 = open("file.txt", 'r')
# print(file1.read(10))  #reads the first 10 characters
# #I love you
# #---------


###################
file1 = open("file.txt", 'r')
print(file1.read(10))
print(file1.read(10)) # continues on the 10th character

#I love you

# You love 


##############

file1 = open('file.txt', 'r')
print(file1.read(10))
file1.seek(0) #returns the curson at the beginning of the file
print(file1.read(10))
# I love you
# I love you 
#################

file1 = open('file.txt', 'r')
list_ = file1.readlines()
print(list_) #['I love you\n', 'You love me\n', 'Everything starts\n', 'From love\n']
########
file1 = open('file.txt', 'r')
list_ = file1.readlines()
list_ = [line.replace('\n', '') for line in list_]
print(list_) #['I love you', 'You love me', 'Everything starts', 'From love']
########
file1 = open('file.txt', 'r')
print(file1.read().split('\n')) #['I love you', 'You love me', 'Everything starts', 'From love', '']

########
#file2 = open('file2.txt', 'x') # 'x' mode creates the file if it does not exist, if it exists then it returns an error: FileExistsError
#print(file2.write('This was written'))#16

############
# file2 = open('file2.txt', 'w')
# list_ = ['apple\n', 'we ate an apple\n', 'we will eat an apple']
# file2.writelines(list_) 
# #apple
# #we ate an apple
# #we will eat an apple
# ############
file2 = open('file2.txt', 'w')
list_ = ['apple', 'we ate an apple', 'we will eat an apple']
list_with_new_line = [line + '\n' for line in list_]
file2.writelines(list_with_new_line) 
#apple

#file2 = open('file2.txt', 'w')
dict_ ={'Aika ': 14, 'Maika': 0} 
file2.writelines(dict_) # will only write the keys 

set_ ={'aika', 'string'}
with open('delete.txt', 'w') as my_file:
    my_file.writelines(set_)




#reading files in CVS format
#----- cvs file contents:
# Hostname, vendor, model, location
# Sw1, Cisco, 4355, London
# Sw2, Cisco, 4324, Amsterdam
# Sw3, Cisco, 4667, Brazil
######

import csv
with open('csv_file.csv', 'r') as my_file:
    reader = csv.reader(my_file) #reader -  this is an iterator
    for row in reader:
        print(row)
# Output:
#['Hostname', ' vendor', ' model', ' location']
# ['Sw1', ' Cisco', ' 4355', ' London']
# ['Sw2', ' Cisco', ' 4324', ' Amsterdam']
# ['Sw3', ' Cisco', ' 4667', ' Brazil']


# получаем заголовки столбоцов


import csv
with open('csv_file.csv', 'r') as my_file:
    reader = csv.reader(my_file) #reader -  this is an iterator
    header = next(reader)
    print('Headers:', header)
    for row in reader:
        print(row)

# # Output
# Headers: ['Hostname', ' vendor', ' model', ' location']
# ['Sw1', ' Cisco', ' 4355', ' London']
# ['Sw2', ' Cisco', ' 4324', ' Amsterdam']
# ['Sw3', ' Cisco', ' 4667', ' Brazil']


# creating a dict
import csv
with open('csv_file.csv', 'r') as my_file:
    reader = csv.DictReader(my_file) #reader -  this is an iterator
    for row in reader:
        print(row)
        print(row['Hostname'], row[' model'])
  
#Output
# {'Hostname': 'Sw1', ' vendor': ' Cisco', ' model': ' 4355', ' location': ' London'}
# Sw1  4355
# {'Hostname': 'Sw2', ' vendor': ' Cisco', ' model': ' 4324', ' location': ' Amsterdam'}
# Sw2  4324
# {'Hostname': 'Sw3', ' vendor': ' Cisco', ' model': ' 4667', ' location': ' Brazil'}
# Sw3  4667

#writing to csv file:

data = [['Hostname', ' vendor', ' model', ' location'], 
        ['Sw1', ' Cisco', ' 4355', ' London'],
        ['Sw2', ' Cisco', ' 4324', ' Amsterdam'],
        ['Sw3', ' Cisco', ' 4667', ' Brazil']]


with open('new_cvs_file.csv', 'w+') as myfile:
    writer = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC) #puts all the values in quotes
    for row in data: 
        writer.writerow(row) 
    #or just writing without a loop
    writer.writerows(data)
    myfile.seek(0)
    print(myfile.read())

#Output:
# Hostname, vendor, model, location
# Sw1, Cisco, 4355, London
# Sw2, Cisco, 4324, Amsterdam
# Sw3, Cisco, 4667, Brazil

list_ = ['1\n', '2\n' ]
write('1\n 2\n')
write(list_)
writelines(list_)

# JSON

#reading a file from json format .json.load()

import json
with open('jason_file.json', 'r') as myfile:
    templates = json.load(f)


for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))

