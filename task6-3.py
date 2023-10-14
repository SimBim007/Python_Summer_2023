  # Напишите программу, которая принимает на вход строку из символов и печатает одну строку из букв
  # Вторую из цифр, третью из прочих символов без повторений.
stroka=input("Введите строку для разложения на элементы: ")
stroka=set(stroka)
bukv=set()
chisl=set()
znaki=set()
for i in stroka:
    if i.isdigit():
        chisl.add(i)
    elif i.isalpha():
        bukv.add(i)
    else:   znaki.add(i)
print(f"Буквы: {bukv}")
print(f"Числа: {chisl}")
print(f"Знаки: {znaki}")
