#   Дан список списков чисел.
#   Сосчитайте сумму всех чисел всех подсписков.
#   Например: [[1,2,3],[10,20],[100]] = 136
lst = [[1,2,3],[10,20],[100]]
lst1 = []
sum=0
for i in lst[0]:
    sum=i+sum
for i in lst[1]:
    sum=i+sum
for i in lst[2]:
    sum=i+sum
lst1.append(sum)
print(lst1)#136





