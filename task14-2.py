#   Напишите рекурсивную функцию, которая вычисляет сумму цифр натурального числа
def sum_rec(n):
    if n==0:
        return 0
    else:
        return n%10+sum_rec(n//10)
n=int(input("--->"))
print(sum_rec(n))



print(145//10)
print(14//10)
print(1//10)