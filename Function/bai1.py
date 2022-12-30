def containsOneA(string):
    b = -1
    for i in string:
        b +=1
        if string[b] == "a" or string[b] == "A":
            return True
        else:
            return False
a = input('nhập kí tự:')
print(containsOneA(a))