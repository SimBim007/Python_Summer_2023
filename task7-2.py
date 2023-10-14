# Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря.
# Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются.
def cesarius(shift, n):
    LST=['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z','A']
    lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a']
    encrypted = ""
    for letter in shift:
        if letter in LST:
            index = LST.index(letter)
            new_index = (index + n) % 26
            encrypted += LST[new_index]
        elif letter in lst:
            index = lst.index(letter)
            new_index = (index + n) % 26
            encrypted += lst[new_index]
        elif letter in lst:
            index = lst.index(letter)
            new_index = (index + n) % 26
            encrypted += lst[new_index]
        else:
            encrypted += letter
    return encrypted

n = int(input("Введите n: "))
shift = input("Введите предложение (англ.): ")
print(cesarius(shift, n))




