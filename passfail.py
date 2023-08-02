def passfail(l):
    passed=[]
    fail=[]
    for i in l:
        if i<33:
            fail.append(i)
        elif i>33:
            passed.append(i)
    return fail,passed
l=[10,32,54,76,89,90,7,65,6]
fail,passed=passfail(l)
print(fail)
print(passed)
