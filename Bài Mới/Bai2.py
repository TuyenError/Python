def getIndexOfCountry(a, b):
        for i in range(len(b)):
            if a== b[i]:
                return i
        return -1
countryNames = ["canada", "france", "usa", "cambodia"]
countryPopulationInMillion  = [110, 70, 250, 8]
a= input("Nhap countryName: ")
if getIndexOfCountry(a,countryNames) >= 0:
    print("Population of",a,"is",countryPopulationInMillion[getIndexOfCountry(a,countryNames)])
else:
    print(a,"has not been found in the list")


# def countA(n):
#     count = 0
#     for i in n:
#         if i == "a" or i == "A":
#             count = count+1
#     return count


# n = input("Nhập ký tự a or A vào: ")
# print("Total number of A is: ", countA(n))


# list=[]
# a =int(input("Nhập số phần tử: "))
# for i in range(a):
#     print("Nhập phần tử thứ",i+1, end=" ")
#     list.append(int(input()))
# print(list)
# number=0
# for j in range((len(list)-1)):
#     if list[j+1] > list[j] :
#         number += 1
# print("Result is: ",number)
