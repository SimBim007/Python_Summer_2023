#   Напишите рекурсивную функцию, которая вычисляет количество
#   цифр введенного целого числа n (n>=0).
def rec_count(n):
    if n<10:
        return 1
    else:
        return  rec_count(n//10)+1


n=int(input("Введите число для посчёта: "))
print(rec_count(n))



def c_dig(n):
    if n==0:
        return 0
    else:
        return 1+c_dig(n//10)
n=int(input("Введите число для посчёта: "))
print(c_dig(n))