#converting to uppercase
s = 'Bharath'
print(s.upper())
print(s.lower())

#split
s = 'Sam,Sundar,Jone'
out = s.split(',')
print(out)

#replace
s = 'Sam,Sundar,Jone,Bharath,Sam'
s = s.replace('Sam','Samarth')
print(s)

#access based on index
s = 'Samarth'
print(s[5])

pan_name = 'bharath Kumar'
pan_number = 'DP!@B0468F'

if pan_name[0].upper() == pan_number[4].upper():
    print('Matching')
else:
    print('Not Matched')
