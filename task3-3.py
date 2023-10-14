#   На вход подается предложение из нескольких слов.
#   Слова разделены пробелами.
#   Напечатайте первое самое длинное слово в этом предложении.
predloj=input("Введите предложение: ")
predloj=predloj.split()
maxx=''
for word in predloj:
    if len(word)>len(maxx):
        maxx=word
print(maxx)