#   Напишите калькулятор(простой).
zadch=input("Введите выражение(вводите значения через пробел): ")
zadch=zadch.split()
print(zadch)
while True:
    if zadch[1]=='+':
        sloj=int(zadch[0])+int(zadch[2])
        print(sloj)
        break
    if zadch[1]=='-':
        vich=int(zadch[0])-int(zadch[2])
        print(vich)
        break
    if zadch[1]=='*':
        vich = int(zadch[0]) * int(zadch[2])
        print(vich)
        break
    if zadch[1]=='/':
        vich=int(zadch[0])/int(zadch[2])
        print(vich)
        break