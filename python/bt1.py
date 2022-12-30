# text = "class2024"
# print(text[:5])

# new = text[0]
# for i in range(1,len(text)):
#     new = new +"," + text[i]
# print(new)

# text = "class2024"
# print(text[3:5])


# q7
# text = input("nhap chuoi: ")
# dem = 0
# for i in text:
#     if i == "a":
#         dem = dem + 1
# if dem == 0:
#     print("a not found")
# else:
#     print(dem, "a not found")



# q8
text = input("nhap chuoi: ")
vitri = []
for i in range(len(text)):
    if text[i] == "a":
        vitri = vitri + [i]
if vitri == []:
    print("a not found")
else:
    print("a found at the index of ",vitri)



# q9
text = "alibaba"
newtext = ""
for i in text:
    if i == "a":
        newtext = newtext + "e"
    else:
        newtext = newtext + i
print(newtext)



# q10
text = input("nhap chuoi: ")
if text == text[::-1]:
    print("it is symmetric word")
else:
    print("It isn't symmetric word")
