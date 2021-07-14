user_age = input('\nВведите год вашего ррождения :')

while type(user_age) != int:
    try:
        user_age = int(user_age)
    except ValueError:
        print('Тип вводимых данных должен быть числом')
        user_age = input('\nПожалуйста, Введите год вашего рождения ЦИФРАМИ :')

print((user_age))