#loops --> do the repeated tasks 

#while ---> infinite cases

#while <condition>(True/false):
    #logic

#it should have some condition which fails as some point

a = input('Enter the number - ')
a = int(a)
count = 0
while count < a:
    print(count)
    #count = count + 1
    count += 1

print('Done')

#use break
a = 10
count = 0

while True:
    print(count)
    count += 1
    if count > a:
        break
print('Done')
