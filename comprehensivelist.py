l1=[x for x in range(11) if x%2!=0]
print(l1)
l2=[x for x in range(11) if x%2==0]
print(l2)
d1={x:x**2 for x in range(11)}
print(d1)
d2={v:k for (k,v) in d1.items()}
print(d2)
l3=['kazama','shinchan','nobita','cobra','panther']
print(max(l3))
print(min(l3))