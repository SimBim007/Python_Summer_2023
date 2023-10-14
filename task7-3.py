d_mas=[[1,6,3,100,56347,0],[3,5,4,12673,8,0]]
p_lst=[]
def max_masss(stroka):
    stroka=(sum(d_mas,[]))
    stroka=sorted(stroka)
    for x in range(3):
        for i in stroka:
            maxx=max(stroka)
        p_lst.append(maxx)
        stroka.pop()
    return  p_lst
print(sorted(max_masss(p_lst)))