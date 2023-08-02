def rightrotate(l):
    n=len(l)-1
    e=l[n]
    for i in range(n):
        l[n-i]=l[n-i-1]
    l[0]=e
    print(l)
l=[1,2,3,4,5]
rightrotate(l)