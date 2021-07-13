# Считаем кредит

name1 = input('Ввведите имя первого человека: ')
name2 = input('Ввведите имя второго человека: ')
name3 = input('Ввведите имя третьего человека: ')
name4 = input('Ввведите имя четвертого человека: ')

salary1 = input('\nВведите зп первого человека: ')
salary2 = input('Введите зп второго человека: ')
salary3 = input('Введите зп третьего человека: ')
salary4 = input('Введите зп четвертого человека: ')

credit = input('\nВведите сумму кредита: ')
period = input('Введите срок в месяцах: ')
percent = input('Введите процент: ')

pay_per_month = (int(credit) / int(period)) + ((int(credit) / 100 * int(percent))) / 12

print('\nЕжемесячный платеж составит - ', pay_per_month, 'рублей.')
print('\n', name1, 'сможет потратить ', int(salary1) - pay_per_month)
print('\n', name2, 'сможет потратить ', int(salary2) - pay_per_month)
print('\n', name3, 'сможет потратить ', int(salary3) - pay_per_month)
print('\n', name4, 'сможет потратить ', int(salary4) - pay_per_month)