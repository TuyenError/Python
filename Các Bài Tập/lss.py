def sum(list1,list2):
    list1=[2,1,3,7,8,9]
    list2=[1,2,3]
    listsum=[]
    if len(list1)>len(list2):
        stlist=len(list1)-len(list2)
        for i in range(stlist):
            list2.append(0)
        for j in range(len(list1)):
            listsum.append(list1[j]+list2[j])
        return listsum
    elif len(list1)<len(list2):
        stl=len(list2)-len(list1)
    for i in range(stl):
        list1.append(0)
    for j in range(len(list2)):
        listsum.append(list1[j]+list2[j])
print(sum())




