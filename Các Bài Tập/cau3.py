def Stamgiac():
    a = int(input("chiều cao: "))
    b = int(input("cạnh huyền: "))
    return 1/2*a*b


def Shcn():
    m = int(input("chiều dài: "))
    # hi
    n = int(input("chiều rộng: "))
    return m*n


print("1. Tính diện tích tam giác")
print("2. Tính diện tích hình chữ nhật")
chon = int(input("chọn công việc: "))
if chon == 1:
    x = Stamgiac()
    print(x)
if chon == 2:
    h = Shcn()
    print(h)
