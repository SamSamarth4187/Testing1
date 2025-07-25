#dictionary --> {}

#dic --> key and value

a = {"Name":"Bharath","Age":25}

#features
#Mutable, unordered, indexing not allowed, duplicate keys also not allowed

a = {"Name":"Bharath",
     "Age":25,
     "Dept":"CSE",
     "Marks":90.0
}

#add new key
#dic_variable[new_key_name] = new_value
a['Pass'] = True
print(a)

#update
#dic_variable[already_present_key_name] = new_value
a['Pass'] = False
print(a)

#del the key
#del dic_variable[already_present_key_name]
del a['Pass']
print(a)

#Read the values
print(a['Name'])

#values can be duplicates, but keys can't be duplicates
a['New_Name'] = 'Bharath'
print(a)

a = {
    "Name":"Bharath",
    "Age":25,
    "Dept":"CSE",
    "Marks":
            {
                "Maths":90,
                "Physics":80,
                "Chemistry":90
            }
     
    }
a = {
    "Name":"Bharath",
    "Age":25,
    "Dept":"CSE",
    "Marks":[90,80,90]
    }
print(a['Marks']['Maths'])

#iterate
for i in a:
    print(i)
    print(a[i])

for key,value in a.items():
    print(key,value)