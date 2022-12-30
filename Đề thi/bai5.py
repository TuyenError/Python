list1=[1,4,2,3,8,4,5,9]
list2=[4,10,5,7,3,3,2,1]
do_dai = len(list1)
i=0
while(do_dai>0):
    if (list2[i]==1):
        do_dai = do_dai -1
        i=i+1
        continue
    elif (list2[i]%2 ==1):
        list1[i] = list2[i]
    i = i+1
    do_dai = do_dai-1
print(list1)
list1 = list1 + list2
print(list1)
