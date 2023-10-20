#   Напишите рекурсивную функцию tri_2(n), которая печатает два треугольника
def snow(n):
    if n==1:
        print("*")
    elif n>1:
        print('*'*n)
        snow(n-1)
        print('*'*n)
    return
snow(5)
