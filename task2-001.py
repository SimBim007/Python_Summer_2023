#   Дан список целых чисел, например [1,2,3,4,5]
#   Создайте новый список, каждый элемент которого является суммой чисел первого и второго списка с накоплением,
#   то есть [1,3,6,10,15]
lst=[1,2,3,4,5]
lst1=[]
sum=0
for i in lst:
    sum = i+sum
    lst1.append(sum)
print(lst1)