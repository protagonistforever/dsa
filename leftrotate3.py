def leftrotate(l):
    n=len(l)-1
    e=l[n]
    for i in range(n):
        l[i-1]=l[i]
    l[n-1]=e
    print(l)
l=[1,2,3,4,5]
leftrotate(l)