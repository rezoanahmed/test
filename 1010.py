product1 = input().split(' ')
product2 = input().split(' ')

code1, unit1, value1 = product1
code2, unit2, value2 = product2

total = ((int(unit1) * float(value1)) + (int(unit2) * float(value2)))
print('VALOR A PAGAR: R$','%.2f'%total)
