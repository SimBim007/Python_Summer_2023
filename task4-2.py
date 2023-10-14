#Спираль чисел N с 0, своими знаниями
n=int(input("Введите число для создания спирали: "))
matrix=[[0]*n for i in range(n)]
kolvo_yacheyk=0
# заполнение первой строки
for i in range(n):
    kolvo_yacheyk+=1
    matrix[0][i]=kolvo_yacheyk # заполняем строку 0, значениями i
j=0 # последняя ячейка
i=n-1
n-=1
while len(matrix)**2 !=kolvo_yacheyk:
    for k in range(n):#движение вниз
        j+=1
        kolvo_yacheyk+=1
        matrix[j][i]=kolvo_yacheyk
    for k in range(n):#влево
        i-=1
        kolvo_yacheyk+=1
        matrix[j][i]=kolvo_yacheyk
    for k in range(n-1):#вверх
        j-=1
        kolvo_yacheyk+=1
        matrix[j][i]=kolvo_yacheyk
    for k in range(n-1):# право
        i+=1
        kolvo_yacheyk+=1
        matrix[j][i]=kolvo_yacheyk
    n-=2
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()