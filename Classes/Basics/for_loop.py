#for --> finite cases

# Using it for numbers
# for <variable_name> in range(start,end,increment):
#     logic

# for i in range(0,10,2):
#     print(i)

#String or list or tuple or dict
#for <variable_name> in string/list/tuple/dic:
#   logic

# s = 'samarth'
# out = ''
# for i in s:
#     out = i + out
# print(out)

# siz = len(s)
# for i in range(siz-1,-1,-1):
#     print(s[i])


#even or not
#even --> positive or not
#positive --> square

for i in range(1,10):
    if i%2 == 0:
        if i > 0:
            print(i**2)


for i in range(1,10):
    if i%2 != 0:
        continue
    if i > 0:
        print(i**2)
