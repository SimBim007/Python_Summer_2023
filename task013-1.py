def infinity():
    x=1
    while True:
        if x%2==0:
            yield -x
        else:
            yield x
        x+=1
y=infinity()
z=int(input("Введите количество повторений: "))
for k in range(z):
    print(next(y))