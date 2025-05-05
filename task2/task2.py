import sys

if len(sys.argv) == 3:
    name_file_circle = sys.argv[1]
    name_file_point = sys.argv[2]
    
else:
    name_file_circle = input("Введите файла с центром окружности и радиусом: ")
    name_file_point = input("Введите файл с координатами точек: ")
    
file_circle = open(name_file_circle)
    
pervay_stroka = file_circle.readline()
x_centre, y_centre = map(float, pervay_stroka.split())
    
vtoray_stroka = file_circle.readline()
radius = float(vtoray_stroka)
    
file_circle.close()
    
file_point = open(name_file_point)

for i in file_point:
    x, y = map(float, i.split())

    dx = x - x_centre
    dy = y - y_centre

    rasstoyanie_square = dx * dx + dy * dy
    radius_square = radius * radius

    if round(rasstoyanie_square) == round(radius_square):
        print(0)  # точка лежит на окружности
    elif rasstoyanie_square < radius_square:
        print(1)  # точка внутри
    else:
        print(2)  # точка снаружи

file_point.close()