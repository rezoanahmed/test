A,B,C = input().split()
if(float(A)>=float(B)+float(C) or float(B)>=float(A)+float(C) or float(C)>=float(B)+float(A)):
	print('NAO FORMA TRIANGULO')
elif((float(A)*float(A))==(float(B)*float(B))+(float(C)*float(C)) or (float(B)*float(B))==(float(A)*float(A))+(float(C)*float(C)) or (float(C)*float(C))==(float(B)*float(B))+(float(A)*float(A))):
	print('TRIANGULO RETANGULO')
elif((float(A)*float(A))>(float(B)*float(B))+(float(C)*float(C)) or (float(B)*float(B))>(float(A)*float(A))+(float(C)*float(C)) or (float(C)*float(C))>(float(B)*float(B))+(float(A)*float(A))):
	print('TRIANGULO OBTUSANGULO')
elif((float(A)*float(A))<(float(B)*float(B))+(float(C)*float(C)) or (float(B)*float(B))<(float(A)*float(A))+(float(C)*float(C)) or (float(C)*float(C))<(float(B)*float(B))+(float(A)*float(A))):
	print('TRIANGULO ACUTANGULO')

if(float(A)==float(B)==float(C)):
	print('TRIANGULO EQUILATERO')
elif((float(A)==float(B)!=float(C)) or (float(B)==float(C)!=float(A)) or (float(A)==float(C)!=float(B))):
	print('TRIANGULO ISOSCELES')
