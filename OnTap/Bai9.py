from math import sqrt

fi = open("Bai9Input", 'r')
x = 0
y = 0
for line in fi:
    data = line.rstrip().split(" ")
    if data[0] == "UP":
        y += int(data[1])
    elif data[0] == "DOWN":
        y -= int(data[1])
    elif data[0] == "LEFT":
        x -= int(data[1])
    elif data[0] == "RIGHT":
        x += int(data[1])
    else:
        print("ERROR")

print(str(round(sqrt(x ** 2 + y ** 2))))
