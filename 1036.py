import math
A,B,C = input().split()
x = (float(B)*float(B)) - (4*float(A)*float(C))
if(float(A)==0 or x < 0):
	print('Impossivel calcular')
else:
	first = (-float(B) + math.sqrt(x))/ (2*float(A))
	second = (-float(B) - math.sqrt(x))/ (2*float(A))
	print('R1 =',"%.5f"%first)
	print('R2 =',"%.5f"%second)