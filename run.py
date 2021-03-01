from math import pi,sqrt
from sys import argv

with open(argv[1]) as file:
    object = []
    for num, line in enumerate(file, 1):
        shape = line.lower()[:line.find('(')].replace(' ','')
        if (shape == "circle"):
            shape_options = line[line.find('(') + 1:line.find(')')].split(',')
            if (len(shape_options) == 2):
                points = shape_options[0].split(' ')
                if (len(points) == 2):
                    number = float(shape_options[1])
                    object.append([num, shape, points, number])
                else:
                    print(line + " " * (len(shape) + 1) + "^")
                    print("Error at column {}: expected <double>\n".format(num))
            elif (len(shape_options) > 2):
                print(line + " " * (len(shape) + 1) + "^")
                print("Error at column {}: unexpected token\n".format(num))
            elif (len(shape_options) < 2):
                print(line + " " * (len(shape) + 1) + "^")
                print("Error at column {}: expected 2 tokens\n".format(num))
        else:
            print(line + "^")
            print("Error at column {}: expected 'circle'\n".format(num))

for i in range(len(object)):
    shape = object[i][1]
    points = object[i][2]
    if (shape == "circle"):
        number = object[i][3]
        x1 = int(points[0])
        y1 = int(points[1])
        perimeter = 2 * pi * number
        area = pi * number ** 2
        print("{}. {}({}, {})".format(object[i][0], object[i][1],
        ' '.join(object[i][2]), object[i][3]))
        print("perimeter = {:.4f}".format(perimeter))
        print("area = {:.4f}".format(area))
        print("\tintersects:")
        for j in range(len(object)-1):
            if (j + 1 != i):
                points_buff = object[j + 1][2]
                number_buff = object[j + 1][3]
                x_buff = int(points_buff[0])
                y_buff = int(points_buff[1])
                distance = sqrt((x_buff - x1) ** 2 + (y_buff - y1) ** 2)
                if (number + number_buff >= distance):
                    print("\t{}. {}({}, {})".format(object[j + 1][0],
                    object[j + 1][1], ' '.join(object[j + 1][2]),
                    object[j + 1][3]))
        print("")
