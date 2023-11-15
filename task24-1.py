# s=[7,5,55,98,123,7]
# s2=[]
# s=[99,92,9]
# s=[0,0,0,999,0,1]
def grom(s):
    l=len(s)
    for i in range(l-1):
        # print("--i--",i)
        for j in range(l-i-1):
            # print("---j---",j)
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
    return print(s)

s=[1,654,2342,4657567,1,34,0,-2,0.5,5.7,213,99,99,9]
grom(s)