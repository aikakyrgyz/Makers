
#operator = input('Input the operand: + - * / // e: ')

while True:

    operator = input('Input the operand: + - * / // e ')
    print('input is ', operator)
    if operator in ('+', '-', '*', '/', '//', 'e'):
        num1 = int(input('Input the first number: '))
        num2 = int(input('Input the second number: '))

        if operator == '+':
            print(num1 + num2)
        elif operator =='-':
            print(num1 - num2)
        elif operator == '*':
            print(num1*num2)
        elif operator == '/':
            if num2 ==0:
                print("You cannot delete by 0")
            else:
                print(num1/num2)
        elif operator == '//':
            if num2 ==0:
                print("You cannot delete by 0")
            else:
                print(num1//num2)
        elif operator == 'e':
            exponent = float(input('Choose the exponent, 2, 3, 4, ...etc'))
            if exponent == 0:
                print('1')
            else:
                print(pow(num1, exponent))

    else:
        print('Invalid Operator')

