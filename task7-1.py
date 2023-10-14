  # Напишите программу которая рассчитывает НОК для списка натуральных чисел
def NOD(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def NOK(a,b):
    return (a*b)//NOD(a,b)
num1=int(input('Введите первое число и нажмите ENTER: '))
num2=int(input('Введите второе число и нажмите ENTER: '))
total=NOK(num1,num2)
print("НОК чисел", num1, "и", num2, "равна = ", total)
