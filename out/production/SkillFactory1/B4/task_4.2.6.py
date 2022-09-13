# Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет
# и возвращается результат проверки


def is_palindrom(word_to_check: str) -> bool:
    new_word=word_to_check.replace(' ','').lower()
    return new_word == new_word[::-1]


print(is_palindrom(input('enter string to check: ')))
