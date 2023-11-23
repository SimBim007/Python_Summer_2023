s1='xyz'
s2='abc'
lst1=[]
lst2=[]
count=0
# print(s1)
for i in s1:
    if i not in lst2:
        lst2.append(i)
    for j in s2:
        if j not in lst1:
            lst1.append(j)
        # print(i,j)
        # print('lst1',lst1)
        # print('lst2--',lst2)

for i,j in enumerate(lst1):
    if lst1[i]==lst2[i]:
        True
    else:
        count+=1
        # print(False)

print(f"{s1} и {s2} --",count)