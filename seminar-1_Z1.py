# По двум заданным числам проверить является ли одно число квадратом второго
a=int(input('Введите число а= '))
b=int(input('Введите число b= '))
if b**2==a:
 print(f'Число {a} является квадратом числа {b}')
elif a**2==b:
 print(f'Число {b} не является квадратом числа {a}')
else:
 print(f'Числа не являются квадратом друг друга')