def maxlst(x):
    print(x)
    x=list(map(str,x))
    print(x)
    x.sort(reverse=True)
    print(x)
    return int(''.join(x))

x=[542,21,9]
print(maxlst(x))



