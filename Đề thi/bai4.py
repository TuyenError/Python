# Hang = int(input("Nhap so: "))
# Cot = int(input("Nhap so: "))
# for i in range (Hang):
#     for i in range (Cot):
#         print("*", end="")
#     print()


# a = int(input("Nhap so: "))
# for x in range(a):
#     for y in range(a, 0, -1):
#         if y < (a-x):
#             print("*", end=" ")
#         else:
#             print(" ", end="")
#     print("")

n=int(input("Nhập số n: "))
s=0
for i in range(0,n):
    s+=1/(i+1)
print("Kết quả:",s)