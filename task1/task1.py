import sys

if len(sys.argv) == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
else:
    n = int(input("Введите количество чисел (n): "))
    m = int(input("Введите длину шага (m): "))

current_num = 1

path = ""

while True:
    path = path + str(current_num)
    next_num = current_num + (m - 1)

    while next_num > n:
        next_num = next_num - n

    if next_num == 1:
        break

    current_num = next_num

print("Путь:", path)