lst=[[1,5,3],[2,44,1,4],[3,3]]
n_lst=[]
for i in lst:
    lst=sorted(i,reverse=True)
    n_lst.append(lst)
print(sorted(n_lst))
