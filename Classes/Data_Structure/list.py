#List --> []

a = [1,2,3,4,5,6,7,8,9]
a = [10.2,4.5,8.9]
a = ['bharath','samarth']
a = [1,2.4,'bharath']

#Features
#Mutable, Ordered, Indexed, Duplicates allowed

#mutable --> able to make changes
#inserting
a = [1,2,3,4]
a.append(5)
print(a)
a.append(7)
print(a)

a.insert(3,10)
print(a)

#remove
#a.remove(value)
a.remove(10)
print(a)

#a.pop(index)
a.pop(4)
print(a)
a.pop()
print(a)

#update
a[2] = 10
print(a)

#Read
for i in a:
    print(i)

print(a[2])

#ordered
a = [1,2,3,4,5]

#duplicates allowed
a = [1,1,1,1,1,1,1,1]
print(a)


