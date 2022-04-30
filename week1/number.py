day_of_birth = int(input('Please enter the day you were born. Example if you were born on Sept 7, 1999, enter 7: '))
print('\tThe day you were born is', day_of_birth)
month_of_birth = int(input('Please enter the month you were born. Example: if it is September enter 9: '))
print('\tThe month you were born is', month_of_birth)
year_of_birth = int(input('Please enter the year of birth: '))
print('\tThe year of birth is', year_of_birth)
sum = day_of_birth + month_of_birth + year_of_birth
print('The sum of entered numbers is', sum)

discount_percentage = float(input('Please enter your discount: '))
#print(discount_percentage)
remaining_payment = abs(((600 * discount_percentage)/100) - 600)
print('The remaining payment is ', remaining_payment)

import math
radius = float(input('Enter the radius of the circle: '))
area = pow(math.pi * radius, 2)
circumference = 2 * math.pi * radius
print(' Radius: ', format(radius, ".2f"), '\n', 'Circumference: ', format(circumference, ".2f"))

