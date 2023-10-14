#Аннаграмма
strok1=input("Введите строку для проверки, является ли она анаграммой: ")
strok2=input("Введите строку для проверки, является ли она анаграммой: ")
lst1=[]
lst2=[]
for i in strok2:
    if i.isalpha():
       lst2.append(i)
for i in strok1:
    if i.isalpha():
       lst1.append(i)
strok2=sorted(lst2)
strok1=sorted(lst1)
strok2=set(lst2)
strok1=set(lst1)
print(lst2)
print(lst1)
if strok2 == strok1:
    print("true")
else:   print("false")
