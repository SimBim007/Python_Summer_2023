#   Вводить в бесконечном цикле зарплаты сотрудников.
#   Окончание ввода - ввод 0.
#   После чего напечатать среднюю зарплату.
zp=[]
while True:
    x=float(input("Введите зп: "))
    if x == 000:
        break
    zp.append(x)
print(zp)
print(f"Средняя зп: {sum(zp)/len(zp)}")