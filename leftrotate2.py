def leftrotate(l):
    l.append(l.pop(0))
    print(l)
l=[1,2,3,4,5,6,7,8,9]
leftrotate(l)