A,B,C = input().split(" ")

TRIANGULO = 0.5 * float(A) * float(C)
CIRCULO = 3.14159 * pow(float(C),2)
TRAPEZIO = 0.5 * (float(A) + float(B)) * float(C)
QUADRADO = pow(float(B),2)
RETANGULO = float(A) * float(B)

print('TRIANGULO:','%.3f'%TRIANGULO)
print('CIRCULO:','%.3f'%CIRCULO)
print('TRAPEZIO:','%.3f'%TRAPEZIO)
print('QUADRADO:','%.3f'%QUADRADO)
print('RETANGULO:','%.3f'%RETANGULO)
