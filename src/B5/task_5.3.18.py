# Реализуйте программу, которая сжимает последовательность символов. На вход подается последовательность вида:
# пример: aaabbccccdaa
# Необходимо вывести строку, где каждая последовательность из одинаковых символов, идущих подряд,
# заменяется на один символ, и длину этой последовательности (включая последовательности единичной длины).
# Вывод должен выглядеть так:
# a3b2c4d1a2

text = 'aaabbccccdaa'
el_n = 0
previous = text[0]
zipped_text = ''
for el in text:
    if previous == el:
        el_n += 1
    else:
        zipped_text += previous + str(el_n)
        el_n = 1
        previous = el

zipped_text += previous + str(el_n)

print(zipped_text)