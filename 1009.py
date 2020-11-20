name = input()
salary = float(input())
sell = float(input())
bonus = (sell*15)/100
totalSalary = salary + bonus
print('TOTAL = R$','%.2f'%totalSalary)