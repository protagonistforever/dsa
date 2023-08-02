def oddeven(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l=[1,2,3,4,5,6,7,8,9,10]
even,odd= oddeven(l)
print(odd)
print(even)
