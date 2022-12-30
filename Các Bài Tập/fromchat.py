# number = int(input("Nhap so: "))
# if number < 0:
#     number = - number
# print(number)

# a = float(input("Nhap so a: "))
# b = float(input("Nhap b: "))
# if a == 0:
#     if b == 0:
#         print("Phuong trinh vo so nghiem:")
#     else:
#         print("Phuong trinh vo nghiem: ")
# else:
#     print("Phuong trinh co nghiem la:", -b/a)

# monhoc = int(input("Nhap so mon hoc: "))
# tongdiem = 0.0
# for i in range(monhoc):
#     diem = float(input("Nhap diem mon thuv" + str(i +1)  + ": "))
#     tongdiem += diem
# print("Diem trung binh la: ", tongdiem/monhoc)

# a = int(input("Nhap so a :"))
# b = int(input("Nhap so b :"))
# c = int(input("Nhap so c :"))
# max = a
# if b > max :
#     max = b
# if c > max :
#     max = c
# print(max)

# r = int(input("nhap ban kinh r: "))
# print("Chu vi=", 2*3.14*r)
# print("Dien tich=",3.14*r*r )


# a= int(input("nhap so thu 1 :"))
# b= int(input("nhap so thu 2 :"))
# c= int(input("nhap so thu 3 :"))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# n=int(input("Nhap so: "))
# if n % 2 == 0:
#     print("So chan")
# else:
#     print("So le")
# str = input("Nhap string : ")
# countA = 0
# for chr in str:
#     if chr == "A" or chr == "a":
#         countA += 1
# print("Count of A:", countA)

# str = input("Nhap string : ")
# countA = 0
# counta = 0
# for chr in str:
#     if chr == "A":
#         countA += 1
#     elif chr == "a":
#         counta += 1
# print("Count of a:", counta)
# print("Count of A:", countA)

# n = input("Nhap chuoi: ")
# sochan=[]
# sole=[]
# for so in n:
#     if int(so) % 2 == 0:
#         sochan.append(int(so))
#     else:
#         sole.append(int(so))
# print("Co",len(sochan),"so chan:",sochan)
# print("Co",len(sole),"so le:", sole)


# n=input("Nhap chuoi: ")
# if n[::-1]==n:
#     print("Chuoi doi xung")
# else:
#     print("Khong doi xung")

# def numberOfUpperCases(s):
#     count_upper = 0
#     for i in s:
#         if i.isupper():
#             count_upper += 1
#     print("Number of uppercase letters: ", count_upper)
# s = str(input())
# numberOfUpperCases(s)

# string=input()
# count_upper = 0
# for i in string:
#         if i.isupper():
#                 count_upper += 1
# print("Number of uppercase letters: ", count_upper)



# def sumFromTo(st, end):
#     s = 0 
#     if st <= end:
#         for i in range(st, end+1):
#             s = s + i
#     else:
#         for i in range(end, st + 1):
#             s = s + i
#     return s

# while True:
#     a = int(input("Nhap so: "))
#     b = int(input("Nhap so: "))
#     print(sumFromTo(a,b))
#     c = int(input("Nhap lai(y/n): "))
#     if c == "n" : break

def sumFromTo (st,end):
    s=0
    if st <= end:
        for i in range (st,end+1):
            s=s+i
    else:
        for i in range(end, st + 1):
            s = s + i
    return s
        
while True:
    a = int(input("Nhập sô: "))
    b = int(input("Nhập sô: "))
    print(sumFromTo(a,b))
    c = int(input("Nhập lai(y/n): "))
    if c == "n": break

