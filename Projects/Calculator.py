
# '''
# a=input("enter the value of a : ")
# b=input("enter the value of b : ")
# operator= input ("enter the operator :")
# a=int(a)
# b=int(b)

# if operator =='+':
#   print("addition of a {0} and b {1}".format(a,b))
#   print(a+b)

# elif operator =='-':
#   print("Sbustaction of a {0} and b {1}".format(a,b))
#   print(a-b)
  
# elif operator == '/':
#   print("division of a {0} and b {1}".format(a,b))
#   print(a/b)

# elif operator == '*':
#   print("multiplication of a {0} and b {1}".format(a,b))
#   print(a*b)

# else:
#   print("Invalid operator. Please use +, -, /, or *.")  

# '''  


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")

# count =0
# while count <1:

# if operator == '+':
#     print ("addition of value of num1 {0} and num2 {1}".format(num1, num2))
#     print(num1 + num2)
# elif operator == '-':
#     print ("Subtraction of value of num1 {0} and num2 {1}".format(num1, num2))
#     print(num1 - num2)
# elif operator == '*':  
#     print ("Multiplication of value of num1 {0} and num2 {1}".format(num1, num2))
#     print(num1 * num2)  
# elif operator == '/':  
#     if num2 != 0:
#         print ("Division of value of num1 {0} and num2 {1}".format(num1, num2))
#         print(num1 / num2)
#     else:
#         print("error")
# else:
#     print("Invalid operator. Please use +, -, *, or /.")        


while True:
  a=int(input("input enter the value of a : "))
  b=int(input("input enter the value of b : "))
  operator = input("enter the operator ")
  print("choose the opertor")
  print("1.addition")
  print("2.substraction")
  print("3.multiplcation")
  print("4.division")
  print("5.exit")

  if operator=='1':
      c=a+b
      print("addition of a {0} and b {1} is {2}".format(a,b,c))

  elif operator=='2':
      c=a-b
      print("substraction of a {0} and b {1} is {2}".format(a,b,c))  

  elif operator=='3':
      c=a*b
      print("multiplication of a {0} and b {1} is {2}".format(a,b,c))

  elif operator=='4':   
      c=a/b
      print("division of a {0} and b {1} is {2}".format(a,b,c))
      

  elif operator == '5':
        break      
  
  else:
     print('Invalid operator')