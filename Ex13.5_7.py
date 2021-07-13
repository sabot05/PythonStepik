# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password),
# которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
#

# объявление функции
def is_valid_password(password):
    words = psw.split(':')
    if (len(words)) != 3:
        return False
    a = words[0]
    b = words[1]
    c = words[2]

    if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False:
        return False

    if (a != a[::-1]) or (int(c) % 2 != 0):
        return False

    if int(b) < 2:
        return False
    for i in range(2, int(b) - 1):
        if int(b) % i == 0:
            return False

    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
