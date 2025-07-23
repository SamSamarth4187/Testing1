a = input('Enter the number 1 - ')
b = input('Enter the number 2 - ')
#it gets the input in string format

#Type casting/ convertion --> converting 1 datatype to another

#int --> string 
#it is possible on all cases

a = -10
a = str(a)

print(type(a))

#float --> string 
#it is possible on all cases

a = 10.2
a = str(a)

print(type(a))

#string ---> int/float
#string value should be purely a digits
a = '123'
a = int(a)
print(type(a))

a = '123.5'
a = float(a)
print(type(a))

#int --> float or float ---> int
#it is possible on all cases