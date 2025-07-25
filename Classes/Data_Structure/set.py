#set --> {}

a = {'name':"bharath"}
print(type(a))
s = {1,2,3,4,5}
print(type(s))

#features
#Mutable, unordered, duplicates not allowed

#insert
a = {1,2,3,4,5}
a.add(7)
print(a)

a.add(7)
print(a)

#remove --> with error for value not present
a.remove(5)
print(a)

# a.remove(5)
# print(a)

#discard --> without error for value not present
a.discard(5)
print(a)

#pop --> this removes random element
a.pop()
print(a)

#Set operations
s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}
print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))


#Iterate
for i in s1:
    print(i)



#List --> Mutable, Ordered, Indexing allowed , Duplicates allowed
#Tuple --> Immutable, Ordered, Indexing allowed , Duplicates allowed
#Dictionary --> Mutable, unordered, Indexing not allowed,duplicates now allowed in keys[Key value]
#Set --> Mutable, unordered, Indexing not allowed,duplicates now allowed