def findfname(x):
    for n in range(len(x)-1, 0, -1):
        if x[n] == " ":
            return x[n+1:]


def findlname(x):
    for n in range(len(x) - 1):
        if x[n] == " ":
            return x[:n]


n = input("Nhap ten: ")
print("Ten cua ban la: " + findfname(n))
print("Ho cua ban la: " + findlname(n))
