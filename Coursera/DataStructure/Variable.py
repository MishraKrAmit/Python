# First_Name = input("First Name :")
# Middle_Name=input("Middle Name :" )
# Last_Name=input("Last Name :")
# if (First_Name)!="":
#     Full_Name = First_Name
# if (Middle_Name) != "":
#     Full_Name= Full_Name +" "+ Middle_Name
# if (Last_Name)!= "":
#     Full_Name= Full_Name +" "+ Last_Name
# print (Full_Name)


# x= input("Enter Value: ")
# x= int(x)
# if x== 3 :
#     print ("Value is equal to  3")
# elif x >=6 & x <= 11  :
#     print("Value is equal to  6")
# elif x== 7 :
#     print ("value is equal to 7")
# else:
#     for i in range(10) :
#         print(i)
# print("All done")

# x= input("Enter Here: ")
# try :
#     x = int(x)
#     print("my test")
# except:
#     print("-1")
# print ("All done", x)


# astr = 'Hello Bob'
# istr = 0
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print(istr)


#astr = 'Hello Bob'
#istr = int(astr)
#print('First', istr)
#astr = '123'
#istr = int(astr)
#print('Second', istr)


# hrs = input("Enter Hours:")
# h = float(hrs)
# if h > 40 :
#    gross_pay= (40 * 10.5) + ((h-40) * (10.5*1.5))
# else:
#    gross_pay= (h * 10.5)
# print (gross_pay)

# score = input("Enter Score: ")
# try :
# 	score= float(score)
# except:
#     score= -1.0
# print(score)
# if score >= 0.9 and score <= 1.0 :
# 	print ("A")
# elif score >= 0.8  and score <= 0.9 :
#     print ("B")
# elif score >= 0.7  and score <= 0.8 :
#     print("C")
# elif score >= 0.6  and score <= 0.7 :
#     print("D")
# elif score < 0.6  and score <= 0.7 :
#     print ("F")
# else :
#     print ("Number not in range")

#
#def addtwo(a, b):
#    added = a + b
#    return a

# x = addtwo(2, 7)
# print(x)
#
#def computepay(h,r):
#   if h > 40 :
#        gross_pay = (40 * r) +((h-40)*(r * 1.5))
#    else :
#        gross_pay= (h * r)
#    return gross_pay
#
#hrs = input("Enter Hours:")
#hrs= float(hrs)
#rate= input("Enter Rate :")
#rate= float(rate)
#p = computepay(hrs,rate)
#print("Pay",p)
#
#num =[5,10,2,1,30,45,5,10,50]
#largenum= -1
#for i in  num :
#    if  i >  largenum :
#        largenum = i
#print(largenum)

# largest = None
# smallest = None
# errmsg=None
#
# while True:
#     num = input("Enter a number: ")
#     try :
#         if num == "done" :
#             break
#         num = int(num)
#     except :
#         num= smallest
#         errmsg = "Invalid input"
#
#     if largest is None :
#         largest= num
#     if smallest is None:
#         smallest= num
#     if num > largest :
#         largest=  num
#     if num < smallest :
#         smallest= num
#
# print(errmsg)
# print("Maximum is",largest)
# print("Minimum is",smallest )
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
