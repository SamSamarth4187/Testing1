#if and else ---> to divert the code based on conditions

#if <condition>(true/false):
    #logic
#else
    #logic


age = input('Enter the age - ')
age = int(age)

# if age < 10:
#     print('Child')
# elif age < 20:
#     print('Teen')
# elif age < 30:
#     print('Middle aged')
# else:
#     print('Adult')

# print('Done')


#if and else in single line
if age < 10:
    print('Child')
else:
    print('Adult')

#"True result" if condition else 'False condition'
print('Child' if age < 10 else 'Adult')

