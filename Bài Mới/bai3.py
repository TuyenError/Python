# def removeSevens(list):
#     newList = []
#     for i in list:
#         if i != 7:
#             newList.append(i)

#     return newList


# n = int(input("Nhap n: "))
# list = []
# for i in range(n):
#     list.append(int(input("Nhap so thu " + str(i + 1) + ": ")))
# print(removeSevens(list))
# -----------------------------------

# def hasPair(list):
#     for i in range(len(list)):
#         for j in range(len(list)):
#             if i != j:
#                 if list[i] == list[j]:
#                     return "HAS PAIR"
#     return "HAS NO PAIR"
# n = int(input("Nhap n: "))
# list = []
# for i in range(n):
#     list.append(int(input("Nhap so thu " + str(i + 1) + ": ")))
# print(hasPair(list))
# ----------------------

# def sum2By2(list):
#     newList = []
#     for i in range(len(list)-1):
#         newList.append(list[i] + list[i+1]) #
#     return newList
# n = int(input("Nhap n: "))
# list = []
# for i in range(n):
#     list.append(int(input("Nhap so thu " + str(i + 1) + ": ")))
# print(sum2By2(list))

# def hasPair(list):
#     for i in range(len(list)):
#         for j in range(len(list)):
#             if i != j:
#                 if list[i] == list[j]:
#                     return "HAS PAIR"
#     return "HAS NO PAIR"


# n = int(input("Nhap n: "))
# list = []
# for i in range(n):
#     list.append(int(input("Nhap so thu " + str(i + 1) + ": ")))
# print(hasPair(list))


#BaiList of card
# def hasPair(list):
#     for i in range(len(list)):
#         for j in range(len(list)):
#             if i != j:
#                 if (list[i][0] == list[j][0]) and (list[i][1] == list[j][1]):
#                     return "HAS PAIR"
#     return "HAS NO PAIR"


# n = int(input("Nhap n: "))
# list = []
# child = []
# for i in range(n):
#     child.append(input("Nhap so thu " + str(i + 1) + ": "))
#     child.append(input("Nhap mau:"))
#     list.append(child)
#     child =[]
# print(hasPair(list))


# def isEqual(list1, list2):
#     if list1 == list2:
#         return True
#     else:
#         return False
# list1 = []
# list2 = []

# n = int(input("Nhap do dai list 1: "))

# for i in range(1, n +1):
#     list1.append(int(input("Nhap phan tu thu " + str(i) + ": ")))
    
# m = int(input("Nhap do dai list 2: "))

# for i in range(1, m +1):
#     list1.append(int(input("Nhap phan tu thu " + str(i) + ": ")))
    
# if isEqual(list1, list2):
#     print("EQUAL")
# else:
#     print("NOT EQUAL")


# def splitBySpace(string):
#     list=[]
#     text = ""
#     for i in string:
#         if i == " ":
#             list.append(text)
#             text =""
#         else:
#             text += str(i)
#     list.append(text)
#     return list
# print(splitBySpace("Hello first year students"))

# mang = eval (input("Nhap mang: "))
# for i in range (len(mang)):
#     for j in range (len(mang)):
#         if mang[i][j] == 7:
#             mang [i][j] = 8
# print(mang)

# mang=eval(input("Nhap mang: "))
# age=int(input("Nhap tuoi: "))
# for i in mang:
#     if i[2]==age:
#         print(i[0])

