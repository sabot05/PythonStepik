# # объявление функции
# Напишите функцию convert_to_python_case(text),
# которая принимает в качестве аргумента строку в
# «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    snake_register = ''
    for i in range(len(text)):
        if text[i].isupper():
            snake_register += '_' + text[i].lower()
        else:
            snake_register += text[i]

    return snake_register.lstrip('_')
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))