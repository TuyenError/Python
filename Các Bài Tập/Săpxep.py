def sapxep (arr):
	for i in range (len(arr)):
		for j in range (len(arr)):
			if arr [i] < arr [j] :
				arr[i] , arr [j] = arr [j], arr[i]
	return arr
a = int (input("Nhập số lượng phần tử: "))
b= []
c = 0
for i in range (a):
    c=int(input("Nhập số phần tử  " + str (+1)+": "))
    b.append(c)
print(" Danh sách sau khi sắp xếp : " , sapxep(b))
