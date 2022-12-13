# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def InputCoordinates():
    xy = ["x", "y"]
    dot = []
    for i in range(2):
        dot.append(float(input(f'введите координату {xy[i]}: ')))
    return dot

def Distance(list1, list2):
    sum = 0
    for i in range(2):
        sum += (list2[i]-list1[i])**2
    from math import sqrt    
    dist = sqrt(sum)
    return dist

    
print('Точка A')
a = InputCoordinates()
print('Точка B')
b = InputCoordinates()

print(f'Расстояние между точками A и B: {round(Distance(a, b), 2)}')


   