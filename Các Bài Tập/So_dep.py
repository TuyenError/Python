
# def Sodep(n):
#     N_str=str(n)
#     x=0
#     y=0
#     for a in N_str:
#         z=int(N_str[y])
#         if int(a) == z :
#             x=x+1
#             if x==z:
#                 y=y+x
#                 x=0
#         else:
#             return "N is not beautiful"
#     return "N is beautiful"

# n=int(input("Nhập N: "))
# print(Sodep(n))

def Fibonaci (n):
    if n<3:
        f=1
    else:
        f=Fibonaci(n-1)+Fibonaci(n-2)
    return f
n=0
while n==0:
    n=int(input("Nhap n#0: "))
print(Fibonaci(n))
