# n = int(input("Nhập: "))
# b = []
# for i in range(n):
#     b.append(int(input("Nhập số: ")))
# a = True
# for i in range(len(b)):
#     if b[i] == 7:
#         print("So 7 o vi tri la: ", i)
#         a = False
#         break
# if a:
#     print("Khong co so 7 nào được nhập")

    

# # n1 = int (input("Nhập "))
# # n2 = int(input("Nhập "))
# # n3 = int(input("Nhập "))
# # if ( n1 == n2 - 1 and n2 == n3 -1):
# #     print("SEQUENCE")
# # else:
# #     print("NOT SEQUENCE")

def numberOfSevens(arr):
    dem = 0
    for i in arr:
        if i == 7:
            dem += 1
    return dem


n = int(input("Nhap so luong phan tu mang: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhap phan tu thu " + str(i+1) + ": ")))
print("There are",  numberOfSevens(arr), "number 7 in the list")
