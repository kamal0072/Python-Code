# first_name="john"
# last_name="khan"
# roll=105
# a=10
# b=a
# a=12
# print(id(a))
# print(id(a))
# print(id(b))
# list1=['kama',12,'khan',23.15]
# print("The For Loop Is going to apply From here....")
# for x in list1:
#     print(x)
#     if x==12:
#         break
#     else:
#         print("This is outside of For Loop")
# print("End Of for Loop")
# print(type(list1))
# print(type(first_name))
# print(type(roll))

# a=b=c=d=10,30,20,30
# print(a,b,c,d)
# print(type(a))
# print(a)

#type of varialbles
#local Variables

# def school():
#     x=10
#     return x  #this is local scope/variable
#     print(x)
# var=school()
# print("The Valuse of variables is:",var)
# print(x) #trying to access local variable so that got err



# name="peter" #This is Global variable
# def school(name):
#     # global name
#     print(name)
#     x=10
#     return x  #this is local scope/variable
#     print("The Global Variable Is:",name)
# var=school("name")
# print("The Valuse of variables is:",var)
# print(name) #trying to global local variable so that got err
# del name
# print(name)

# name="peter"
# def show():
#     # global name
#     name="bablu"
#     # global name
#        #local Variable
#     print("The Global Variable Inside Function:",name)
# show()
# print("The Global Variable Outside Function:",name)

# a=20
# b="Kamal"
# c=23.50000544545
# d=-10+10j

# print("d is a complex number")  
# print("a","=",type(a),
#     "b","=",type(b),
#     "c","=",type(c),
#     "d","=",type(d),
#     isinstance(d,complex)
#     )
# print(
#     "Id of a=",id(a),
#     "Id Of b=",id(b),
#     "Id Of c=",id(c),
#     "Id Of d=",id(d))
# print("")

# a=0
# try:
#     b=1/a
#     raise Exception("Can not do it")
# except:
#     print("All Is Not Ok")
# finally:
#     print('All Okey')

# import calendar as cal  
# print(cal.month_name[5])  

# x = 0b10100 #Binary Literals  
# y = 100 #Decimal Literal   
# z = 0o215 #Octal Literal  
# u = 0o12   #Hexadecimal Literal  
  
# #Float Literal  
# float_1 = 100.5   
# float_2 = 1.5e5 
  
# #Complex Literal   
# a = 5+3.14j  
  
# print(x, y, z, u)  
# print(float_1, float_2)  
# print(a, a.imag, a.real)  


# conditional statements

# x=int(input("Enter Your Age:"))
# y=int(input("Enter Your Age:"))
# z=int(input("Enter Your Age:"))
# # name=input("enter your name=")
# if x>y and x>z:
#     print(" x is oldest")
# if y>x and y>z:
#     print("Y Is oldest ")
# if z>x and z>y:
#     print("z is oldest")

# a=int(input("Enter Your age of a="))
# b=int(input("Enter Your age of b="))
# c=int(input("Enter Your age of c="))

# if a>b or b>c:
#     print("a is right")     

# x=int(input("Enter The value of x:"))
# if x%2==0:
#     print("So x is even")
# else:
#     print("then x is not even")

# x=int(input("Enter x:"))
# y=int(input("Enter y:"))

# if x>y:
#     print("X is right")
# elif x>=y:
#     print("x is may be right")
# else:
#     print("x must be wronmg")






#looping starts here
# name=[45,8,8,5]
# list1=[55,45,23.4]
# for x in name:
#     print(x)
# print("-------")
# for y in list1:
#     print(y)

# z=name+list1
# print(z)
# for val in z:
#     print(val)

# x=[45,4.4,23,45]
# for mul in x:
#     res=mul+10
#     print(res)

# list = [10,30,23,43,65,12]  
# sum = 0  
# for i in list:  
#     sum = sum+i  
# print("The sum is:",sum)  

# lis1=['kk','hj','jha']

# for x in range(len(lis1)):
#     print(list[x])

# list = ['Peter','Joseph','Ricky','Devansh']  
# for i in range(len(lis1)):  
#     print("Hello",list[i])  


# rows=int(input("Enter Number of rows:"))
# for i in range(0,rows+1):
#     for j in range(i):
#         print("*",end='')
#     print("")
