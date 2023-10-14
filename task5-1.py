#   Введите число n.
#   Напечатайте треугольник паскаля
def next_row(row):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
    return row

row = []
x=int(input())
for i in range(x):
    row = next_row(row)
    print(row)
