while True:
    print('===================Calculator=====================')
    a = input('Enter the values seperated by commas - ')
    print('Choose the operation')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    operator = input('Enter the operation - ')

    #type convert
    a = int(a)
    b = int(b)

    if operator == '1':
        print('Addition')
        c = a+b
        print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

    elif operator == '2':
        print('Subtraction')
        c = a-b
        print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

    elif operator == '3':
        print('Multiplication')
        c = a*b
        print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))

    elif operator == '4':
        print('Division')
        c = a/b
        print('The input 1 is {0} and the input 2 is {1} and the result is {2}'.format(a,b,c))
    
    elif operator == '5':
        break

    else:
        print('Invalid operator')
        print('Sorry.....')
        continue

    print('Wow....You are done !!')
    print('')


