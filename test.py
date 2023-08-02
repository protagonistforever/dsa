def rotate(l):
    l.insert(0,l.pop())
    print(l)
    return l
l=[12,34,56,78,9,10]
l=rotate(l)