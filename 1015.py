import math
first = input().split(' ')
second = input().split(' ')
x1,y1 = first
x2,y2 = second
x = pow((float(x2) - float(x1)),2)
y = pow((float(y2) - float(y1)),2)

distance = math.sqrt(x + y)
print('%.4f'%distance)
