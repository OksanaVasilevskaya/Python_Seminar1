#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет
n=int(input(f'Введите число обозначающее день недели: '))
if n==1:print('понедельник- не является выходным днём')
elif n==2:print('вторник- не является выходным днём')
elif n==3:print('среда- не является выходным днём')
elif n==4:print('четверг- не является выходным днём')
elif n==5:print('пятница- не является выходным днём')
elif n==6:print('суббота- является выходным днём')
elif n==7:print('воскресенье- является выходным днём')
else:print('Введено не корректное число')
