cur_position = []
target_position = []
data = input("Input the letter of the current position: ") 
cur_position.append(data)
while ord(cur_position[0])>72:
    print('The letter must be between A and H')
    data = input("Input the letter of the current position: ")
    cur_position.clear()
    cur_position.append(data)

data = input("Input the number of the current position: ") 
cur_position.append(data)
while int(cur_position[1])>8:
    print('The letter must be 1 - 8' )
    data = input("Input the letter of the current position: ")
    cur_position.pop()
    cur_position.append(data) 

data = input("Input the letter of the target position: ")
target_position.append(data)
while ord(target_position[0])>72:
    print('The letter must be between A and H')
    data = input("Input the letter of the current position: ")
    target_position.clear()
    target_position.append(data)
data = input("Input the number of the target position: ") 
target_position.append(data)
while int(target_position[1])>8:
    print('The letter must be between 1 - 8' )
    data = input("Input the letter of the current position: ")
    target_position.pop()
    target_position.append(data)
if target_position[0] == cur_position[0] and int(target_position[1])==int(cur_position[1]):
    print('You must make a step')
elif abs(ord(target_position[0]) - ord(cur_position[0])) == abs(int(target_position[1]) - int(cur_position[1])) and abs(int(target_position[1])-int(cur_position[1]))<8 and abs(ord(cur_position[0])- ord(target_position[0]))<8:
    print("Yes\n")

else:
    print('No')
# if(ord(cur_position[0])>72 or int(cur_position[1])>8):
#     print("Wrong range,must be between 1 and 8")
#if(ord(cur_position[0])>72 or int(cur_position[1])>8):
    #print("Wrong range,must be between 1 and 8")
# if abs(target_position[1] - cur_position[1]) == 1 and target_position[0] == cur_position[0]:
#   print('Yes, you can move vertically\n')
# else:
#   print('You cannot move vertically')
