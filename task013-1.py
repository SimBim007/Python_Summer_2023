#   Создайте функцию генератор ,которая создаёт бесконечную последовательность.
def infinity(n):
    for x in range(1,n):
        if x%2==0:

            yield -x
        else:

            yield x
y=infinity(100)
for k in y:
    print(k)


