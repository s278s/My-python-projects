from decimal import Decimal
from time import sleep

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return 'zero is not allowed'
    else:
        return x/y


while True:
    operator = input('enter one of \n+ - * / exit: ')
    if operator.lower() == 'exit':
        for i in range(3,0,-1):
            print(i,end='..' if i >= 2 else '\n')
            sleep(1)
        break

    if operator not in '+-*/':
        print('wrong operator')
        continue

    try:
        number1 = Decimal(input('enter the first number: '))
        number2 = Decimal(input('enter the second number: '))
    except:
        print('wrong number')
        continue

    if operator == '+':
        print(add(number1,number2))
        continue

    if operator == '-':
        print(sub(number1,number2))
        continue

    if operator == '*':
        print(mul(number1,number2))
        continue

    if operator == '/':
        print(div(number1,number2))
print('You exited the program')
