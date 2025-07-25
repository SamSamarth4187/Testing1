while True:
    a=int(input("enter the value of a: "))
    b=int(input("enter the value of b: "))

    print("choose the operatin to be performed")
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.rxit")

    operator =input("choose the operator")

    if operator=='1':
        c=a+b
        print("value of a{0} and b{1} is {2} ".format(a,b,c))

    elif operator =='2':
        c=a-b
        print("substraction of value a {0} and b {1} is {2} ". format(a,b,c) )

    elif operator == '3':  
        c=a*b
        print("multiplication of value a {0} and b {1} is {2} ".format(a,b,c))  

    elif operator =='4':
        if b!=0:
            c=a/b
            print("division of value a {0} and b {1} is 2{2} ". format(a,b,c))
        else:
            print("throw error")

    elif operator =='5':
        print("exit out of loop")
        break    

    else:
        print("Invalid operator.")    
        continue
    
    print("wow you have successfully completed the operation")

