# Напишите функцию is_palindrome(text),
# которая принимает в качестве аргумента строку text
# и возвращает значение True если указанный текст является палиндромом и False в противном случае.
def is_palindrome(text):
    list_of_text = list()
    lower_text = text.lower()
    for i in range(len(lower_text)):
        if lower_text[i].isalpha():
            list_of_text.append(lower_text[i])
    new_text = ''.join(list_of_text)

    if new_text == new_text[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
