# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)
 
# print(quicksort([3,6,8,10,1,2,1]))
# # Prints "[1, 1, 2, 3, 6, 8, 10]"
 
# animals = ['cat', 'dog', 'monkey']
# for animal in animals:
#     print(animal)

# def sign(x):
#     if x > 0:
#         return 'positive'
#     elif x < 0:
#         return 'negative'
#     else:
#         return 'zero'
 
# for x in [1,23,5]:
#     print(sign(x))

   



# a = array([1, 2, 3])   # Tạo 1 numpy array rank = 1
# print(type(a))            # Prints "<class 'numpy.ndarray'>"
# print(a.shape)            # Prints "(3,)"
# print(a[0], a[1], a[2])   # Prints "1 2 3"
# a[0] = 5                  # Thay đổi giá trị của 1 phần tử
# print(a)                  # Prints "[5, 2, 3]"
 
# b = np.array([[1,2,3],[4,5,6]])    # Tạo 1 numpy array rank = 2
# print(b.shape)                     # Prints "(2, 3)"
# print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"