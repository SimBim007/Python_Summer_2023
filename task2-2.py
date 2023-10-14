#   Введите список lst, состоящий из чисел.
#   Найдите и напечатайте наименьшее число из списка lst.
lst=[]
z=int(input())
for i in range(z):
    x=int(input("Введите числа: "))
    lst.append(x)
lst=sorted(lst)
print(f"Наименьшее число из списка: {lst[0]}")