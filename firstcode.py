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