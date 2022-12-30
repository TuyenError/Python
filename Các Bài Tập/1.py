# #Câu 1:
# string_1="hello"
# string_2=string_1
# num_1=5.0
# num_2=5
# check_book = (string_2 is string_1) and ( num_1 is num_2)
# print(check_book)
# string_1="pnv"
# string_3=string_1
# print("string_1 is =" is string_1)
# print("string_3 is =" is string_3)


# #Câu 2:
# list1= [1,4,2,3,8,4,5,9]
# list2= [4,10,5,7,3,3,2,1]
# do_dai=len(list1)
# i=0
# while (do_dai>0):
#     if (list2[i]==1):
#         do_dai=do_dai -1
#         i=i+1
#         continue
#     elif(list2[i]%2 ==1):
#         list1[i] = list2[i]
#     i=i+1
#     do_dai = do_dai - 1

# print(list1)
# list1 = list1+list2
# print(list1)


# #1
# X = int (input("Nhập số từ bàn phím: "))
# if X==3:
#     print(3)
# else:
#     print(0)

#2

# X = int(input("Nhập số từ bàn phím: "))
# Y = int(input("Nhập số từ bàn phím: "))
# Z = int(input("Nhập số từ bàn phím: "))
# if X==3:
#     if Y>3:
#         print("4")
#     else:
#         print("3")
# else:
#     if Y>3:
#         print("2")
#         if Z <10:
#             print("6")
#         else:
#             print("5")
#     else:
#         print("1")


#3
# X = int(input("Nhập số từ bàn phím: "))
# Y = int(input("Nhập số từ bàn phím: "))
# Z = int(input("Nhập số từ bàn phím: "))
# if X==3:
#     if Y>3:
#         print("3")
# else:
#     if Y>3:
#         if Z<10:
#             print("4")
#         else:
#             print("1")


#4
# X = int(input("Nhập số từ bàn phím: "))
# Y = int(input("Nhập số từ bàn phím: "))
# Z = int(input("Nhập số từ bàn phím: "))
# if X==3:
#     if Y>3:
#         print("3")
# else:
#     if Y>3:
#         if Z>10:
#             print("4")
#     else:
#         print("1")

6
# value1 = (x > 5 and y == 9)
# value2 = (y == 1 or y ==2)
# value3 = (z == 5 or z == 7 or z == 9)

# #7

# x = int(input("Nhap: "))
# lower = (x < 0)
# between = (10 < x < 15)
# if lower or between: 
#     print("Valid")

# #8
# x=int(input("Nhap: "))
# equal=x==10
# low=x<10
# high=x>10
# if high:
#     print("to high")
# elif equal:
#     print("good job")
# else: #elif low
#     print("to low")


#IF ELIF ELSE
#Exercise1
#1
"""
The result is:
red
blue
"""
#2
"""
The result is:
red
"""
#Exercise 2
#1
"""
The result is:
one
"""

#2
"""
NOTHING
"""
#Exercise 3
#1

"False"
#Exercise 4
"True"
#Exercise 5
#1
"red"
#Exercise 6
#1
"Nothing"
#Exercise 7

#1
"(6,10)"
#2
"[10,23]"
#3
"(23, +infinity)"


#Exercise 8
#1
"B"
#Exercise 9
"True"
#Cau 1
# theNumber = int(input("Nhap so: "))
# if theNumber < 0:
# 	print("Negative number!")
# else:
# 	print("Positive number!")


# Cau 2
# theNumber = int(input("Nhap so: "))
# if theNumber <0:
#     theNumber =  - theNumber
# print(theNumber)

#Cau 3
# firstNumber = int(input("Nhap: "))
# secondNumber = int(input("Nhap: "))
# print(firstNumber + secondNumber)

#Cau 4

# firstNumber = int(input("Nhap: "))
# secondNumber = int(input("Nhap: "))
# if firstNumber == secondNumber :
#     print("numbers are equal " )
# else:
#     print("numbers are not equal")

#Cau 5

# firstNumber = int(input("Nhap: "))
# secondNumber = int(input("Nhap: "))
# if (firstNumber + secondNumber) < 20:
#     print("Sum is less than 20 " )
# else:
#     print("Sum is greater or equal to 20")

# Cau 6
# score = int (input("Nhap diem: "))
# if score < 50 :
#     print ("bad!")
# elif 50 <= score < 80:
#     print("not bad, not good")
# elif 80 <= score <= 100:
#     print("excellent!")
# else:
#     print("are you crazy?!") 

#Cau 7


# firstNumber = int(input("Nhap: "))
# secondNumber = int(input("Nhap: "))
# if firstNumber <= secondNumber:
#     print("Greatest number is: ",secondNumber)
# else:
#     print("Greatest number is: ",firstNumber)

# Cau 8
# firstNumber = int(input("Nhap: "))
# secondNumber = int(input("Nhap: "))
# if firstNumber > secondNumber:
#     print("Smallest number is: ", secondNumber)
# else:
#     print("Smallest number is: ", firstNumber)

#Cau 9:
# firstNumber = int(input("Nhap: "))
# secondNumber = int(input("Nhap: "))
# thirrdNuber = int(input("Nhap: "))
# if firstNumber == secondNumber == thirrdNuber:
#     print("all equal")
# else:
#     print("not all equal")

# s1 = int (input("Nhap: "))
# s2 = int(input("Nhap: "))
# s3 = int(input("Nhap: "))
# s4 = int(input("Nhap: "))
# Mylist = len(s1,s2,s3,s4)
# print(Mylist)
# a=[]
# for i in range(4):
#     a+=[input("Nhap ten: ")]
# b=str(len(a[0]))
# for i in range(1,4):
#     b += "-" + str(len(a[i]))
# print(b)

# n = "hello"
# for i in range (len(n)):
#     print ("Y",end="")

# n =input("Nhap: ")
# for i in range (len(n)):
#     print ("Y",end="")

# a = input("Nhap: ")
# if len(a) <= 3:
#     print("It's small !")
# elif (len(a) >= 4 and len(a) <= 6) or (len(a) >= 8 and len(a) <=10):
#     print("It's medium !")
# elif len(a) == 7:
#     print("It's exactly the average !")
# else:
#     print("It’s big !")

# number = int(input("Nhap so: "))
# mode = input("Nhap mode: ")

# inside = 1 <= number <= 10
# outside = number < 1 or number > 10

# if mode == "inside":
#     print(inside)
# elif mode == "outside":
#     print(outside)

# n = input ("Nhap: ")
# for i in range(len(n)):
#     print (n[:len(n)-i])

# n = int(input ("Nhap: "))
# for i in range(n):
#     for e in range(n-i):
#         print("X",end=" ")
#     print("")
    



