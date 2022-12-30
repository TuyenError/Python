
n = int(input('Nhap n: '))
a = []
for x in range(n):
	a += [int(input('Nhap so: '))]
for i in range(n):
	for j in range(n):
		if a[i] > a[j]:
			a[i], a[j] = a[j], a[i]
print(a)
