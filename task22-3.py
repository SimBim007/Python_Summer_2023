import keyword
k=keyword.kwlist
for i in k:
    k.pop(0)
    i='<kw>'
    k.append(i)
print(k)