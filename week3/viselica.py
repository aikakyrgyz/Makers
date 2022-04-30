import random

list_ = ['rain', 'sun', 'love', 'happiness', 'code', 'game']

if len(list_)==1:
    key = list_[0]
else:
    key = list_[random.randint(0, len(list_))]

stars = list('*' * len(key))
#stars =''.join(list('*' * len(key)))
#print(stars)

print("This is the word to guess: ")
print(stars)

while True:
    letter = input('Enter a letter:')
    if letter in key:
        n = key.count(letter)
        start = 0
        for i in range(n):
            index = key.index(letter, start, len(key))
            stars[index] = letter
            start = index+1
        print(stars)
        # guessed_part = ''.join(stars)
        # print(guessed_part)
    else:
        print(f'Letter {letter} is not in the word')
    guessed_part = ''.join(stars)
    if guessed_part == key:
        print('You won! The word was','[', guessed_part,']')
        break 
