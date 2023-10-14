#   Ввести два числа x И y.
#   Напечатать ВТОРОЕ ПО ВЕЛИЧИНЕ их чисел x+y, x-y, x*y, x/y, x//y
x=int(input("Введите число x: "))
y=int(input("Введите число y: "))
mas=[x+y, x-y, x*y, x/y, x//y]
print(mas)
mas=sorted(mas)
print(mas[3])