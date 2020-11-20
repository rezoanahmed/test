A,B,C = input().split()
if((float(A)+float(B)>float(C)) and (float(B)+float(C)>float(A)) and (float(A)+float(C)>float(B))):
	perimeter = float(A)+float(B)+float(C)
	print('Perimetro =','%.1f'%perimeter)
else:
	area = ((float(A)+float(B))/2)*float(C)
	print('Area =','%.1f'%area)
