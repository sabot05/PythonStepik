# Напишите функцию is_palindrome(text),
# которая принимает в качестве аргумента строку text
# и возвращает значение True если указанный текст является палиндромом и False в противном случае.
def is_palindrome(text):
    new = text.lower()
    mylist = list()
    for i in range(len(new)):
        if new[i].isalpha():
            mylist.append(new[i])
    s = ''.join(mylist)

    if s == s[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
