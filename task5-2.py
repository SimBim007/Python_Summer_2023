#   Ввести число. Напечатать все его делители.
#   Например: 12, Вывод: 1,2,3,4,6,12
ch=abs(int(input("Введите число: ")))
d = [ x for x in range(1, ch // 2 + 1) if ch % x == 0 ]
print(d)