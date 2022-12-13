# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x>0 and y>0:
    print(f'Точка с координатами ({x}, {y}) находится в первой четверти')
elif x<0 and y>0:
    print(f'Точка с координатами ({x}, {y}) находится во второй четверти') 
elif x<0 and y<0:
    print(f'Точка с координатами ({x}, {y}) находится в третьей четверти')
elif x>0 and y<0:
    print(f'Точка с координатами ({x}, {y}) находится в четвертой четверти')          
else:
    print(f'Точка с координатами ({x}, {y}) находится на оси координат')