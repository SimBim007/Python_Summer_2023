#   Ввести два числа x и y.
#   Напечатать наибольшее из чисел x+y, x-y, x*y, x/y, x//y.
x=int(input("Введите число x: "))
y=int(input("Введите число y: "))
sum=x+y
raz=x-y
proiz=x*y
dele=x/y
dele2=x//y
mas=[sum, raz, proiz, dele2,dele]
mas=sorted(mas)
print(mas[4])
