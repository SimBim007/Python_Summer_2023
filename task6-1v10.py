def rim_arab(rim):
    rim_cifra_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}# Создаём словарь в который содержит соотвествие римских цифр к арабским
    arab=0
    prev_value=0
    for i in reversed(rim):# В цикле проходим по каждой римской цифре в обратном порядке
        value=rim_cifra_dict[i]
        if value>=prev_value:# Если значение больше или равно предыдущему значению,
            arab+=value# прибавляем его к переменной (arab)
        else:# Если
            arab-=value# Не равно мы вычитаем его(значение) из (arab)
        prev_value=value# Обновляем значение предыдущей цифры на текущее значение
    return arab# Возвращаем (arab)
r=input("Введите РИМСКОЕ ЧИСЛО: ")
print(rim_arab(r))