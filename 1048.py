salary = float(input())
if(salary>=0 and salary<=400):
	percent = 15
	increased = (salary*percent)/100
elif(salary>400 and salary<=800):
	percent = 12
	increased = (salary*percent)/100
elif(salary>800 and salary<=1200):
	percent = 10
	increased = (salary*percent)/100
elif(salary>1200 and salary<=2000):
	percent = 7
	increased = (salary*percent)/100
elif(salary>2000):
	percent = 4
	increased = (salary*percent)/100


newsalary = salary+increased
print('Novo salario:','%.2f'%newsalary)
print('Reajuste ganho:','%.2f'%increased)
print('Em percentual:',percent,'%')
