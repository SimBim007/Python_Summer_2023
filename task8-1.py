def t_str(s):# Создаём функцию которая принимает строку (s) в качестве агрумента
    lst=list(s)# Преобразуем строку в список
    i=0
    while i<len(lst)-1:# Пока 'i' меньше чем длина списка -1
        if lst[i]=='А' and lst[i+1]=='Г':# Ксли текущий символ и следующий символ равны (А) и (Г),
            lst[i],lst[i+1]=lst[i+1],lst[i]# мы меняем их местами
            i+=2
        elif lst[i]=='Ц' and lst[i+1]=='Т':# Если текущий символ и следующий равны 'Ц' и 'Т',
            lst=lst[:i+1]+['А','Г']+lst[i+1:]# мы вставляем между ними 'А' и 'Г' между ними используя срезы
            i+=3
        else:
            i+=1
    t_str=''.join(lst)
    return t_str
s=input('Введите строку: ')
print(t_str(s))