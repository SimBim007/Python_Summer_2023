import keyword
k=keyword.kwlist
print(k)
# for i in k:
#     k.pop(0)
#     i='<kw>'
#     k.append(i)
# print(k)
stroka='False None True and'
lst=stroka.split()
# print(lst)
for i,j in enumerate(lst):
    if j in k:
        lst[i]='<kw>'
print(lst)