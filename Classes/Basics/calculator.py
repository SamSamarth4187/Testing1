a = input('Enter the number 1 - ')
b = input('Enter the number 2 - ')
operator = input('Enter the operator - ')

#type convert
a = int(a)
b = int(b)

if operator == '+':
    print('Addition')
    c = a+b
    print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

elif operator == '-':
    print('Subtraction')
    c = a-b
    print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

elif operator == '*':
    print('Multiplication')
    c = a*b
    print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

elif operator == '/':
    print('Division')
    c = a/b
    print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

else:
    print('Invalid operator')


