#1. dump
import json
info = {
    'name':'Alice',
    'age':79,
    'book': 'Chamber of Secrets'
}
# with open('file.json', 'w') as my_file:
#     json.dump(info, my_file)

#2.dumps
json_object = json.dumps(info)
print(json_object)
print(type(json_object)) #<class 'str'>
#3. load
with open('file.json') as my_file:
    python_object = json.load(my_file)
    print(python_object) #single quotes 
#now we can work the returned values as with a python dictionary
python_object['name' ] = 'Aika'
print(python_object)
with open('file.json', 'w') as my_file:
    json.dump(python_object,my_file)

#4.loads
json_str = '{"name":"Alice", "age":79, "book":"Chamber of Secrets"}'
python_object = json.loads(json_str)
print(json_str)
print(python_object)

#working with HarryPotter file
#import json
with open('HarryPotter.json') as my_file:
    dictionary = json.load(my_file)
    books = dictionary['books']
    for book in books:
        book['author'] = 'J.K.Rowling'
    print(dictionary)

with open('HarryPotter.json', 'w') as my_file:
    json.dump(dictionary, my_file)