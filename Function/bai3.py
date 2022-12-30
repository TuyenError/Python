def fl(input):
    for i in range(len(input)):
        if input[i] == ".":
            return i
    return -1
 
n = float(input("Nhap so: "))
Str = str(n)
m = fl(Str)
if m>0:
    print(Str+ " Has a integer part equal to ",Str[:m], " and a decimal part equal to ",Str[m+1:])